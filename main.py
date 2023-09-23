import argparse
from DBConnection import DBConnection, Client

parser = argparse.ArgumentParser(description='A DBMS written in python')

parser.add_argument('-s','--server', default=False, help='Start the dbms')
parser.add_argument('-c' '--client', default=True, help='Stop any running instances of the DB')
args = parser.parse_args()
print(args)


def start_dbms():
    if args.server:
        connection = DBConnection()
    else:
        client_connection = Client()
        client_connection.connect()

def main():
    start_dbms()

if __name__ == '__main__':
    main()