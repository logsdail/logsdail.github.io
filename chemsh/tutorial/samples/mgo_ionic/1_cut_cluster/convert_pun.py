from chemsh import *
from chemsh.io.converter import convert_to_atoms
from ase.io import write
from sys import stdout

mgo = Fragment(coords='mgo_shells_periodic.pun', connmode='ionic')
slab = convert_to_atoms(mgo)
write("slab_mgo.cif", slab)
