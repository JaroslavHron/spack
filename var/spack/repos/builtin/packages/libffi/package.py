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
import os

class Libffi(AutotoolsPackage):
    """The libffi library provides a portable, high level programming
    interface to various calling conventions. This allows a programmer
    to call any function specified by a call interface description at
    run time."""
    homepage = "https://sourceware.org/libffi/"
    url="https://github.com/libffi/libffi/archive/v3.2.1.tar.gz"

    version('3.2.1', '9066486bcab807f7ddaaf2596348c1db')
    version('3.2', '9c856376517415adcef1a16a2b3f4e54')
    version('3.1', '663d72841855334ff65b16d8d5decfe5')
    version('3.0.13', '901a57bea6e88f5b15ef8b50a0cc3199')
    version('3.0.12', '3f39fa63eb58b3cbde7c4412fd1b0858')

    # version('3.1', 'f5898b29bbfd70502831a212d9249d10',url =
    # "ftp://sourceware.org/pub/libffi/libffi-3.1.tar.gz") # Has a bug
    # $(lib64) instead of ${lib64} in libffi.pc

    # Older tarballs don't come with a configure script
    depends_on('m4',       type='build')
    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('gettext')

    def autoreconf(self, spec, prefix):
        #os.environ['ACLOCAL_PATH'] = spec['libtool'].prefix + '/share/aclocal'
        #autoreconf('--install', '-v')
        autoreconf("--install", "--verbose", "--force",
                   "-I", os.path.join(spec['automake'].prefix,"share", "aclocal"),
                   "-I", os.path.join(spec['libtool'].prefix,"share", "aclocal"),
                   "-I", os.path.join(spec['gettext'].prefix,"share", "aclocal"),
                   )
