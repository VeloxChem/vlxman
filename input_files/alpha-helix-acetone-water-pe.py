import veloxchem as vlx

ens_parser = vlx.EnsembleParser()

ensemble = ens_parser.structures(
    trajectory_file = "alpha-helix-acetone-water.xtc",
    topology_file = "alpha-helix-acetone-water.tpr",
    qm_region = 'resname LIG',
    num_snapshots = 3,
    pe_cutoff = 3.0,
    npe_cutoff = 5.0,
)

print("number residues PE = ", ensemble[0]["number_residues_pe"])
print("number residues NPE = ", ensemble[0]["number_residues_npe"])

ens_drv = vlx.EnsembleDriver()

ens_drv.set_env_models(
    pe_model=["CP3", "SEP"],
    npe_model=["ff19sb", "tip3p"],
)

scf_options = {
   "scf_type": "restricted",
   "conv_thresh": 1.0e-6,
   "max_iter": 150,
   "xcfun": "cam-b3lyp",
   "grid_level": 4,
}

property_options = {
    "property": "absorption",
    "nstates": 5,
    "nto": True,
}

results = ens_drv.compute(
   ensemble,
   basis_set = "aug-pcseg-1",
   scf_options = scf_options,
   property_options = property_options,
)

ens_drv.plot_uv_vis_spectra(
    results,
    show_individual = True,
    show_sticks = True,
    xlim_nm = (150, 275)
)
