import veloxchem as vlx

xyz = """6

Br             0.292251925963        -0.530005031920         1.963221543874
C             -0.008381678181         0.499022521674        -0.034884137977
Cl            -0.287893641771         1.434303975146        -1.858332515049
H             -0.837844225207        -0.206449386030        -0.209332881841
H              1.024283313182         0.201932181495        -0.282126932725
H             -0.188961744123         1.427656999929         0.531671525243"""

molecule = vlx.Molecule.read_xyz_string(xyz)
molecule.set_charge(-1)
basis = vlx.MolecularBasis.read(molecule, "def2-svp")

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = "B3LYP"
scf_results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_drv.transition = True
opt_results = opt_drv.compute(molecule, basis, scf_results)
