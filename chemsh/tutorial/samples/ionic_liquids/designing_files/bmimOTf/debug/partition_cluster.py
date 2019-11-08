from chemsh import *

bmimOTf = Fragment(coords='bmimOTf.pun')
#, connmode='ionic')

origin = [ 5.96093808200000e+00, 9.53870605600000e+00, 8.40279744600000e+00 ]

regions = bmimOTf.partition(cutoff_boundary=6.0, radius_active=10.0, origin=origin, qmmm_interface='explicit')

regions.save('bmimOTf_shells_regions.pun', 'pun')

