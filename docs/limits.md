# Pushing the limits

VeloxChem has the stated goal to be *science-enabling* and should provide:

- a fast return of results

- coverage of dense 3D system of sizes up to and beyond 500 atoms in the quantum region

- accurate description of electronically excited states that show a more diffuse character than the ground state

- stable and reliable convergence of iterative equation solvers

- automatized workflows for complex simulations involving e.g. embedding and dynamics

## Performance and scaling

### Personal computers (laptop/desktop)

#### Resolution of identity

Timings are in seconds, measured on 1 LUMI-CPU node with 128 cores (8 MPI x 16 OMP). Systems are water clusters of different sizes. The time spent in one Fock-J build is measured with and without RI. Speedup can be 10x, 20x, 40x or 100x depending on basis set and system size

:::{image} ../images/ri.png
:width: 800px
:align: center
:::

### High-performance computing 

#### HPC-CPU

*MPI/OpenMP parallel Fock matrix construction*

With a highly efficient MPI/OpenMP implementation of linear response functions (here specifically complex polarization propagator theory), calculations have been performed of the frequency-dependent polarizabilities for fullerenes consisting of up to 540 carbon atoms. These calculations were performed on AMD EPYC Zen2 64-core CPUs. See {cite}`Brand2021` for further details.


:::{image} ../images/alpha_fullerene.png
:width: 600px
:align: center
:::

#### HPC-GPU

*GPU-accelerated Fock matrix construction*

VeloxChem diagonalizes the Fock matrix in SCF iterations. Up to a point of some 30,000+ basis functions, this diagonalization step does not represent a bottleneck in the calculation and the Fock matrix construction shows sub-quadratic scaling with respect to system size. See {cite}`veloxchem-gpu` for further details.

:::{figure} ../images/hpc-gpu-scaling.jpeg
:width: 600px
:align: center

Timings are obtained with use a single AMD MI-250X node with 4 GPUs.
:::

*Multi-node acceleration*

VeloxChem implements MPI for multi-node acceleration. It is recommended to run 1 MPI-rank per node and as many OpenMP threads as there are GPU devices on the node. 

:::{figure} ../images/veloxchem-gpu-strong-scaling.png
:height: 400px
:align: center

Strong scaling report using a range of 1--27 nodes of type AMD MI-250X with 4 GPUs. The system is a complete DNA sequence with 20 base pairs and includes a solvation shell of waters in the QM region to properly solvate the phosphate backbone, and timings refer to the construction of an auxiliary Fock matrix in a linear response calculation.
:::