from chemsh              import *
from chemsh.utils        import testutils
#from chemsh.io.converter import convert_to_atoms
#from ase.visualize       import view

cuso4_solv = Fragment(coords='cuso4_solv.pun', connmode='ionic')

ff = 'FIELD'

#qm_theory = NWChem(method='scf', basis='3-21g', maxiter=100)

mm_theory = DL_POLY(frag=cuso4_solv, ff=ff)#, temperature=285.15)#, conjugate=True)

#qm_region = cuso4_solv.getRegion(1)

#qmmm = QMMM(qm=qm_theory,
#            mm=mm_theory,
#            frag=cuso4_solv,
#            coupling='ionic',
#            qm_region=qm_region,
#            embedding='electrostatic',
#            dipole_adjust=True)

#sp = SP(theory=qmmm, gradients=False)
sp = SP(theory=mm_theory, gradients=True)

sp.run()

ecalc = sp.result.energy
print("\n### sp.result.gradients =", sp.result.gradients)
