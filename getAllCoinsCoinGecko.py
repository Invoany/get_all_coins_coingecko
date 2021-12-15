import json
import requests
import pandas as pd
from datetime import datetime
import os

base_url = "https://api.coingecko.com/api/v3/"
output_folder= "Output"
#Use this to obtain all the coins' id in order to make API calls

def get_coins_list_coingecko():
    print("Getting the List with all the Coins under CoinGecko")
    response = requests.get(base_url + "coins/list")
    print("Request Url = {}".format(response.url))
    response_json = json.loads(response.text)
    all_coins = pd.DataFrame.from_dict(response_json)
    all_coins.index.name = 'index'
    print("Retrieved a Total of {} Coins".format(str(len(all_coins)) ))
    print(all_coins)
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)
    try:
        all_coins.to_csv(os.path.join(output_folder, 'AllCoins_CoinGecko_{}.csv'.format(str(datetime.today().strftime('%Y%m%d'))) ))
    except:
        print("It was not possible to save/create the file")
    return all_coins