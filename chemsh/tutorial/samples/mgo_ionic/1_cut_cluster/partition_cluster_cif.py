from chemsh import *

mgo = Fragment(coords='mgo_shells_cluster_cif.pun', connmode='ionic')

# Define the origin for the cluster - this is the mid-point of an MgO (100) facet
# origin = [ 3.97900846268733, 3.97900846268733, -3.97900846268733 ]
origin = 0 # Corresponds to atom 1

# Define the atoms to have in the QM region. Here we choose atoms 1-14 inclusive.
for i in range(14):
    mgo.names[i] += "1".encode()

regions = mgo.partition(cutoff_boundary=6.0, radius_active=10.0, origin=origin, qmmm_interface='explicit', interface_exclude=["O"])
regions.save('mgo_shells_regions_cif.pun', 'pun')

