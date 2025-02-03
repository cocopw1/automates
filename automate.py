class afd:
    def __init__(self, nbetat:int, startetat:int, alphabet:str):
        self.nbetat = nbetat;
        self.curr = startetat;
        self.aphabet = alphabet;
        self.etat = [];
        for o in range(nbetat):
            self.etat.append(o);

class etat:
    def __init__(self,name:str, id:int):
        self.name = name;
        self.id = id;

class arc :
    def __init__(self, provenance: int, destination : int, value:str):
        self.provenance = provenance;
        self.destination = destination;
        self.value = value;