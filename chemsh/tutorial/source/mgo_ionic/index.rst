.. chemshpy documentation master file, created by
   sphinx-quickstart on Tue Aug 15 13:23:13 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

****************************
**Modelling an MgO surface**
****************************

*A case study by Joe-Jackson Masters and Rowan Hanson, Cardiff University.*
*Funding is gratefully acknowledged from CCP5*

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   setup_cluster
   ffield
   qm_mm_spoint
   geom_opt
   adsorb_add
   vib_freq
   ipot

.. ## NEED TO MOVE THESE FILES TO A MORE APPROPRIATE LOCATION ##   
   addCharges
   addShells

The following tutorial focuses on an **ionic** MgO surface in a **QM/MM** environment. This tutorial will illustrate a chronological method for perfoming energy calculations on a solid surface, and will guide through cutting and partitioning a cluster. Later, the tutorial will also demonstrate how an adsorbate can be included, for further study of solid state chemistry.

It is recommended that crystal structures are obtained from `ICSD <http://icsd.cds.rsc.org/search/basic.xhtml>`_. For the purpose of this tutorial, the MgO cystal structure used is: :mod:`American Mineralogist (1976) 61, (*) p266-p271`.

