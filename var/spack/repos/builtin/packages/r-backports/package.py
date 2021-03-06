# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RBackports(RPackage):
    """Implementations of functions which have been introduced
    in R since version 3.0.0. The backports are conditionally
    exported which results in R resolving the function names to
    the version shipped with R (if available) and uses the
    implemented backports as fallback. This way package developers
    can make use of the new functions without worrying about the
    minimum required R version."""

    homepage = "https://cloud.r-project.org/package=backports"
    url      = "https://cloud.r-project.org/src/contrib/backports_1.1.1.tar.gz"
    list_url = "https://cloud.r-project.org/src/contrib/Archive/backports"

    version('1.1.4', sha256='ee4b5efef22fa7ef27d7983ffcd31db52f81e1fbb7189c6e89ee09b69349ff03')
    version('1.1.3', sha256='e41bd146824ec921994f1b176d0e4cca0b36dd3db32ca7a954d872a5ba214cc1')
    version('1.1.1', '969543a0af32dc23bba9bb37ec82008c')
    version('1.1.0', 'b97a71b026fd7ede0e449be93d160c17')

    depends_on('r@3.0.0:', type=('build', 'run'))
