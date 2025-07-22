import os
import shutil

class File:

    def __init__(self, file_info) -> None:
        self.__location__ = os.path.dirname(os.path.realpath(__file__))
        self.filename = file_info["filename"]
        self.line_indexes = file_info["line_indexes"]
        self.date_format = file_info["date_format"]
        self.line_diff = file_info["line_diff"] # Defines how many lines to skip at the beginning of each of the CSV files.
        if not self.mvdir_to_cwd():
            return 


    def mvdir_to_cwd(self):
        try:
            new_loc = shutil.move(f'{os.path.expanduser("~")}\\Downloads\\{self.filename}', f'{self.__location__}')
            print(f"File {self.filename} moved to {new_loc}")
            return 1
        except FileNotFoundError:
            print(f"File {self.filename} not found")
            return 0

    def delete_transactions(self):
        try:
            os.remove(f"{self.__location__}\\{self.filename}")
        except FileNotFoundError:
            pass

    def clear_csv(self):
        try:
            open(f"{self.__location__}\\unsorted_csv.csv", 'w').close()
        except FileNotFoundError:
            pass
    
