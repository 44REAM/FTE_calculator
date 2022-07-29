
import json

import pandas as pd
from django.shortcuts import render
import dash
from dash import dcc, html
from django_plotly_dash import DjangoDash
import plotly.express as px

from .forms import WorkLoadForm
from .constants import WorkMultiplier, WorkTime, province_df, calculate_workload
from .models import WorkLoad
# Create your views here.


app = DjangoDash('SimpleExample')   # replaces dash.Dash
with open("data/geo.json", "r") as read_file:
    geojson = json.load(read_file)

def get_province_df():
    data = province_df.copy()
    df = pd.DataFrame(list(WorkLoad.objects.all().values())).groupby(['province'], as_index=False).sum()

    data = data.merge(df, how = 'left')
    data.fillna(0.0, inplace=True)

    _, _, human = calculate_workload(data)
    data['workload'] = human
    return data

def dashboard(request):
    df = get_province_df()
  
    fig = px.choropleth(df, geojson=geojson, color="workload",
                        locations="province",featureidkey="properties.Province",
                        projection="mercator", 
                        color_continuous_scale = 'reds',
                        hover_data={
                            'province': False,
                            'workload': ':.2f',
                            'name':True
                        }
                    )
    #fig.update_traces(hovertemplate='GDP: %{} <br>Life Expectancy: %{name}')
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
        margin = {"t":0,"b":0,"l":0,"r":0},
        autosize = True,
        coloraxis  = {
            'cmin':0, 
            'cmax':8,
            'colorbar': {
                'thickness' : 15,
                'len': 0.2,
                'y': 0.8
            }
            }
    )

    app.layout = html.Div(children=[

        dcc.Graph(
            id='example-graph',
            figure=fig,
            style={'width': '95vw', 'height': '95vh'},
            config={'displayModeBar': False},
            
        )
    ])
    context = {}
    return render(request, 'dashboard.html', context)

def home(request):
    form = WorkLoadForm()

    if request.method == 'POST':
        form=WorkLoadForm(request.POST)
        if form.is_valid():

            try:
                form.save()
            except:
                pass
            minute_per_day, minute_per_year, human = calculate_workload(form.cleaned_data)


            context = {
                'minute_per_day': round(minute_per_day,2),
                'minute_per_year': round(minute_per_year,2), 
                'human':round(human,2),
                'data':form.cleaned_data,
                'WorkMultiplier':WorkMultiplier,
                'WorkTime':WorkTime
                }
            return render(request, 'result.html', context)


    context = {'form':form}
    return render(request, 'home.html', context)
