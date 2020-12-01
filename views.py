from django.shortcuts import render
import numpy as np
import pandas as pd
from django.http import HttpResponse


# Create your views here.

def home(request):
    world = pd.read_csv('https://raw.githubusercontent.com/arc7creat/covdat/main/covid_19_data.csv',encoding='utf-8',na_values=None)
    posit =world.Confirmed.max()
    worlt = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    newposit = worlt[worlt.columns[-1]].sum()
    d1 = worlt[['Country/Region',worlt.columns[-1]]].groupby('Country/Region').sum()
    d1=d1.reset_index()
    d1.columns=['Country/Region','values']
    d1= d1.sort_values(by='values',ascending=False)
    d2 = d1.loc[lambda d1: (d1['Country/Region'] == ('India'))
         |(d1['Country/Region'] == ('US'))
         |(d1['Country/Region'] == ('Brazil'))
         |(d1['Country/Region'] == ('Singapore'))
            ]
    barplotval= d2['values'].values.tolist()
    countryname= d2['Country/Region'].values.tolist()
    showMap = 'True'
    context = {'posit':posit, 'newposit':newposit, 'countryname':countryname, 'barplotval':barplotval, 'showMap':showMap}
    return render(request,'home.html',context)


def usPage(request):
    worlt = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    posit = worlt[['Country/Region',worlt.columns[-1]]].groupby('Country/Region').sum()
    posit=posit.reset_index()
    posit.columns=['Country/Region','values']
    posit= posit.sort_values(by='values',ascending=False)
    iposit = posit.loc[lambda posit: (posit['Country/Region'] == ('US'))]
    iposit = iposit['values'].values.tolist()
    usaco = pd.read_csv('https://raw.githubusercontent.com/arc7creat/covdat/main/us_counties_covid19_daily.csv',encoding='utf-8',na_values=None)
    usaco['date'] = pd.to_datetime(usaco['date'],format = '%Y-%m-%d').dt.strftime("%d/%m/%Y")
    weather_houston = pd.read_csv('https://raw.githubusercontent.com/arc7creat/covdat/main/data_houston_weather.csv',encoding='utf-8',na_values=None)
    contry = usaco[usaco.state == 'Texas']
    stat = contry[contry.county == 'Houston']
    stats = stat.reset_index()
    dtfhouston = weather_houston[['Time', 'Temperature','Humidity (%)','Wind Speed (mph)']]
    dtfhouston= dtfhouston.reset_index()
    cthw = dtfhouston[['Time', 'Temperature','Humidity (%)','Wind Speed (mph)']].copy()
    cthw['cases'] = stats['cases'].copy()
    weather_usdate= weather_houston['Time'].values.tolist()
    weather_ustemp= weather_houston['Temperature'].values.tolist()
    weather_ushum = weather_houston['Humidity (%)'].values.tolist()
    weathr_uswin = weather_houston['Wind Speed (mph)'].values.tolist()
    cthw_case = cthw['cases'].values.tolist()
    context = {'iposit':iposit ,'weather_usdate':weather_usdate,'weather_ustemp':weather_ustemp,'weather_ushum':weather_ushum,'weathr_uswin':weathr_uswin,'cthw_case':cthw_case}
    return render(request,'us.html',context)
        
def indiaPage(request):
    worlt = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    posit = worlt[['Country/Region',worlt.columns[-1]]].groupby('Country/Region').sum()
    posit=posit.reset_index()
    posit.columns=['Country/Region','values']
    posit= posit.sort_values(by='values',ascending=False)
    indposit = posit.loc[lambda posit: (posit['Country/Region'] == ('India'))]
    indposit = indposit['values'].values.tolist()
    indco = pd.read_csv('https://raw.githubusercontent.com/arc7creat/covdat/main/covid_19_india.csv',encoding='utf-8',na_values=None)
    contry = indco[indco.State == 'Delhi']
    stats = contry.reset_index()
    weather_delhi = pd.read_csv('https://raw.githubusercontent.com/arc7creat/covdat/main/data_new-delhi_weather.csv',encoding='utf-8',na_values=None)
    dtfdelhi = weather_delhi[['Time', 'Temperature','Humidity (%)','Wind Speed (mph)']]
    dtfdelhi= dtfdelhi.reset_index()
    cthw = dtfdelhi[['Time', 'Temperature','Humidity (%)','Wind Speed (mph)']].copy()
    cthw['Confirmed'] = stats['Confirmed'].copy()
    weather_inddate= weather_delhi['Time'].values.tolist()
    weather_indtemp= weather_delhi['Temperature'].values.tolist()
    weather_indhum = weather_delhi['Humidity (%)'].values.tolist()
    weathr_indwin = weather_delhi['Wind Speed (mph)'].values.tolist()
    cthw_case = cthw['Confirmed'].values.tolist()
    context = {'indposit':indposit ,'weather_inddate':weather_inddate,'weather_indtemp':weather_indtemp,'weather_indhum':weather_indhum,'weathr_indwin':weathr_indwin,'cthw_case':cthw_case}
    return render(request,'india.html',context)

