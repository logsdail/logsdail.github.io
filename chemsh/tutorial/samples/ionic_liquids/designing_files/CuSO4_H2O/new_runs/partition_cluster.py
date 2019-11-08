from chemsh import *
#from chemsh.io.converter import convert_to_atoms
#from ase.visualize import view

cuso4_solv = Fragment(coords='cuso4_solv.pun', connmode='ionic')

origin = 0

for i in range(6):
    cuso4_solv.names[i] += "1".encode()

regions = cuso4_solv.partition(cutoff_boundary=6.0, radius_active=10.0, origin=origin, qmmm_interface='explicit', interface_exclude=["O_a", "O_b", "O_c", "O_d", "O_e", "O_f", "H_a", "H_b"])

regions.save('cuso4_solv_regions.pun', 'pun')

#view(convert_to_atoms(regions))
