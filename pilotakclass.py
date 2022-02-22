f = open(f"pilotak.txt","r",encoding="UTF-8")
l = [sor.strip().split(";") for sor in f ]
f.close()
l.remove(l[0])

class Pilotak():
    def __init__(self,sor):
        self.nev = sor[0]  
        self.szuletes = sor[1]
        self.nemzetiseg = sor[2]
        self.rajtszam = sor[3]

