import logging
from decimal import Decimal

from tax_bracket import TaxBracket

class TaxBracketCollection:
    def __init__(self, tax_brackets_configuration):
        self.tax_brackets = []
        for bracket in tax_brackets_configuration['brackets']:
            new_bracket = TaxBracket(
                bracket['income'],
                bracket['rate']
            ) 
            self.tax_brackets.append(new_bracket)

        self.top_marginal_bracket = TaxBracket(
            Decimal('Infinity'),
            tax_brackets_configuration['top_marginal_rate']
        )
        
        logging.info(
            f"Initialized with {len(tax_brackets_configuration['brackets'])} " \
            f"brackets, top marginal rate of "\
            f"{tax_brackets_configuration['top_marginal_rate']}"
        )
    
    def calculate_tax(self, income):
        if income < 0:
            raise Exception("Negative incomes are not supported")

        total_tax = 0
        for bracket in self.tax_brackets:
            if income == 0:
                break
            taxable_in_bracket = min(income, bracket.income)
            total_tax += bracket.calculate_tax(taxable_in_bracket)
            income -= taxable_in_bracket

        if income > 0:
            total_tax += self.top_marginal_bracket.calculate_tax(income)

        return total_tax
