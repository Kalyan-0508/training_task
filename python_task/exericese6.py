
import pandas as pd

celsius = [25, 30, 18, 22, 27]
c_series = pd.Series(celsius)
print("Celsius Series:")
print(c_series)
f_series = (c_series * 9/5) + 32
print("\nFahrenheit Series:")
print(f_series)
