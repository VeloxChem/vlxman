import veloxchem as vlx

xyz_str = """12
propanol
C              0.287122604482        -0.658439248096         1.352543198101
C              0.224057122961        -0.230177036308        -0.123498537286
C             -1.211810163746        -0.086289617161        -0.646362355309
O             -1.865244099222         0.943810244897         0.043408964407
H             -0.138850281128         0.127254486586         2.013590563967
H              1.345443988487        -0.818617209367         1.650405684477
H             -0.266954871175        -1.608743753962         1.513003144654
H              0.758475938136         0.738103480182        -0.253354377301
H              0.752941954799        -0.990737769186        -0.740193839208
H             -1.190106706453         0.157165363176        -1.734264017680
H             -1.766243401522        -1.044101824780        -0.510744786230
H             -1.823078650351         0.710040930866         1.007688030780
"""

molecule = vlx.Molecule.read_xyz_string(xyz_str)

conf = vlx.ConformerGenerator()
conformers = conf.generate(molecule)

# Now we will compute the Boltzmann-weighted RESP charges:
empty_mol = vlx.Molecule()
empty_bas = vlx.MolecularBasis()

resp_settings = { 
    'molecules': conformers['molecules'],
    'filename': 'resp'
}
method_settings = {'basis': '6-31g*'}                                           

resp_drv = vlx.RespChargesDriver()
resp_drv.update_settings(resp_settings, method_settings)
resp_charges = resp_drv.compute(empty_mol, empty_bas, 'resp')

print("Boltzmann-weighted RESP charges =" , resp_charges)
