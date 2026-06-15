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
scf_drv.filename="h2o2-crf"

scf_drv.xcfun = "b3lyp"
scf_results = scf_drv.compute(molecule, basis)

crf_drv = vlx.CubicResponseDriver()
crf_drv.filename="h2o2-crf"

crf_drv.a_operator = "electric dipole"
crf_drv.b_operator = "magnetic dipole"
crf_drv.c_operator = "electric dipole"
crf_drv.d_operator = "electric dipole"

# available operators
# crf.b_operator = "electric dipole"
# crf.b_operator = "magnetic dipole"
# crf.b_operator = "linear momentum"
# crf.b_operator = "angular momentum"

crf_drv.a_component = "z"
crf_drv.b_component = "x"
crf_drv.c_component = "x"
crf_drv.d_component = "z"

crf_drv.b_frequencies = [0.0656, 0.1312]
crf_drv.c_frequencies = [0.0656, 0.1312]
crf_drv.d_frequencies = [0.0656, 0.1312]

crf_drv.damping = 0.004556  # 1000 cm-1

crf_results = crf_drv.compute(molecule, basis, scf_results)

