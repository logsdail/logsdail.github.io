from chemsh import *

cuso4_solv = Fragment(coords='cuso4_solv.pun', connmode='ionic')

origin = [ -1.41921573000000e+01, 1.17488619300000e+01, 6.46379159500000e-01 ]

regions = cuso4_solv.partition(cutoff_boundary=6.0, radius_active=10.0, origin=origin, qmmm_interface='explicit')

regions.save('cuso4_solv_shells_regions.pun', 'pun')

