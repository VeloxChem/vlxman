import veloxchem as vlx

rea1 = vlx.Molecule.read_smiles("[Br]")
rea2 = vlx.Molecule.read_smiles("CCl")
rea1.set_charge(-1)

pro1 = vlx.Molecule.read_smiles("[Cl]")
pro2 = vlx.Molecule.read_smiles("CBr")
pro1.set_charge(-1)

tsguesser = vlx.TransitionStateGuesser()
results = tsguesser.find_transition_state([rea1, rea2], [pro1, pro2])
