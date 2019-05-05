#!/usr/bin/python3
import socket, pickle, os, sys

help = "Usage: [HOST] [PORT]"

try:
    host = sys.argv[1]
    port = sys.argv[2]
except IndexError:
    print(help)
    sys.exit()

print(f"Server running on {host}:{port}")