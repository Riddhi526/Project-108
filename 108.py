import pandas as pd
import csv
import plotly.figure_factory as pf

data = pd.read_csv("data.csv")
fig = pf.create_distplot([data["Avg Rating"].tolist()],["rating"])
fig.show()