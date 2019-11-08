.. _qm_mm_spoint:

*******************************
Single-Point Energy Calculation
*******************************

.. note:: The scripts for this step of the tutorial can be found in :mod:`mgo_ionic/2_mgo_sp`.

`1. Quantum Mechanics (QM)`_
============================

.. note:: The QM calculations in this example use NWChem.

**NWChem** requires a **.basis** and **.ecp** file which can be obtained from `Basis Set Exchange <http://bse.pnl.gov/bse/portal>`_. Below are the :mod:`mgo_nwchem.basis` and :mod:`mgo_nwchem.ecp` files used in this tutorial:

.. literalinclude:: ../../samples/mgo_ionic/2_mgo_sp/mgo_nwchem.basis
.. literalinclude:: ../../samples/mgo_ionic/2_mgo_sp/mgo_nwchem.ecp

The **.ecp** file is important as this sets the *Effective Core Potential*. This is a representative potential which replaces some core electrons. For example, :mod:`Mg1`, the QM active region, is assigned as :mod:`nelec 10` (12 electrons, less 2 from the 1s orbital) whereas :mod:`bq_Mg2_e`, boundary atoms, is assigned as :mod:`nelec 0` (or no explicit electrons).

`2. Molecular Mechanics (MM)`_
==============================

.. note:: The MM calculations in this example use GULP.

**GULP** uses a force field argument which can be given in one of two ways: taken from the literature or generated manually using the :doc:`ffield` tutorial. An example of the force field used in this tutorial, :mod:`mgo_2body.ff`, is shown below:

.. literalinclude:: ../../samples/mgo_ionic/2_mgo_sp/mgo_2body.ff

This force field uses the Buckingham :mod:`buck`, Lennard-Jones :mod:`lennard`, Spring :mod:`spring` and Coulomb :mod:`coulomb` interatomic potentials. More information on these can be found in the `GULP manual <http://nanochemistry.curtin.edu.au/local/docs/gulp/gulp4.2_manual.pdf>`_.

`3. Calculating the Single-Point Energy`_
=========================================

The input structure used in this calculation is the :mod:`mgo_shells_region.pun` created previously. Here the :mod:`connmode` has been changed from **Ionic** to **None** to ensure the QM/MM code does not try to terminate any bonds between the QM and MM regions using link atoms. 

.. Is it necessary to change the connectivity? Seems strange

.. literalinclude:: ../../samples/mgo_ionic/2_mgo_sp/mgo_sp_energy.py
   :lines: 4

Next, our parameters for the QM/MM calculation are defined:

.. literalinclude:: ../../samples/mgo_ionic/2_mgo_sp/mgo_sp_energy.py
   :lines: 8-27

where:
- :mod:`qm_theory` specifies using **NWChem** arguments, the **basis** and **ecp** file names. All calculations in this tutorial have been carried out using the DFT method with the B3LYP functional. 
- :mod:`mm_theory` specifies using **GULP** arguments, and the **force field** file name. 
- :mod:`qm_region` gets the list of atoms in the **QM** region which in this case is :mod:`region(1)`.

The above are combined in :mod:`qmmm`. Here, :mod:`shl_maxcycles` ensures a full convergence in the optimisiation of the shells and QM charge density. :mod:`sp.run()` is then used calculate the single-oint QM/MM energy.

.. note:: :mod:`testutils.validate()` is used as a validation tool to ensure the calculated energy is accurate to the set tolerance. This will throw either a **Pass** or **Fail** but does not necessarily mean the calculation failed.

.. note:: As well as the single-point energy, the ionisation energy can be calculated by following the :doc:`ipot` tutorial.
