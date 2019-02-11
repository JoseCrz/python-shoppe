import csv

from clients.models import ClientModel

class ClientServices:

    def __init__ (self, file_name):
        self.file_name = file_name

    def create_client (self, client):
        with open(self.file_name, mode = "a") as f:
            writer = csv.DictWriter(f, fieldnames = ClientModel.schema())
            writer.writerow(client.to_dict())
    
    def list_clients (self):
        with open(self.file_name, mode = "r") as f:
            reader = csv.DictReader(f, fieldnames = ClientModel.schema())

            return list(reader)
