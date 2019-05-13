from sqlwrap import Table
from rows import *

class TablePropertyName(Table):
    row_klass = PropertyName

class TableEnvironmentFingerprint(Table):
    row_klass = EnvironmentFingerprint

class TableConstantSmiles(Table):
    row_klass = ConstantSmiles

class TableRuleSmiles(Table):
    row_klass = RuleSmiles

class TableRuleEnvironment(Table):
    row_klass = RuleEnvironment

class TableRule(Table):
    row_klass = Rule

class TablePair(Table):
    row_klass = Pair

    def get_pairs_from_rule_environment_id(self, renvid):
        pairs = []
        for pair in self:
            if pair.rule_environment_id == renvid:
                pairs.append(pair)
        return pairs

class TableCompound(Table):
    row_klass = Compound

class TableCompoundProperty(Table):
    row_klass = CompoundProperty
