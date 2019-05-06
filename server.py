#!/usr/bin/python3
import socket, pickle, os, sys

def main():
    help = "Usage: [HOST] [PORT]"

    try:
        host = sys.argv[1]
        port = sys.argv[2]
    except IndexError:
        print(help)
        sys.exit()

    print("This program is intened to share todo between machines")
    print("It must be running in order to get the todos")
    print("If you create a todo while the server isn't running it won't be backed up\n")
    print(f"Server running on {host}:{port}")

main()