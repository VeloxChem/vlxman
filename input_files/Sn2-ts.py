import veloxchem as vlx

xyz = """11

C             -0.958565365001         0.082810329601        -0.607450127181
C             -1.266721765210         0.161564304416         0.737205612337
O             -0.571318406706        -0.552635962856         1.581216123694
H             -0.667255223825        -0.898103805146        -0.989570052974
H             -1.527769932065         0.699085898972        -1.303754236807
H             -2.265113517907         0.463899870329         1.071348490367
H              0.409312502108        -0.359313992243         1.284450564771
C              1.287844465926         0.704569952196        -0.410356738245
O              1.643992797005         0.079820002858         0.643629892952
H              1.725114973846         0.336050045752        -1.360438050652
H              1.213061740911         1.806920314360        -0.314034717792"""

molecule = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(molecule, "def2-svp")

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = "B3LYP"
scf_results = scf_drv.compute(molecule, basis)

opt_drv = vlx.OptimizationDriver(scf_drv)
opt_drv.transition = True
opt_results = opt_drv.compute(molecule, basis, scf_results)
