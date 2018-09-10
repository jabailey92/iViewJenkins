import tkinter
import argparse
from jConnection import jConn

def createParser():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--ip', help="Jenkins IP Address", required=True)
    parser.add_argument('--user', help="Jenkins user to connect with", required=True)
    parser.add_argument('--apiToken', help="Jenkins API token to use", required=True)
    return parser


if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()
    conn = jConn(args.ip, args.user, args.apiToken)
    #top = tkinter.Tk()
    #top.mainloop()
