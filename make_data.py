#!/usr/bin/env python

import sys, os
import argparse
#import pickle
import tqdm
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors

def run(iname):
    bname = os.path.basename(iname).split('_')[0]
    lines = open(iname, 'rt').read().split('\n')
    out_smi = open(bname+'.smi', 'wt')
    out_csv = open(bname+'.csv', 'wt')

    print('ID\tMW\tlogP\tn\tvalue\tstd', file=out_csv)

    D = {}
    for line in lines:
        if line.startswith('#') or len(line) == 0:
            continue
        it = line.split('\t')
        smiles, chembl_id, assay_type, relation, value, units, flag = it
        if smiles not in D:
            D[smiles] = dict(chembl_id=chembl_id, entries=[])
        D[smiles]['entries'].append((assay_type, relation, value, units))

    pbar = tqdm.tqdm(total=len(D), ascii=False)
    for smiles in D:
        pbar.update()

        N = len(D[smiles]['entries'])

        values = []
        for entry in D[smiles]['entries']:
            if entry[3] != 'nM':
                continue
            try:
                value = float(entry[2])
            except:
                continue
            values.append(value)

        n = len(values)

        if n == 0:
            continue

        mol = Chem.MolFromSmiles(smiles)
        if mol is None:
            continue

        if n == 1:
            avg = round(values[0], 2)
            std = '*'
        else:
            values = np.array(values)
            avg = round(np.mean(values), 2)
            std = round(np.std(values), 2)

        if avg == 0.0:
            continue

        mw = round(Descriptors.MolWt(mol), 2)
        logp = round(Descriptors.MolLogP(mol), 2)

        chembl_id = D[smiles]['chembl_id']

        print(smiles, chembl_id, sep='\t', file=out_smi)
        print(chembl_id, mw, logp, n, avg, std, sep='\t', file=out_csv)

    out_smi.close()
    out_csv.close()

parser = argparse.ArgumentParser()
#parser.add_argument('-i', '--init', action='store_true', dest='initialize', help='Initialize')
parser.add_argument('iname', type=str, help='input smiles')
args = parser.parse_args()

iname = args.iname

assert iname.endswith('_orig.smi')

run(iname)
#pickle.dump(D, open('.dump.pkl', 'wb'))
