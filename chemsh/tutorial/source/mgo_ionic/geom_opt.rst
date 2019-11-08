.. _geom_opt:

*********************
Geometry Optimisation
*********************

.. note:: The scripts for this step of the tutorial can be found in :mod:`chemsh/3_mgo_opt`.

The geometry optimisation calculation, :mod:`mgo_opt_energy.py`, follows a similar script to the previous example with an alternative argument :mod:`opt.run()` rather than :mod:`sp.run()` as shown below:

.. literalinclude:: ../../samples/mgo_ionic/3_mgo_opt/mgo_opt_energy.py
    :lines: 29-33

Here the geometry optimisiation has several variables:
 * :mod:`algorithm` is used to specify the optimisation algorithm used by the calculator, in this case :mod:`lbfgs` has been used.
 * :mod:`maxcycle` determines the maximum number of optimisation cycles. The cycler will cease after energy convergence or at the limit set here.
 * :mod:`maxene` determines the maximum number of energy and gradient calculations per cycle.
 * :mod:`frozen` allows the user to specify which regions will be frozen during the calculation. All regions not explicitly selected here will be free. In this example, only region **1** is free.

This script has also included the ability to run this calculation in parallel rather than serial as shown at the end of :mod:`qm_theory`:

.. literalinclude:: ../../samples/mgo_ionic/3_mgo_opt/mgo_opt_energy.py
    :lines: 8-14
