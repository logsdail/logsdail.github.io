.. _ipot:

********************
Ionisation Potential
********************

.. toctree::
   :maxdepth: 1
   :caption: Contents:

.. note:: Ths scripts for this step in the tutorial can be found in :mod:`mgo_ionic/7_mgo_ip`.

This tutorial will run through how to calculate the ionisation potential of a system. As with the previous theme, this tutorial will be delivered by using an MgO cluster as the example.

.. literalinclude:: ../../samples/mgo_ionic/7_mgo_ip/mgo_ip.py

Above is the ChemShell script that will be used in this calculation. Essentially, this is based on the single-point energy calculation with the slight complication being that an electron needs to be removed from the system.
To account for this, we need two definitions for the MgO environment. The first is that of the non-ionised MgO.

.. literalinclude:: ../../samples/mgo_ionic/7_mgo_ip/mgo_ip.py
    :lines: 6-7

The second definition is found later in the script.

.. literalinclude:: ../../samples/mgo_ionic/7_mgo_ip/mgo_ip.py
    :lines: 38-39

As the ionisation potential is the enrgy required to remove an electron from a species, the :mod:`totalcharge` value has increased by **+1** from 8 to 9. This also changes the environment to an open shell system, with a multiplicity change from a singlet (**1**) to a doublet (**2**)


The ionisation potential of MgO is calculated using the equation below:

.. math:: E_{IP} = E_{[MgO_{surf}]^{+}} - E_{[MgO_{surf}]^0} + E_{corr}

.. note:: In this tutorial, we have used a 3-21G basis set which results in :math:`E_{IP}= 9.0197` eV.

A more accurate calculation can be obtained if the Jost correction is applied to the script. The Jost correction is applied when dealing with charged species in QM/MM calculations, as the relaxed region has a finite space. The Jost correction used the following equation:

.. math:: E_{corr} = -\frac{{{Q}^{2}(\varepsilon - 1))}}{2R(\varepsilon + 1)}

Where:

        * Q = total charge of the electrons in the defect, units e.
        * \varepsilon = dielectric constant of MgO, no units.
        * R = radius of the relaxed region (\ :math:`a_(0)`\), units a.u. bohr
