from spack import *

class Uflacs(Package):
    """UFLACS - UFL Analyser and Compiler System

    Uflacs, the UFL Analyser and Compiler System, is a collection of
    algorithms for processing symbolic UFL forms and expressions. The
    main feature is efficient translation of tensor intensive symbolic
    expressions into a low level expression representation and C++
    code.
    """

    homepage = "https://bitbucket.org/fenics-project/uflacs-deprecated"
    url      = "https://bitbucket.org/fenics-project/uflacs-deprecated/downloads/uflacs-1.6.0.tar.gz"

    version('1.6.0','33bf5a51de9be4403a2b7dde5e4f3afa')
    

    extends('python')
    depends_on('py-setuptools', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-six', type=("build","run"))
    depends_on('ufl@1.6.0', type=("build","run"), when='@1.6.0')
    
    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix={0}'.format(prefix))
