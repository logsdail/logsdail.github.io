from chemsh       import *
from chemsh.cluster.jost_corr import jost_corr_bulk

# Creation of unionised mfi cluster fragment
zsm5 = Fragment(coords='optimized_zsm5.pun', connmode='covalent', totalcharge=0)

ff = 'zeolite_gulp.ff'

# Parameters of the qmmm object
qm_charge = int(zsm5.totalcharge)

qm_theory = NWChem(method='scf', basis='3-21g', maxiter=100, charge=qm_charge, mult=1)

mm_theory = GULP(ff=ff)

qm_region = zsm5.getRegion(1)

# Parameters of boundary_charge_adjust function in qmmm.py file
silicate_modifiers = {("si","o1"):0.3}

# Creation of qmmm object
qmmm = QMMM(qm=qm_theory,
            mm=mm_theory,
            frag=zsm5,
            qm_region=qm_region,
            bond_modifiers=silicate_modifiers,
            embedding='electrostatic',
            coupling='covalent',
            dipole_adjust=True)

# Creation of sp object
sp = SP(theory=qmmm, gradients=False)

sp.run()

# Saving of sp energy in variable to use in IP calculation
ecalc_neutral = sp.result.energy




# Creation of ionised mfi cluster fragment
zsm5_ionised = Fragment(coords='optimized_zsm5.pun', connmode='covalent',
                       totalcharge=1)

# Altering of charge and multiplicity to account for lost electron
qm_theory.charge = 1
qm_theory.mult = 2

# Inserting of ionised fragment in qmmm object
qmmm.frag = zsm5_ionised

# Creation of sp object
sp_ionised = SP(theory=qmmm, gradients=False)
sp_ionised.run()

# Saving of sp energy in variable to use in IP calculation
ecalc_ionised = sp_ionised.result.energy




# IP calculation. Hartree --> eV taken from NIST
ionisation_potential = ecalc_ionised - ecalc_neutral
print("Ionisation potential = ", ionisation_potential*27.21138602, " eV")

# Parameters of Jost correction
Q = 1   # Total charge of the defect (electrons).
epsilon = 1.71  # This is the relative response to how the atoms in the cluster respond to the change in charge
R = 10  # Radius of relaxed region. This is in a.u. Bohr. Equal to radius of active region.

# Formation of Jost correction. Equation imported from jost_corr file
jost_corr = jost_corr_bulk(Q,epsilon,R)

#The IP with the Jost correction applied
print("The Jost correction is", jost_corr)
print("Using this correction, the more accurate value of the ionisation potential = ", (ionisation_potential*27.21138602) + jost_corr, " eV")
