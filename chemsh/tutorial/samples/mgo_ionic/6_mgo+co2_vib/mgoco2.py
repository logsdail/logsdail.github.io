from chemsh       import *
from chemsh.utils import testutils
from numpy import append as np_append

mgo = Fragment(coords='mgoco2end.pun', connmode=None)

qm_charge = int(mgo.totalcharge)

qm_theory = NWChem(method='dft',
                   functional='blyp',
                   basis='mgoco2_nwchem.basis',
                   ecp='mgo_nwchem.ecp',
                   charge=qm_charge,
                   unique_listing=True,
	    	   path="mpirun -np 4 nwchem")
	    	   #path="nwchem")

mm_theory = GULP(ff='mgo_2body.ff',
                 conjugate=True)

qm_region = np_append(mgo.getRegion(1),[341,342,343])
#qm_region = mgo.getRegion(1)

qmmm = QMMM(qm=qm_theory,
            mm=mm_theory,
            frag=mgo,
            qm_region=qm_region,
            coupling='ionic',
            shl_maxcycles=5,
            shl_tolerance=0.001)

opt = Opt(theory=qmmm, thermal=True, frozen=[mgo.getRegion(5,4,3,2,1)])
#          algorithm="lbfgs", tolerance=0.005, trustradius="energy",
#          maxcycle=200, maxene=300, frozen=[mgo.getRegion(5,4,3,2)])

opt.run()


