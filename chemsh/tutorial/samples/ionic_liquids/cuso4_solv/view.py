from chemsh.io.converter import convert_to_atoms
from ase.visualize import view



cluster = Fragment(coords='<<filename>>', connmode='ionic')

view(convert_to_atoms(cluster))
