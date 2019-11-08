.. _ipot_dp:

********************************************
Ionisation potentials & Deprotonation energy
********************************************

`7. Ionisation Potential of silicate`_
======================================

The ionisation potential of the :mod:`mfi` cluster can be calculated by finding the single-point energy of the cluster before and after an electron has been removed from an O atom in the :mod:`qm_region`. The difference between these energies must be the energy supplied to ionise the cluster.

This calculation can be done by running the input file :mod:`mfi_ip.py` in the directory :mod:`zeol_covalent/3_silicate_ip`. 

In the code, the single-point energy of the neutral silicate is calculated first, using the same method as in section :mod:`3`, with a few minor differences.

When creating the neutral :mod:`mfi` cluster fragment, there is an additional :mod:`totalcharge` parameter, which is subject to change when an electron is removed:

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
   :lines: 5

The value of :mod:`totalcharge` is accessed from the :mod:`mfi` cluster fragment and saved as an integer variable in :mod:`charge`, meaning that we can access this charge elsewhere:

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
   :lines: 10

When defining :mod:`qm_theory`, the NWChem parameters now include :mod:`charge` as well as :mod:`mult` (multiplicity). This is because it is only the :mod:`qm_region` of the cluster that is affected during the ionisation procedure. For the unionised fragment, :mod:`charge` is neutral, and :mod:`mult` is 1: 

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
   :lines: 12

After calculating the sp energy of the neutral :mod:`mfi` cluster fragment, it is saved as a variable using the following line.

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
   :lines: 37

Next, the :mod:`mfi_ionised` cluster fragment is created, and the :mod:`totalcharge` parameter has changed:

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
   :lines: 43-44

The :mod:`qm_theory` NWChem parameters :mod:`charge` and :mod:`mult` have also changed to 1 and 2 respectively now that an electron has been removed from the :mod:`qm_region` of the cluster. The :mod:`charge` parameter is accessed and altered using :mod:`qm_theory.charge`, and the :mod:`mult` parameter is accessed and altered using :mod:`qm_theory.mult`.

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
   :lines: 47-48

The :mod:`qmmm` cluster fragment :mod:`frag` is accessed and altered to :mod:`mfi_ionised` using :mod:`qmmm.frag`

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
  :lines: 51

After calculating the sp energy of the ionised :mod:`mfi` cluster fragment, it is saved as a variable using the following line.

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
   :lines: 58

Using both of the single-point energies we have aquired before and after ionisation saved as :mod:`ecalc_neutral` and :mod:`ecalc_ionised`, the ionisation potential is calculated using the following equation:

.. math:: 
   E_{IP} = E_{[zsm5]^{+}} - E_{[zsm5]^{0}} + E_{corr}


The correction term represents the Jost correction. A function, :mod:`jost_corr_bulk()`, is used to calculate this.

.. math::
   E_{corr} = -\frac{Q^2}{2R}(1-\frac{1}{\varepsilon})

The ionisation potential is first calculated without the Jost correction, and stored in a variable :mod:`ionisation_potential`. A multiplication factor of 27.21138602 is required to display the energy in eV instead of a.u.

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
  :lines: 64-65

After this, the parameters are defined that are required for the :mod:`jost_corr_bulk()` function. 

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
  :lines: 68-70

These parameters are used to find the Jost correction using the :mod:`jost_corr_bulk()` function. The correction is saved in the variable :mod:`jost_corr`.

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
  :lines: 73

Finally, the ionisation potential is calculated and displayed with the Jost correction applied using the variables :mod:`ionisation_potential` and :mod:`jost_corr`.

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
  :lines: 77


`8. Ionisation Potential of zeolite`_
=====================================

The ionisation potential of zeolite can be calculated by running the input file :mod:`zeol_ip.py` in the directory :mod:`zeol_covalent/8_zeol_ip`. 

mod:`zsm5` and :mod:`zsm5_ionised` are the cluster fragments used instead of :mod:`mfi` and :mod:`mfi_ionised`. The rest of the python script is the same as the one described in section :mod:`7`.

The Jost correction for zsm5 uses the same constants as mfi also.


`9. Deprotonation Energy of zeolite`_
=====================================

Due to the H+ cation in the zeolite cluster, the material becomes very acidic, and so zsm5 can be used for acid-catalysed reactions. By calculating the deprotonation energy of the zeolite cluster, this will give us an indication as to how acidic the cluster is.

The deprotonation energy of the :mod:`zsm5` cluster can be calculated by finding the single-point energy of the cluster before and after deprotonation energy. The difference between these energies must be the energy supplied to deprotonate the cluster.

The deprotonation energy can be calculated by running the input file :mod:`deprotonation_energy.py` in the directory :mod:`zeol_covalent/9_deproton_energy`. 

To begin with, the single-point energy of a zsm5 fragment is calculated in the same way as section :mod:`3`, with a few minor differences.

To create a neutral :mod:`zsm5` cluster fragment, we include an additional :mod:`totalcharge` parameter, which is subject to change when a proton is removed:

.. literalinclude:: ../../samples/zeol_covalent/9_deproton_energy/deprotonation_energy.py
   :lines: 6

