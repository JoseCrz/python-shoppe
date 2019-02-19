import click

from clients.services import ClientServices
from clients.models import ClientModel

@click.group()
def clients ():
    """Manages the clients life cycle"""
    pass


@clients.command()
@click.option("-n", "--name", type = str, prompt = True, help = "Client's name")
@click.option("-c", "--company", type = str, prompt = True, help = "Client's company")
@click.option("-e", "--email", type = str, prompt = True, help = "Client's email")
@click.option("-p", "--position", type = str, prompt = True, help = "Client's position")
@click.pass_context
def create (ctx, name, company, email, position):
    """Creates a new client"""

    client = ClientModel(name, company, email, position)
    client_services = ClientServices(ctx.obj["file_name"])

    client_services.create_client(client)


@clients.command()
@click.pass_context
def list (ctx):
    """Lists all clients"""
    
    client_services = ClientServices(ctx.obj["file_name"])

    clients_list = client_services.list_clients()

    click.echo((" " * 34 ) + "ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION")
    click.echo("_" * 100)

    for client in clients_list:
        click.echo("{uid}  | {name}  |  {company}  |  {email}  | {position}".format(
                uid = client["uid"],
                name = client["name"],
                company = client["company"],
                email = client["email"],
                position = client["position"]))


@clients.command()
@click.argument("client_uid", type = str)
@click.pass_context
def update (ctx, client_uid):
    """Updates a client"""
    client_services = ClientServices(ctx.obj["file_name"])

    clients_list = client_services.list_clients()

    client = [client for client in clients_list if client["uid"] == client_uid]
    
    if client:
        client = _update_client_flow(ClientModel(**client[0]))
        client_services.update_client(client)

        click.echo("Client updated successfuly!")
    else:
        click.echo("Client not found!")


def _update_client_flow (client):
    click.echo("Leave blank if you don't want to change it")

    client.name = click.prompt("New name: ", type = str, default = client.name)
    client.company = click.prompt("New company: ", type = str, default = client.company)
    client.email = click.prompt("New email: ", type = str, default = client.email)
    client.position = click.prompt("New position: ", type = str, default = client.position)

    return client

@clients.command()
@click.pass_context
def delete (ctx, client_uid):
    """Deletes a client"""
    pass

all = clients