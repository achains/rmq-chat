import argparse
import sys

from repl import repl


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('channel', type=str)

    args = parser.parse_args(args=argv)
    repl(initial_channel=args.channel)


if __name__ == '__main__':
    main(sys.argv[1:])
