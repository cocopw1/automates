import automate;
from parse import parse;
file  = open("conf.aut");
text = file.read();
file.close()

#parsing
lines = text.split("\n")
if lines[0]== "afd":
    alphabet = lines[1];
    nbetat = int(lines[2])
    etats = []
    for i in range(nbetat):
        name = lines [3+i*((len(alphabet))+1)]
        print(name)
        arcs = []
        for j in range(len(alphabet)):
            li = parse('{} {} {}' ,lines[4+i*(len(alphabet)+1)+j]);
            print (f"{li[0]}, {li[1]}, {li[2]}")
            arcs.append(automate.arc(provenance=li[0], destination=li[2],value=li[1]))
        etats.append(automate.etat(name=name,id = i,arcs=arcs))
    afd = automate.afd(nbetat=nbetat,startetat= 0, alphabet= alphabet,etats=etats)
