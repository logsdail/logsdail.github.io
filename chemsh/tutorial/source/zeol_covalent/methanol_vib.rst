.. _methanol_vib:

*********************************************
Methanol adsorption & Vibrational frequencies
*********************************************

`10. Methanol adsorption onto zeolite structure`_
=================================================

As explained breifly in section :mod:`9`, zeolites are used industrialy as acid catalysts in a variety of different reactions, and these often include the adsorption of methanol. More information concerning the calculations, geometries and reactivity of such reactions can be read about in the following article:

`Methanol Adsorption in Zeolites - A First-Principles Study <https://dx.doi.org/10.1021/jp960365z>`_ 

During the adsorption process, methanol can undergo conversion reactions to products such as gasoline or dimethyl ether.

This tutorial will describe how methanol is adsorbed onto a zeolite surface, and the adsorption-energy calculated, computationally. To find the adsorption energy, 3 individual energies must be calculated:

- The energy of an optimized zeolite system.

- The energy of an optimized methanol molecule.

- The energy of an optimized methanol-bound zeolite system.

All of the above can be completed by running the input file :mod:`methanol_adsorption.py` found in the directory :mod:`zeol_covalent/10_methanol_adsorb`

To begin with, a :mod:`zsm5` cluster fragment is created. The cluster is optimized using a basic optimization script. This is the same script we have seen repeatedly throughout the preceeding tutorials.

The value of the optimized energy is saved in the variable :mod:`ecalc_zsm5_optimized`.

.. literalinclude:: ../../samples/zeol_covalent/10_methanol_adsorb/adsorption_energy.py
   :lines: 42

Next, a :mod:`methanol` fragment is created in the same way, with coordinates read from :mod:`methanol.pun`:

.. literalinclude:: ../../samples/zeol_covalent/10_methanol_adsorb/adsorption_energy.py
   :lines: 48

The methanol molecule is in the :mod:`qm_region` only. To denote this, all of the atom labels have a '1' suffix too. It is also worth noting that the coordinates of the methanol molecule are set so that the methanol molecule adsorbs onto the :mod:`zsm5` structure in the correct position and orientation.

At this point, we would usually define the :mod:`qm_theory` and :mod:`mm_theory` to produce the combined :mod:`qmmm` object. However, as the methanol molecule is part of the zeolite :mod:`qm_region` only, we only define the :mod:`qm_theory`, with the fragment :mod:`methanol` set as a parameter.

.. literalinclude:: ../../samples/zeol_covalent/10_methanol_adsorb/adsorption_energy.py
   :lines: 51

In the :mod:`opt` object, the theory is set to :mod:`qm_theory` as opposed to :mod:`qmmm` as usual. Again, because there is are no mm atoms in the structure.

.. literalinclude:: ../../samples/zeol_covalent/10_methanol_adsorb/adsorption_energy.py
   :lines: 54-56

The value of the optimized energy is saved in the variable :mod:`ecalc_methanol_optimized`.

.. literalinclude:: ../../samples/zeol_covalent/10_methanol_adsorb/adsorption_energy.py
   :lines: 61

Finally, a methanol-adsorbed zeolite cluster fragment is produced. We redefine both constituent fragments used before, and combine them as such:

.. literalinclude:: ../../samples/zeol_covalent/10_methanol_adsorb/adsorption_energy.py
   :lines: 72

The above code illustrates the use of the :mod:`append()` function. It adds the content of the :mod:`methanol` fragment to the :mod:`zsm5` cluster fragment. As such, this fragment now contains the atoms, charges and connectivity of a zeolite, and a methanol molecule. 

Because of these changes to the :mod:`zsm5` cluster fragment, we have to redefine any qm data that will be input to the :mod:`qmmm` object. 

.. literalinclude:: ../../samples/zeol_covalent/10_methanol_adsorb/adsorption_energy.py
   :lines: 77-79

The atoms frozen during optimization must also be updated.

.. literalinclude:: ../../samples/zeol_covalent/10_methanol_adsorb/adsorption_energy.py
   :lines: 96

The value of the optimized energy is saved in the variable :mod:`ecalc_zsm5_optimized`.

.. literalinclude:: ../../samples/zeol_covalent/10_methanol_adsorb/adsorption_energy.py
   :lines: 106

Now that we have the energy of the three structures, we can compare the variable's :mod:`ecalc_zsm5_optimized`, :mod:`ecalc_methanol_optimized` and :mod:`ecalc_adsorbed_optimized` to find the adsorption energy. The equation is:

.. math:: 
   E_{adsorption} = E_{methanol-zsm5} - (E_{methanol} + E_{zsm5})

The energy is calculated, with an appropriate a.u. to eV conversion factor, and displayed to screen using the following code:

.. literalinclude:: ../../samples/zeol_covalent/10_methanol_adsorb/adsorption_energy.py
   :lines: 116-117

`11. Vibrational frequencies of free and adsorbed methanol`_
============================================================

The vibrational frequency of the free and adsorbed methanol molecule can be calculated by running the input file :mod:`methanol_vib.py` found in the directory :mod:`zeol_covalent/11_methanol_vib`.

When finding the vibrational frequency of the free methanol molecule, the code is very similar to a traditional optimization script explained in the previous tutorials. To begin, the fragment :mod:`methanol` is created using coordinates read from :mod:`methanol.pun`.

As all of the methanol atoms are in the :mod:`qm_region`, the :mod:`mm_theory` can be ignored.

The only difference to a usual optimization object is the :mod:`thermal=True` parameter.  Here, DL_FIND calculates a finite-difference Hessian and thermal corrections to the enthalpy and entropy. In this mode there is no optimisation stage. If there are no frozen atoms, as in the case of the free methanol example, the rotational and translation modes are projected out before determining the vibrational frequencies. If frozen atoms are found this projection is not applicable but the softest modes can be selectively ignored in the thermochemical analysis.  

Note that thermal calculations work in mass-weighted coordinates throughout. The displacements used and resulting Hessian will therefore not agree exactly with the output of a force module calculation (even if the same masses and del value are specified), where the mass-weighted Hessian is generated from an initial Cartesian Hessian.

When finding the vibrational frequency of the adsorbed methanol molecule, we must include also some atoms from the :mod:`zsm5` fragment.  This follows in a similar fashion to that seen in section 10.

Towards the end of the output from this run, DL_FIND will report the thermochemical analysis, which covers the vibrational frequency modes, the vibrational energy correction to E_electronic, the total zero point energy (ZPE), total vibrational enthalpy contribution (E vib) and the total vibrational entropy contibution  (S vib).
