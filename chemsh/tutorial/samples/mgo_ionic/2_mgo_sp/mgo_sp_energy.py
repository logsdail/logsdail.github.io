from chemsh       import *
from chemsh.utils import testutils

mgo = Fragment(coords='mgo_shells_regions.pun', connmode=None)

qm_charge = int(mgo.totalcharge)

qm_theory = NWChem(method='dft',
                   functional='b3lyp',
                   basis='mgo_nwchem.basis',
                   ecp='mgo_nwchem.ecp',
                   charge=qm_charge,
                   unique_listing=True)

mm_theory = GULP(ff='mgo_2body.ff',
                 conjugate=True)

qm_region = mgo.getRegion(1)

qmmm = QMMM(qm=qm_theory,
            mm=mm_theory,
            frag=mgo,
            qm_region=qm_region,
            coupling='ionic',
            shl_maxcycles=5,
            shl_tolerance=0.001)

sp = SP(theory=qmmm, gradients=False)

sp.run()

ecalc = sp.result.energy

eref = -131.579792677 
tolerance = 1.0e-9

testutils.validate(ecalc, eref, tol=tolerance)

