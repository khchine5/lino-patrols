.. _patrols.tested.patrols:

Patrols
=======

.. include:: /include/tested.rst

The following statement imports a set of often-used global names::

>>> from lino.api.doctest import *

We can now refer to every installed app via it's `app_label`.
For example here are some simple Django operations to verify 
that the demo database is initialized:

>>> patrols.Patrol.objects.count()
50
>>> patrols.Area.objects.count()
4

