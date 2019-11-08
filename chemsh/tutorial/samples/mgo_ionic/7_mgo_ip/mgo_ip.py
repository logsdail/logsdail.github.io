from chemsh       import *
from chemsh.utils import testutils
from chemsh.cluster.jost_corr import jost_corr_surf

# This is our unionised fragment
mgo = Fragment(coords='mgo_shells_regions.pun', connmode=None,
	       totalcharge=8)

qm_charge = int(mgo.totalcharge)

qm_theory = NWChem(method='dft',
                functional='b3lyp',
                basis='mgo_nwchem.basis',
                ecp='mgo_nwchem.ecp',
                charge=qm_charge,
                unique_listing=True,
                mult=1,
		path="mpirun")
	
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

sp_neutral = SP(theory=qmmm, gradients=False)
sp_neutral.run()
ecalc_neutral = sp_neutral.result.energy

# This is our ionised fragment
mgo_ionised = Fragment(coords='mgo_shells_regions.pun', connmode=None,
                       totalcharge=9)

# This is now open shell, so we alter the multiplicity
qm_theory.charge = 9
qm_theory.mult = 2

# This our ionised cluster
qmmm.frag = mgo_ionised

sp_ionised = SP(theory=qmmm, gradients=False)
sp_ionised.run()
ecalc_ionised = sp_ionised.result.energy

#For mgo
eref_neutral = -131.923916441 
tolerance = 1.0e-9
testutils.validate(ecalc_neutral, eref_neutral, tol=tolerance)

#For mgo_ionised
eref_ionised = -131.592447262
testutils.validate(ecalc_ionised, eref_ionised, tol=tolerance)


# And the ionisation potential. Hartree --> eV taken from NIST
ionisation_potential = ecalc_ionised - ecalc_neutral
print("Ionisation potential = ", ionisation_potential*27.21138602, " eV")

Q = 1   #Charge. This is in units e.
epsilon = 10  #Dielectric Constant. This is unitless.
R = 20  #Radius of relaxed region. This is in a.u. Bohr.
jost_corr = jost_corr_surf(Q,epsilon,R)

#The IP with the Jost correction applied
print("The Jost correction is", jost_corr)
print("Using this correction, the more accurate value of the ionisation potential = ", (ionisation_potential*27.21138602) + jost_corr, " eV")

