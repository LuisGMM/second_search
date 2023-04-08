API Reference
=============

This section contains and automatically API documentation by making use of the `sphinx-autoapi` extension.
This ensures documentation to be up-to-date and enable developers to focus on just writing source code and
corresponding docstrings.

.. toctree::
   :titlesonly:

   {% for page in pages %}
   {% if page.top_level_object and page.display %}
   {{ page.include_path }}
   {% endif %}
   {% endfor %}

