import veloxchem as vlx
import numpy as np 

molecule = vlx.Molecule.read_xyz_string("""10

O             -1.009866880244         1.299407071912         1.951947754409
C              0.031038818173         2.001294498224         1.244371321259
C              0.339506903623         0.795807201271         2.029917688849
C              0.600316751832        -0.544462572436         1.394186918859
H             -0.026285836651         1.930258644799         0.154459855148
H              0.271804379347         2.990968281608         1.641505800108
H              0.794935917667         0.948100885444         3.014899839267
H              0.113110324011        -0.610670447580         0.412641743927
H              1.681576973773        -0.701096452623         1.264343536564
H              0.213803265264        -1.354101659046         2.029564064183""")

basis = vlx.MolecularBasis.read(molecule, 'def2-svp')

scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = 'cam-b3lyp'
scf_drv.filename = 'methoxirane-ord'
scf_results = scf_drv.compute(molecule, basis)

cpp_drv = vlx.ComplexResponse()
cpp_drv.frequencies = np.arange(0.2, 0.35, 0.0025)
cpp_drv.damping = 0.0045563
cpp_drv.property = "ord"
cpp_drv.filename = 'methoxirane-ord'

cpp_results = cpp_drv.compute(molecule, basis, scf_results)
