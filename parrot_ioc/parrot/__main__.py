import textwrap

import caproto.server

from .parrot import Parrot


def main():
    ioc_options, run_options = caproto.server.ioc_arg_parser(
        default_prefix='pa0:',
        desc=textwrap.dedent(Parrot.__doc__)
    )

    ioc = Parrot(**ioc_options)
    caproto.server.run(ioc.pvdb, **run_options)


if __name__ == '__main__':
    main()
