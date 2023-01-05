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
from spack import *


class PyPetsc4py(Package):
    """Petsc4py are python interface to PETSc library."""
    homepage = "https://bitbucket.org/petsc/petsc4py"
    url      = "https://bitbucket.org/petsc/petsc4py/get/3.7.0.tar.gz"

    version('3.7.0', '288eebd8bcded076f0097f66728fd768')
    version('3.6.0', 'd8bd6cca2741faa59d5c34f8c76f60d5')

    extends('python')
    
    depends_on('py-setuptools', type='build')

    depends_on('py-cython')
    depends_on('py-mpi4py')
    depends_on('py-numpy@1.6:')
    depends_on('petsc@3.7.0:3.7.9', when='@3.7.0:3.7.9')
    depends_on('petsc@3.6.0:3.6.9', when='@3.6.0:3.6.9')

    def install(self, spec, prefix):
        setup_py('build_src', '--force')
        setup_py('install', '--prefix={0}'.format(prefix))
