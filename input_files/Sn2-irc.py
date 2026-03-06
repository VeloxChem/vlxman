import veloxchem as vlx

xyz = """6

Br      -0.4416      -0.9091        2.1101                         
C       -0.2491       0.3460        0.0853                         
Cl      -0.0460       1.6507       -2.0207                         
H       -1.0663      -0.1558       -0.4146                         
H        0.7665       0.0369       -0.1207                         
H       -0.4248       1.3056        0.5523"""
molecule = vlx.Molecule.read_xyz_string(xyz)
molecule.set_charge(-1)
basis = vlx.MolecularBasis.read(molecule, "def2-svp")

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = "B3LYP"
scf_results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_drv.irc = True
opt_results = opt_drv.compute(molecule, basis, scf_results)
