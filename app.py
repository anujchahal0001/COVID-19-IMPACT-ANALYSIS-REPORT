import numpy as np
import pandas as pd
import plotly.graph_objs as go
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_core_components as dcc






external_stylesheet = [
    {
    'href' : "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css",
    'rel' : "stylesheet",
    'integrity' : "sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC",
    'crossorigin' : "anonymous"
    }
]

patients = pd.read_csv('state_wise_daily.csv')



total = patients.shape[0]
active = patients[patients['Status']=='Confirmed'].shape[0]
recovered = patients[patients['Status']=='Recovered'].shape[0]
deaths = patients[patients['Status']=='Deceased'].shape[0]

options=[
    {'label':'All','value':'All'},
    {'label':'Hospitalized','value':'Hospitalized'},
    {'label':'Recovered','value':'Recovered'},
    {'label':'Deceased','value':'Deceased'}
    ]

option1 =[
    {'label':'All','value':'All'},
    {'label':'Mask','value':'Mask'},
    {'label':'Sanitizer','value':'Sanitizer'},
    {'label':'Oxygen','value':'Oxygen'}
]

option2 = [
    {'label':'Red Zone', 'value':'Red Zone'},
    {'label':'Blue Zone', 'value':'Blue Zone'},
    {'label':'Green Zone', 'value':'Green Zone'},
    {'label':'Orange Zone', 'value':'Orange Zone'}
]





app = dash.Dash(__name__,external_stylesheets=external_stylesheet) #you haven't put the closing bracket here

app.layout = html.Div([
    html.H1('corona virus pandemic',style={'color':'#fff','text-align':'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3('Total Cases',className='text-light'),
                    html.H4(total,className='text-light')
                ],className='card-body')
            ],className='card bg-danger')
        ],className='col-md-3'),
        html.Div([html.Div([
                html.Div([
                    html.H3('Active Cases',className='text-light'),
                    html.H4(active,className='text-light')
                ],className='card-body')
            ],className='card bg-info')],className='col-md-3'),
        html.Div([html.Div([
                html.Div([
                    html.H3('Recovered Cases',className='text-light'),
                    html.H4(recovered,className='text-light')
                ],className='card-body')
            ],className='card bg-warning')],className='col-md-3'),
        html.Div([html.Div([
                html.Div([
                    html.H3('Total deaths',className='text-light'),
                    html.H4(deaths,className='text-light')
                ],className='card-body')
            ],className='card bg-success')],className='col-md-3')
    ],className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='plot-graph',options=option1, value='All'),
                    dcc.Graph(id='graph')
                ],className='card-body')
            ],className='card bg-success')
        ],className='col-md-6'),
#spelling of col-md is wrong
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='my_dropdown', options=option2,value='Status'),
                    dcc.Graph(id='the_graph')
                ],className='card-body')
            ],className='card bg-info')
        ],className='col-md-6')
    ],className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker',options=options, value ='All'),#spelling mistake in options and value
                    dcc.Graph(id='bar')
                ],className='card-body')
            ],className='card')
        ],className='col-md-12')
    ],className='row')
],className='Container')


@app.callback(Output('bar','figure'),[Input('picker','value')])
def update_graph(type):

    if type=='All':
        return {'data':[go.Bar(x=patients['State'],y=patients['Total'])],
                'layout':go.Layout(title='State Total Count',plot_bgcolor='orange')
                }
    if type=='Hospitalized':
        return {'data':[go.Bar(x=patients['State'],y=patients['Hospitalized'])],
                'layout':go.Layout(title='State Total Count',plot_bgcolor='orange')
                }
    if type=='Recovered':
        return {'data':[go.Bar(x=patients['State'],y=patients['Recovered'])],
                'layout':go.Layout(title='State Total Count',plot_bgcolor='orange')
                }
    if type=='Deceased':
        return {'data':[go.Bar(x=patients['State'],y=patients['Deceased'])],
                'layout':go.Layout(title='State Total Count',plot_bgcolor='orange')
                }


@app.callback(Output('graph','figure'),[Input('plot-graph','value')])
def generate_graph(type):

    if type=='All':
        return {'data':[go.Line(x=patients['Status'], y=patients['Total'])],
                'layout':go.Layout(title='Commodities Total Count', plot_bgcolor='pink')}


    if type=='Mask':
        return {'data':[go.Line(x=patients['Status'], y=patients['Mask'])],
                'layout':go.Layout(title='Commodities Total Count', plot_bgcolor='pink')}


    if type=='Sanitizer':
        return {'data':[go.Line(x=patients['Status'], y=patients['Sanitizer'])],
                'layout':go.Layout(title='Commodities Total Count', plot_bgcolor='pink')}


    if type=='Oxygen':
        return {'data':[go.Line(x=patients['Status'], y=patients['Oxygen'])],
                'layout':go.Layout(title='Commodities Total Count', plot_bgcolor='pink')}



@app.callback(Output('the_graph','figure'),[Input('my_dropdown','value')])
def generate_graph(my_dropdown):
    piechart = px.pie(data_frame = patients,names=my_dropdown,hole=0.3)
    return (piechart)



if __name__=='__main__':
     app.run_server(debug=True)