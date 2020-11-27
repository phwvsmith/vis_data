# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import streamlit as st
import datetime
import plotly.graph_objs as go
import pandas as pd
from geopy.geocoders import Nominatim
import json
import numpy as np
from geopy.extra.rate_limiter import RateLimiter
# from datetime import datetime



st.set_page_config(
        page_title="COVID-19 & NHS Wales - visualisation application",
        layout='wide')

st.write('---\n')
st.title('COVID-19 & NHS Wales - visualisation application')

st.write('---\n')
st.header('Bed use by non-covid patients (7 day average)')

#
#
#
##beds
#df_beds_genandacute_noncovid = pd.read_csv('beds_healthboard_genandacute_non-covid.csv', index_col='Date')
#df_ventbeds_noncovid = pd.read_csv('ventbeds_healthboard_non-covid.csv', index_col='Date')
#
#def clean_combine_dfs(df):
#    cols = df.columns
#    df.reset_index(inplace=True)
#    list_dfs = []
#    for col in cols:
#        df_tmp = df[['Date', col]].copy()
#        df_tmp.loc[:, f'{col}_name'] = col
#        df_tmp = df_tmp.rename(columns={col: 'beds', f'{col}_name': 'Health Board'})
#        list_dfs.append(df_tmp)
#    df = pd.concat(list_dfs)
#    return df
#
#dict_dfs = {'beds_genandacute_noncovid':df_beds_genandacute_noncovid,
#            'ventbeds_noncovid':df_ventbeds_noncovid}
#
#
#for key, value in dict_dfs.items(): 
#    dict_dfs[key] = clean_combine_dfs(value)
#
#
#df_beds_genandacute_noncovid = dict_dfs['beds_genandacute_noncovid']
#df_ventbeds_noncovid = dict_dfs['ventbeds_noncovid']
#
#
#df_beds_genandacute_noncovid = df_beds_genandacute_noncovid.rename(columns={'beds':'beds_genandacute_noncovid'})
#df_ventbeds_noncovid = df_ventbeds_noncovid.rename(columns={'beds':'ventbeds_noncovid'})
#
#
#df_beds = pd.concat([df_beds_genandacute_noncovid,
#                     df_ventbeds_noncovid], axis=1)
#
#df_beds = df_beds[['beds_genandacute_noncovid','ventbeds_noncovid']]
#
#
#df_beds['Health Board'] = df_beds_genandacute_noncovid['Health Board']
#df_beds['Date'] = df_beds_genandacute_noncovid['Date'] 
#df_beds['Health Board'] = [i.rstrip() for i in df_beds['Health Board']]
#
#
#def get_location_info(df):
#    locator = Nominatim(user_agent='myGeocoder')
#    df = df.reset_index(drop=True)
#    df['Local Health Board'] = df['Health Board']
#    df = df.rename(columns={'Health Board':'address'})
#
#    df = df.replace({'address': {'Betsi Cadwaladr University Local Health Board': 'Bangor LL57 2PW, Wales',
#                                          'Powys Teaching Local Health Board': 'Powys LD3 0LU, Wales',
#                                          'Hywel Dda University Local Health Board': 'Carmarthen SA31 3BB, Wales',
#                                          'Aneurin Bevan University Local Health Board': 'Lodge Road, Caerleon, Newport NP18 3XQ, Wales',
#                                          'Cardiff and Vale University Local Health Board':'Heath Park, Cardiff CF14 4XW, Wales',
#                                          'Cwm Taf Morgannwg University Local Health Board': 'Abercynon, Rhondda Cynon Taff CF45 4SN, Wales',
#                                          'Swansea Bay University Local Health Board':'Baglan Energy Park, Baglan, Port Talbot SA12 7BR, Wales',
#                                          'Velindre University NHS Trust':'Parc, Nantgarw, Cardiff CF15 7QZ'}})
#
#
#    addresses = df['address'].unique()
#
#    dict_points = {}
#    # 1 - conveneint function to delay between geocoding calls
#    geocode = RateLimiter(locator.geocode, min_delay_seconds=1)
#
#    for i in addresses:
#        dict_points[i] = geocode(i)
#    
#    
#    list_coordinates = []
#    for i in addresses:
#        coordinate = list(dict_points[i][1])
#        list_coordinates.append(coordinate)
#    dict_coordintates = {}
#    for i,j in zip(addresses,list_coordinates):
#        dict_coordintates[i] = j
#
#    df['coordinates'] = [dict_coordintates[i] for i in df['address']]
#    df['lat'] = [i[0] for i in df['coordinates']]
#    df['lon'] = [i[1] for i in df['coordinates']]
#    
#    return df
#
#df_beds = get_location_info(df_beds)
#
#
#
#
###***Nominatim stopped working so hacking a solution using past dataframe
#
#
#
#    df_beds = df_beds.reset_index(drop=True)
#    df_beds['Local Health Board'] = df_beds['Health Board']
#    df_beds = df_beds.rename(columns={'Health Board':'address'})
#
#    df_beds = df_beds.replace({'address': {'Betsi Cadwaladr University Local Health Board': 'Bangor LL57 2PW, Wales',
#                                          'Powys Teaching Local Health Board': 'Powys LD3 0LU, Wales',
#                                          'Hywel Dda University Local Health Board': 'Carmarthen SA31 3BB, Wales',
#                                          'Aneurin Bevan University Local Health Board': 'Lodge Road, Caerleon, Newport NP18 3XQ, Wales',
#                                          'Cardiff and Vale University Local Health Board':'Heath Park, Cardiff CF14 4XW, Wales',
#                                          'Cwm Taf Morgannwg University Local Health Board': 'Abercynon, Rhondda Cynon Taff CF45 4SN, Wales',
#                                          'Swansea Bay University Local Health Board':'Baglan Energy Park, Baglan, Port Talbot SA12 7BR, Wales',
#                                          'Velindre University NHS Trust':'Parc, Nantgarw, Cardiff CF15 7QZ'}})
#
#
#    addresses = df_beds['address'].unique()
#
#
#
#
#    for i in addresses:
#        dict_points[i] = [dfTEMP['coordinates'][dfTEMP['address']==i].iloc[0], dfTEMP['lat'][dfTEMP['address']==i].iloc[0], dfTEMP['lon'][dfTEMP['address']==i].iloc[0]]
#
#
#    df['coordinates'] = [dict_points[i][0] for i in addresses]
#
#    df_beds['coordinates'] = [dict_points[i][0] for i in df_beds['address']]
#    df_beds['lat'] = [dict_points[i][1] for i in df_beds['address']]
#    df_beds['lon'] = [dict_points[i][2] for i in df_beds['address']]
#
#
#
#
#
#
#
#
#
#
#dfTEMP=pd.read_csv('override.csv', index_col= 'Unnamed: 0')



