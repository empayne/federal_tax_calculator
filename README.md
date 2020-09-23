# federal_tax_calculator

Small command line utility to calculate federal income tax rates. To run it, clone the repository to your local machine and run:

```
python3 federal.py <income> 
```

Sample output is as follows:

```
python3 federal.py 500000
143902.87
```

To see intermediate calculations, run in verbose mode with `-v`:

```
python3 federal.py 500000 -v
INFO:root:Initialized with 4 brackets, top marginal rate of 0.33
INFO:root:added tax of $7280.25 ($48535.00 at rate 0.15)
INFO:root:added tax of $9949.47 ($48534.00 at rate 0.205)
INFO:root:added tax of $13885.04 ($53404.00 at rate 0.26)
INFO:root:added tax of $18529.55 ($63895.00 at rate 0.29)
INFO:root:added tax of $94258.56 ($285632.00 at rate 0.33)
143902.87
```

To use an alternate configuration file, specify the path with `-c` (a flat tax rate configuration file is included as an example):
```
python3 federal.py 500000 -v -c ./config/flat_tax_rate.json
INFO:root:Initialized with 0 brackets, top marginal rate of 0.16
INFO:root:added tax of $80000.00 ($500000.00 at rate 0.16)
80000.00
```

To run tests, run the following command:
```
python3 -m unittest test_tax_bracket test_tax_bracket_collection test_utils
```
