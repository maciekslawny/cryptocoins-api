from json import loads
from requests import get

AMOUNT_OF_COINS = 15
url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page={AMOUNT_OF_COINS}&page=1&sparkline=false'
all_coins_data = loads(get(url).text)



def create_coin():
    coins_list = []
    for coin in all_coins_data:
        opis = ''
        if (coin == all_coins_data[0] or coin == all_coins_data[1] or coin == all_coins_data[2]):
            coin_id = coin['id']
            coin_url = f'https://api.coingecko.com/api/v3/coins/{coin_id}'
            opis = loads(get(coin_url).text)['description']['en']
        coin_info = [coin['name'], coin['current_price'], round(coin['price_change_percentage_24h'], 1), coin['image'], coin['ath'], coin['ath_date'], opis]
        coins_list.append(coin_info)
        
    return coins_list

create_coin()
