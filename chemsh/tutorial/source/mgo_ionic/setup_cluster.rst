.. _setup_cluster:

****************************
Setting up the QM/MM Cluster
****************************

.. note:: The scripts for this step of the tutorial can be found in :mod:`mgo_ionic/1_cut_cluster`.

This section of the tutorial will outline how to set up the QM/MM cluster using :mod:`construct_cluster.py`. To run a script in **ChemShell** is similar to running a **python** script: :mod:`chemsh construct_cluster.py` will run the script :mod:`construct_cluster.py`. We will need a **.pun** file containing the periodic crystalline structure of interest, in this example :mod:`mgo_shells_periodic.pun`

.. note:: It is possible to use other file formats as inputs using the :mod:`io.tools` in ChemShell, with an example given in the :mod:`mgo_ionic/1_cut_cluster/mgo_cluster_cif.py`.

The most relevant lines from :mod:`construct_cluster.py` are:

.. literalinclude:: ../../samples/mgo_ionic/1_cut_cluster/construct_cluster.py
   :lines: 4, 7-8

where:

* :mod:`mgo` is a Fragment containing the periodic input structure in :mod:`'mgo_shells_periodic.pun'` and the connectivity (denoted as :mod:`connmode`) is ionic.
* :mod:`cluster` is contructed using the command :mod:`cluster_construct()`, which needs the following variables:
        * :mod:`radius_cluster` determines the size of the cluster
        * :mod:`origin_atom` dictates where the cluster is based, for this example a surface atom
        * :mod:`adjust_charge` the ionic charge is not uniform from the bulk to the surface due to the loss of nearest neighbours, thus this setting is often required to account for this inhomogeneity
        * :mod:`radius_active` sets the size of the sampling region. This should always be set to at least as large as the largest optimisation region.
        * :mod:`bq_margin` and :mod:`bq_density` set both the number and position of point charges around the edge of the cluster. This is done to approximate the missing periodic electrostatic interactions. Typically this is denoted as **F**.

Next, the cluster needs to be partitioned into regions. The :mod:`construct_cluster.py` script will have written a new **.pun**, in this case called :mod:`mgo_shells_cluster.pun`. To proceed, it is required that the **QM** region is manually input to this file. This is done by relabelling the relevant atoms with a suffix of **"1"**, e.g. :mod:`Mg` becomes :mod:`Mg1`. In :mod:`partition_cluster.py` we have automated this process using a :mod:`for` loop:

.. literalinclude:: ../../samples/mgo_ionic/1_cut_cluster/partition_cluster.py
   :lines: 12-13

The embeded cluster is then split into regions later in :mod:`partition_cluster.py` script:

.. literalinclude:: ../../samples/mgo_ionic/1_cut_cluster/partition_cluster.py
   :lines: 15-16

The script will write a **.pun** file denoting the regions of the system, which is this case is called :mod:`mgo_shells_regions.pun`.

