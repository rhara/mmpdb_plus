import sys
import pickle
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors

"""
lines = open('000064_orig.smi', 'rt').read().split('\n')
out_smi = open('000064.smi', 'wt')
out_csv = open('000064.csv', 'wt')
smiles_dict = {}
print('ID\tMW\tlogP', file=out_csv)
count = 0
for line in lines:
    if line.startswith('#') or len(line) == 0:
        continue
    it = line.split('\t')
    smiles, chembl_id, assay_type, relation, value, units, flag = it
    if smiles not in smiles_dict:
        smiles_dict[smiles] = []
    smiles_dict[smiles].append((assay_type, relation, value, units, flag))
    mol = Chem.MolFromSmiles(smiles)
    count += 1
    mw = round(Descriptors.MolWt(mol), 2)
    logp = round(Descriptors.MolLogP(mol), 2)
    print(smiles, chembl_id, sep='\t', file=out_smi)
    print(count, chembl_id, mw, logp, sep='\t', file=out_csv)

if out_smi != sys.stdout:
    out_smi.close()
if out_csv != sys.stdout:
    out_csv.close()

# pickle.dump(smiles_dict, open('.dump.pkl', 'wb'))
"""

smiles_dict = pickle.load(open('.dump.pkl', 'rb'))
for k in smiles_dict:
    v = smiles_dict[k]
    values = []
    for entry in smiles_dict[k]:
        if entry[3] != 'nM':
            continue
        try:
            value = float(entry[2])
        except:
            continue
        values.append(value)
    values = np.array(values)
    avg = np.mean(values)
    std = np.std(values)
    print(f'{k} valid={values.shape[0]}/{len(v)} {avg}+-{std}')
