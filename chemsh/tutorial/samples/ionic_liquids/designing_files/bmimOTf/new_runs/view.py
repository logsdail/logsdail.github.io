from chemsh.io.converter import convert_to_atoms
from ase.visualize import view



cluster = Fragment(coords='bmimOTf_shells_cluster.pun', connmode='ionic')

view(convert_to_atoms(cluster))
