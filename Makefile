python2:
	spack install python

python3:
	spack install python@3.6.3

numpy: python2 python3
	spack install py-numpy ^python@3.6.3

openmpi:
	spack install openmpi schedulers=slurm fabrics=pmi,verbs


spack spec -I py-mpi4py ^openmpi schedulers=slurm fabrics=pmi,verbs
spack spec -I py-mpi4py ^python@3.6.3 ^openmpi schedulers=slurm fabrics=pmi,verbs
