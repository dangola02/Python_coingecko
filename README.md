# Python_coingecko
Python program that pulls N amount of crypto currencies sorted by market capitalization.
## Instalation
Program uses requests and json library to send HTTP request and get data in json format.

```shell
-pip install requests
```

## Usage

To run type these commands:

```shell
cd src/
python3 coingecko.py
```

To run tests type following commands:

```shell
cd test/
python3 test.py
```

## Examples

Here is the example of usage:

```shell
Enter number of crypto currencies to pull:
15
['bitcoin', 'ethereum', 'cardano', 'tether', 'binancecoin', 'ripple', 'solana', 'usd-coin', 'polkadot', 'dogecoin', 'avalanche-2', 'terra-luna', 'binance-usd', 'uniswap', 'cosmos']
