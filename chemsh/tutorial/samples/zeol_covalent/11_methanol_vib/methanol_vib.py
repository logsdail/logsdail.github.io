from chemsh       import *
from chemsh.cluster.getFrozen import getNotQM

# Creation of methanol fragment
methanol = Fragment(coords="methanol.pun")

# Defining of qm theory for use in opt object. Note: No mm_theory or qmmm object as only qm atoms.
qm_theory = NWChem(frag=methanol, method='scf', basis='3-21g')

# Creation of optimization object
opt = Opt(theory=qm_theory, maxcycle=200, maxene=100, thermal=True)

opt.run()



methanol = Fragment(coords='methanol.pun', connmode='covalent')
zsm5 = Fragment(coords='zsm5.pun', connmode='covalent')
zsm5.append(methanol)

qm_region = zsm5.getRegion(1)
qm_charge = int(zsm5.totalcharge)

silicate_modifiers = {("si","o1"):0.3}
reverse_silicate_modifiers = {("si","o1"):-0.3}
ff = 'zeolite_gulp.ff'

qm_theory = NWChem(method='scf', basis='3-21g', charge=qm_charge)
mm_theory = GULP(ff=ff)

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
opt = Opt(theory=qmmm, maxcycle=200, maxene=100, thermal=True, frozen=frozen)

opt.run()


