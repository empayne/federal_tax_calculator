import logging
from utils import Utils

class TaxBracket:
    def __init__(self, income, rate):
        if income < 0: raise Exception("Negative incomes are not supported")
        if rate < 0: raise Exception("Negative tax rates are not supported")

        self.income = income
        self.rate = rate

    def calculate_tax(self, taxable_income):
        if taxable_income > self.income:
            raise Exception(
                "calculate_tax called with taxable_income beyond bracket limit"
            )

        tax = taxable_income * self.rate
        logging.info(
            f"added tax of ${Utils.format_currency(tax)} " \
            f"(${Utils.format_currency(taxable_income)} at rate {self.rate})"
        )
        return tax