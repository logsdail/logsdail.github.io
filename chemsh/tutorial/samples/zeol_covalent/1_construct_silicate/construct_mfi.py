from chemsh import *

# Creation of mfi unit cell fragment
mfi = Fragment(coords='mfi.c', connmode='covalent')
mfi.save('mfi.xyz','xyz')

# Creation of mfi cluster 
cluster = mfi.construct_cluster(radius_cluster=25.0, origin_atom=4, adjust_charge='coordination_scaled',
                                 radius_active=10.0, bq_margin=5.0, bq_density=2)

# Saving of mfi cluster
cluster.save('mfi.pun', 'pun')
cluster.save('mfi.pun.xyz', 'xyz')

    

