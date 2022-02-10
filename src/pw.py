#! /usr/bin/python3

# Repositório de senhas que não é seguro

import pyperclip
import sys

def readPassword(key, dict):
    return dict[key]

# def updatePassword(key, value, dict):
#     dict.setdefault(key, value)

passwords = {'email': 1234, 'blog': 567}


if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()


doing = sys.argv[1]
if doing == 'read':
    account = sys.argv[2]
    if account in passwords:
        pyperclip.copy(readPassword(account, passwords))
        print(f'Password for {account} copied to clipboard')
    else:
        print(f"There's no account named {account}")

# elif todo == 'update':
#     account = sys.argv[2]
#     password = sys.argv[3]
#     updatePassword(account, password, passwords)
#     print(passwords) 