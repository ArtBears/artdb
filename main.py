import argparse
from DBConnection import DBConnection

parser = argparse.ArgumentParser(description='A DBMS written in python')

parser.add_argument('--start', default=True, help='Start the dbms')
parser.add_argument('--stop', default=False, help='Stop any running instances of the DB')
args = parser.parse_args()
print(args)


def start_dbms():
    connection = DBConnection()

def main():
    start_dbms()

if __name__ == '__main__':
    main()