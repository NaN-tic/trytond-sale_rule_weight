# This file is part of the sale_rule_weight module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class SaleRuleWeightTestCase(ModuleTestCase):
    'Test Sale Rule Weight module'
    module = 'sale_rule_weight'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleRuleWeightTestCase))
    return suite