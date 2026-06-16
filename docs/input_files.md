(sec:input-file-examples)=

# Input/output file examples



<div style="margin: 2em 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.74em; table-layout: fixed;">
  <thead>
    <tr style="background-color: #f0f0f0; border-bottom: 2px solid #333;">
      <th style="padding: 12px; text-align: left; border: 1px solid #ddd; width: 28%;">Description</th>
      <th style="padding: 12px; text-align: center; border: 1px solid #ddd; width: 18%;">Python script <br>(input)</th>
      <th style="padding: 12px; text-align: center; border: 1px solid #ddd; width: 18%;">Text format <br>(input)</th>
      <th style="padding: 12px; text-align: center; border: 1px solid #ddd; width: 18%;">Log file<br>(output)</th>
      <th style="padding: 12px; text-align: center; border: 1px solid #ddd; width: 18%;">HDF5 file<br>(output)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:ref-states" style="text-decoration: none; color: inherit;">Reference states</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:rhf">SCF optimization</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/biphenyl-scf.py" download>biphenyl-scf.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/biphenyl-scf.inp" download>biphenyl-scf.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/biphenyl-scf.out" download>biphenyl-scf.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/biphenyl-scf.h5" download>biphenyl-scf.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:rohf">ROHF optimization</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/tempo-roscf.py" download>tempo-roscf.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/tempo-roscf.inp" download>tempo-roscf.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/tempo-roscf.out" download>tempo-roscf.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/tempo-roscf.h5" download>tempo-roscf.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:uhf">UHF optimization</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/trityl-uscf.py" download>trityl-uscf.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/trityl-uscf.inp" download>trityl-uscf.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/trityl-uscf.out" download>trityl-uscf.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/trityl-uscf.h5" download>trityl-uscf.h5</a>
      </td>
    </tr>
    <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:hamiltonian" style="text-decoration: none; color: inherit;">Hamiltonian</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:static-electric-fields">Static Electric Field</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/pna-field.py" download>pna-field.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/pna-field.inp" download>pna-field.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/pna-field.out" download>pna-field.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/pna-field.h5" download>pna-field.h5</a>
      </td>
    </tr>
    <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:environment" style="text-decoration: none; color: inherit;">Environment</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:cpcm">CPCM</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/eth-cpcm.py" download>eth-cpcm.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/eth-cpcm.inp" download>eth-cpcm.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/eth-cpcm.out" download>eth-cpcm.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/eth-cpcm.h5" download>eth-cpcm.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:smd">SMD</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/eth-smd.py" download>eth-smd.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/eth-smd.inp" download>eth-smd.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/eth-smd.out" download>eth-smd.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/eth-smd.h5" download>eth-smd.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:pe">PE/NPE</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/hs276_pe.py" download>hs276_pe.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/hs276_pe.inp" download>hs276_pe.inp</a>
        <a href="../input_files/solvent_pe.pot" download>solvent_pe.pot</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/hs276_pe.out" download>hs276_pe.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/hs276_pe.h5" download>hs276_pe.h5</a>
      </td>
    </tr>
    <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:pes" style="text-decoration: none; color: inherit;">Potential energy surfaces</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:GS-opt">S0 Optimization</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/bithio-S0-opt.py" download>bithio-S0-opt.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/bithio-S0-opt.inp" download>bithio-S0-opt.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/bithio-S0-opt.out" download>bithio-S0-opt.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/bithio-S0-opt.h5" download>bithio-S0-opt.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:freeze">Set/Freeze coordinate</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/bithio-freeze.py" download>bithio-freeze.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/bithio-freeze.inp" download>bithio-freeze.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/bithio-freeze.out" download>bithio-freeze.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/bithio-freeze.h5" download>bithio-freeze.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:scan">Scan coordinate</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/bithio-scan.py" download>bithio-scan.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/bithio-scan.inp" download>bithio-scan.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/bithio-scan.out" download>bithio-scan.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/bithio-scan.h5" download>bithio-scan.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:TS-opt">TS optimization</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/Sn2-ts.py" download>Sn2-ts.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/Sn2-ts.inp" download>Sn2-ts.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/Sn2-ts.out" download>Sn2-ts.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/Sn2-ts.h5" download>Sn2-ts.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:IRC">IRC</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/Sn2-irc.py" download>Sn2-irc.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/Sn2-irc.inp" download>Sn2-irc.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/Sn2-irc.out" download>Sn2-irc.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/Sn2-irc.h5" download>Sn2-irc.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:ES-opt">S1 Optimization</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/bithio-S1-opt.py" download>bithio-S1-opt.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/bithio-S1-opt.inp" download>bithio-S1-opt.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/bithio-S1-opt.out" download>bithio-S1-opt.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/bithio-S1-opt.h5" download>bithio-S1-opt.h5</a>
      </td>
    </tr>    
    <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:uv_vis" style="text-decoration: none; color: inherit;">UV/Vis absoprtion/emission</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:TDDFT-uv">TDDFT</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/tq-uv-vis.py" download>tq-uv-vis.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/tq-uv-vis.inp" download>tq-uv-vis.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/tq-uv-vis.out" download>tq-uv-vis.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/tq-uv-vis.h5" download>tq-uv-vis.h5</a>
      </td>
    </tr>     
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:cpp-uv">CPP</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/tq-cpp.py" download>tq-cpp.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/tq-cpp.inp" download>tq-cpp.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/tq-cpp.out" download>tq-cpp.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/tq-cpp.h5" download>tq-cpp.h5</a>
      </td>
    </tr>
        <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:fop" style="text-decoration: none; color: inherit;">First-order properties</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:dipole">Electric dipole moment GS</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/pna-GS-dipole.py" download>pna-GS-dipole.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/pna-GS-dipole.inp" download>pna-GS-dipole.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/pna-GS-dipole.out" download>pna-GS-dipole.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/pna-GS-dipole.h5" download>pna-GS-dipole.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:res-region">Electric dipole moment ES</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/pna-ES-dipole.py" download>pna-ES-dipole.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/pna-ES-dipole.out" download>pna-ES-dipole.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/pna-ES-dipole.h5" download>pna-ES-dipole.h5</a>
      </td>
    </tr> 
        <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:alpha" style="text-decoration: none; color: inherit;">Polarizability</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:nonres-region">Nonresonant region</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/meth-nonres.py" download>meth-nonres.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/meth-nonres.inp" download>meth-nonres.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/meth-nonres.out" download>meth-nonres.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/meth-nonres.h5" download>meth-nonres.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:res-region">Resonant region</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/eth-res.py" download>eth-res.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;"> 
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
       <a href="../output_files/eth-res.out" download>eth-res.out</a>   
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
       <a href="../output_files/eth-res.h5" download>eth-res.h5</a>
       </td>
    </tr> 
    <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:ecd" style="text-decoration: none; color: inherit;">Optical activity and dichroism</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:TDDFT-ecd">ECD (TDDFT)</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/alanine-ecd.py" download>alanine-ecd.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/alanine-ecd.inp" download>alanine-ecd.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/alanine-ecd.out" download>alanine-ecd.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/alanine-ecd.h5" download>alanine-ecd.h5</a>
      </td>
    </tr>     
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:cpp-ecd">ECD (CPP)</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/alanine-cpp.py" download>alanine-cpp.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/alanine-cpp.inp" download>alanine-cpp.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/alanine-cpp.out" download>alanine-cpp.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/alanine-cpp.h5" download>alanine-cpp.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:cpp-ord">ORD (CPP)</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/methoxirane-ord.py" download>methoxirane-ord.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/methoxirane-ord.out" download>methoxirane-ord-cpp.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/methoxirane-ord.h5" download>methoxirane-ord-cpp.h5</a>
      </td>
    </tr>
    <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:vib_spect" style="text-decoration: none; color: inherit;">Vibrational spectroscopies</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:ir">IR</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/acro-ir.py" download>acro-ir.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/acro-ir.inp" download>acro-ir.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/acro-ir.out" download>acro-ir.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/acro-ir.h5" download>acro-ir.h5</a>
      </td>
    </tr>       
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:raman">Raman</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/acro-raman.py" download>acro-raman.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/acro-raman.inp" download>acro-raman.inp</a>
      </td>git add 
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/acro-raman.out" download>acro-raman.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/acro-raman.h5" download>acro-raman.h5</a>
      </td>
    </tr>   
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:rrs">Resonance Raman</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/acro-rr.py" download>acro-rr.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/acro-rr.inp" download>acro-rr.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/acro-rr.out" download>acro-rr.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/acro-rr.h5" download>acro-rr.h5</a>
      </td>
    </tr>
    <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:weak_interactions" style="text-decoration: none; color: inherit;">Weak interactions</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:c6">C6</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/meth-c6.py" download>meth-c6.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/meth-c6.inp" download>meth-c6.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/meth-c6.out" download>meth-c6.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/meth-c6.h5" download>meth-c6.h5</a>
      </td>
    </tr>
    <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:loc_prop" style="text-decoration: none; color: inherit;">Localized properties</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:esp">ESP</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/h2o-esp.py" download>h2o-esp.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/h2o-esp.inp" download>h2o-esp.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/h2o-esp.out" download>h2o-esp.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/h2o-esp.h5" download>h2o-esp.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:resp">RESP</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/h2o-resp.py" download>h2o-resp.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/h2o-resp.inp" download>h2o-resp.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/h2o-resp.out" download>h2o-resp.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/h2o-resp.h5" download>h2o-resp.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#subsec:bol-weighted-resp">Boltzmann-weighted RESP</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/pro-resp-bw.py" download>pro-resp-bw.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/pro-resp-bw.inp" download>pro-resp-bw.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/pro-resp-bw.out" download>pro-resp-bw.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/pro-resp-bw.h5" download>pro-resp-bw.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:loprop">LoProp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/h2o-loprop.py" download>h2o-loprop.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/h2o-loprop.inp" download>h2o-loprop.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/h2o-loprop.out" download>h2o-loprop.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/h2o-loprop.h5" download>h2o-loprop.h5</a>
      </td>
    </tr>
    <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:nlo" style="text-decoration: none; color: inherit;">Multi-photon interactions</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:tpa">Two-photon absorption</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/pna-tpa.py" download>pna-tpa.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/pna-tpa.inp" download>pna-tpa.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/pna-tpa.out" download>pna-tpa.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
       <a href="../output_files/pna-tpa.h5" download>pna-tpa.h5</a>
      </td>
    </tr>     <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:tpacs">TPA cross section</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/pna-tpacs.py" download>pna-tpacs.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/pna-tpacs.inp" download>pna-tpacs.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/pna-tpacs.out" download>pna-tpacs.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/pna-tpacs.h5" download>pna-tpacs.h5</a>
      </td>
    </tr>   
    <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:xray" style="text-decoration: none; color: inherit;">X-ray spectroscopies</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:xps">XPS</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/esca-xps.py" download>esca-xps.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/esca-xps.inp" download>esca-xps.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/esca-xps.out" download>esca-xps.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
       <a href="../output_files/esca-xps.h5" download>esca-xps.h5</a>
      </td>
    </tr>     <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:xas-cvs">XAS (CVS)</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/xas-cvs.py" download>xas-cvs.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/xas-cvs.inp" download>xas-cvs.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
       <a href="../output_files/xas-cvs.out" download>xas-cvs.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
       <a href="../output_files/xas-cvs.h5" download>xas-cvs.h5</a>
      </td>
    </tr> 
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:xas-cpp">XAS (CPP)</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/esca-nexafs.py" download>esca-nexafs.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/esca-nexafs.inp" download>esca-nexafs.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/esca-nexafs.out" download>esca-nexafs.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/esca-nexafs.h5" download>esca-nexafs.h5</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:rixs">RIXS</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/esca-rixs.py" download>esca-rixs.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/esca-rixs.inp" download>esca-rixs.inp</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/esca-rixs.out" download>esca-rixs.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/esca-rixs.h5" download>esca-rixs.h5</a>
      </td>
    </tr>   
    <tr style="background-color: #f5f5f5;">
      <td colspan="5" style="padding: 10px; font-weight: bold; border: 1px solid #ddd; text-align: center;">
        <a href="#sec:general-response" style="text-decoration: none; color: inherit;">General response functions</a>
      </td>
    </tr>
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:cpp_lrf">Linear response</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/h2o2-lrf.py" download>h2o2-lrf.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/h2o2-lrf.out" download>h2o2-lrf.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/h2o2-lrf.h5" download>h2o2-lrf.h5</a>
      </td>
    </tr>  
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:cpp_qrf">Quadratic response</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/h2o2-qrf.py" download>h2o2-qrf.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/h2o2-qrf.out" download>h2o2-qrf.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/h2o2-qrf.h5" download>h2o2-qrf.h5</a>
      </td>
    </tr>   
    <tr style="background-color: #fff;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:cpp_crf">Cubic response</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../input_files/h2o2-crf.py" download>h2o2-crf.py</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/h2o2-crf.out" download>h2o2-crf.out</a>
      </td>
      <td style="padding: 8px; text-align: center; border: 1px solid #ddd;">
        <a href="../output_files/h2o2-crf.h5" download>h2o2-crf.h5</a>
      </td>
    </tr>    
  </tbody>
</table>
</div>

