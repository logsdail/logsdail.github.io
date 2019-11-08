.. _vib_freq:

*********************
Vibrational Frequency
*********************

.. note:: The scripts for this step of the tutorial can be found in :mod:`chemsh/6_mgo+co2_vib/`

To calculate the vibrational frquency of the surface, the script :mod:`mgoco2.py` is implemented. Essentially, this is the same as in :doc:`geom_opt`. The difference comes from how the coordinates are read and the variables in the optimisation calculation. Here, :mod:`thermal=True` is the most important change.

.. literalinclude:: ../../samples/mgo_ionic/6_mgo+co2_vib/mgoco2.py
