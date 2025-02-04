


class arc :
    def __init__(self, provenance: int, destination : int, value:str):
        self.provenance = provenance;
        self.destination = destination;
        self.value = value;

class etat:
    def __init__(self,name:str, id:int, arcs:list[arc]):
        self.name = name;
        self.id = id;
        self.arcs = arcs
class afd:
    def __init__(self, nbetat:int, startetat:int, alphabet:str, etats:list[etat]):
        self.nbetat = nbetat;
        self.curr = startetat;
        self.aphabet = alphabet;
        self.etat = etats;