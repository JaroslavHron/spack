##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class PyPyani(PythonPackage):
    """pyani is a Python3 module that provides support for calculating
    average nucleotide identity (ANI) and related measures for whole genome
    comparisons, and rendering relevant graphical summary output. Where
    available, it takes advantage of multicore systems, and can integrate
    with SGE/OGE-type job schedulers for the sequence comparisons."""

    homepage = "http://widdowquinn.github.io/pyani"
    url      = "https://pypi.io/packages/source/p/pyani/pyani-0.2.7.tar.gz"

    version('0.2.7', '239ba630d375a81c35b7c60fb9bec6fa')
    version('0.2.6', 'd5524b9a3c62c36063ed474ea95785c9')

    depends_on('python@3.5:')
    depends_on('py-setuptools', type='build')
    depends_on('py-matplotlib', type=('build', 'run'))
    depends_on('py-seaborn',    type=('build', 'run'))

    # Required for ANI analysis
    depends_on('py-biopython',  type=('build', 'run'))
    depends_on('py-pandas',     type=('build', 'run'))
    depends_on('py-scipy',      type=('build', 'run'))

    # Required for ANIb analysis
    depends_on('blast-plus~python', type='run')

    # Required for ANIm analysis
    depends_on('mummer', type='run')
