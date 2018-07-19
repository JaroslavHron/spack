##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at IBM.
#
# This file is part of Spack.
# Created by Serban Maerean, serban@ibm.com, All rights reserved.
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


class Globalarrays(AutotoolsPackage):
    """The Global Arrays (GA) toolkit provides a shared memory style
    programming environment in the context of distributed array data
    structures.
    """

    homepage = "http://hpc.pnl.gov/globalarrays/"
    url = "https://github.com/GlobalArrays/ga"

    version('master', git='https://github.com/GlobalArrays/ga', branch='master')

    variant('i8', default=False, description='Build with 8 byte integers')

    depends_on('blas')
    depends_on('lapack')
    depends_on('mpi')
    depends_on('scalapack')

    patch('ibm-xl.patch', when='%xl')
    patch('ibm-xl.patch', when='%xl_r')


    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool', type='build')
    depends_on('m4', type='build')
    depends_on('perl', type='build')

    #force_autoreconf = True

    def configure_args(self):
        options = []

        options.extend([
            '--with-openib',
            '--with-pic',
            '--with-blas={0}'.format(self.spec['blas'].prefix),
            '--with-lapack={0}'.format(self.spec['lapack'].prefix)
        ])

        return options
