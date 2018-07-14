######################################################
# Stock Technical Analysis with Python               #
# File management module for symbols                 #
# Aroom Gonzalez                                     #
#                                                    #
# Current version: 0.0                               #
#                                                    #
######################################################


# 1. Import packages

import pandas as pd
from datetime import datetime
import pandas_datareader as web

# 2. Functions

def read_exchange_symbol_directory(file):
    df = pd.read_csv(file)
    return df

def download_yahoo_historical_data(dyhd_symbol, start_date, end_date):
    """
    Downloads historical data using yahoo API

    :param dyhd_symbol: symbol name as str
    :param start_date:
    :param end_date:
    :return: historical data supplied by yahoo's API
    :rtype: dataframe
    """
    dyhd_symbol_data = web.DataReader(dyhd_symbol, 'yahoo', start_date, end_date)
    return dyhd_symbol_data



# 3. Data initialization

# The following symbol directories were downloaded from
# https://www.nasdaq.com/screening/company-list.aspx
# file names were changed to be more explicit about their content
# open original files in excel, convert text to data, using the symbol '|', replace all commas with hyphen,
# and save as csv
EXCHANGE_FILES = ['Data\\nyse.csv', 'Data\\nasdaq.csv', 'Data\\amex.csv']
COLUMNS = [['Symbol', 'Name', 'LastSale', 'MarketCap', 'Sector', 'industry'],
           ['Symbol', 'Name', 'LastSale', 'MarketCap', 'Sector', 'industry'],
           ['Symbol', 'Name', 'LastSale', 'MarketCap', 'Sector', 'industry']]
end = datetime.today()
start = datetime(2000, 1, 1)
pd.set_option('display.expand_frame_repr', False)  # Forces to display all the info when printed


# 4. Initial calculations


# 5. Main module

for i in range(len(EXCHANGE_FILES)):
    directory_file = EXCHANGE_FILES[i]
    valid_columns = COLUMNS[i]
    df = pd.read_csv(directory_file, usecols=valid_columns)
    # Work only with symbols that have a defined sector:
    df = df[df['Sector'].notnull()]
    if i == 0:
        data_path = 'Data\\nyse'
    elif i == 1:
        data_path = 'Data\\nasdaq'
    elif i == 2:
        data_path = 'Data\\amex'
    for symbol in df['Symbol']:
        symbol_data = download_yahoo_historical_data(symbol, start, end)  # type: pandas.core.frame.DataFrame
        symbol_data = symbol_data.interpolate(method='linear')  # Fill NaN values using linear interpolation
        symbol_data.to_csv(data_path + symbol + '.csv')


# 6. Screen output

# 7. Files outputs

