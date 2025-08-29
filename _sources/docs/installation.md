# Installing the program

## Installing precompiled binaries using conda

Binaries are available for the three main operating systems:

- Windows
- macOS
- Linux

[Conda](https://docs.conda.io/en/latest/) is an open-source package and environment management system that runs on Windows, macOS, and Linux. The [conda-forge](https://conda-forge.org/) channel contains a large number of open-source certified packages enabling scientific work. It is recommended that you install the minimal installer for conda named miniconda, or the community-driven installer named miniforge, that includes only conda, Python, the packages they depend on, and a small number of other useful packages, including pip, zlib and a few others.

Retrieve miniconda or miniforge from the following website

> <https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html>

Install the version for 64-bit computers that comes with Python (>=3.9).

Start a conda terminal, or Anaconda Prompt / Miniforge Prompt as it is referred to on a Windows system. Conda supports multiple *environments* and you start in the one named `base` as is typically indicated by the prompt. To create a new and additional environment named `vlxenv` and install VeloxChem, Matplotlib, and Jupyter notebook (and package dependencies such as NumPy and SciPy) into it, you enter the following command line statement

```
$ conda create -n vlxenv veloxchem matplotlib jupyterlab -c veloxchem -c conda-forge
```

````{admonition} Considerations for NumPy performance
:class: tip

On Linux, we recommend installing `veloxchem` alongside `libopenblas` to ensure that `numpy` uses a high-performance backend for linear algebra operations.
````

You can list your conda environments

```
$ conda env list
```

The activated environment will be marked with an asterisk (the `base` environment to begin with) and you can activate your new environment with the command

```
$ conda activate vlxenv
```

as should be indicated by getting a modified prompt.

Inside this newly created environment, you should now be ready to start JupyterLab with the command

```
$ jupyter-lab
```

which should open in your default web browser. A notebook in JupyterLab allows for interactive execution of Python code written into cells. You should now be able to import the VeloxChem module in a cell:

```
import veloxchem as vlx
```

and start calculations. See the [eChem](https://kthpanor.github.io/echem) book for a multitude of examples.


## Installing from source

### Obtaining the source code

The source code can be downloaded from the [GitHub repository](https://github.com/VeloxChem/VeloxChem):

```
$ git clone https://github.com/VeloxChem/VeloxChem.git
```

### Build prerequisites

- [CMake](https://cmake.org/)
- C++ compiler supporting the C++20 standard and OpenMP
- [Eigen](https://gitlab.com/libeigen/eigen)
- [Libxc](https://libxc.gitlab.io/)
- [Python](https://www.python.org/) (>=3.9) that includes the interpreter, the development header files, and the development libraries
- [MPI4Py](https://mpi4py.readthedocs.io/en/stable/)
- [pybind11](https://pybind11.readthedocs.io/en/stable/)
- [scikit-build](https://scikit-build.readthedocs.io/en/latest/)

Optional, add-on dependencies:

- [dftd4-python](https://dftd4.readthedocs.io/en/latest/)

See {ref}`external-dependencies` for instructions on how to get these add-ons.

To avoid clashes between dependencies, we recommend to always use a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html).

(with-conda)=
### Installing on Unix-like systems with dependencies from conda-forge

[Conda](https://docs.conda.io/en/latest/) and the software packaged on the [conda-forge](https://conda-forge.org/) channel provide build isolation and greatly simplify the installation of VeloxChem.

- Move to the folder containing the source code:

  ```
  $ cd VeloxChem
  ```

- Create and activate the conda environment:

  ```
  $ conda env create -f vlx_env.yml
  $ conda activate vlxenv
  ```

  This will create and activate a conda environment named `vlxenv`. In this environment all the build dependencies will be installed from the conda-forge channel, including the C++ compiler, MPI, [NumPy](https://numpy.org), [MPI4Py](https://mpi4py.readthedocs.io/en/stable/), etc.

  Note that the MPICH library will be installed by the `vlx_env.yml` file. If you prefer another MPI library such as Open MPI, you can edit the .yml file and replace mpich by openmpi. Read more about the .yml file in [this page](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually).

- Set scikit-build and cmake options:

  ```
  $ export SKBUILD_CONFIGURE_OPTIONS="-DCMAKE_CXX_COMPILER=mpicxx"
  ```

  If you are installing VeloxChem on macOS you may also need to set the
  `CMAKE_ARGS` environment variable. See [Known issues](known-issues-macos) for
  details.

- Build and install VeloxChem in the conda environment:

  ```
  $ python3 -m pip install --no-build-isolation -v .
  ```

  By default, the build process will use *all* available cores to compile the C++ sources in parallel. This behavior can be controlled via the `VLX_NUM_BUILD_JOBS` environment variable:

  ```
  $ VLX_NUM_BUILD_JOBS=N python3 -m pip install --no-build-isolation -v .
  ```

  which will install VeloxChem using *N* cores.

- The environment now contains all that is necessary to run VeloxChem. You can deactivate it by

  ```
  $ conda deactivate
  ```

### Installing on Cray system

- Load Cray modules:

  ```
  $ module load PrgEnv-gnu
  $ module load cpe
  $ module load cray-python
  ```

- Create and activate a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html) with `--system-site-packages`

  ```
  $ python3 -m venv --system-site-packages vlxenv
  $ source vlxenv/bin/activate
  $ python3 -m pip install --upgrade pip setuptools wheel
  $ python3 -m pip install h5py pytest psutil geometric cmake pybind11-global scikit-build ninja rdkit
  ```

- Clone [Eigen](https://gitlab.com/libeigen/eigen).

- Install Libxc according to [Libxc documentation](https://libxc.gitlab.io/).

  If you need to run nonlinear response or TDDFT gradient using VeloxChem, add
  cmake options `-DDISABLE_KXC=OFF -DDISABLE_LXC=OFF` when installing Libxc.

- Compile VeloxChem

  ```
  $ cd VeloxChem
  $ export EIGEN_INCLUDE_DIR=/path/to/your/eigen
  $ export SKBUILD_CONFIGURE_OPTIONS="-DCMAKE_CXX_COMPILER=CC"
  $ export CMAKE_PREFIX_PATH=/path/to/your/libxc:$CMAKE_PREFIX_PATH
  $ export LD_LIBRARY_PATH=/path/to/your/libxc/lib:$LD_LIBRARY_PATH
  $ python3 -m pip install --no-build-isolation -v .
  ```

  If you are installing VeloxChem on an HPC cluster, please make sure to run the
  above compilations on an interactive compute node.

- CrayBLAS environment variables

  When running VeloxChem on Cray systems, we recommend setting the following environment
  variables:

  ```
  export CRAYBLAS_LEVEL1_LEGACY=1
  export CRAYBLAS_LEVEL2_LEGACY=1
  export CRAYBLAS_LEVEL3_LEGACY=1
  ```

### Installing on Ubuntu

- Install dependencies using apt

  ```
  $ sudo apt update
  $ sudo apt install build-essential wget cmake git python3 python3-pip python3-venv
  $ sudo apt install libopenblas-openmp-dev liblapacke-dev libeigen3-dev mpich
  ```

- Install Libxc according to [Libxc documentation](https://libxc.gitlab.io/).

  If you need to run nonlinear response or TDDFT gradient using VeloxChem, add
  cmake options `-DDISABLE_KXC=OFF -DDISABLE_LXC=OFF` when installing Libxc.

- Create and activate a [virtual enviroment](https://docs.python.org/3/tutorial/venv.html)

  ```
  $ python3 -m venv vlxenv
  $ source vlxenv/bin/activate
  $ python3 -m pip install --upgrade pip setuptools wheel
  $ python3 -m pip install numpy mpi4py h5py cmake pybind11-global scikit-build
  ```

- Install VeloxChem:

  ```
  $ cd VeloxChem
  $ export SKBUILD_CONFIGURE_OPTIONS="-DCMAKE_CXX_COMPILER=mpicxx"
  $ export CMAKE_PREFIX_PATH=/path/to/your/libxc:$CMAKE_PREFIX_PATH
  $ export LD_LIBRARY_PATH=/path/to/your/libxc/lib:$LD_LIBRARY_PATH
  $ python3 -m pip install --no-build-isolation -v .
  ```

### Installing on PowerLinux

- See {ref}`with-conda`

### Installing on macOS

- See {ref}`with-conda`

(known-issues-macos)=
- Known issues

  On macOS you may encounter the following error at the end of the ``pip install`` step:

  ```
  ...
      base_version = tuple(int(x) for x in base_version.split("."))
  ValueError: invalid literal for int() with base 10: ''
  error: subprocess-exited-with-error
  ...
  ```

  One workaround is to manually add the ``CMAKE_OSX_DEPLOYMENT_TARGET`` option
  to ``CMAKE_ARGS`` and redo the ``pip install`` step:

  ```
  $ python3 -c 'import sysconfig; print(sysconfig.get_platform())'
  macosx-10.9-x86_64

  $ export CMAKE_ARGS="-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.9"
  $ python3 -m pip install --no-build-isolation .
  ```

  Another issue that one may encounter on macOS is that the ``-march=native``
  flag is not supported by the compiler. The workaround is to add
  ``-DENABLE_ARCH_FLAGS=OFF`` to ``CMAKE_ARGS``. For example:

  ```
  $ export CMAKE_ARGS="-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.9 -DENABLE_ARCH_FLAGS=OFF"
  $ python3 -m pip install --no-build-isolation .
  ```

(external-dependencies)=
### External dependencies

- [dftd4-python](https://dftd4.readthedocs.io/en/latest/)

  It is recommended to install the dftd4-python package in a conda environment:

  ```
  $ conda install dftd4-python -c conda-forge
  ```

  Alternatively, you can compile it using ``meson``. If you want to use custom
  math library, add `-Dlapack=custom` and `-Dcustom_libraries=...` to the
  `meson setup` command.

  ```
  $ python3 -m pip install meson ninja cffi
  $ cd dftd4-3.7.0/
  $ meson setup _build -Dpython=true -Dpython_version=$(which python3)
  $ meson test -C _build --print-errorlogs
  $ meson configure _build --prefix=/path/to/your/dftd4
  $ meson install -C _build
  $ export PYTHONPATH=$PYTHONPATH:/path/to/your/dftd4/lib/python.../site-packages
  $ export LD_LIBRARY_PATH=/path/to/your/dftd4/lib64:$LD_LIBRARY_PATH
  $ export OMP_STACKSIZE=256M
  ```
