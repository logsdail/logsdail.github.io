from chemsh import *
from chemsh.io.converter import cif_to_fragment
from sys import stdout

#mgo = Fragment(coords='mgo_shells_periodic.pun', connmode='ionic')
mgo = cif_to_fragment('slab_mgo.cif', connmode='ionic', remove_z_axis=True)
mgo.addCharges({'O' :-2.0, 
                'Mg':2.0})
mgo.addShells('O', displace=0.0, charges={'O':-2.792547})

# Note python counts atoms from zero!
cluster = mgo.construct_cluster(radius_cluster=20.0, origin_atom=40, adjust_charge='coordination_scaled', radius_active=10.0, bq_margin=7.0, bq_density=3)
cluster.save('mgo_shells_cluster_cif.pun', 'pun')

#print(mgo.charges)

print("Core Atoms: " + str(mgo.shells.coreatoms))
print("Names: " + str(mgo.shells.names))
print("Coordinates: " + str(mgo.shells.coords))
print("Displace: " + str(mgo.shells.displace))
print("Charges: " + str(mgo.shells.charges))
