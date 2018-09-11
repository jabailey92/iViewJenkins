from GUI import GUI
import argparse
from jConnection import jConn
from ViewerLogging import logger

def createParser():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('--ip', help="Jenkins IP Address", required=True)
    parser.add_argument('--user', help="Jenkins user to connect with", required=True)
    parser.add_argument('--apiToken', help="Jenkins API token to use", required=True)
    parser.add_argument('--verbose', help="Verbose", action='store_true')
    return parser


if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()
    log = logger(args.verbose)
    conn = jConn(args.ip, args.user, args.apiToken, log)
    jobs = conn.get_all_jobs()
    gui = GUI(jobs, log, conn)
