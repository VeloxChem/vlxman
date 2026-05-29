import veloxchem as vlx

xyz = """11

C             -0.772206248395        -0.016434096868        -0.700635679983
C             -1.157624142179         0.116691700218         0.629930069612
O             -0.534771749693        -0.472057533376         1.590777149894
H             -0.334883197498        -0.962653156131        -1.024922593811
H             -1.308352079024         0.557531631886        -1.461079703193
H             -1.919349306829         0.862668481717         0.921400518030
H              0.534705086383        -0.454816980252         1.291420902615
C              1.139768858836         0.703530479892        -0.326058007507
O              1.587155883988        -0.062426334892         0.580297008673
H              1.440795850994         0.540107465558        -1.379038105661
H              0.900306757095         1.765287583053        -0.100647468887"""
molecule = vlx.Molecule.read_xyz_string(xyz)
molecule.set_charge(0)
basis = vlx.MolecularBasis.read(molecule, "def2-svp")

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = "B3LYP"
scf_results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_drv.irc = True
opt_results = opt_drv.compute(molecule, basis, scf_results)
