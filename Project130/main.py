import csv
import pandas as pd 

df = pd.read_csv("finaloutput.csv")

print(df.shape)

del df["Name1"]

del df["Radius1"]

del df["Mass1"]

del df["Distance1"]

del df["Luminosity"]

df = df.rename({
    'Name' : 'Star_name',

    'Distance' : 'Star_distance',

    'Radius' : "Star_radius",

    'Mass' : 'Star_mass'
}
, axis = "columns")

df.to_csv("final.csv")

