import veloxchem as vlx

molecule = vlx.Molecule.read_xyz_string("""4
Hydrogen peroxide
O  -0.65564532 -0.06106286 -0.03621403
O   0.65564532  0.06106286 -0.03621403
H  -0.97628735  0.65082652  0.57474201
H   0.97628735 -0.65082652  0.57474201
""")
basis = vlx.MolecularBasis.read(molecule, "def2-svpd")

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.filename="h2o2-qrf"

scf_drv.xcfun = "b3lyp"
scf_results = scf_drv.compute(molecule, basis)

qrf_drv = vlx.QuadraticResponseDriver()
qrf_drv.filename="h2o2-qrf"
qrf_drv.print_level = 2

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

