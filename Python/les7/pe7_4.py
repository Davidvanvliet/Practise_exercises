#1723682
#David van Vliet

#een dictionary maken van een textdocument en de key en de value splitten met een :
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

#als de volledige naam wordt opgegeven moet het ticker symbol als output terugkomen
tickers = tickers()
naam = input('Enter company name: ')
print("Ticker symbol: ", (tickers[naam]))

#als het ticker symbool wordt opgegeven moet de volledige naam als output terugkkomen
symbool = input('Enter ticker symbool: ')
for woord, ticker in tickers.items():
    if ticker == symbool:
        print("Company name: ", woord)