#df_beds.to_csv('override.csv')
df_beds=pd.read_csv('override.csv', index_col= 'Unnamed: 0')


#Get population info for health boards and clean up the dataframe
population_health_boards = pd.read_csv('popln_health_boards.csv')
population_health_boards = population_health_boards[['Unnamed: 1','All ages .1']]
population_health_boards = population_health_boards.drop(labels=[0, 1, 2], axis=0)
population_health_boards = population_health_boards.rename(columns={'Unnamed: 1':'Health Board','All ages .1':'population'})
population_health_boards['Health Board'] = [i.rstrip() for i in population_health_boards['Health Board']]

#population_health_boards doesn't local in column name so reassign names to match df_beds
population_health_boards['Health Board'] = [i for i in df_beds['Local Health Board'].unique() if i != 'Velindre University NHS Trust']

#create popln dictionary
dict_population = {}
for i in population_health_boards['Health Board']: 
    dict_population[i] = population_health_boards['population'][population_health_boards['Health Board'] == i].iloc[0]

# df_beds['population'] = [df_beds['Local Health Board']]

#change popln to int in prep for operations
for i in dict_population: 
    dict_population[i] = int(dict_population[i]) 

#check this should be 3,152,879
total_population = sum(dict_population.values())


#add popln column to df_beds
df_beds['population'] = df_beds['Local Health Board'].map(dict_population) 

#fill in popln for Velindre sames as Cardiff and Vale University Local Health Board (as same health board region)
Velindre_population = df_beds[df_beds.loc[:,'Local Health Board'] == 'Cardiff and Vale University Local Health Board']['population'].iloc[0]
df_beds.loc[df_beds['Local Health Board'] == 'Velindre University NHS Trust', 'population'] = Velindre_population


#Get ventbeds_noncovid beds_genandacute_noncovid per 100k columns
df_beds['ventbeds_noncovid_per_100000'] = df_beds['ventbeds_noncovid'] / df_beds['population'] *100000
df_beds['beds_genandacute_noncovid_per_100000'] = df_beds['beds_genandacute_noncovid'] / df_beds['population'] *100000

#change date column to datetime then sort dataframe by date order and change nack to string
df_beds['Date'] = pd.to_datetime(df_beds['Date'], dayfirst=True)
df_beds = df_beds.sort_values('Date', ascending=True)
df_beds['Date'] = df_beds['Date'].dt.strftime('%d/%m/%Y')

