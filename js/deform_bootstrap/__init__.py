# -*- coding: utf-8 -*-

from fanstatic import Library
from fanstatic import Resource
from js.deform import deform_js
from pkg_resources import resource_filename


deform_bootstrap_dir = resource_filename(
    "deform_bootstrap",
    "static")
library = Library(
    "deform_bootstrap",
    deform_bootstrap_dir)
deform_bootstrap_js = Resource(
    library,
    "deform_bootstrap.js",
    depends=[deform_js, ])
