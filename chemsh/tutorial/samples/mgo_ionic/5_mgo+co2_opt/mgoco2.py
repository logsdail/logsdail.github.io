from chemsh       import *
from chemsh.utils import testutils
from numpy import append as np_append

mgo = Fragment(coords='mgo_shells_regions.pun', connmode=None)
co2 = Fragment(coords='co2.xyz', connmode=None)

mgo.append(co2)
mgo.save('mgoco2start.pun','pun')

qm_charge = int(mgo.totalcharge)

qm_theory = NWChem(method='dft',
                   functional='b3lyp',
                   basis='mgoco2_nwchem.basis',
                   ecp='mgo_nwchem.ecp',
                   charge=qm_charge,
                   unique_listing=True,
	    	   path="mpirun -np 4 nwchem")

mm_theory = GULP(ff='mgo_2body.ff',
                 conjugate=True)

qm_region = np_append(mgo.getRegion(1),[341,342,343])

qmmm = QMMM(qm=qm_theory,
            mm=mm_theory,
            frag=mgo,
            qm_region=qm_region,
            coupling='ionic',
            shl_maxcycles=5,
            shl_tolerance=0.001)

opt = Opt(theory=qmmm,
          algorithm="lbfgs", tolerance=0.005, trustradius="energy",
          maxcycle=200, maxene=300, frozen=[mgo.getRegion(5,4,3,2)])

opt.run()

mgo.save('mgoco2end.pun','pun')

ecalc = opt.result.energy

eref = -319.166650933
tolerance = 1.0e-3

# The pass for this tutorial seems to be inconsistent. If the calc takes 38 steps, 
# instead of 37, then you may get a marginal fail. One could increase the tolerance?
testutils.validate(ecalc, eref)

