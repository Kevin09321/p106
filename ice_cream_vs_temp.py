import plotly.express as px
import csv

with open("../data/icecream.csv") as csv_file:
      df = csv.DirectReader(csv_file)
      fig = px.scatter(df,x="Temperature", y="Ice-cream Sales( ₹ )")
      fig.show
