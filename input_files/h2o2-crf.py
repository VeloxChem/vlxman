import veloxchem as vlx

molecule = vlx.Molecule.read_smiles("OO")
basis = vlx.MolecularBasis.read(molecule, "def2-svpd")

scf_drv = vlx.ScfRestrictedDriver()

scf_drv.xcfun = "b3lyp"
scf_results = scf_drv.compute(molecule, basis)

crf_drv = vlx.CubicResponseDriver()

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

