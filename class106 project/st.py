import pandas as pd
import plotly.express as px

df=pd.read_csv("sm.csv")
fig=px.scatter(df,x="Marks In Percentage",y="Days Present",)
fig.show()