import argparse
import sys
import uuid

from repl import repl


def _get_id():
    return "id" + str(uuid.uuid1().fields[-1])[:5]


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--channel",
        "-c",
        help="Name of the channel to connect, default='flood'",
        default="flood",
    )
    parser.add_argument(
        "--nick",
        "-n",
        help="Your name that will be shown in the chat",
        default=_get_id(),
    )

    args = parser.parse_args(args=argv)
    repl(initial_channel=args.channel, nickname=args.nick)


if __name__ == "__main__":
    main(sys.argv[1:])
