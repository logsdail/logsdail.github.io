# Method of dft used instead of scf
qm_theory = NWChem(method='dft',
                   functional='b3lyp',
                   basis='3-21g',
                   charge=0,
                   unique_listing=True,
		   path="mpirun -np 4 nwchem")

# Additional conjugate parameter
mm_theory = GULP(ff=ff,
                 conjugate=True)
