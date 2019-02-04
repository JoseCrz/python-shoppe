clients = "José,Sara,"

# Function that lists all the clients
def list_clients ():
    global clients
    print(clients)


#Function that creates a client 
def create_client (client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
        list_clients()
    else:
        print("Client already exists!")
        

#Funciont that deletes a client
def delete_client ():
    pass

    
# Private functions that adds a comma to separate each client on the list
def _add_comma ():
    global clients
    clients += ","

    
#Private function that prints a menu
def _print_welcome ():
    print("Welcome to the Shoppe Administration")
    print("*" * 50)
    print("What would you like to do?")
    print("[C]reate client")
    print("[D]elete client")


if __name__ == "__main__":
    _print_welcome()
    command = input("type letter: ")

    if command == "C":
        client_name = input("What's the client name?: ")
        create_client(client_name)

    elif command == "D":
        delete_client()

    else:
        print("Command not found")

