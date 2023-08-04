# 官方文档地址：https://click-docs-zh-cn.readthedocs.io/zh/latest/index.html

# 需求：使用上下文值作为 click.option() 默认值
import click

@click.group()
@click.pass_context
def cli(ctx):
    """
    CLI
    """
    ctx.ensure_object(dict)
    ctx.obj['DEFAULT_ENVIRONMENT'] = "dev"


def default_from_context(default_name):

    class OptionDefaultFromContext(click.Option):

        def get_default(self, ctx):
            self.default = ctx.obj[default_name]
            return super(OptionDefaultFromContext, self).get_default(ctx)

    return OptionDefaultFromContext

@cli.command()
@click.option('-e', '--environment', required=True,
              cls=default_from_context('DEFAULT_ENVIRONMENT'))
def show_env(environment):
    click.echo(environment)

# 错误的写法
# @cli.command()
# @click.option('-e', '--environment', required=True, default=click.get_current_context().obj['DEFAULT_ENVIRONMENT'])
# def show_env(environment):
#     click.echo(environment)


if __name__ == "__main__":
    commands = (
        'show_env',
        '--help',
    )

    import sys, time
    time.sleep(1)
    print('Click Version: {}'.format(click.__version__))
    print('Python Version: {}'.format(sys.version))
    for cmd in commands:
        try:
            time.sleep(0.1)
            print('-----------')
            print('> ' + cmd)
            time.sleep(0.1)
            cli(cmd.split())

        except BaseException as exc:
            if str(exc) != '0' and \
                    not isinstance(exc, (click.ClickException, SystemExit)):
                raise