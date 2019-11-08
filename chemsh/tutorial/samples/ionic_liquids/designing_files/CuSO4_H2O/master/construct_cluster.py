from chemsh import *
from sys import stdout
import time

s1 = time.time()
cuso4_solv = Fragment(coords='CONFIG', connmode='ionic')
e1 = time.time()
print("file read time:")
print(e1 - s1)

s2 = time.time()
cuso4_solv.addCharges({'S':2.00000, 'O1':-1.00000, 'O2':-1.00000, 'O3':-1.00000, '04':-1.00000, 'CU':2.00000, 'O6':-0.84760, 'H1':0.42380, 'H2':0.42380})
print("Charges: " + str(cuso4_solv.charges))
e2 = time.time()
print("charges add time:")
print(e2 - s2)

#cluster.save('cuso4_solv.pun', 'pun')

s3 = time.time()
cluster = cuso4_solv.construct_cluster(radius_cluster=20.0, origin_atom=0, radius_active=10.0, bq_margin=3.0, bq_density=1)
e3 = time.time()
print("cluster add time:")
print(e3 - s3)

s4 = time.time()
cuso4_solv.save('cuso4_solv.pun', 'pun')
e4 = time.time()
print("save time:")
print(e4 - s4)


'''
from chemsh import *
from sys import stdout

mgo = Fragment(coords='mgo_shells_periodic.pun', connmode='ionic')

# Note python counts atoms from zero!
cluster = mgo.construct_cluster(radius_cluster=20.0, origin_atom=40, adjust_charge='coordination_scaled', radius_active=10.0, bq_margin=7.0, bq_density=3)
cluster.save('mgo_shells_cluster.pun', 'pun')

print(mgo.charges)

print("Core Atoms: " + str(mgo.shells.coreatoms))
print("Names: " + str(mgo.shells.names))
print("Coordinates: " + str(mgo.shells.coords))
print("Displace: " + str(mgo.shells.displace))
print("Charges: " + str(mgo.shells.charges))
'''
