from chemsh import *
#from chemsh.io.converter import convert_to_atoms
#from ase.visualize import view

bmimOTf = Fragment(coords='bmimOTf.pun', connmode='ionic')

origin = 0

for i in range(25):
    bmimOTf.names[i] += "1".encode()

for i in range(6405-6412):
    bmimOTf.names[i] += "1".encode()

regions = bmimOTf.partition(cutoff_boundary=6.0, radius_active=10.0, origin=origin, qmmm_interface='explicit', interface_exclude=[])

regions.save('bmimOTf_shells_regions.pun', 'pun')

#view(convert_to_atoms(regions))
