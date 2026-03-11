import veloxchem as vlx

molecule = vlx.Molecule.read_smiles("OO")
basis = vlx.MolecularBasis.read(molecule, "def2-svpd")

scf_drv = vlx.ScfRestrictedDriver()

scf_drv.xcfun = "b3lyp"
scf_results = scf_drv.compute(molecule, basis)

crs = vlx.ComplexResponse()

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

