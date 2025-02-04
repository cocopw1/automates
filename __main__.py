import automate;
import sys;
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
        arcs = []
        for j in range(len(alphabet)):
            li = parse('{} {} {}' ,lines[4+i*(len(alphabet)+1)+j]);
            arcs.append(automate.arc(provenance=li[0], destination=li[2],value=li[1]))
        etats.append(automate.etat(name=name,id = i,arcs=arcs))
    afd = automate.afd(nbetat=nbetat,startetat= 0, alphabet= alphabet,etats=etats)
    print(sys.argv[1]);
    for c in sys.argv[1]:
        afd.navigate(c);
    print(afd.__getstate__().name)