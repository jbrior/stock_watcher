from bs4 import BeautifulSoup
import requests
import time
import random
import csv

# Define Company Stock URL's
urls = {
    'Apple': 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch',
    'Amazon': 'https://finance.yahoo.com/quote/AMZN?p=AMZN&.tsrc=fin-srch',
    'Lifevantage': 'https://finance.yahoo.com/quote/LFVN?p=LFVN&.tsrc=fin-srch'
}

# Define/Set default index & stock prices
x_value = 0
y_value1 = 1000.0
y_value2 = 1000.0
y_value3 = 1000.0

# Define fieldnames for csv file
fieldnames = ["x_value", "y_value1", "y_value2", "y_value3"]

# Create csv file to store prices for chart
# Write header(fieldnames) for data
with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
    csv_writer.writeheader()

# Function to get company stock price for specified url
def get_stock_price(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    current_price_code = soup.find('div', class_='quote-header-section Cf Pos(r) Mb(5px) '
                                                 'Maw($maxModuleWidth) Miw($minGridWidth) '
                                                 'smartphone_Miw(ini) Miw(ini)!--tab768 Miw(ini)!--tab1024 Mstart(a) '
                                                 'Mend(a) Px(20px) smartphone_Pb(0px) smartphone_Mb(0px)')
    c_price = current_price_code.find('span', class_='Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)').text

    # Check if text has comma
    # And take out comma to cast from String to Float
    if ',' in c_price:
        c_price = c_price.replace(',', '')

    return float(c_price)

# Infinite loop to write current price to data.csv
while True:

    # Start appending prices to data.csv
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

        info = {
            "x_value": x_value,
            "y_value1": get_stock_price(urls['Apple']),
            "y_value2": get_stock_price(urls['Amazon']),
            "y_value3": get_stock_price(urls['Lifevantage'])
        }

        csv_writer.writerow(info)
        print(x_value, get_stock_price(urls['Apple']), get_stock_price(urls['Amazon']),
              get_stock_price(urls['Lifevantage']))

    x_value += 1

    # ------------ For testing ------------
    # y_value1 = y_value1 + random.randint(-20, 20)
    # y_value2 = y_value2 + random.randint(-20, 20)
    # y_value3 = y_value3 + random.randint(-20, 20)

    time.sleep(1)
