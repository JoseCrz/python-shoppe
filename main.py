import sys
import csv
import os

CLIENTS_FILE_NAME = ".clients.csv"
CLIENT_SCHEMA = ["name", "company", "email", "position"]
clients = []


def list_clients ():
    """Lists all the clients"""

    global clients
    for idx, client in enumerate(clients):
        print("{uid} | {name} | {company} | {email} | {position}"
        .format(uid=idx, name = client["name"], company = client["company"], email = client["email"], position = client["position"]))




def create_client (client):
    """Recieves a client name, if it doesn't exists, is added to the list, else is ommited"""

    global clients
    if client not in clients:
        clients.append(client)
        #list_clients()
        print("Client successfully created")
    else:
        print("Client already exists!")


def update_client (client_name):
    """Searches the clients list for the name given, if it exists, asks the user for the updated version"""
    

    global clients
    client = search_client(client_name)

    if client:
        client_to_update_index = clients.index(client)
        print("~~~ Leave blank if you don't want to update that field ~~~")

        for key in clients[client_to_update_index].keys():
            updated_info = input("What's the new {}?: ".format(key))
            if updated_info:
                clients[client_to_update_index][key] = updated_info
            
        print("Update successful")
        list_clients()
            
    else:
        print("Client not found!")
            

def delete_client (client_name):
    """Searches the clients list for the given nane, if it exists, deletes the client"""

    global clients
    client = search_client(client_name)
    if client:
        clients.remove(client)
        print("Client deleted successfuly!")
        #list_clients()
    else:
        print("Client not found!")

def search_client(client_name):
    """Searches for a specific client on the list and returns the client if found """

    global clients
    
    for client in clients:
        if client["name"] == client_name:
            return client
    
    return False

#-----------PRIVATE FUNCTIONS-------------------

def _get_clients_from_file ():
    """retrieves the clients data from a CSV file and puts in a dictionary"""
    
    #Checks if the file exist, if not, is created
    if not os.path.exists(CLIENTS_FILE_NAME):
        with open(CLIENTS_FILE_NAME, mode="w") as f:
            writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
            writer.writerow({"name": "name", "company": "company", "email":"email", "position": "position"})

    with open(CLIENTS_FILE_NAME, mode="r") as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)


def _save_clients_to_file ():
    """Saves the clients to a CSV file for data persistency"""

    tmp_file_name = "{}.tmp".format(CLIENTS_FILE_NAME)
    with open(tmp_file_name, mode="w") as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENTS_FILE_NAME)
        os.rename(tmp_file_name, CLIENTS_FILE_NAME)

def _print_welcome ():
    """Private function that prints a menu"""

    print("Welcome to the Shoppe Administration")
    print("-" * 50)
    print("What would you like to do?")
    print("[C]reate client")
    print("[L]ist clients")
    print("[U]pdate")
    print("[D]elete client")
    print("[S]earch client")

def _get_client_name () :
    """Private function that returns the name given by the user"""

    client_name = None

    while not client_name:
        client_name = input("What's the client name?: ")

        if client_name.lower() == "exit":
            client_name = None
            break
    
    if not client_name:
        sys.exit()
        
    return client_name


def _get_client_info (info_field):
    """Ask the user for the specified field"""
    info = input("What is the client's {}? : ".format(info_field))
    return info 

#___________________________________________________
#---------------------- MAIN -----------------------
#___________________________________________________

if __name__ == "__main__":
    _get_clients_from_file()

    _print_welcome()
    command = input("type letter: ")
    command = command.upper()

    if command == "C":
        print("***** Create Client *****")

        client = {
            "name": _get_client_info("name"),
            "company": _get_client_info("company"),
            "email": _get_client_info("email"),
            "position": _get_client_info("position")
        }

        create_client(client)

    elif command == "L":
        print("***** List of clients *****")
        list_clients()
    
    elif command == "U":
        print("***** Update Client *****")

        client_name = _get_client_info("name")
        update_client(client_name)

    elif command == "D":
        print("***** Delete Client *****")
        
        client_name = _get_client_info("name")
        delete_client(client_name)

    elif command == "S":
        print("***** Search Client *****")

        client_name = _get_client_info("name")
        found = search_client(client_name)

        if found:
            print("The client is on the list")
        else:
            print("Sorry, {} is not on the list".format(client_name))

    else:
        print("Command not found")
    
    _save_clients_to_file()

