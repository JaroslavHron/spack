##############################################################################
# Copyright (c) 2013-2016, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
# Please also see the LICENSE file for our notice and the LGPL.
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
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install dijitso
#
# You can edit this file again by typing:
#
#     spack edit dijitso
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Dijitso(Package):
    """A Python module for distributed just-in-time shared library building."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://bitbucket.org/fenics-project/dijitso"
    url      = "https://bitbucket.org/fenics-project/dijitso/downloads/dijitso-2016.2.0.tar.gz"

    version('2016.2.0', '589b36bc79f94028b8db170151b828b6')

    extends('python')

    # FIXME: Add additional dependencies if required.
    # depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=nolink)
    depends_on('py-setuptools', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-mpi4py', type=("build","run"))
    depends_on('py-six', type=("build","run"))
    depends_on('py-python-subprocess32', type=("build","run"))

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
