import csv
import pandas as pd
import plotly.figure_factory as ff

df = pd.read_csv('phone.csv')
fig = ff.create_distplot([df['Avg Rating'].tolist()], ['Average Rating'],show_hist = True )
fig.show()