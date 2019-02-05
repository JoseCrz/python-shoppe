import sys

clients = [
    {
        "name": "José",
        "company": "Apple",
        "email": "cueramjose@gmail.com",
        "position": "Software Engineer"
    },
    {
        "name": "Eugenio",
        "company": "Bad Robot Productions",
        "email": "eugenio@badrobot.com",
        "position": "Film Director"
    }
]


def list_clients ():
    """Lists all the clients"""

    global clients
    for idx, client in enumerate(clients):
        print("{uid} | {name} | {company} | {email} | {position}"
        .format(uid=idx, name = client["name"], company = client["company"], email = client["email"], position = client["position"]))




def create_client (client_name):
    """Recieves a client name, if it doesn't exists, is added to the list, else is ommited"""

    global clients
    if client_name not in clients:
        clients.append(client_name)
        list_clients()
    else:
        print("Client already exists!")


def update_client (client_name):
    """Searches the clients list for the name given, if it exists, asks the user for the updated version"""
    

    global clients 
    if client_name not in clients:
        print("Client not found!")
        
    else:
        updated_client_name = input("What's the new name?: ")
        client_to_update_index = clients.index(client_name)
        clients[client_to_update_index] = updated_client_name
        print("Update successful!")
        list_clients()



def delete_client (client_name):
    """Searches the clients list for the given nane, if it exists, deletes the client"""

    global clients
    if client_name not in clients:
        print("Client not found!")
    else:
        clients.remove(client_name)
        print("Deleted successfuly!")
        list_clients()

def search_client(client_name):
    """Searches for a specific client on the list and returns: True if found, False if not """

    global clients
    
    for client in clients:
        if client == client_name:
            return True
    
    return False

#-----------PRIVATE FUNCTIONS-------------------

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


if __name__ == "__main__":
    _print_welcome()
    command = input("type letter: ")
    command = command.upper()

    if command == "C":
        print("***** Create Client *****")

        client_name = _get_client_name()
        create_client(client_name)

    elif command == "L":
        print("***** List of clients *****")
        list_clients()
    
    elif command == "U":
        print("***** Update Client *****")

        client_name = _get_client_name()
        update_client(client_name)

    elif command == "D":
        print("***** Delete Client *****")
        
        client_name = _get_client_name()
        delete_client(client_name)

    elif command == "S":
        print("***** Search Client *****")

        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print("The client is on the list")
        else:
            print("Sorry, {} is not on the list".format(client_name))

    else:
        print("Command not found")

