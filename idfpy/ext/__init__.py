"""idfpy extension system.

Extensions are organized as sub-packages under ``idfpy.ext``.  Each sub-package
exposes a ``MIXIN_MAP`` (``dict[str, type]``) that maps generated model class
names to mixin classes.  The code generator discovers these mappings at
generation time and injects the mixins into the class hierarchy so that IDE
autocompletion works out of the box.
"""
