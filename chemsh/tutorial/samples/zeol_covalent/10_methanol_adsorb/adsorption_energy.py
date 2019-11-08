from chemsh       import *
from chemsh.cluster.getFrozen import getNotQM


# Creation of zeolite cluster fragment
zsm5 = Fragment(coords='zsm5.pun', connmode='covalent')

ff = 'zeolite_gulp.ff'

# Defining of parameters for qmmm object
qm_theory = NWChem(method='scf', basis='3-21g', maxiter=100)

mm_theory = GULP(ff=ff)

qm_region = zsm5.getRegion(1)

# Parameters of boundary_charge_adjust function in qmmm.py file
silicate_modifiers = {("si","o1"):0.3}
reverse_silicate_modifiers = {("si","o1"):-0.3} 

# Creation of qmmm object
qmmm = QMMM(qm=qm_theory,
            mm=mm_theory,
            frag=zsm5, 
            qm_region=qm_region, 
            bond_modifiers=silicate_modifiers, 
            embedding='electrostatic', 
            coupling='covalent', 
            dipole_adjust=True)

# Defining of atoms frozen during optimization
frozen = getNotQM(zsm5.natoms, qm_region)

# Creation of optimization object
opt = Opt(theory=qmmm,
          algorithm='lbfgs', tolerance=0.0045, trustradius='energy',
          maxcycle=200, maxene=100, maxstep=1.0, frozen=frozen)

opt.run()

# Saving of optimized energy in variable to use in adsorption calculation
ecalc_zsm5_optimized = opt.result.energy




# Creation of methanol fragment
methanol = Fragment(coords="methanol.pun")

# Defining of qm theory for use in opt object. Note: No mm_theory or qmmm object as only qm atoms.
qm_theory = NWChem(frag=methanol, method='scf', basis='3-21g')

# Creation of optimization object
opt = Opt(theory=qm_theory,
          algorithm='lbfgs', tolerance=0.0045, trustradius='energy',
          maxcycle=200, maxene=100, maxstep=1.0)

opt.run()

# Saving of optimized energy in variable to use in adsorption calculation
ecalc_methanol_optimized = opt.result.energy




# Creation of unedited zsm5 and methanol fragments (Note: methanol coords set to fit zsm5)
# Note: We cannot use already-created zsm5 & methanol fragments. Doing so gives incorrect energy.
zsm5 = Fragment(coords='zsm5.pun', connmode='covalent')
methanol = Fragment(coords='methanol.pun', connmode='covalent')

# expansion of zsm5 to include zeolite molecule
zsm5.append(methanol)

ff = '''#'''

# Redefining of parameters for qmmm object
qm_theory = NWChem(method='scf', basis='3-21g', maxiter=100) 

qm_region = zsm5.getRegion(1)

# Parameters of boundary_charge_adjust function in qmmm.py file
silicate_modifiers = {("si","o1"):0.3}
reverse_silicate_modifiers = {("si","o1"):-0.3}

# Creation of qmmm object
qmmm = QMMM(qm=qm_theory,
            mm=mm_theory,
            frag=zsm5,
            qm_region=qm_region,
            bond_modifiers=silicate_modifiers,
            embedding='electrostatic',
            coupling='covalent',
            dipole_adjust=True)

# Defining of atoms frozen during optimization
frozen = getNotQM(zsm5.natoms, qm_region)

# Creation of optimization object
opt = Opt(theory=qmmm,
          algorithm='lbfgs', tolerance=0.0045, trustradius='energy',
          maxcycle=200, maxene=100, frozen=frozen)

opt.run()

# Saving of optimized energy in variable to use in adsorption calculation
ecalc_adsorbed_optimized = opt.result.energy




# adsorption calculation. Hartree --> eV taken from NIST
print("The energy of the optimized zeolite is ", ecalc_zsm5_optimized)
print("The energy of the optimized methanol is ", ecalc_methanol_optimized)
print("The energy of the optimized methanol-bound zeolite structure is ", ecalc_adsorbed_optimized)
print()
adsorption_energy = ecalc_adsorbed_optimized - (ecalc_zsm5_optimized + ecalc_methanol_optimized)
print("Using these values, the energy of adsorption = ", adsorption_energy*27.21138602, " eV")
