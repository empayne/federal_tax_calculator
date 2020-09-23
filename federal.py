import argparse
import logging

from tax_bracket_collection import TaxBracketCollection
from utils import Utils

def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-v", "--verbose", 
        help="show intermediate tax values", 
        action="store_true"
    )
    parser.add_argument(
        "-c", "--config",
        help="specify location of configuration file"
    )
    parser.add_argument("income", help="income in dollars", type=float)
    args = parser.parse_args()  

    return args.income, args.verbose, args.config

def setup_logger(verbose):
    log_level = logging.INFO if verbose else logging.ERROR
    logging.basicConfig(level=log_level)

def calculate_tax_owed(income, configuration):
    tax_brackets = TaxBracketCollection(configuration)
    return tax_brackets.calculate_tax(income)

def calculate_effective_tax_rate(income, configuration):
    tax_brackets = TaxBracketCollection(configuration)
    return tax_brackets.effective_tax_rate(income)

def main():
    income, verbose, config_file = parse_arguments()
    configuration = Utils.read_tax_brackets_configuration(config_file)
    setup_logger(verbose)
    
    tax_owed = calculate_tax_owed(income, configuration)
    effective_tax_rate = calculate_effective_tax_rate(income, configuration)
    logging.info(f"calculated an effective tax rate of {effective_tax_rate}")
    print(Utils.format_currency(tax_owed))

main()