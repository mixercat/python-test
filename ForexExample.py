from forex_python.converter import CurrencyRates
c = CurrencyRates()
print(c.get_rates('USD'))
print(type(c.get_rates('USD')))
print(c.convert('USD', 'THB', 1))