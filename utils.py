import json

class Utils:
    @classmethod
    def format_currency(self, value):
        # For a more robust use case, we may want to use a currency class
        # (eg. https://pypi.org/project/money/) versus using a float and
        # printing out the rounded value.
        return format(value, '.2f')

    @classmethod
    def read_tax_brackets_configuration(self, config_file):
        if config_file is None: config_file = "./config/brackets.json"

        with open(config_file) as json_data_file:
            tax_brackets_configuration = json.load(json_data_file)
        return tax_brackets_configuration
