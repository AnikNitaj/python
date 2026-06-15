import pandas as pd

data = {"name":["A","B","C"],
        "age":[18,20,39],
        "City":["Prishtin","Malishev","Deqanit"]
        }


df = pd.DataFrame(data)

print(df)

fajlli = pd.read_csv("data.csv")
print(fajlli)

teDhenat = df.to.csv("data.csv",index=false)
print(teDhenat)