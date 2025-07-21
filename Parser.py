import os
import csv
import operator
from datetime import datetime

class Parser:

    def __init__(self, filename, indexes, date_format, line_diff):
        self.__location__ = os.path.dirname(os.path.realpath(__file__))
        self.filename = filename
        self.indexes = indexes
        self.date_format = date_format
        self.line_diff = line_diff # Defines the number of lines to skip at the beginning of the csv before you get to the actual data
    
    def handle_negative(self, amount):

        if amount=='':
            return amount

        amount = float(amount)

        if amount < 0:
            amount *= -1

        return amount

    def parse_file(self):
        try:
            with open(f"{self.__location__}\\{self.filename}", 'r') as read_file:

                reader = csv.reader(read_file, delimiter=',')

                for i in range(self.line_diff):
                    next(read_file) # Point to the next line in the csv

                with open(f"{self.__location__}\\unsorted_csv.csv", 'a+', newline='') as write_file:
                    writer = csv.writer(write_file, delimiter=',')
                    for line in reader:
                        if line != []:
                            writer.writerow([datetime.strptime(line[self.indexes[0]], self.date_format).strftime('%m/%d/%Y'), 
                                             line[self.indexes[1]], 
                                             self.handle_negative(line[self.indexes[2]]), 
                                             self.handle_negative(line[self.indexes[3]])]) # should write date, description, debit, credit
                        else:
                            break
        except FileNotFoundError:
            pass

    