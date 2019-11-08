.. _adsorb_add:

*******************
Adding an Adsorbate
*******************

The next step in this tutorial will go through how to add an adsorbate to a surface. Here we will consider the adsorbtion of CO\ :sub:`2`. To work out the energy of adsorption (E\ :sub:`ads`), we need to first know the enegry of the surface (MgO), the energy of the adsorbate (CO\ :sub:`2`) and the energy of the combined system (MgO--CO\ :sub:`2`):

.. math::
   E_{ads} = E_{MgO_{suf}+CO_2} - E_{MgO_{surf}} - E_{CO_2}

We have already calculated the **single-point energy** of MgO in the previous examples. We now need to do the same for both CO\ :sub:`2` and MgO--CO\ :sub:`2`.

`1. Single-Point Energy of Adsorbate`_
=======================================

.. note:: The scripts for this step of the tutorial can be found in :mod:`chemsh/4_co2_opt/`.

Unlike in the previous example, there is no need to consider **MM** methods for CO\ :sub:`2` as it is a single molecule rather than a vast bulk material. Instead the script :mod:`co2_opt_energy.py` is much shorter and looks like:

.. literalinclude:: ../../samples/mgo_ionic/4_co2_opt/co2_opt_energy.py
    :lines: 6-21

`2. Single-Point Energy of the Adsorbed State`_
================================================

.. note:: The scripts for this step of the tutorial can be found in :mod:`chemsh/5_mgo+co2_opt/`.

This step *does* required consideration of both **QM** and **MM**, so the script :mod:`mgoco2.py` looks like:

.. literalinclude:: ../../samples/mgo_ionic/5_mgo+co2_opt/mgoco2.py
    :lines: 1-46, 49

To keep things clean, we *append* the CO\ :sub:`2` coordinates (:mod:`co2.xyz`) to the end of the MgO coordinates (:mod:`mgo_shells_region.pun`) and write a new **.pun** file, :mod:`mgoco2start.pun`.
We now have a total of 344 atoms in the system (0-343 in terms of python). :mod:`qm_region` now accounts for all of *region 1* and atoms *341, 342, 343* (CO\ :sub:`2`). Running this calculation will cause some fo the coordinates to change, as a result of the optimisation of bond lengths. The new coordinates are saved in the file :mod:`mgoco2end.pun`.