#remove Local from the column to make the id geojson match work
df_beds['Local Health Board'] = [x.strip().replace("Local ", "") for x in df_beds['Local Health Board']] 

#Make a copy of dataframe make a copy of 'Local Health Board' called location
#then change 'Date', 'Local Health Board' to multi index and take out any nans (shouldn't be there anymore)
# df_beds = df_beds.copy()
df_beds['location'] = df_beds['Local Health Board']

df_beds = df_beds.set_index(['Date', 'Local Health Board'])
df_beds = df_beds.replace(np.nan, 0)


#upload geojson
wales_health_boards = json.load(open('Local_Health_Boards__April_2019__Boundaries_WA_BFE.geojson'))

#see if loaded ok
#wales_health_boards['features'][0]['properties']

#get id (?)

hb_id_map = {}
for feature in wales_health_boards['features']:
    feature['id'] = feature['properties']['lhb19cd']
    hb_id_map[feature['properties']['lhb19nm']] = feature['id'] 

#remove 'Velindre University NHS Trust' for the chloropleth vis
df_chloro = df_beds.loc[df_beds['location'] != 'Velindre University NHS Trust'].copy()



#match up ids into new id column
df_chloro['id'] = df_chloro['location'].apply(lambda x:hb_id_map[x])


#get date back in as a column and convert it to datetime
df_chloro.reset_index(inplace=True)
df_chloro['Date'] = pd.to_datetime(df_chloro['Date'], dayfirst=True)



df_genandacute_noncovid = df_chloro[['Date', 'beds_genandacute_noncovid']].copy()

df_genandacute_noncovid.Date = pd.to_datetime(df_genandacute_noncovid.Date, dayfirst=True)

df_genandacute_noncovid =df_genandacute_noncovid.groupby(['Date']).sum().reset_index()

df_genandacute_noncovid['7 day average'] = df_genandacute_noncovid.rolling(window=7, on=df_genandacute_noncovid.index).mean()

st.write('   \n')
st.write('**General and acute beds**')
traces=[go.Scatter(
    x = df_genandacute_noncovid['Date'],
    y = df_genandacute_noncovid['7 day average'].round(0),
    line = dict(shape = 'linear', color = '#31446B', width= 4),
    hovertemplate = "<extra></extra><br>Date: %{x}<br>Non-covid patients: %{y}"
    
)]

layout = go.Layout(
#    title = 'General and acute beds',
#    font=dict(family='sans-serif'),
    xaxis_title="Date",
    yaxis_title="Patients",
    plot_bgcolor='rgba(0,0,0,0)',
    hoverdistance=1000, # Distance to show hover label of data point
    spikedistance=1000, # Distance to show spike
    margin={"r":0,"t":0,"l":0,"b":0},
    xaxis=dict(
        linecolor="#BCCCDC",
        showspikes=True, # Show spike line for X-axis
        # Format spike
        spikethickness=2,
        spikedash="dot",
        spikecolor="#999999",
        spikemode="across",
    ),
)

fig = go.Figure(data=traces,layout=layout)

fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
#fig.show()
fig.update_layout(width=775, height=355)
st.plotly_chart(fig)

df_ventbeds_noncovid = df_chloro[['Date', 'ventbeds_noncovid']].copy()
df_ventbeds_noncovid.Date = pd.to_datetime(df_ventbeds_noncovid.Date, dayfirst=True)
df_ventbeds_noncovid =df_ventbeds_noncovid.groupby(['Date']).sum().reset_index()
df_ventbeds_noncovid['7 day average'] = df_ventbeds_noncovid.rolling(window=7, on=df_ventbeds_noncovid.index).mean()

st.write('   \n')
st.write('**Ventilator beds**')
traces=[go.Scatter(
    x = df_ventbeds_noncovid['Date'],
    y = df_ventbeds_noncovid['7 day average'].round(0),
    line = dict(shape = 'linear', color = '#31446B', width= 4),
    hovertemplate = "<extra></extra><br>Date: %{x}<br>Non-covid patients: %{y}"


    
)]

layout = go.Layout(
#    title = 'Ventilator beds',
#     barmode = 'stack'
    xaxis_title="Date",
    yaxis_title="Patients",
    hoverdistance=1000, # Distance to show hover label of data point
    spikedistance=1000, # Distance to show spike
    margin={"r":0,"t":0,"l":0,"b":0},
    xaxis=dict(
        linecolor="#BCCCDC",
        showspikes=True, # Show spike line for X-axis
        # Format spike
        spikethickness=2,
        spikedash="dot",
        spikecolor="#999999",
        spikemode="across",
    ),
    plot_bgcolor='rgba(0,0,0,0)'
)

