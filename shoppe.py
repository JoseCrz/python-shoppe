import click

from clients import commands as clients_commands

FILE_NAME = ".clients.csv" 

@click.group()
@click.pass_context
def cli (ctx):
    ctx.obj = {}
    ctx.obj["file_name"] = FILE_NAME


cli.add_command(clients_commands.all)