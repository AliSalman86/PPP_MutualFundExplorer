# importing CSV module tp be used for reading/parsing/writing data from .csv files
import csv

class Portfolio:
    def __init__(self, portfolio_name, *funds):
        self.portfolio = portfolio_name
        self.funds = funds
        self.funds_list = []

class Fund:
    pass

# open the file for reading
with open("Resources/COWZ-holdings.csv", "r") as fund_csv:
    csv_reader = csv.reader(fund_csv)
    # converting the csv object to a list so it can be easy to handle
    fund_csv_data = list(csv_reader)
    # Next line added for developing/debuging prposes only
    # print(fund_csv_data[:16])
    # Data need to be cleaned up before parsing to info, header, and actual holdings data
    # blank rows need to be removed as well
    # The data being read from the CSV can be classified to: ignored (empty rows), info (The fund info like name, inception date and AUM),
    # header data, and holdings data
    # We can use the logic of each row length to determine the data type


    # holdings_csv_parser:
    """ holding_csv_parser is a function that accept one read csv document (document) as an argument and parse the data contained as
        1) ignorable (not usable) if the row is empty
        2) fund info: when the length of the row is 1
        3) header: when the length of the row is equal to the length of data fields but the header_fullfilled switch still false
        4) data: when the header marked as recorded and length of the raw equal to data fields
        the method to return the fund data list at the end
    """ 

    def holdings_csv_parser(document):
        # let's define some global variables:
        fund_data_list = [] # => The list to contain all parsed data as list of disctionaries
        info_lines_list = []    # => a list to hold multiple lines of data deemed as (info)
        # Define counters:
        ignored_lines_counter = 0
        info_lines_counter = 0
        # Swiches, marks and trigger(s):
        header_fullfilled = False   # a trigger that is false when no header is accounted for and switch to True and mark header as found
        # iterating through the list of read csv
        for line in document[:16]:
            # ignore the line if length is 0
            if len(line) == 0:
                ignored_lines_counter += 1
            
            elif len(line) == 1:
                fund_data_list.append({
                    "Data Type": "info",
                    "Fund Info": line
                })
                info_lines_counter += 1
            
            elif len(line) == 3 and not header_fullfilled:
                fund_data_list.append({
                    "Data Type": "header",
                    "Fund Name H": line[0],
                    "Fund Ticker H": line[1],
                    "Fund Weight H": line[2]
                })
                header_fullfilled = True

            elif len(line) == 3 and header_fullfilled:
                fund_data_list.append({
                    "Data Type": "Data",
                    "Fund Name": line[0],
                    "Fund Ticker": line[1],
                    "Fund Weight": line[2]
                })

        print(ignored_lines_counter)
        print(info_lines_counter)
        return fund_data_list

cowz_sheet = holdings_csv_parser(fund_csv_data)
print(cowz_sheet)