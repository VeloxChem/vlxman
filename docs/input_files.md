(sec:input-file-examples)=

# Input file examples


| Description | Python script (input) | Text format (input) | Log file (output)  | HDF5 file (output)   |
|-------------|:---------------:|:-------------:|:--------:|:--------:|
| [Reference states](#sec:ref-states) | |  | |  |
| [SCF optimization](#sec:rhf)   | {download}`biphenyl-scf.py <../input_files/biphenyl-scf.py>`| {download}`biphenyl-scf.inp <../input_files/biphenyl-scf.inp>` | {download}`biphenyl-scf.out <../output_files/biphenyl-scf.out>`| {download}`biphenyl-scf.h5 <../output_files/biphenyl-scf.h5>` |
| [ROHF optimization](#sec:rohf)   | {download}`tempo-roscf.py <../input_files/tempo-roscf.py>`| {download}`tempo-roscf.inp <../input_files/tempo-roscf.inp>` | {download}`tempo-roscf.out <../output_files/tempo-roscf.out>`| {download}`tempo-roscf.h5 <../output_files/tempo-roscf.h5>` |
| [UHF optimization](#sec:uhf)   | {download}`trityl-uscf.py <../input_files/trityl-uscf.py>`| {download}`trityl-uscf.inp <../input_files/trityl-uscf.inp>` | {download}`trityl-uscf.out <../output_files/trityl-uscf.out>`| {download}`trityl-uscf.h5 <../output_files/trityl-uscf.h5>` |
 | |  | |  |  |
| [Hamiltonian](#sec:hamiltonian)  | |  | |  |
| [Static Electric Field](#sec:static-electric-fields) | {download}`pna-field.py <../input_files/pna-field.py>`| {download}`pna-field.inp <../input_files/pna-field.inp>` | {download}`pna-field.out <../output_files/pna-field.out>`| {download}`pna-field.h5 <../output_files/pna-field.h5>` |
 | |  | |  |  |
| [Environment](#sec:environment)  | |  | |  |
| [CPCM](#sec:cpcm)  | {download}`eth-cpcm.py <../input_files/eth-cpcm.py>`| {download}`eth-cpcm.inp <../input_files/eth-cpcm.inp>` | {download}`eth-cpcm.out <../output_files/eth-cpcm.out>`| {download}`eth-cpcm.h5 <../output_files/eth-cpcm.h5>` |
| [SDM](#sec:sdm)  | {download}`eth-smd.py <../input_files/eth-smd.py>`| {download}`eth-smd.inp <../input_files/eth-smd.inp>` | {download}`eth-smd.out <../output_files/eth-smd.out>`| {download}`eth-smd.h5 <../output_files/eth-smd.h5>` |
 | |  | |  |  |
| [Potentail energy surfaces](#sec:pes)   | |  | |  |
|[Ground State Optimization](#sec:GS-opt) | {download}`bithio-S0-opt.py <../input_files/bithio-S0-opt.py>`| {download}`bithio-S0-opt.inp <../input_files/bithio-S0-opt.inp>` | {download}`bithio-S0-opt.out <../output_files/bithio-S0-opt.out>`| {download}`bithio-S0-opt.h5 <../output_files/bithio-S0-opt.h5>` |
|[Excited State Optimization](#sec:ES-opt) | {download}`bithio-S1-opt.py <../input_files/bithio-S1-opt.py>`| {download}`bithio-S1-opt.inp <../input_files/bithio-S1-opt.inp>` | {download}`bithio-S1-opt.out <../output_files/bithio-S1-opt.out>`| {download}`bithio-S1-opt.h5 <../output_files/bithio-S1-opt.h5>` |

<div style="margin: 2em 0;">
<table style="width: 100%; border-collapse: collapse; font-size: 0.8em; table-layout: fixed;">
  <thead>
    <tr style="background-color: #f0f0f0; border-bottom: 2px solid #333;">
      <th style="padding: 12px; text-align: left; border: 1px solid #ddd; width: 28%;">Description</th>
      <th style="padding: 12px; text-align: center; border: 1px solid #ddd; width: 18%;">Python script (input)</th>
      <th style="padding: 12px; text-align: center; border: 1px solid #ddd; width: 18%;">Text format (input)</th>
      <th style="padding: 12px; text-align: center; border: 1px solid #ddd; width: 18%;">Log file (output)</th>
      <th style="padding: 12px; text-align: center; border: 1px solid #ddd; width: 18%;">HDF5 file (output)</th>
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
    <tr style="background-color: #f9f9f9;">
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
    <tr style="background-color: #f9f9f9;">
      <td style="padding: 8px; padding-left: 24px; border: 1px solid #ddd;">
        <a href="#sec:sdm">SDM</a>
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
    <tr style="background-color: #f9f9f9;">
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
  </tbody>
</table>
</div>

