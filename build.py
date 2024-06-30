"""For pybuilder usage"""
#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

# pylint: disable=invalid-name
name = "EG2"
default_task = "publish"

# pylint: disable=unused-argument
# pylint: disable=unnecessary-pass
@init
def set_properties(project):
    """To set project properties"""
    pass
