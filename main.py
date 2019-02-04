clients = "José,Sara,"

# Function that lists all the clients
def list_clients ():
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
        

def delete_client ():
    pass

#-----------PRIVATE FUNCTIONS-------------------

def _add_comma ():
    """Private functions that adds a comma to separate each client on the list"""
    global clients
    clients += ","


def _print_welcome ():
    """Private function that prints a menu"""

    print("Welcome to the Shoppe Administration")
    print("*" * 50)
    print("What would you like to do?")
    print("[C]reate client")
    print("[U]pdate")
    print("[D]elete client")

def _get_client_name () :
    """Private function that returns the name given by the user"""

    return input("What's the client name?: ")


if __name__ == "__main__":
    _print_welcome()
    command = input("type letter: ")

    if command == "C":
        client_name = _get_client_name()
    
    elif command == "U":
        client_name = _get_client_name()

    elif command == "D":
        delete_client()

    else:
        print("Command not found")

