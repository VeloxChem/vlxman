import veloxchem as vlx

molecule = vlx.Molecule.read_name("methane")
basis = vlx.MolecularBasis.read(molecule, "def2-svpd")

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = "b3lyp"
scf_results = scf_drv.compute(molecule, basis)

c6_drv = vlx.C6Driver()

c6_results = c6_drv.compute(molecule, basis, scf_results)
