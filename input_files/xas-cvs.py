import veloxchem as vlx
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

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = "cam-b3lyp-100"
scf_results = scf_drv.compute(molecule, basis)

rsp_drv = vlx.LinearResponseEigenSolver()
rsp_drv.core_excitation = True

# To get the C K-edge,
# everythining up to and including the C 1s orbitals
rsp_drv.num_core_orbitals = 8
rsp_drv.nstates = 20

rsp_results = rsp_drv.compute(molecule, basis, scf_results)
