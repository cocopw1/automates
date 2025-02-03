class afd:
    def __init__(self, nbetat:int, startetat:int):
        self.nbetat = nbetat;
        self.curr = startetat;
        self.etat = [];
        for o in range(nbetat):
            
