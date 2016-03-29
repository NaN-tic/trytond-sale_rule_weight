# This file is part of the sale_rule_weight module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['SaleRuleCondition']


class SaleRuleCondition:
    __metaclass__ = PoolMeta
    __name__ = 'sale.rule.condition'

    @classmethod
    def __setup__(cls):
        super(SaleRuleCondition, cls).__setup__()
        criteria = ('weight', 'Total Weight')
        if criteria not in cls.criteria.selection:
            cls.criteria.selection.append(criteria)

    def evaluate_weight(self, sale):
        return self.apply_comparison(sale.weight)
