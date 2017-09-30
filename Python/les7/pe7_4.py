#1723682
#David van Vliet


with open ('tickerfile.txt','r') as document1:
    tickers = {}
    for line in document1:
        line = line.strip()
        if not line:
            continue
        key, value = line.split(':')
        tickers[key] = value

print(tickers)
