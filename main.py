#!/usr/bin/python3

import sys, server, getopt

def main(argv):
    try:
      opts, args = getopt.getopt(argv,"h:p:",["host=","port="])
    except getopt.GetoptError:
      print("Usage: main.py -h <HOST> -p <PORT>")
      sys.exit(2)
    if len(opts) < 2:
        print("Usage: main.py -h <HOST> -p <PORT>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            host = str(arg)
        if opt == "-p":
            port = int(arg)
    server.run(host, port)        

if __name__ == "__main__":
    main(sys.argv[1:])