The value of :mod:`totalcharge` is accessed from the :mod:`zsm5` cluster fragment and saved as an integer variable in :mod:`charge`, meaning that we can access this charge elsewhere:

.. literalinclude:: ../../samples/zeol_covalent/9_deproton_energy/deprotonation_energy.py
   :lines: 11

When defining :mod:`qm_theory`, the NWChem parameters now include :mod:`charge` as well as :mod:`mult`. This is because it is only the :mod:`qm_region` of the cluster that is affected during the deprotonation procedure. For the regular cluster fragment, :mod:`charge` is neutral, and :mod:`mult` is 1: 

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
   :lines: 12

The rest of the sp calculation is carried out as normal, and the value of the sp energy is saved in the variable :mod:`ecalc_regular`.

.. literalinclude:: ../../samples/zeol_covalent/7_silicate_ip/mfi_ip.py
   :lines: 37

As we are going to continue using this :mod:`zsm5` cluster fragment to produce the deprotonated cluster, we must revert back the charges changed by the dipole-adjust by changing the :mod:`bond_modifiers` parameter in the :mod:`qmmm` object to :mod:`reverse_silicate_modifiers`.

.. literalinclude:: ../../samples/zeol_covalent/9_deproton_energy/deprotonation_energy.py
   :lines: 42

Now, we must deprotonate the :mod:`zsm5` cluster. This is achieved using the :mod:`delete()` function on the :mod:`zsm5` cluster fragment. The function uses positional arguments, and as the H atom was the final atom added during the zeolite construction procedure, it is the 551st atom and therefore has position 550 in the fragment.

.. literalinclude:: ../../samples/zeol_covalent/9_deproton_energy/deprotonation_energy.py
   :lines: 48

We must amend to totalcharge parameter in the zsm5 fragment to reflect the fact that the structure is now proton-deficient.

.. literalinclude:: ../../samples/zeol_covalent/9_deproton_energy/deprotonation_energy.py
   :lines: 51

After these two changes, a deprotonated zeolite now exists within the :mod:`zsm5` cluster fragment.

The value of :mod:`totalcharge` is accessed from the :mod:`zsm5` cluster fragment and saved as an integer variable in :mod:`charge`, meaning that we can access this charge elsewhere:

.. literalinclude:: ../../samples/zeol_covalent/9_deproton_energy/deprotonation_energy.py
   :lines: 54

The :mod:`qm_region` is updated to reflect the fact that there is no longer a H atom bound to an O atom in the region anymore. This is again carried out by using the :mod:`getRegion()` function, which adds any atoms with a '1' suffix to the :mod:`qm_region`. 

.. literalinclude:: ../../samples/zeol_covalent/9_deproton_energy/deprotonation_energy.py
   :lines: 57

The :mod:`qmmm` object and the atoms frozen during optimization are redefined, which are inserted as parameters to the :mod:`opt` object. 

The optimized energy of the deprotonated :mod:`zsm5` cluster fragment is saved as a variable using the following line.

.. literalinclude:: ../../samples/zeol_covalent/9_deproton_energy/deprotonation_energy.py
   :lines: 80

Now that we have the energy of the regular and deprotonated structure, :mod:`ecalc_regular` and :mod:`ecalc_deprotonated`, we can find the deprotonation energy. The equation is:

.. math:: 
   E_{deprotonation} = E_{[zsm5]^{-}} - E_{[zsm5]^{0}} + E_{corr}

The correction term is the same as the ionisation potential, the Jost correction. The function, :mod:`jost_corr_bulk()`, is used to calculate this.

.. math::
   E_{corr} = -\frac{Q^2}{2R}(1-\frac{1}{\varepsilon})

The deprotonation energy is first calculated without the Jost correction, and stored in a variable :mod:`deprotonation_energy`. A multiplication factor of 27.21138602 is required to display the energy in eV instead of a.u.

.. literalinclude:: ../../samples/zeol_covalent/9_deproton_energy/deprotonation_energy.py
   :lines: 88-89

After this, the parameters are defined that are required for the :mod:`jost_corr_bulk()` function. As you can see, the dielectric constant and the radius of the relaxed region parameters are unchanged when compared to the ionisation potential Jost correction parameters, though the charge has changed from 1 to -1.

.. literalinclude:: ../../samples/zeol_covalent/9_deproton_energy/deprotonation_energy.py
   :lines: 92-94

These parameters are used to find the Jost correction using the :mod:`jost_corr_bulk()` function. Again, the correction is saved in the variable :mod:`jost_corr`.

.. literalinclude:: ../../samples/zeol_covalent/9_deproton_energy/deprotonation_energy.py
   :lines: 97

Finally, the deprotonation energy is calculated and displayed with the Jost correction applied using the variables :mod:`deprotonation_energy` and :mod:`jost_corr`.

.. literalinclude:: ../../samples/zeol_covalent/9_deproton_energy/deprotonation_energy.py
   :lines: 102
 
A perhaps more accurate value can be recited from the paper `Modelling metal centres, acid sites and reaction mechanisms in microporous catalysts <https://dx.doi.org/10.1039/c6fd00010j>`_. 
Any difference between the value from the paper (~1100kJ/mol) and the value calculated in the script (~1150kJ/mol) may be due to the size of the default qm region.