fig = go.Figure(data=traces,layout=layout)

fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
#fig.show()
fig.update_layout(width=775, height=355)
st.plotly_chart(fig)


st.write('---\n')
st.header('Daily bed use by non-covid patients for each Local Health Board')

st.subheader('General and acute beds occupied per 100k people')

# cade from https://community.plotly.com/t/animated-choroplethmapbox/37723/2
def numpy_dt64_to_str(dt64):
    day_timestamp_dt = (dt64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')
    day_dt = dt.datetime.utcfromtimestamp(day_timestamp_dt)
    return day_dt.strftime("%b %Y")

plot_var = 'beds_genandacute_noncovid_per_100000'



#not sure why  they do the date slice so will ignore
# wales_df = df_chloro[(df_chloro.Date > datetime(2020, 11, 10))]
#df_chloro = df_chloro.round({'beds_genandacute_noncovid_per_100000':0,'ventbeds_noncovid_per_100000':0})
#df_chloro = pd.read_csv('data_annimation_short.csv')

df_chloro1 = df_chloro.copy()

df_chloro1['YearMonth'] = pd.to_datetime(df_chloro1['Date']).apply(lambda x: '{year}-{month}'.format(year=x.year, month=x.month))

df_chloro1 = df_chloro1.groupby(['YearMonth', 'location', 'id'])['beds_genandacute_noncovid_per_100000'].mean()
df_chloro1= df_chloro1.round(0)
df_chloro1 = df_chloro1.reset_index()
df_chloro1.rename(columns={'YearMonth': 'Date'})
df_chloro1.columns = ['Date', 'location', 'id', 'beds_genandacute_noncovid_per_100000']
df_chloro1['Date'] = pd.to_datetime(df_chloro1['Date'])



days1 = np.sort(df_chloro1.Date.unique())

plot_df1 = df_chloro1[df_chloro1.Date == days1[-1]]

plot_df1 = plot_df1.sort_values(by=['Date', 'location'])
df_chloro1 = df_chloro1.sort_values(by=['Date', 'location'])

fig_data1 =go.Choroplethmapbox(name = 'General and acute beds occupied by non-covid patients per 100k people',
                              geojson=wales_health_boards, locations=plot_df1.id, 
                              z=plot_df1[plot_var],
                              zmin=0.0,
                              zmax=df_chloro1[plot_var].max(),
                              customdata = np.stack((pd.Series(plot_df1['location']), 
                                                     plot_df1['beds_genandacute_noncovid_per_100000'].round(4)), 
                                                    axis=-1),
                              hovertemplate = "<extra></extra><em>%{customdata[0]}  </em><br>beds_genandacute_noncovid_per_100000:  %{customdata[1]}",
#                               colorbar={'title':'hospitalisations per 1000 people', 'titleside':'top', 'thickness':20},
                              colorscale="cividis",
                              showscale=True,
                              marker_opacity=0.7,
                              marker_line_width=0,
                              colorbar=dict(outlinewidth=1,
                                            outlinecolor="#333333",
                                            len=0.9,
                                            lenmode="fraction",
#                                             xpad=30,
#                                             xanchor="right",
                                            bgcolor=None,
#                                            title=dict(text="general and acute noncovid per 100k",
#                                                       font=dict(size=14)),
                                            tickvals=[0,50,100,150,200,250,300],
                                            ticktext=["0", "50", "100", "150", "200", "250", "300"],
                                            tickcolor="#333333",
                                            tickwidth=2,
                                            tickfont=dict(color="#333333",
                                                          size=12)),
                              )



token = open(r'mapbox_token.txt', 'r').read()
fig_layout1 = go.Layout(mapbox_style="light",
                       mapbox_zoom=5.5,
                       mapbox_accesstoken=token,
                       mapbox_center={"lat": 52.461159, "lon": -3.622836},
                       margin={"r":0,"t":0,"l":0,"b":0},
                       plot_bgcolor=None)

fig_layout1["updatemenus"] = [dict(type="buttons",
                                  buttons=[dict(label="Play",
                                                method="animate",
                                                args=[None,
                                                      dict(frame=dict(duration=600,
                                                                      redraw=True),
                                                           fromcurrent=True,
                                                           transition=dict(duration=1,))]),
#                                                                            easing="quadratic-in-out"))]),
                                           dict(label="Pause",
                                                method="animate",
                                                args=[[None],
                                                      dict(frame=dict(duration=0,
                                                                      redraw=True),
                                                           mode="immediate",
                                                           transition=dict(duration=0)
                                                          )])],
                                  direction="left",
                                  pad={"r": 10, "t": 35},
                                  showactive=True,
                                  x=0.1,
                                  xanchor="right",
                                  y=0,
                                  yanchor="top")]

sliders_dict1 = dict(active=len(days1) - 1,
                    visible=True,
                    yanchor="top",
                    xanchor="left",
                    currentvalue=dict(font=dict(size=20),
                                      prefix="Date: ",
                                      visible=True,
                                      xanchor="right"),
                    pad=dict(b=10,
                             t=10),
                    len=0.875,
                    x=0.125,
                    y=0,
                    steps=[])

import datetime as dt
fig_frames1 = []
for day in days1:
    plot_df1 = df_chloro1[df_chloro1.Date == day]
    frame = go.Frame(data=[go.Choroplethmapbox(locations=plot_df1.id,
                                               z=plot_df1[plot_var],

                                               name="",
                                               customdata = np.stack((pd.Series(plot_df1['location']), 
                                                     plot_df1['beds_genandacute_noncovid_per_100000'].round(4)), 
                                                    axis=-1),
                                               hovertemplate = "<extra></extra><em>%{customdata[0]}  </em><br>beds_genandacute_noncovid_per_100000:  %{customdata[1]}"
                                              )],
                     name=numpy_dt64_to_str(day))
    fig_frames1.append(frame)

    slider_step = dict(args=[[numpy_dt64_to_str(day)],
                             dict(mode="immediate",
                                  frame=dict(duration=600,
                                             redraw=True),
                                  transition=dict(duration=1,
                                                 ))
                            ],
                       method="animate",
                       label=numpy_dt64_to_str(day))
    sliders_dict1["steps"].append(slider_step)

fig_layout1.update(sliders=[sliders_dict1])

# Plot the figure 
fig1=go.Figure(data=fig_data1, layout=fig_layout1, frames=fig_frames1)
fig1.update_layout(width=700, height=400)
#fig.show()
st.plotly_chart(fig1)




df_chloro2 = df_chloro.copy()

df_chloro2['YearMonth'] = pd.to_datetime(df_chloro2['Date']).apply(lambda x: '{year}-{month}'.format(year=x.year, month=x.month))

df_chloro2 = df_chloro2.groupby(['YearMonth', 'location', 'id'])['ventbeds_noncovid_per_100000'].mean()
df_chloro2= df_chloro2.round(0)
df_chloro2 = df_chloro2.reset_index()
df_chloro2.rename(columns={'YearMonth': 'Date'})
df_chloro2.columns = ['Date', 'location', 'id', 'ventbeds_noncovid_per_100000']
df_chloro2['Date'] = pd.to_datetime(df_chloro2['Date'])



days2 = np.sort(df_chloro2.Date.unique())

plot_df2 = df_chloro2[df_chloro2.Date == days2[-1]]

plot_df2 = plot_df2.sort_values(by=['Date', 'location'])
df_chloro2 = df_chloro2.sort_values(by=['Date', 'location'])


st.subheader('Ventilator beds occupied per 100k people')
plot_var = 'ventbeds_noncovid_per_100000'

fig_data2 =go.Choroplethmapbox(geojson=wales_health_boards, locations=plot_df2.id, 
                              z=plot_df2[plot_var],
                              zmin=0.0,
                              zmax=df_chloro2[plot_var].max(),
                              name="",
                              customdata = np.stack((pd.Series(plot_df2['location']), 
                                                     plot_df2['ventbeds_noncovid_per_100000'].round(4)), 
                                                    axis=-1),
                              hovertemplate = "<extra></extra><em>%{customdata[0]}  </em><br>ventbeds_noncovid_per_100000:  %{customdata[1]}",
#                               colorbar={'title':'hospitalisations per 1000 people', 'titleside':'top', 'thickness':20},
                              colorscale="cividis",
                              showscale=True,
                              marker_opacity=0.7,
                              marker_line_width=0,
                              colorbar=dict(outlinewidth=1,
                                            outlinecolor="#333333",
                                            len=0.9,
                                            lenmode="fraction",
#                                             xpad=30,
#                                             xanchor="right",
                                            bgcolor=None,
#                                            title=dict(text="ventilator noncovid per 100k",
#                                                       font=dict(size=14)),
                                            tickvals=[0,2,4,6,8,10],
                                            ticktext=["0", "2", "4", "6", "8", "10"],
                                            tickcolor="#333333",
                                            tickwidth=2,
                                            tickfont=dict(color="#333333",
                                                          size=12)),
                              )

fig_layout2 = go.Layout(mapbox_style="light",
                       mapbox_zoom=5.5,
                       mapbox_accesstoken=token,  
                       mapbox_center={"lat": 52.461159, "lon": -3.622836},
                       margin={"r":0,"t":0,"l":0,"b":0},
                       plot_bgcolor=None)

fig_layout2["updatemenus"] = [dict(type="buttons",
                                  buttons=[dict(label="Play",
                                                method="animate",
                                                args=[None,
                                                      dict(frame=dict(duration=600,
                                                                      redraw=True),
                                                           fromcurrent=True,
                                                           transition=dict(duration=1,))]),
#                                                                            easing="quadratic-in-out"))]),
                                           dict(label="Pause",
                                                method="animate",
                                                args=[[None],
                                                      dict(frame=dict(duration=0,
                                                                      redraw=True),
                                                           mode="immediate",
                                                           transition=dict(duration=0)
                                                          )])],
                                  direction="left",
                                  pad={"r": 10, "t": 35},
                                  showactive=True,
                                  x=0.1,
                                  xanchor="right",
                                  y=0,
                                  yanchor="top")]

sliders_dict2 = dict(active=len(days2) - 1,
                    visible=True,
                    yanchor="top",
                    xanchor="left",
                    currentvalue=dict(font=dict(size=20),
                                      prefix="Date: ",
                                      visible=True,
                                      xanchor="right"),
                    pad=dict(b=10,
                             t=10),
                    len=0.875,
                    x=0.125,
                    y=0,
                    steps=[])

import datetime as dt
fig_frames2 = []
for day in days2:
    plot_df2 = df_chloro2[df_chloro2.Date == day]
    frame = go.Frame(data=[go.Choroplethmapbox(locations=plot_df2.id,
                                               z=plot_df2[plot_var],
                                               name="",

                                               customdata = np.stack((pd.Series(plot_df2['location']), 
                                                     plot_df2['ventbeds_noncovid_per_100000'].round(4)), 
                                                    axis=-1),
                                               hovertemplate = "<extra></extra><em>%{customdata[0]}  </em><br>ventbeds_noncovid_per_100000:  %{customdata[1]}"
                                              )],
                     name=numpy_dt64_to_str(day))
    fig_frames2.append(frame)

    slider_step = dict(args=[[numpy_dt64_to_str(day)],
                             dict(mode="immediate",
                                  frame=dict(duration=600,
                                             redraw=True),
                                  transition=dict(duration=1,
                                                 ))
                            ],
                       method="animate",
                       label=numpy_dt64_to_str(day))
    sliders_dict2["steps"].append(slider_step)

fig_layout2.update(sliders=[sliders_dict2])

# Plot the figure 
fig=go.Figure(data=fig_data2, layout=fig_layout2, frames=fig_frames2)
#fig.show()
fig.update_layout(width=700, height=400)
st.plotly_chart(fig)


st.write('---\n')
st.header('Mean daily bed use by non-covid patients for each Local Health Board')

st.write('   \n')
st.write('**General and acute beds**')

glglggl =df_chloro.groupby(df_chloro['Local Health Board']).mean()

glglggl = glglggl.sort_values('beds_genandacute_noncovid_per_100000')
traces=[go.Bar(
    y = glglggl.index,
    x = glglggl['beds_genandacute_noncovid_per_100000'].round(1),
    orientation='h',
    marker=dict(
        color='#666870',
        line=dict(color='#00204C', width=4)),


    
)]

layout = go.Layout(
#    title = 'General and acute beds',
#     barmode = 'stack'
    yaxis_title="Health Board",
    xaxis_title="Patients",
    plot_bgcolor='rgba(0,0,0,0)',
    margin={"r":0,"t":0,"l":50,"b":0},
)

fig = go.Figure(data=traces,layout=layout)
# pyo.plot(fig, filename='line3.html')
fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
#fig.show()
fig.update_layout(width=775, height=355)
st.plotly_chart(fig)

st.write('   \n')
st.write('**Ventilator beds**')
glglggl = glglggl.sort_values('ventbeds_noncovid_per_100000')
traces=[go.Bar(
    y = glglggl.index,
    x = glglggl['ventbeds_noncovid_per_100000'].round(1),
    orientation='h',
    marker=dict(
        color='#666870',
        line=dict(color='#00204C', width=4)),


    
)]

layout = go.Layout(
#    title = 'Ventilator beds',
#     barmode = 'stack'
    yaxis_title="Health Board",
    xaxis_title="Patients",
    plot_bgcolor='rgba(0,0,0,0)',
    margin={"r":0,"t":0,"l":0,"b":0},
)

fig = go.Figure(data=traces,layout=layout)
# pyo.plot(fig, filename='line3.html')
fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
#fig.show()
fig.update_layout(width=775, height=355)
st.plotly_chart(fig)




st.write('---\n')


st.header('Health Boards by high risk individuals')

st.subheader('Health Boards with highest proportion of black, asian and minority ethnic groups (PHW 2015):')
st.write('   \n')
st.write('1.Cardiff and Vale Health Board')
st.write('2.Swansea Bay Health Board')
st.write('3.Aneurin Bevan University Health Board')

#st.subheader('Daily bed use by non-covid patients for Swansea Bay, Cardiff and Vale and Aneurin Bevan University Health Boards')


df = df_chloro[['Date', 'Local Health Board','ventbeds_noncovid_per_100000','beds_genandacute_noncovid_per_100000']].copy()

df['Local Health Board'] = [x.strip().replace("Local ", "") for x in df['Local Health Board']] 

df['Local Health Board'].unique()

dict_color = {'Swansea Bay University Health Board': '#FFE945',
              'Cardiff and Vale University Health Board':'#31446B',
              'Aneurin Bevan University Health Board':'#CAB969'}

st.write('   \n')
st.write('**General and acute beds occupied by non-covid patients per 100k people**')
# Build graph
layout = go.Layout(
#    title='General and acute beds occupied by non-covid patients per 100k people',
    plot_bgcolor="#FFFFFF",
    margin={"r":0,"t":0,"l":0,"b":0},
    legend=dict(
        # Adjust click behavior
        itemclick="toggleothers",
        itemdoubleclick="toggle",
    ),
    xaxis=dict(
        title="Date",
        linecolor="#BCCCDC",
        showspikes=True, # Show spike line for X-axis
        # Format spike
        spikethickness=2,
        spikedash="dot",
        spikecolor="#999999",
        spikemode="across",
    ),
    yaxis=dict(
        title="Non-covid patients",
        linecolor="#BCCCDC"
    )
)

data = []

for i in ['Aneurin Bevan University Health Board',
          'Swansea Bay University Health Board', 
          'Cardiff and Vale University Health Board']:
    Date = df.loc[df['Local Health Board'] == i, "Date"]
    ventbeds_noncovid_per_100000 = df.loc[df['Local Health Board'] == i, "beds_genandacute_noncovid_per_100000"]
    line_chart = go.Scatter(
        x=Date,
        y=ventbeds_noncovid_per_100000,
        name=i,
        line = dict(shape = 'linear', color = dict_color[i], width= 3),
        
    )
    data.append(line_chart)

fig = go.Figure(data=data, layout=layout)
fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
#fig.show(config={"displayModeBar": False, "showTips": False}) # Remove floating menu and unnecesary dialog box
fig.update_layout(width=975, height=355)
st.plotly_chart(fig, displayModeBar=False, showTips='False')

st.write('   \n')
st.write('**Ventilator beds occupied by non-covid patients per 100k people**')
layout = go.Layout(
#    title='Ventilator beds occupied by non-covid patients per 100k people',
    plot_bgcolor="#FFFFFF",
    margin={"r":0,"t":0,"l":0,"b":0},
    legend=dict(
        # Adjust click behavior
        itemclick="toggleothers",
        itemdoubleclick="toggle",
    ),
    xaxis=dict(
        title="Date",
        linecolor="#BCCCDC",
        showspikes=True, # Show spike line for X-axis
        # Format spike
        spikethickness=2,
        spikedash="dot",
        spikecolor="#999999",
        spikemode="across",
    ),
    yaxis=dict(
        title="Non-covid patients",
        linecolor="#BCCCDC"
    )
)

data = []

for i in ['Aneurin Bevan University Health Board',
          'Swansea Bay University Health Board', 
          'Cardiff and Vale University Health Board']:
    Date = df.loc[df['Local Health Board'] == i, "Date"]
    ventbeds_noncovid_per_100000 = df.loc[df['Local Health Board'] == i, 'ventbeds_noncovid_per_100000']
    line_chart = go.Scatter(
        x=Date,
        y=ventbeds_noncovid_per_100000,
        name=i,
        line = dict(shape = 'linear', color = dict_color[i], width= 3),
        
    )
    data.append(line_chart)

fig = go.Figure(data=data, layout=layout)
fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
#fig.show(config={"displayModeBar": False, "showTips": False}) # Remove floating menu and unnecesary dialog box
fig.update_layout(width=975, height=355)
st.plotly_chart(fig, displayModeBar=False, showTips='False')



st.subheader('Health Boards ranked by proportion of most deprived areas (gov.wales 2020):')
st.write('1.Aneurin Bevan University Health Board')
st.write('2.Cwm Taf Morgannwg University Health Board')
st.write('3.Cardiff and Vale University Health Board')
st.write('4.Swansea Bay University Health Board')
st.write('5.Betsi Cadwaladr University Health Board')
st.write('6.Hywel Dda University Health Board')
st.write('7.Powys Teaching Health Board')


df_vis = pd.read_csv('master_geos_wales.csv')

df_quint = df_vis[df_vis.wimd_2019 < 383]

df_count_lower=df_quint.groupby(df_quint['Health Board']).count()

df_count_total=df_vis.groupby(df_vis['Health Board']).count()

df_count_total['Percentage most deprived'] = df_count_lower['id']/df_count_total['id']*100

df_count_total = df_count_total.sort_values('Percentage most deprived')

#st.write('   \n')
#st.write('**Health Boards by percentage of Lower Layer Super Output Areas ranked as \"most deprived\" by Welsh Index of Multiple Deprivation**')
traces=[go.Bar(
    y = df_count_total.index,
    x = df_count_total['Percentage most deprived'].round(1),
    orientation='h',
    marker=dict(
        color='#666870',
        line=dict(color='#00204C', width=4)),
   
)]

layout = go.Layout(
#    title = 'Health Boards by percentage of LLSOAs ranked as \"most deprived\" by Welsh Index of Multiple Deprivation',
#     barmode = 'stack'
    yaxis_title="Health Board",
    xaxis_title="Percentage most deprived",
    plot_bgcolor='rgba(0,0,0,0)',
    margin={"r":0,"t":0,"l":50,"b":0}
)

fig = go.Figure(data=traces,layout=layout)
# pyo.plot(fig, filename='line3.html')
fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
#fig.show()
fig.update_layout(width=775, height=355)
#st.plotly_chart(fig)




df_age = pd.read_csv('age.csv')

df_age = df_age.sort_values('Aged 85 and over per 100k')
traces=[go.Bar(
    y = df_age['Health Board'],
    x = df_age['Aged 85 and over per 100k'].round(0),
    orientation='h',
    marker=dict(
        color='#666870',
        line=dict(color='#00204C', width=4)),

#     hovertemplate = "<br>Health Board: %{y}<br>Non-covid patients: %{x}"

    #plotly.colors.sequential.Viridis
#     mode = "lines",
#     line = list(color = "green")
#     marker = {'line':{'color': 'black'}} ##31446B
    
#     marker=dict(color=[0, 10000000, 2, 3,0, 10000000, 2, 3])
    
)]

layout = go.Layout(
    title = 'Health Board by number of individuals aged 85 and over per 100k',
#     barmode = 'stack'
    yaxis_title="Health Board",
    xaxis_title="Aged 85 and over per 100k people",
    plot_bgcolor='rgba(0,0,0,0)',
    margin={"r":0,"t":0,"l":0,"b":0}
)

fig = go.Figure(data=traces,layout=layout)
# pyo.plot(fig, filename='line3.html')
fig.update_xaxes(showline=True, linewidth=2, linecolor='black')
fig.update_yaxes(showline=True, linewidth=2, linecolor='black')
fig.update_layout(width=575, height=355)
#st.plotly_chart(fig)


#
#
#fig = px.scatter_mapbox(df_vis, lat="long", lon="lat", hover_data=["wimd_2019"],
#                        color="wimd_2019",
#                        color_continuous_scale= px.colors.sequential.Cividis,
##                         colorscale="cividis",
##                         size="wimd_2019",
#                        zoom=7, height=900)
#fig.update_layout(mapbox_style="light", mapbox_accesstoken='*****')
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
##fig.show()
#fig.update_layout(width=1800, height=800)
#st.plotly_chart(fig)
#
#
#
#df_useful = pd.read_csv('
#
#df_useful['UA19CD'].unique()
#
#dict_link ={}
#for i in df_useful['UA19CD'].unique():
#    dict_link[i] = df_useful['Health Board'][df_useful['UA19CD']==i].iloc[0]
#
#
#areas = df_vis['ladnm'].unique()
#
#df_vis.to_csv('master_geos_wales.csv')
#
#df_vis['Health Board'] = [dict_link[i] for i in df_vis['ladcd']]
