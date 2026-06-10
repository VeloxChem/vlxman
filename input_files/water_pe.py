import veloxchem as vlx

solute_xyz = """3
water
O        0.0000000000      0.0000000000      0.0000000000
H        0.6891400000      0.8324710000      0.0000000000
H        0.7224340000     -0.8726890000      0.0000000000
"""

molecule = vlx.Molecule.read_xyz_string(solute_xyz)
basis = vlx.MolecularBasis.read(molecule, "def2-svp")

scf_drv = vlx.ScfRestrictedDriver()

# requires PyFraME until we get an internal PE module
scf_drv.potfile = "solvent.pot"

scf_results = scf_drv.compute(molecule, basis)
