#!/usr/bin/python

import click
import requests
import json

@click.command()
@click.option('--swagger-spec', '-s', multiple=True)
@click.option('--verbose', '-v', is_flag=True)
def launch_cli(swagger_spec, verbose):
    specs = []
    for spec_file in swagger_spec:
        if spec_file.startswith('http://') or spec_file.startswith('https://'):
            r = requests.get(spec_file)
            r.raise_for_status()
            specs.append(r.json())


    for s in specs:
        #click.echo(json.dumps(s, indent=2))
        click.echo("Swagger Version: {0}".format(s['swaggerVersion']))
        click.echo("Api Version: {0}".format(s['apiVersion']))
        click.echo("Resource Path: {0}".format(s['resourcePath']))
        for api in s['apis']:
            click.echo("  Path: {0}".format(api['path']))
            click.echo("  Description: {0}".format(api['description']))
            for op in api['operations']:
                click.echo("    Operation: {0}".format(op['nickname']))
                click.echo("    Summary: {0}".format(op['summary']))
                click.echo("    Method: {0}".format(op['method']))
                click.echo("    Type: {0}".format(op['type']))
                click.echo("    Produces: {0}".format(",".join(op['produces'])))
                click.echo("    Consumes: {0}".format(",".join(op['consumes'])))
                for param in op['parameters']:
                    click.echo("      Name: {0}".format(param['name']))
                    click.echo("      Type: {0}".format(param['type']))
                    click.echo("      Param Type: {0}".format(param['paramType']))
                    click.echo("      Required: {0}".format(param['required']))
                    click.echo("      Allow Multiple: {0}".format(param['allowMultiple']))
                    click.echo("      Description: {0}".format(param['description']))
                if 'responseMessages' in op:
                    for resp in op['responseMessages']:
                        click.echo("      Code: {0}".format(resp['code']))
                        click.echo("      Message: {0}".format(resp['message']))
                        click.echo("      Model: {0}".format(resp['responseModel']))



if __name__ == '__main__':
    launch_cli()