import os
import sys

from chat import Chat

if __name__ == "__main__":
    try:
        nick = sys.argv[1]
        Chat(nickname=nick).run()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
