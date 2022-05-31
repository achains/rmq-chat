__all__ = ['repl']

import sys


class Chat:
    def __init__(self):
        self.current_channel = ""

    def change_channel(self, channel: str):
        print(f"== Connected to {channel} ==")
        return 0

    def send_msg(self, msg: str):
        pass


def _handle_command(chat: Chat, command: str):
    COMMANDS = {
        "switch": lambda channel: chat.change_channel(channel),
        "exit": lambda: sys.exit(0)
    }
    cmd, *args = command.split()
    COMMANDS[cmd](*args)


def repl(initial_channel: str):
    chat = Chat()
    chat.change_channel(initial_channel)

    while True:
        msg = input(">> ")
        if msg.startswith('!'):
            try:
                _handle_command(chat, msg.strip('!'))
            except KeyError:
                print("Error: Invalid command")
        else:
            chat.send_msg(msg=msg)
