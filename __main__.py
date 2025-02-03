import automate
from parse import parse
file  = open("conf.aut");
text = file.read();
file.close()

#parsing
lines = text.split("\n")
