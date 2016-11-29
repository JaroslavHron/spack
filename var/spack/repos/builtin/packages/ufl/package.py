from spack import *

class Ufl(Package):
    """UFL - Unified Form Language

The Unified Form Language (UFL) is a domain specific language for
declaration of finite element discretizations of variational
forms. More precisely, it defines a flexible interface for choosing
finite element spaces and defining expressions for weak forms in a
notation close to mathematical notation.  UFL is part of the FEniCS
Project.

For more information, visit http://www.fenicsproject.org

    """

    homepage = "https://bitbucket.org/fenics-project/ufl"
    url      = "https://bitbucket.org/fenics-project/ufl/downloads/ufl-2016.1.0.tar.gz"

    version('2016.1.0', git='https://bitbucket.org/fenics-project/ufl', tag='ufl-2016.1.0')
    version('1.7.0dev', git='https://bitbucket.org/fenics-project/ufl', commit='f3d31f2aea32141b2789a42839d0b22d188b6f2a')
    version('1.6.0', git='https://bitbucket.org/fenics-project/ufl', tag='ufl-1.6.0')
    

    extends('python')
    depends_on('py-setuptools', type="build")
    depends_on('py-numpy', type=("build","run"))
    depends_on('py-six', type=("build","run"))
    
    def install(self, spec, prefix):
        python('setup.py', 'install', '--prefix={0}'.format(prefix))
