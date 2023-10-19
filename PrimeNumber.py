n = int(input("entrez un entier naturel : "))
if n <= 1:
    print("pas de nombre premiers inferieures a 1")
else:
    print("les nombres premiers inférieurs à ce nombre sont :")
    for g in range(2, n):
        K = True
        for i in range(2, int(g ** 0.5) + 1):
            if g % i == 0:
                K = False
                break
        if K:
            print(g)
