clients = "José,Sara,"


def list_clients ():
    """Lists all the clients"""

    global clients
    print(clients)



def create_client (client_name):
    """Recieves a client name, if it doesn't exists, is added to the list, else is ommited"""

    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
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
        clients = clients.replace(client_name + ",", updated_client_name + ",")
        print("Update successful!")
        list_clients()



def delete_client (client_name):
    """Searches the clients list for the given nane, if it exists, deletes the client"""

    global clients
    if client_name not in clients:
        print("Client not found!")
    else:
        clients = clients.replace(client_name + ",", "")
        print("Deleted successfuly!")
        list_clients()

def search_client(client_name):
    """Searches for a specific client on the list and returns: True if found, False if not """

    global clients
    clients_list = clients.split(",")
    for client in clients_list:
        if client == client_name:
            return True
    
    return False

#-----------PRIVATE FUNCTIONS-------------------

def _add_comma ():
    """Private functions that adds a comma to separate each client on the list"""
    global clients
    clients += ","


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

    return input("What's the client name?: ")


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

