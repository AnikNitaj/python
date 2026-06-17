import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv("lesson14.csv")

nobel_prices = ds.groupby("Continent")["Nobel Prices"].sum()

no_of_continents  = nobel_prices.count()

colors = ["gold","lightcoral","yellow","orange","lightskyblue","aquamarine","burlywood"]

plt.figure(figsize=(10,10))

nobel_prices.plot(kind="pie",colors=colors,autopct="%1.1f%%")

plt.show()