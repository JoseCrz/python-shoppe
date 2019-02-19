import csv
import os

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
    
    def update_client (self, updated_client):
        clients_list = self.list_clients()

        updated_clients_list = []
        for client in clients_list:
            if client["uid"] == updated_client.uid:
                updated_clients_list.append(updated_client.to_dict())
            else:
                updated_clients_list.append(client)
        
        self._save_to_disk(updated_clients_list)
    
    def _save_to_disk (self, clients):
        tmp_file_name = self.file_name + ".tmp"
        with open (tmp_file_name, mode = "a") as f:
            writer = csv.DictWriter(f, fieldnames = ClientModel.schema())
            writer.writerows(clients)

        os.remove(self.file_name)
        os.rename(tmp_file_name, self.file_name)
