class arc :
    def __init__(self, provenance: int, destination : int, value:str):
        self.provenance = int(provenance)-1;
        self.destination = int(destination)-1;
        self.value = value;

class etat:
    def __init__(self,name:str, id:int, arcs:list[arc], acceptant:bool):
        self.name = name;
        self.id = id;
        self.arcs = arcs;
        self.acceptant = acceptant;
    def getArcfromValue(self, value: str)-> arc:
        for arc in self.arcs:
            if arc.value == value:
                return arc
        return None;
class afd:
    def __init__(self, nbetat:int, startetat:int, alphabet:str, etats:list[etat]):
        self.nbetat = nbetat;
        self.curr = startetat;
        self.alphabet = alphabet;
        self.etat = etats;
    def navigate(self, value:str):
        if value in self.alphabet:
            
            self.curr= self.etat[self.curr].getArcfromValue(value).destination;
            print(self.etat[self.curr].name, self.curr, self.etat[self.curr].id)
            if self.curr <0:
                self = None;
    def __getstate__(self):
        return self.etat[self.curr]