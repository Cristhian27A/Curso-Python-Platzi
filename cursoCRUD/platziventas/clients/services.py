import csv
import os
from clients.models import Client


class ClientService:
    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, mode='a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())

            if f.tell() == 0:
                writer.writeheader()

            writer.writerow(client.to_dict()) 

    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            return list(reader)

    def get_client_by_uid(self, client_uid):
        """Busca un cliente por su UID."""
        clients = self.list_clients()
        for client in clients:
            if client['uid'] == client_uid:
                return client
        return None

    def update_client(self, updated_client):
        clients = self.list_clients()

        updated_clients = []
        for client in clients:
            if client['uid'] == updated_client['uid']:
                updated_clients.append(updated_client)
            else:
                updated_clients.append(client)

        self._save_to_disk(updated_clients)

    def delete_client(self, client_uid):
        """Elimina un cliente por su UID."""
        clients = self.list_clients()
        updated_clients = [client for client in clients if client['uid'] != client_uid]
        self._save_to_disk(updated_clients)

    def _save_to_disk(self, clients):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name, mode='w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writeheader()
            writer.writerows(clients)

        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)

