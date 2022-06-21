def inverter(palavra, **kwargs):
    if "inverso" in kwargs:
        if len(kwargs["inverso"]) < len(palavra):
            num = kwargs["i"]+1
            kwargs["inverso"] += palavra[-num]
            return inverter(palavra, inverso = kwargs["inverso"], i = num)
        else:
            return kwargs["inverso"]
    else:
        return inverter(palavra, inverso = palavra[-1], i = 1)

n = int(input())
for num in range(n):
    palavra = input()
    print(inverter(palavra))