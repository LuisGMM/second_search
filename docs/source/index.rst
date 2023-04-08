Welcome to documentation!
================================


This static website contains the automatically generated documentation. 

.. code-block:: bash

   # Clean previous work and construct docs again
   make clean && make html

   # Serve documentation with desired web browser
   firefox build/html/index.html

.. toctree::
   :maxdepth: 2
   :caption: Introduction

   about

.. toctree::
   :maxdepth: 2
   :caption: Theory

   theory_template_1.md

.. toctree::
   :maxdepth: 2
   :caption: Examples

   examples/index

.. toctree::
   :maxdepth: 2
   :caption: References

   autoapi/index
   bibliography


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
