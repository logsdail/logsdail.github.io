from chemsh                   import *
from chemsh.utils             import testutils
from chemsh.cluster.getFrozen import getNotQM

cuso4_solv = Fragment(coords='cuso4_solv_regions.pun', connmode='ionic')

qm_charge = int(cuso4_solv.totalcharge)

qm_theory = NWChem(method='dft',
                   functional='b3lyp',
                   basis='3-21g',
                   charge=qm_charge,
                   unique_listing=True,
                   maxiter=100,
                   mult=2,
                   path="mpirun -np 4 nwchem")

mm_theory = DL_POLY(ff='FIELD')#, conjugate=True)

qm_region = range(6) 

qmmm = QMMM(qm=qm_theory,
            mm=mm_theory,
            frag=cuso4_solv,
            qm_region=qm_region,
            coupling='ionic',
            embedding='electrostatic',
            shl_maxcycles=5,
            shl_tolerance=0.001)

frozen = getNotQM(cuso4_solv.natoms, qm_region)

opt = Opt(theory=qmmm,
          algorithm="lbfgs", tolerance=0.0045, trustradius="energy",
          maxcycle=500, maxene=500, frozen=frozen)

opt.run()

ecalc = opt.result.energy

#eref =
#tolerance = 1.0e-6
#testutils.validate(ecalc, eref, tol=tolerance)

cuso4_solv.save('cuso4_solv_opt.pun', 'pun')
