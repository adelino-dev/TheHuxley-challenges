def getBets(bets = {}):

    bet = input().split()
    name = bet[0]
    numbers = bet[1:]

    if bet[0] =="FIM":
        return bets

    else:
        bets[name] = numbers
        return getBets(bets=bets)


def calcHits(bets, rightNumbers):
    names = bets.keys()
    
    names_hits = {}
    for name in names:
        numbers = bets[name]
        hits = 0
        for number in numbers:
            if number in rightNumbers:
                hits += 1

        names_hits[name] = hits

    return names_hits


def getRank(names_hits):
    names = bets.keys()
    hits_values = []
    rank = []

    for name in sorted(names):
        hits = str(names_hits[name])
        rank.append(hits+" "+name)
        hits_values.append(hits)
    
    
    isTied = len(set(hits_values)) == 1

    if not isTied:
        rank.sort()

    for i in range(len(rank)):
        name = (rank[i].split())[1]
        hits = names_hits[name]

        if hits > 0:
            hits = "+"*names_hits[name]
            rank[i] = name+" "+hits

        else:
            rank[i] = name

    return rank


bets = getBets()
rightNumbers = input().split('-')
names_hits = calcHits(bets, rightNumbers)
rank = getRank(names_hits)

for string in rank:
    print(string)