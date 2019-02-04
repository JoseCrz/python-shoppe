clients = "José,Sara,"

# Function that lists all the clients
def list_clients ():
    global clients
    print(clients)


#Function that creates a client 
def create_client (client_name):
    global clients
    clients += client_name
    _add_comma()


# Private functions that adds a comma to separate each client on the list
def _add_comma ():
    global clients
    clients += ","


if __name__ == "__main__":
    list_clients()
    create_client("Mich")
    list_clients()

