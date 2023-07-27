from .BaslerCamera import BaslerCamera


def main():
    import sys
    import tango.server

    args = ["BaslerCamera"] + sys.argv[1:]
    tango.server.run((BaslerCamera,), args=args)