def singaPage(request):
    worlt = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    posit = worlt[['Country/Region',worlt.columns[-1]]].groupby('Country/Region').sum()
    posit=posit.reset_index()
    posit.columns=['Country/Region','values']
    posit= posit.sort_values(by='values',ascending=False)
    iposit = posit.loc[lambda posit: (posit['Country/Region'] == ('Singapore'))]
    iposit = iposit['values'].values.tolist()
    singco = pd.read_csv('https://raw.githubusercontent.com/arc7creat/covdat/main/covid_19_data.csv',encoding='utf-8',na_values=None)
    singco['ObservationDate'] = pd.to_datetime(singco['ObservationDate'],format = '%m/%d/%Y').dt.strftime("%d/%m/%Y")
    contry = singco[singco.Country == 'Singapore']
    stats = contry.reset_index()
    weather_singa = pd.read_csv('https://raw.githubusercontent.com/arc7creat/covdat/main/data_singapore_weather.csv',encoding='utf-8',na_values=None)
    dtfsinga = weather_singa[['Time', 'Temperature','Humidity (%)','Wind Speed (mph)']]
    dtfsinga= dtfsinga.reset_index()
    cthw = dtfsinga[['Time', 'Temperature','Humidity (%)','Wind Speed (mph)']].copy()
    cthw['Confirmed'] = stats['Confirmed'].copy()
    weather_singdate= weather_singa['Time'].values.tolist()
    weather_singtemp= weather_singa['Temperature'].values.tolist()
    weather_singhum = weather_singa['Humidity (%)'].values.tolist()
    weathr_singwin = weather_singa['Wind Speed (mph)'].values.tolist()
    cthw_case = cthw['Confirmed'].values.tolist()
    context = {'iposit':iposit ,'weather_singdate':weather_singdate,'weather_singtemp':weather_singtemp,'weather_singhum':weather_singhum,'weathr_singwin':weathr_singwin,'cthw_case':cthw_case}
    return render(request,'singapore.html',context)

def brazPage(request):
    worlt = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',encoding='utf-8',na_values=None)
    posit = worlt[['Country/Region',worlt.columns[-1]]].groupby('Country/Region').sum()
    posit=posit.reset_index()
    posit.columns=['Country/Region','values']
    posit= posit.sort_values(by='values',ascending=False)
    iposit = posit.loc[lambda posit: (posit['Country/Region'] == ('Brazil'))]
    iposit = iposit['values'].values.tolist()
    braco = pd.read_csv('https://raw.githubusercontent.com/arc7creat/covdat/main/brazil_covid19_cities.csv',encoding='utf-8',na_values=None)
    contry = braco[braco.state == 'RJ']
    stat = contry[contry.name == 'Rio de Janeiro']
    stats = stat.reset_index()
    weather_brio = pd.read_csv('https://raw.githubusercontent.com/arc7creat/covdat/main/data_Rio%20de%20Janeiro_weather.csv',encoding='utf-8',na_values=None)
    dtfrio = weather_brio[['Time', 'Temperature','Humidity (%)','Wind Speed (mph)']]
    dtfrio= dtfrio.reset_index()
    cthw = dtfrio[['Time', 'Temperature','Humidity (%)','Wind Speed (mph)']].copy()
    cthw['cases'] = stats['cases'].copy()
    weather_bradate= weather_brio['Time'].values.tolist()
    weather_bratemp= weather_brio['Temperature'].values.tolist()
    weather_brahum = weather_brio['Humidity (%)'].values.tolist()
    weathr_brawin = weather_brio['Wind Speed (mph)'].values.tolist()
    cthw_case = cthw['cases'].values.tolist()
    context = {'iposit':iposit ,'weather_bradate':weather_bradate,'weather_bratemp':weather_bratemp,'weather_brahum':weather_brahum,'weathr_brawin':weathr_brawin,'cthw_case':cthw_case}
    return render(request,'brazil.html',context)
    
    