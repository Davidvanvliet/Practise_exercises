#1723682
#David van Vliet

def tickers():
    with open ('tickerfile.txt','r') as document1:
        tickers = {}
        for line in document1:
            line = line.strip()
            if not line:
                continue
            key, value = line.split(':')
            tickers[key] = value
    return tickers

tickers = tickers()
naam = input('Enter company name: ')
print("Ticker symbol: ", (tickers[naam]))

symbool = input('Enter ticker symbool: ')
for woord, ticker in tickers.items():
    if ticker == symbool:
        print("Company name: ", woord)
