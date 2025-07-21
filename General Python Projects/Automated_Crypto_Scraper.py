from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime
import os
import time

def automated_crypto_scraper():
    url = 'https://coinmarketcap.com/currencies/bitcoin/'
    
    page = requests.get(url)
    
    soup = BeautifulSoup(page.text, 'html')
    
    crypto_name = soup.find('span', class_ = 'sc-65e7f566-0 lsTl').text
    
    crypto_price = soup.find('span', class_ = 'sc-65e7f566-0 WXGwg base-text').text
    
    final_price = crypto_price.replace('$','')
    
    date_time = datetime.now()
    
    dict = {'Crypto Name': crypto_name,
           'Price': final_price,
           'TimeStamp': date_time}
    
    df = pd.DataFrame([dict])
    
    df.to_csv(r'C:\Users\wgephar\OneDrive - Purdue Research Foundation\Documents\Python Tutorial\Crypto Web Puller\Automated_Crypto_Scraper.csv', index = False)
    
    if os.path.exists(r'C:\Users\wgephar\OneDrive - Purdue Research Foundation\Documents\Python Tutorial\Crypto Web Puller\Automated_Crypto_Scraper.csv'):
        df.to_csv(r'C:\Users\wgephar\OneDrive - Purdue Research Foundation\Documents\Python Tutorial\Crypto Web Puller\Automated_Crypto_Scraper.csv', mode='a', header = False, index = False)
    else:
        df.to_csv(r'C:\Users\wgephar\OneDrive - Purdue Research Foundation\Documents\Python Tutorial\Crypto Web Puller\Automated_Crypto_Scraper.csv', index = False)
    print(df)

while True:
    automated_crypto_scraper()
    time.sleep(10)
