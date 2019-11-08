from chemsh              import *
from chemsh.utils        import testutils
#from chemsh.io.converter import convert_to_atoms
#from ase.visualize       import view

cuso4_solv = Fragment(coords='cuso4_solv.pun')
#cuso4_solv = Fragment(coords='CONFIG')

mm = DL_POLY(frag=cuso4_solv, ff='FIELD', temperature=285.15)

sp = SP(theory=mm, gradients=True)
sp.run()

ecalc = sp.result.energy
print("\n### sp.result.gradients =", sp.result.gradients)


'''
qm_charge = int(cuso4_solv.totalcharge)

qm_theory = NWChem(method='dft',
                   functional='b3lyp',
#                   basis='cuso4_solv_nwchem.basis',
#                   ecp='cuso4_solv_nwchem.ecp',
                   charge=qm_charge,
                   unique_listing=True)

mm_theory = DL_POLY(ff='FIELD',
                 conjugate=True)

qm_region = cuso4_solv.getRegion(1)

qmmm = QMMM(qm=qm_theory,
            mm=mm_theory,
#            frag=cuso4_solv,
            qm_region=qm_region,
            coupling='ionic',
            shl_maxcycles=5,
            shl_tolerance=0.001)

sp = SP(theory=qmmm, gradients=False)

sp.run()

ecalc = sp.result.energy

#eref = 
tolerance = 1.0e-9

testutils.validate(ecalc, eref, tol=tolerance)
'''
