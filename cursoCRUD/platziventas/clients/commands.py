import click
from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """Manages the clients lifecycle"""
    pass

@clients.command()
@click.option('-n', '--name', prompt=True, help='The client name')
@click.option('-c', '--company', prompt=True, help='The client company')
@click.option('-e', '--email', prompt=True, help='The client email')
@click.option('-p', '--position', prompt=True, help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Create a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)
    click.echo(f"Client {name} created successfully!")

@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])
    clients = client_service.list_clients()

    click.echo("ID | Name | Company | Email | Position")
    click.echo("*" * 100)

    for client in clients: 
        click.echo(f"{client['uid']} | {client['name']} | {client['company']} | {client['email']} | {client['position']}")

@clients.command()
@click.argument('client_uid')
@click.pass_context
def update(ctx, client_uid):
    """Updates a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client = client_service.get_client_by_uid(client_uid) 

    if client:
        client['name'] = click.prompt('New name', default=client['name'])
        client['company'] = click.prompt('New company', default=client['company'])
        client['email'] = click.prompt('New email', default=client['email'])
        client['position'] = click.prompt('New position', default=client['position'])

        client_service.update_client(client)
        click.echo(f"Client {client_uid} updated successfully!")
    else:
        click.echo("Client not found.")

@clients.command()
@click.argument('client_uid')
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.delete_client(client_uid)
    click.echo(f"Client {client_uid} deleted successfully.")


all = clients

