import click

from cli.generate.upload_vector_db import upload_vector_db

@click.group()
@click.version_option(version='1.0.0')
@click.pass_context
def cli(ctx):
    pass

cli.add_command(upload_vector_db, "upload_vector_db")


