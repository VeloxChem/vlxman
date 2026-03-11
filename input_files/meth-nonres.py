import veloxchem as vlx

molecule = vlx.Molecule.read_name("methane")
basis = vlx.MolecularBasis.read(molecule, "def2-svpd")

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = "b3lyp"
scf_results = scf_drv.compute(molecule, basis)

lr_drv = vlx.LinearResponseDriver()

lr_drv.property = "polarizability"
lr_drv.frequencies = [0.0656]  # static field is default

lr_results = lr_drv.compute(molecule, basis, scf_results)

