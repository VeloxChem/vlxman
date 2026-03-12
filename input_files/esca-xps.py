import veloxchem as vlx
import copy
import numpy as np

molecule = vlx.Molecule.read_xyz_string("""13
ESCA b3lyp/def2-svp optimized geometry
C              1.326024532622         0.471089167011        -1.154937296389
C              0.484399509715         0.908494386259         0.037569541020
C              0.270494167717        -0.188493907246         1.053914467110
O              0.701245126416        -1.308212251798         0.971080711541
C             -0.582260522270         0.210893702941         2.291730106998
F             -0.731967860619        -0.799813015071         3.135965340271
F             -1.800383044157         0.625073687043         1.897202571864
F              0.003899498844         1.231896946553         2.943599980006
H              1.453639490166         1.302028888463        -1.864264306255
H              0.853135331881        -0.368249103011        -1.686230702784
H              2.322713498820         0.134038471332        -0.833394707486
H              0.936346512410         1.764030447212         0.571699332428
H             -0.514670521097         1.267150587304        -0.270103071648""")

basis = vlx.MolecularBasis.read(molecule, "def2-svp")

# Ground state SCF
scf_drv = vlx.ScfRestrictedDriver()
scf_drv.xcfun = "pbe"
scf_drv.ri_coulomb = True
scf_results = scf_drv.compute(molecule, basis)

# Create a molecular ion
molecular_ion = copy.deepcopy(molecule)
molecular_ion.set_charge(1)
molecular_ion.set_multiplicity(2)

# create a FCH on the C 1s core orbitals and
# compute the core ionization energy
ies = []
nalpha = molecule.number_of_alpha_electrons()
orbs = scf_drv.molecular_orbitals
gs_energy = scf_drv.get_scf_energy()

for mo in [4, 5, 6, 7]:
    # remove the selected MO from the occupied beta list for MOM
    occa = np.arange(0, nalpha, 1).tolist()
    occb = np.arange(0, nalpha, 1).tolist()
    occb.remove(mo)

    # run the SCF with a full core hole on the selected MO
    scf_ion = vlx.ScfUnrestrictedDriver()
    scf_ion.xcfun = "pbe"
    scf_ion.ri_coulomb = True
    scf_ion.maximum_overlap(molecular_ion, basis, orbs, occa, occb)
    fch_results = scf_ion.compute(molecular_ion, basis)
    fch_energy = scf_ion.get_scf_energy()

    # Calculate the core-ionization energy
    ie = (fch_energy - gs_energy) * vlx.hartree_in_ev()
    
    ies.append(ie)
