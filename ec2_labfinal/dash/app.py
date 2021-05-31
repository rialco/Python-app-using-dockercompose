# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://localhost:4550/ in your web browser.

import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

import mysql.connector as mysqlc
import numpy as np

hostname = os.getenv('MYSQL_HOST')
username = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
database = os.getenv('MYSQL_DB')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

conn = mysqlc.connect(host=hostname, user=username,
                      passwd=password, db=database)
# Check if connection was successful
if (conn.is_connected()):
    # Carry out normal procedure
    print("Connection successful")
else:
    # Terminate
    print("Connection unsuccessful")

mycursor = conn.cursor()
mycursor.execute("SELECT * FROM casos_covid")
data = mycursor.fetchall()

ciudades = []
edades = []
sexos = []
estados = []

ranks = []

for row in data:
    ciudades.append(row[1])
    edades.append(int(row[2]))
    sexos.append(row[3])
    estados.append(row[4])
    ranks.append(row[0])

new_data = {'Ciudad': ciudades, 'Edad': edades,
            'Sexo': sexos, 'Estado': estados}

df = pd.DataFrame(new_data, index=ranks)

fig = px.bar(df, x="Ciudad", y="Edad", color="Sexo", barmode="group")

fig2 = px.bar(df, x="Ciudad", y="Edad", barmode="group")

fig3 = px.bar(df, y="Edad", x="Sexo", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Estructua del computador 2'),

    html.Div(children='''
        Ricardo Alvarez Correa, Krissten Martinez, Jose padilla
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    dcc.Graph(
        id='example-graph2',
        figure=fig2
    ),

    dcc.Graph(
        id='example-graph3',
        figure=fig3
    )
])


if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0", port=4550)
