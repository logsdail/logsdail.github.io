from chemsh import *
from sys import stdout
#from chemsh.io.converter import convert_to_atoms
#from ase.visualize import view

cuso4_solv = Fragment(coords='CONFIG', connmode='ionic')

cuso4_solv.addCharges({'S':2.00000,
                       'O1':-1.00000, 'O2':-1.00000, 'O3':-1.00000, 'O4':-1.00000,
                       'CU':2.00000,
                       'O6':-0.84760,
                       'H1':0.42380, 'H2':0.42380})

cluster = cuso4_solv.construct_cluster(radius_cluster=20.0, origin_atom=0, 
                                       radius_active=10.0, bq_margin=3.0, bq_density=1)

cluster.save('cuso4_solv.pun', 'pun')

#view(convert_to_atoms(cluster))

