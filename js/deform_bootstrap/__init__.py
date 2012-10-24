# -*- coding: utf-8 -*-

from fanstatic import Library
from fanstatic import Resource
from js.bootstrap import bootstrap_js
from js.chosen import chosen_jquery
from js.deform import deform_js
from js.deform import resource_mapping
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


def includeme(config):
    resource_mapping['chosen'] = chosen_jquery
    resource_mapping['bootstrap'] = bootstrap_js
