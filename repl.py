__all__ = ["repl"]

import sys

from chat import Chat


def _exit_repl(chat: Chat):
    chat.finish()
    sys.exit(0)


def _handle_command(chat: Chat, cmd: str):
    commands = {
        "switch": lambda channel: chat.change_topic(channel),
        "exit": lambda: _exit_repl(chat),
    }
    command_name, *args = cmd.split()
    commands[command_name](*args)


def repl(initial_channel: str, nickname: str):
    chat = Chat(nickname=nickname, topic=initial_channel)
    chat.activate()

    try:
        while True:
            msg = input("")
            if msg.startswith("!"):
                try:
                    _handle_command(chat, msg.strip("!"))
                except KeyError:
                    print("Error: Invalid command")
            else:
                chat.send_message(msg=msg)
    except KeyboardInterrupt:
        _exit_repl(chat)
