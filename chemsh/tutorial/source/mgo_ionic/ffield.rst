.. _ffield:

************************
Generating a Force Field
************************

.. toctree::
   :maxdepth: 1
   :caption: Contents:
      
.. note:: The scripts for this step in the tutorial can be found in :mod:`mgo_ionic/mgo_fit`.

This tutorial will show you how to manually generate a force field for use in **MM** calculations. This is only relevant if you do not have a suitable forcefield to work with in your QM/MM calculations.

To generate our forcefield, we will use the General Utility Lattice Program. We need the following information about our system
        * Cell parameters
        * MgO structure in fractional or Cartesian (must be specified)
        * Species (core/shell and charge)
        * Starting guess for force field

All of this information is then structured in an input file with file extension :mod:`.gin`, e.g. input.gin. A full example file is shown below:

.. literalinclude:: ../../samples/mgo_ionic/mgo_fit/input.gin

The first line of this input file dictate the type of calculation being run and should be kept the same in most cases:
   * :mod:`fit` means that the forcefield will be fitted, rather than the system altered
   * :mod:`conp` ensures fitting is down under constant pressure conditions
   * :mod:`prop` allows evaluation of system properties once completed
   * :mod:`simul` provides simultaneous fitting and coordinate optimisation
   * :mod:`opti` is necessary to also perform the unit cell optimisation

After this line, most of the file is specific to your system. Line three are your cell parameters in the form :mod:`A` (length of cell side **A**), :mod:`B` (length of cell side **B**), :mod:`C` (length of cell side **C**), :math:`\alpha` (angle between **X** and **Y**), :math:`\beta` (angle between **X** and **Y**) and :math:`\gamma` (angle between **X** and **Y**\).

To specify betwen *fractional* and *Cartesian* structures, the next line in the script should read :mod:`fractional` or :mod:`Cartesian` respectively.
Following the format :mod:`Atom`, :mod:`core`/:mod:`shell`, :mod:`X`, :mod:`Y`, :mod:`Z`, input your structural data immediately below.
