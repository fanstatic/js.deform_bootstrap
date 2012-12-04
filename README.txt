js.deform_bootstrap
===================

Introduction
------------

This library packages `deform_bootstrap`_ for `fanstatic`_.

.. _`fanstatic`: http://fanstatic.org
.. _`deform_bootstrap`: http://pypi.python.org/pypi/deform_bootstrap/

This requires integration between your web framework and ``fanstatic``,
and making sure that the original resources (shipped in the ``resources``
directory in ``js.deform_bootstrap``) are published to some URL.

Included resources
------------------

``js.deform_bootstrap`` is different from most ``js.`` packages in that it
doesn't include any resources itself.  It references the resources from
``deform_bootstrap`` instead.

Usage in Pyramid
----------------

To use this package in `Pyramid`_ you have to include the following
packages::

  deform_bootstrap
  js.deform
  js.deform_bootstrap

.. caution::

  `js.deform_bootstrap` must be included **after** `js.deform` as it
  overrides some parts of its configuration.

.. _`Pyramid`: http://www.pylonsproject.org/projects/pyramid

