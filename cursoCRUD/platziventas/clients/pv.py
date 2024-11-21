import click
from clients import commands as clients_commands

CLIENTS_TABLE = '.clients.csv'

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE

#Aqui se registran todos los comandos desde commands
cli.add_command(clients_commands.all)

if __name__ == '__main__':
    cli()
