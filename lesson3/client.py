import json
import socket
import sys
import time
from socket import *

from common.utils import send_message, get_message
from common.variables import *


def process_ans(message):
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def create_presence(account_name='Guest'):
    out = {
        ACTION: PRESENSE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def main():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапозоне от 1024 до 65535')
        sys.exit(1)
    transport = socket(AF_INET, SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    try:
        send_message(transport, message_to_server)
        message_from_server = get_message(transport)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')
        sys.exit(1)
    status_message = process_ans(message_from_server)
    print(status_message)
    sys.exit(1)


if __name__ == '__main__':
    main()
