from chemsh	  import *

# Creation of zsm5 cluster fragment
zsm5 = Fragment(coords='zsm5.pun', connmode='covalent')

# Parameters of the qmmm object
ff = 'zeolite_gulp.ff'

qm_theory = NWChem(method='scf', basis='3-21g', maxiter=100)

mm_theory = GULP(ff=ff)

qm_region = zsm5.getRegion(1)

# Parameter of boundary_charge_adjust function in qmmm.py file
silicate_modifiers = {("si","o1"):0.3}

# Creation of qmmm object
qmmm = QMMM(qm=qm_theory, 
            mm=mm_theory, 
            frag=zsm5,
            coupling='covalent',
            qm_region=qm_region, 
            bond_modifiers=silicate_modifiers, 
            embedding='electrostatic',
            dipole_adjust=True)

# Creation of sp object
sp = SP(theory=qmmm, gradients=False)

sp.run()
