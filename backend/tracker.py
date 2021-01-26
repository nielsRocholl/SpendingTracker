import csv
import os
import datetime


class Write:
    def __init__(self):
        self.money = 0
        self.destination = 'Data/data.csv'
        self.column_titles = ["Date", "Total Balance", "Trading 212", "BlockFi", "Savings Account",
                              "Checking Account", ]
        self.w = 'w'
        self.a = 'a'
        self.date = datetime.date.today().strftime("%d/%m/%Y")
        self.total_balance = self.retrieve_most_recent()[0][2]
        self.trading212 = self.retrieve_most_recent()[0][3]
        self.blockfi = self.retrieve_most_recent()[0][4]
        self.savings_account = self.retrieve_most_recent()[0][5]
        self.checking_account = self.retrieve_most_recent()[0][6]

    '''
    Add data to data.csv
    '''

    def add_data(self):
        self.mkdir()
        with open(self.destination, self.a, newline='') as file:
            writer = csv.writer(file)
            writer.writerow([str(self.date), str(self.total_balance), str(self.trading212), str(self.blockfi),
                             str(self.savings_account), str(self.checking_account)])

    '''
    create directory if it does not exists
    '''

    def mkdir(self):
        # create data.csv if it does not exist, this file holds all data
        if not os.path.exists(self.destination):
            os.mkdir(self.destination)
        else:
            # if it does exists check if the column titles are correct
            with open(self.destination, newline='') as f:
                reader = csv.reader(f)
                row1 = next(reader)
                if not row1 == self.column_titles:
                    self.write(self.column_titles, self.w)

    '''
    Write a row to data.csv
    '''

    def write(self, item, write_append):
        with open(self.destination, write_append, newline='') as file:
            writer = csv.writer(file)
            writer.writerow(item)

    '''
    Returns last row from data.csv
    '''

    def retrieve_most_recent(self):
        return self.import_csv()[-1]

    '''
    Stores all date in data.csv in data
    '''

    def import_csv(self):
        data = []
        row_index = 0
        with open(self.destination, "r", encoding="utf-8", errors="ignore") as scraped:
            reader = csv.reader(scraped, delimiter=',')
            for row in reader:
                if row:  # avoid blank lines
                    row_index += 1
                    columns = [str(row_index), row[0], row[1], row[2], row[3], row[4], row[5]],
                    data.append(columns)
        return data

    '''
    print most recent addition to data.csv
    '''

    def print_most_recent_data(self):
        print(self.total_balance)
        print(self.trading212)
        print(self.blockfi)
        print(self.savings_account)
        print(self.checking_account)

    '''
    Update data
    '''

    def update_data(self, trading212=None, blockfi=None, savings=None, checking=None):
        if trading212 is not None:
            self.trading212 = trading212
        if blockfi is not None:
            self.blockfi = blockfi
        if savings is not None:
            self.savings_account = savings
        if checking is not None:
            self.checking_account = checking
        self.total_balance = int(self.trading212) + int(self.blockfi) + int(self.savings_account) + \
                             int(self.checking_account)
        self.add_data()
