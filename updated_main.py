import os
import argparse
from File import *
from Parser import *
from datetime import date
from datetime import datetime

__location__ = os.path.dirname(os.path.realpath(__file__))

parser = argparse.ArgumentParser(prog="Finance Parsing")
parser.add_argument("-u", "--user", nargs=1, required=False)
args = parser.parse_args()

anthony = {
    "checking": {
        "filename": "Export.csv", 
        "line_indexes": [1, 2, 4, 5],
        "date_format": '%m/%d/%Y',
        "line_diff": 4,
    },
    "credit": {
        "filename": date.today().strftime("%Y-%m-%d") + "_transaction_download.csv",
        "line_indexes": [0, 3, 5, 6],
        "date_format": '%Y-%m-%d',
        "line_diff": 1,
    },
}

alli = {
    "checking": {
        "filename": "export.csv",
        "line_indexes": [0, 2, 3, 4],
        "date_format": '%m/%d/%Y',
        "line_diff": 1,
    },
    "credit": {
        "filename": date.today().strftime("%Y-%m-%d") + "_transaction_download.csv",
        "line_indexes": [0, 3, 5, 6],
        "date_format": '%Y-%m-%d',
        "line_diff": 1,
    },
}

def clear_files():
        open(f"{__location__}\\unsorted_csv.csv", 'w').close()
        open(f"{__location__}\\file.csv", 'w').close()
        open(f"{__location__}\\final.csv", 'w').close()

def sort_csv():
        data = csv.reader(open(f'{__location__}\\unsorted_csv.csv'), delimiter=',')
        data = sorted(data, key=operator.itemgetter(0))
        with open(f"{__location__}\\final.csv", 'a+', newline='') as write_file:
            writer = csv.writer(write_file, delimiter=',')
            for line in data:
                writer.writerow(line)
        print("csv sorted")

def main():
    clear_files()
    if (not args.user == None):
        if args.user[0] == "Alli":
            files = [File(alli["checking"]), File(alli["credit"])]
        else:
            files = [File(anthony["checking"]), File(anthony["credit"])]
    else:
        files = [File(anthony["checking"]), File(anthony["credit"])]
    
    for file in files:
        Parser(file.filename, file.line_indexes, file.date_format, file.line_diff).parse_file()
        file.delete_transactions()

    sort_csv() 

if __name__ == "__main__":
    main()