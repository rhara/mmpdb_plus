#!/usr/bin/env python

import sys, sqlite3, re
from rows import *
from tables import *
from sqlwrap import conn

conn[0] = sqlite3.connect(sys.argv[1])

out = sys.stdout

table_property_name = TablePropertyName('property_name')
table_environment_fingerprint = TableEnvironmentFingerprint('environment_fingerprint')
table_constant_smiles = TableConstantSmiles('constant_smiles')
table_rule_smiles = TableRuleSmiles('rule_smiles')
table_rule_environment = TableRuleEnvironment('rule_environment')
table_rule = TableRule('rule')
table_pair = TablePair('pair')
table_compound = TableCompound('compound')
table_compound_property = TableCompoundProperty('compound_property')

out.write('renv_id\tradius\tenv_fpid\tsmirks\tconstant_smiles\tfrom_smiles\tfrom_name\tto_smiles\tto_name\n')

for renv in table_rule_environment:
    env_fpid = renv.environment_fingerprint_id
    env_fp = table_environment_fingerprint[env_fpid].fingerprint
    radius = renv.radius
    rule_id = renv.rule_id
    from_smiles_id = table_rule.idmap[rule_id].from_smiles_id
    to_smiles_id = table_rule.idmap[rule_id].to_smiles_id
    from_smiles = table_rule_smiles.idmap[from_smiles_id].smiles
    to_smiles = table_rule_smiles.idmap[to_smiles_id].smiles
    env_items = f'{renv.id}\t{radius}\t{env_fpid}\t{from_smiles}>>{to_smiles}'
    pairs = table_pair.get_pairs_from_rule_environment_id(renv.id)
    for pair in pairs:
        compound1_name = table_compound.idmap[pair.compound1_id].public_id
        compound2_name = table_compound.idmap[pair.compound2_id].public_id
        compound1_smiles = table_compound.idmap[pair.compound1_id].clean_smiles
        compound2_smiles = table_compound.idmap[pair.compound2_id].clean_smiles
        constant_smiles = table_constant_smiles.idmap[pair.constant_id].smiles
        pair_items = f'{constant_smiles}\t{compound1_smiles}\t{compound1_name}\t{compound2_smiles}\t{compound2_name}'
        out.write(f'{env_items}\t{pair_items}\n')
