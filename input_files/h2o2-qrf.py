import veloxchem as vlx

molecule = vlx.Molecule.read_smiles("OO")
basis = vlx.MolecularBasis.read(molecule, "def2-svpd")

scf_drv = vlx.ScfRestrictedDriver()

scf_drv.xcfun = "b3lyp"
scf_results = scf_drv.compute(molecule, basis)

qrf_drv = vlx.QuadraticResponseDriver()

qrf_drv.a_operator = "electric dipole"
qrf_drv.b_operator = "magnetic dipole"
qrf_drv.c_operator = "electric dipole"

# available operators
# qrf.b_operator = "electric dipole"
# qrf.b_operator = "magnetic dipole"
# qrf.b_operator = "linear momentum"
# qrf.b_operator = "angular momentum"

qrf_drv.a_component = "z"
qrf_drv.b_component = "x"
qrf_drv.c_component = "x"

qrf_drv.b_frequencies = [0.0656, 0.1312]
qrf_drv.c_frequencies = [0.0656, 0.1312]

qrf_drv.damping = 0.004556  # 1000 cm-1

qrf_results = qrf_drv.compute(molecule, basis, scf_results)

