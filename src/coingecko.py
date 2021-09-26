import requests 
import json 
 
print("Enter number of crypto currencies to pull:") 
while True: 
    num_of_cryptos = input() 
    if num_of_cryptos.isdecimal(): 
        num_of_cryptos = int(num_of_cryptos) 
        break 
    else: 
        print("Entered input is not a number") 
 
cryptos = [] 
 
n = 1 
while len(cryptos) < num_of_cryptos: 
    r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page='+ str(n) +'&sparkline=false').text 
    r_json = json.loads(r) 
 
    if len(r_json) == 0: 
        print('The number is too big, showing ' + str(len(cryptos)) + ' cryptos') 
        break 
 
    cryptos += list(map(lambda crypto: crypto['id'], r_json[0:(num_of_cryptos-len(cryptos))])) 
    n += 1 
print(cryptos)