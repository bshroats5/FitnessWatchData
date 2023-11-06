import pandas as pd
import plotly.io as pio
import plotly.graph_objects as go
pio.templates.default = "plotly_white"
import plotly.express as px

data = pd.read_csv("Apple-Fitness-Data.csv")
print(data.head())
print(data.isnull().sum())


# Step Count Over Time
fig1 = px.line(data, x="Time",
y="Step Count",
title="Step Count Over Time")
fig1.show()
