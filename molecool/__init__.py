"""
molecool
A Python package for analyzing and visualizing xyz files
"""

# Add imports here --> note the star allows you to do all functions
from .functions import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
