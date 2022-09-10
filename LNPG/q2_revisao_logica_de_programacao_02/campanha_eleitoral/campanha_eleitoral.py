def getPrice(media):
    prices = {
    "internet":3000.0,
    "revista":750.0,
    "outdoor":1500.0,
    "radiofm":500.0,
    "radioam":300.0, 
    "tv20":1200.0,
    "tv20+":2000.0
    }

    return prices[media]

def printResult(candidate, medias):
    price = 0
    for media in medias:
        price += getPrice(media)
    
    print("%s: %.2f" % (candidate, price) )

if __name__ == "__main__":
    data = {}

    while True:
        text = input()

        if text == "FIM":
            break

        else:

            candidate, qnt = text.split()
            medias = []

            for i in range(int(qnt)):
                media = input()

                if media == "radio":
                    media += input()
                
                elif  media == "tv":
                    h = int(input())
                    if h > 20:
                        media += '20+'
                    else:
                        media += '20'

                medias.append(media)

            data[candidate] = medias

    for candidate in data:
        medias = data[candidate]
        printResult(candidate, medias)
    
