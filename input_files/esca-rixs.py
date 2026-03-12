import veloxchem as vlx
import copy
import numpy as np

molecule = vlx.Molecule.read_xyz_string("""13
ESCA b3lyp/def2-svp optimized geometry
C              1.326024532622         0.471089167011        -1.154937296389
C              0.484399509715         0.908494386259         0.037569541020
C              0.270494167717        -0.188493907246         1.053914467110
O              0.701245126416        -1.308212251798         0.971080711541
C             -0.582260522270         0.210893702941         2.291730106998
F             -0.731967860619        -0.799813015071         3.135965340271
F             -1.800383044157         0.625073687043         1.897202571864
F              0.003899498844         1.231896946553         2.943599980006
H              1.453639490166         1.302028888463        -1.864264306255
H              0.853135331881        -0.368249103011        -1.686230702784
H              2.322713498820         0.134038471332        -0.833394707486
H              0.936346512410         1.764030447212         0.571699332428
H             -0.514670521097         1.267150587304        -0.270103071648""")

basis = vlx.MolecularBasis.read(molecule, "def2-svp")

xcfun = "cam-b3lyp"

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = xcfun
scf_results = scf_drv.compute(molecule, basis)

rixs_drv = vlx.RixsDriver()
rixs_drv.nstates = 20   # number of final valence-excited states
rixs_drv.num_core_orbitals = 8   # number of core orbitals
rixs_drv.num_core_states = 10  # number of intermediate core-excited states
rixs_drv.restricted_subspace = False 

rixs_drv.photon_energy = 276 / vlx.hartree_in_ev()  # value of the incoming photon energy in a.u.

rixs_results = rixs_drv.compute(molecule, basis, scf_results)
