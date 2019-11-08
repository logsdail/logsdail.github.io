from chemsh.io.converter import convert_to_atoms
from ase.visualize import view



cluster = Fragment(coords='cuso4_solv_regions.pun', connmode='ionic')

view(convert_to_atoms(cluster))
