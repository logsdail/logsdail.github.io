from chemsh import *
from sys import stdout
import time
#from ase.visualize import view

bmimOTf = Fragment(coords='CONFIG', connmode='ionic')

bmimOTf.addCharges({'CR':-0.11000,
                    'NA':0.15000,
                    'CW':-0.13000,
                    'HCR':0.21000,
                    'HCW':0.21000,
                    'C1':-0.17000,
                    'H1':0.13000,
                    'C2':0.01000,
                    'HC':0.06000,
                    'CS':-0.12000,
                    'CT':-0.18000})

cluster = bmimOTf.construct_cluster(radius_cluster=20.0, origin_atom=0, radius_active=10.0, bq_margin=3.0, bq_density=1)

cluster.save('bmimOTf_shells_cluster.pun', 'pun')

#view(cluster)
