from __future__ import annotations
class arc :
    def __init__(self, provenance: int, destination : int, value:str):
        self.provenance = int(provenance)-1;
        self.destination = int(destination)-1;
        self.value = value;
    def print(self):
        print(f"arc from : {self.provenance} to : {self.destination} if : {self.value}")
    def clone(self)-> arc:
        res = arc(self.provenance,self.destination,self.value);
        return res;
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
    def getDestfromValue(self, value: str):
        if (self.getArcfromValue(value)!=None):
            return self.getArcfromValue(value).destination;
        else :
            return -1
    def print(self):
        print ( f"etat : {self.name}, id : {self.id}, Acceptant : {self.acceptant}")
        for i in self.arcs:
            i.print()
    def clone(self) -> etat:
        ar = []
        for arc in self.arcs:
            ar.append(arc.clone())
        res = etat(name=self.name,id = self.id,arcs=ar,acceptant=self.acceptant)
        return res
class afd:
    def __init__(self, nbetat:int, startetat:int, alphabet:str, etats:list[etat]):
        self.nbetat = nbetat;
        self.curr = startetat;
        self.alphabet = alphabet;
        self.etat = etats;
    def navigate(self, value:str):
        if self.curr:
            if value in self.alphabet:
                
                self.curr= self.etat[self.curr].getArcfromValue(value).destination;
                self.curr = None
                print(self.etat[self.curr].name, self.curr, self.etat[self.curr].id)
            
    def __getstate__(self):
        return self.etat[self.curr]
class afn:
    def __init__(self, nbetat:int, startetat:list[int], alphabet:str, etats:list[etat]):
        self.nbetat = nbetat;
        self.curr = startetat;
        self.alphabet = alphabet;
        self.etat = etats;
    def navigate(self, value:str):
        if value in self.alphabet:
            todel = []
            for i in range(len(self.curr)):
                print("newstate")
                self.curr[i]= self.etat[self.curr[i]].getDestfromValue(value);
                if self.curr[i]<0:
                    todel.append(i)
                print(self.etat[self.curr[i]].name, self.curr[i], self.etat[self.curr[i]].id)
            for i in todel:
                self.curr.pop(i)
    def __getstate__(self):
        res = []
        for i in self.curr:
            res.append(self.etat[i])
        return res
    def print(self):
        print(f"afn, alphabet : {self.alphabet}, nbetat : {self.nbetat}, etat courant {str(self.curr)}")
        for i in self.etat:
            i.print()
    def clone(self)-> afn:
        etats = []
        for etat in self.etat:
            etats.append(etat.clone())
        res = afn(self.nbetat,self.curr,self.alphabet)
        return res;
    def toAFD(self):
         
         for letter in self.alphabet:
            newAFD = self.clone();
            newAFD.navigate(letter);
            newAFD.__getstate__();
            

        
        