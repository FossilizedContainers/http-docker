import requests
import click
import docker
import json

@click.group()
def cli():
    pass

@cli.command()
@click.argument('metadata')
def run(metadata):
   container = client.containers.list()[0]
   ip_address = str(container.attrs['NetworkSettings']['IPAddress'])
   ip_address = "127.0.0.1"

   run_metadata = json.load(open(metadata))

   files = {
      "metadata.json": open(metadata, 'rb')
   }
   for input in run_metadata['inputs']:
      typ = run_metadata['inputs'][input]['type']
      location = run_metadata['inputs'][input]['location']
      files[str(input)] =  open(location, 'rb')

   # debug
   print(files)
   print(container.attrs)
   print(ip_address)

   # send the request, get back a NetCDF
   netCDF = requests.post('http://' + ip_address + ':4000/', files=files)
   # printing the file that the client recieved back from the srever in the response message
   print(netCDF.content)

@cli.command()
@click.argument('filepath')
@click.argument('tagname')
def build_server(filepath, tagname):
    # Build the image first
    print('Building http server image if not built already...\n')
    client.images.build(path=filepath, tag=tagname)
    #build(filepath, tagname)
    print('Finished building the image...\n')
    # Running the container now
    #The port number, as an integer. For example, {'2222/tcp': 3333}
    #will expose port 2222 inside the container as port 3333 on the host.
    print('Now running the container...\n')
    port = {'80/tcp':4000}
    cont = client.containers.run('http-server', ports=port, tty=True, stdin_open=True, detach=True)
    print(cont.logs().decode('utf-8'))

# command mostly for testing
# will stop all containers and prune them
@cli.command()
def clean():
    for container in client.containers.list():
        container.stop()

    client.containers.prune()

def main():
    global client
    client = docker.from_env()
    cli()

if __name__ == '__main__':
    main()
