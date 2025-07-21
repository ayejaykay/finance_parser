import csv
import os
import shutil
import operator
from datetime import date
from datetime import datetime

file_info = {
        "anthony_checking": {
            "filename": "CHK_8314_CURRENT_VIEW.csv", 
            "line_indexes": [1, 2, 3, 4]
        },
        "anthony_credit": {
            "filename": date.today().strftime("%Y-%m-%d") + "_transaction_download.csv",
            "line_indexes": [0, 3, 5, 6],
        },
        "alli_checking": {
            "filename": "",
            "line_indexes": [],
        },
        "alli_credit": {
            "filename": "",
            "line_indexes": [],
        }
}

class File:

    def __init__(self) -> None:
        self.__location__ = os.path.dirname(os.path.realpath(__file__))
        self.filename_checking = "CHK_8314_CURRENT_VIEW.csv"
        self.filename_credit = date.today().strftime("%Y-%m-%d") + "_transaction_download.csv"

    def mvdir_to_cwd(self):
        shutil.move(f'C:\\Users\\akahl\\Downloads\\{self.filename_checking}', f'{self.__location__}')
        shutil.move(f'C:\\Users\\akahl\\Downloads\\{self.filename_credit}', f'{self.__location__}')

    def delete_transactions(self):
        os.remove(f"{self.__location__}\\{self.filename_checking}")
        os.remove(f"{self.__location__}\\{self.filename_credit}")

    def clear_csv(self):
        open(f"{self.__location__}\\unsorted_csv.csv", 'w').close()

    def clear_files(self):
        open(f"{self.__location__}\\file.csv", 'w').close()
        open(f"{self.__location__}\\final.csv", 'w').close()

        

class Parse:

    def __init__(self) -> None:
        self.files = File()
        self.line = []
        self.filename_checking = self.files.filename_checking
        self.filename_credit = self.files.filename_credit
        self.checking_fields = [datetime.strptime(self.line[1], '%m-%d-%Y').strftime('%m/%d/%Y'), self.line[2], self.line[3], self.line[4]]
        self.credit_fields = [datetime.strptime(self.line[0], '%Y-%m-%d').strftime('%m/%d/%Y'), self.line[3], self.line[5], self.line[6]]

    def parse_csv(self):
        self.parse_checking()
        self.parse_credit()
        self.sort_csv()

    def parse_checking(self):
        with open(f"{self.files.__location__}\\{self.filename_checking}", 'r') as read_file:
            reader = csv.reader(read_file, delimiter=',')
            next(read_file)
            with open(f"{self.files.__location__}\\unsorted_csv.csv", 'a+', newline='') as write_file:
                writer = csv.writer(write_file, delimiter=',')
                for line in reader:
                    if line != []:
                        writer.writerow([datetime.strptime(line[1], '%m-%d-%Y').strftime('%m/%d/%Y'), line[2], line[3], line[4]]) # should write date, description, debit, credit
                    else:
                        break
        print("checking written")

    def parse_credit(self):
        with open(f"{self.files.__location__}\\{self.filename_credit}", 'r') as read_file:
            reader = csv.reader(read_file, delimiter=',')
            next(read_file)
            with open(f"{self.files.__location__}\\unsorted_csv.csv", 'a+', newline='') as write_file:
                writer = csv.writer(write_file, delimiter=',')
                for line in reader:
                    if line != []:
                        writer.writerow([datetime.strptime(line[0], '%Y-%m-%d').strftime('%m/%d/%Y'), line[3], line[5], line[6]]) # should write date, description, debit, credit
                    else:
                        break
        print("credit written")

    def parse_file(self):
        # file_type = get_file_type()
        with open(f"{self.files.__location__}\\{self.filename_credit}", 'r') as read_file:
            reader = csv.reader(read_file, delimiter=',')
            next(read_file)
            with open(f"{self.files.__location__}\\unsorted_csv.csv", 'a+', newline='') as write_file:
                writer = csv.writer(write_file, delimiter=',')
                for line in reader:
                    if line != []:
                        writer.writerow([datetime.strptime(line[0], '%Y-%m-%d').strftime('%m/%d/%Y'), line[3], line[5], line[6]]) # should write date, description, debit, credit
                    else:
                        break

    def sort_csv(self):
        data = csv.reader(open(f'{self.files.__location__}\\unsorted_csv.csv'), delimiter=',')
        data = sorted(data, key=operator.itemgetter(0))
        with open(f"{self.files.__location__}\\final.csv", 'a+', newline='') as write_file:
            writer = csv.writer(write_file, delimiter=',')
            for line in data:
                writer.writerow(line)
        print("csv sorted")

    
    

def main():
    files = File()
    parser = Parse()
    files.clear_files()
    files.mvdir_to_cwd()
    parser.parse_csv()
    files.delete_transactions()
    files.clear_csv()

if __name__ == "__main__":
    main()
