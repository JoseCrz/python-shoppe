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
    pass


@clients.command()
@click.pass_context
def update (ctx, client_uid):
    """Updates a client"""
    pass


@clients.command()
@click.pass_context
def delete (ctx, client_uid):
    """Deletes a client"""
    pass

all = clients