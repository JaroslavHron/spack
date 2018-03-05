from spack import *

class Dijitso(PythonPackage):
    """dijitso

A Python module for distributed just-in-time shared library building

For more information, visit http://www.fenicsproject.org.

    """

    homepage = "https://bitbucket.org/fenics-project/dijitso"
    url      = "https://bitbucket.org/fenics-project/dijitso/downloads/dijitso-2017.2.0.tar.gz"

    version('2017.2.0', git='https://bitbucket.org/fenics-project/dijitso', tag='2017.2.0')
    version('2017.1.0', git='https://bitbucket.org/fenics-project/dijitso', tag='2017.1.0')
    version('2016.2.0', git='https://bitbucket.org/fenics-project/dijitso', tag='dijitso-2016.2.0')
    version('2016.1.0', git='https://bitbucket.org/fenics-project/dijitso', tag='dijitso-2016.1.0')
    
    depends_on('py-setuptools', type="build")
