import veloxchem as vlx

xyz_str = """3
water    
O    0.0000000    0.0000000   -0.1653507
H    0.7493682    0.0000000    0.4424329
H   -0.7493682    0.0000000    0.4424329
"""

molecule = vlx.Molecule.read_xyz_string(xyz_str)
basis = vlx.MolecularBasis.read(molecule, "6-31G*")

esp_drv = vlx.EspChargesDriver()

esp_drv.grid_type = "chelpg"

esp_drv.equal_charges = "2=3"

chelpg_charges = esp_drv.compute(molecule, basis)
