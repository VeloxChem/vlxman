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
scf_drv.filename="h2o2-lrf"

scf_drv.xcfun = "b3lyp"
scf_results = scf_drv.compute(molecule, basis)

crs = vlx.ComplexResponse()
crs.filename="h2o2-lrf"

# available operators
# crs.b_operator = "electric dipole"
# crs.b_operator = "magnetic dipole"
# crs.b_operator = "linear momentum"
# crs.b_operator = "angular momentum"

crs.a_operator = "electric dipole"
crs.b_operator = "magnetic dipole"

crs.a_components = ["x", "y", "z"]
crs.b_components = ["x", "y", "z"]

crs.damping = 0.004556  # 1000 cm-1
crs.frequencies = [0.0656]

crs_results = crs.compute(molecule, basis, scf_results)

