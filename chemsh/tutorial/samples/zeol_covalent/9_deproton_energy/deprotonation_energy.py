from chemsh       import *
from chemsh.cluster.getFrozen import getNotQM
from chemsh.cluster.jost_corr import jost_corr_bulk

# Creation of zsm5 cluster fragment
zsm5 = Fragment(coords='zsm5.pun', connmode='covalent', totalcharge=0)

ff = 'zeolite_gulp.ff'

# Parameters of the qmmm object
qm_charge = int(zsm5.totalcharge)

qm_theory = NWChem(method='scf', basis='3-21g', maxiter=100, charge=qm_charge, mult=1)

mm_theory = GULP(ff=ff)

qm_region = zsm5.getRegion(1)

# Parameters of boundary_charge_adjust function in qmmm.py file
silicate_modifiers = {("si","o1"):0.3}
reverse_silicate_modifiers = {("si","o1"):-0.3}

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

# Saving of sp energy in variable to use in DE calculation
ecalc_regular = sp.result.energy

# Removal of dipole-adjust to continue using zsm5 cluster fragment
qmmm.boundary_charge_adjust(reverse_silicate_modifiers)




# Deletion of the H atom in zsm5 cluster fragment during deprotonation
zsm5.delete(550) 

# Altering of charge in zsm5 cluster fragment to account for lost proton
zsm5.totalcharge=-1

# Altering of charge in qm_theory to account for lost proton
qm_theory.charge = int(zsm5.totalcharge)

# Resetting of zsm5 qm_region due to lost proton
qm_region = zsm5.getRegion(1)

# Creation of new qmmm object
qmmm = QMMM(qm=qm_theory,
            mm=mm_theory,
            frag=zsm5,
            coupling='covalent',
            qm_region=qm_region,
            bond_modifiers=silicate_modifiers,
            embedding='electrostatic',
            dipole_adjust=True)

# Defining of atoms not involved in optimization
frozen = getNotQM(zsm5.natoms, qm_region)

# Creation of opt object
opt = Opt(theory=qmmm, 
          algorithm="lbfgs", tolerance=0.15, trustradius="energy",
          maxcycle=500, maxene=500, frozen=frozen)

opt.run()

# Saving of opt energy in variable to use in DE calculation
ecalc_deprotonated = opt.result.energy




# Deprotonation energy calculation including eV conversion
print("The energy of the protonated zeolite structure is: ", ecalc_regular)
print("The energy of the deprotonated zeolite structure is: ", ecalc_deprotonated)
deprotonation_energy = ecalc_deprotonated - ecalc_regular
print("The deprotonation energy is: ", deprotonation_energy*27.21138602, " eV")

# Parameters for jost_corr_bulk() function
Q = -1   #Charge. This is in units e.
epsilon = 1.71  #Dielectric Constant. This is unitless.
R = 10  #Radius of relaxed region. This is in a.u. Bohr. Equal to radius of active region

# Parameters for jost_corr_bulk() function
jost_corr = jost_corr_bulk(Q,epsilon,R)

# Deprotonation energy calculation with Jost correction including eV conversion
print()
print("The Jost correction is", jost_corr)
print("Using this correction, the more accurate value of the deprotonation energy = ", (deprotonation_energy*27.21138602) + jost_corr, " eV")
