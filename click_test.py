import click

@click.group()
@click.option("-n", "--name", default="hello")
@click.pass_context
def cli(ctx, name):
    """
    A simple CLI for testing.
    """
    print("cli.................", ctx.obj)

@cli.command()
@click.option("-p", "--password", default="password")
@click.pass_context
def hello(ctx, password):
    print("hello..............", ctx.obj)
    print("Hello, world!")

def test():
    cli(obj={"a":"1"})

if __name__ == "__main__":
    test()