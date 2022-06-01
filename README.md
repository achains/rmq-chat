# rmq-chat
Multi-user chat on Python using RabbitMQ
## Usage
```bash
$ python main.py --channel=<channel_name> --nick=<nickname>
```

## Example
```bash
$ python main.py --channel=flood --nick=achains

[INFO] Current topic flood
Hello world!
achains [06/01/2022, 14:55:40]: Hello world!
!switch work
[INFO] Current topic work
Hello work!
achains [06/01/2022, 14:56:02]: Hello work!
!exit
== Closing connection ==
```

## Contributors
- Kirill Ivanov
- Arthur Saliou
