from bs4 import BeautifulSoup
import requests
import yfinance as yf
import pandas as pd

# import json
# with open('amd.json') as json_file:
#     amd_info = json.load(json_file)
#     # Print the type of data variable    
#     #print("Type:", type(apple_info))
# amd_info

# print(amd_info["country"])
# print(amd_info["sector"])
# amd = yf.Ticker("AMD")
# amd_share_price_data = amd.history(period="max")

# print(amd_share_price_data.head())


# amd = yf.Ticker("AMD")
# def main():
#     print()

# if __name__=="__main__":
#     main()

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"

data  = requests.get(url).text

soup = BeautifulSoup(data, 'html5lib')
print(soup.find_all("title"))

# Amazon.com, Inc. (AMZN) Stock Historical Prices &amp; Data - Yahoo Finance

amazon_data = pd.DataFrame()

accumulator = []
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text
    accumulator.append([date,Open,high,low,close,adj_close,volume])

amazon_data = pd.DataFrame(accumulator, columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"], index=None)

print(amazon_data.head)
    
# Date      Open      High       Low     Close Adj Close       Volume
# 0   Jan 01, 2021  3,270.00  3,363.89  3,086.00  3,206.20  3,206.20   71,528,900
# 1   Dec 01, 2020  3,188.50  3,350.65  3,072.82  3,256.93  3,256.93   77,556,200
# 2   Nov 01, 2020  3,061.74  3,366.80  2,950.12  3,168.04  3,168.04   90,810,500
# 3   Oct 01, 2020  3,208.00  3,496.24  3,019.00  3,036.15  3,036.15  116,226,100
# 4   Sep 01, 2020  3,489.58  3,552.25  2,871.00  3,148.73  3,148.73  115,899,300
# ..           ...       ...       ...       ...       ...       ...          ...
# 56  May 01, 2016    663.92    724.23    656.00    722.79    722.79   90,614,500
# 57  Apr 01, 2016    590.49    669.98    585.25    659.59    659.59   78,464,200
# 58  Mar 01, 2016    556.29    603.24    538.58    593.64    593.64   94,009,500
# 59  Feb 01, 2016    578.15    581.80    474.00    552.52    552.52  124,144,800
# 60  Jan 01, 2016    656.29    657.72    547.18    587.00    587.00  130,200,900

# [61 rows x 7 columns]>


    # Finally we append the data of each row to the table
# for link in soup.find_all("a", href=True):
#     print(link.get("href"))