import veloxchem as vlx

xyz = """
9
Furan
C              1.263508000000         0.553747000000        -1.899688000000
C              0.075870000000         1.120048000000        -1.486750000000
O             -0.901359000000         0.256504000000        -1.640416000000
C             -0.410431000000        -0.855575000000        -2.136972000000
C              0.949830000000        -0.720590000000        -2.319101000000
H              2.241662000000         1.015668000000        -1.895242000000
H             -0.048058000000         2.120474000000        -1.094289000000
H             -0.997252000000        -1.735683000000        -2.363437000000
H              1.631419000000        -1.463477000000        -2.711184000000
"""
mol = vlx.Molecule.read_xyz_string(xyz)
basis = vlx.MolecularBasis.read(mol, 'def2-svp')
scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = 'b3lyp'
scf_drv.pressure = 50
scf_drv.pressure_units = 'GPa'
scf_drv.filename = 'furan-gostshyp'

scf_results = scf_drv.compute(mol, basis)
