metas = []

n = int(input())
for i in range(n):
    meta = input()
    metas.append(meta)

m = int(input())
for i in range(m):
    concluida = input()
    if concluida in metas:
        metas.remove(concluida)

pendentes = len(metas)

if pendentes > 0:
    print("Ainda falta(m) %i objetivo(s)!" % len(metas))
    for meta in metas:
        print(meta)

else:
    print("Smelly Cat, Smelly Cat, what are they feeding you?")