from sqlwrap import Row

class PropertyName(Row):
    keys = 'id name'.split()

class EnvironmentFingerprint(Row):
    keys = 'id fingerprint'.split()

class ConstantSmiles(Row):
    keys = 'id smiles'.split()

class RuleSmiles(Row):
    keys = 'id smiles num_heavies'.split()

class RuleEnvironment(Row):
    keys = 'id rule_id environment_fingerprint_id radius'.split()

class Rule(Row):
    keys = 'id from_smiles_id to_smiles_id'.split()

class Pair(Row):
    keys = 'id rule_environment_id compound1_id compound2_id constant_id'.split()

class Compound(Row):
    keys = 'id public_id input_smiles clean_smiles clean_num_heavies'.split()

class CompoundProperty(Row):
    keys = 'id compound_id property_name_id value'.split()
