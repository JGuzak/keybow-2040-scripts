import click
import os
import psutil

@click.command()
@click.option("--script", required=True, help="Relative or absolute path to the script you wish to load.")
@click.option("--keybow-drive-name", default="CIRCUITPY", help="The name of the keybow file system.")

def upload(script, keybow_drive_name):
    click.echo(psutil.disk_partitions(all=True))
    # click.echo(f"Finding {script}!")

if __name__ == '__main__':
    upload()