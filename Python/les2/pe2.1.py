#1723682
#David van Vliet

letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')
freq = [0 for _ in range(3)]
for c in letters:
    freq[ord(c) - ord('A')] += 1

print(freq)

#Telt het aantal keren dat een letter voorkomt



