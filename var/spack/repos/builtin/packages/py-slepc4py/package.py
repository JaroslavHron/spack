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
#     spack install py-slepc4py
#
# You can edit this file again by typing:
#
#     spack edit py-slepc4py
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PySlepc4py(Package):
    """Slepc4py are python interface to SLEPc library."""
    homepage = "https://bitbucket.org/slepc/slepc4py"
    url      = "https://bitbucket.org/slepc/slepc4py/downloads/slepc4py-3.7.0.tar.gz"

    version('3.7.0', 'c4775e88b0825c7313629c01de60ecb2')
    version('3.6.0', '3d4c163dc482438684cdaa485ebf37fd')
    
    extends('python')
    
    depends_on('py-cython', type='build')
    depends_on('py-petsc4py@3.7.0:', when='@3.7.0:')
    depends_on('py-petsc4py@:3.6.9', when='@:3.6.9')
    depends_on('py-numpy')
    depends_on('slepc@3.7.0:3.7.9', when='@3.7.0:')
    depends_on('slepc@3.6.0:3.6.9', when='@:3.6.9')

    def install(self, spec, prefix):
        setup_py('install', '--prefix={0}'.format(prefix))
