import numpy as np
import veloxchem as vlx

molecule = vlx.Molecule.read_molecule_string("""
C        0.67759997    0.00000000    0.00000000
C       -0.67759997    0.00000000    0.00000000
H        1.21655197    0.92414474    0.00000000
H        1.21655197   -0.92414474    0.00000000
H       -1.21655197   -0.92414474    0.00000000
H       -1.21655197    0.92414474    0.00000000
""")
basis = vlx.MolecularBasis.read(molecule, "def2-svpd")

scf_drv = vlx.ScfRestrictedDriver()

scf_drv.xcfun = "b3lyp"
scf_results = scf_drv.compute(molecule, basis)

crs = vlx.ComplexResponse()

# to be implemented (together with a plot function)
#crs.property = "polarizability"

crs.a_operator = "electric dipole"
crs.b_operator = "electric dipole"

crs.a_components = ["x"]
crs.b_components = ["x"]

crs.frequencies = np.arange(0.0, 0.4, 0.0025)

crs_results = crs.compute(molecule, basis, scf_results)
