# NWChem DFT (B3LYP) optimisation

from chemsh       import *
from chemsh.utils import testutils

co2 = Fragment(coords="co2.xyz")

nwchem = NWChem(frag=co2, method='dft', functional='b3lyp', basis='3-21g')

opt = Opt(theory=nwchem,
          algorithm='lbfgs', tolerance=0.005, trustradius='energy',
          maxcycle=200, maxene=100, maxstep=1.0) 

opt.run()

ecalc = opt.result.energy

eref = -187.523633340 
tolerance = 1.0e-4

testutils.validate(ecalc, eref, tol=tolerance)

