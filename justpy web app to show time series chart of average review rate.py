from itertools import groupby
import pandas as pd
import justpy as jp
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\Users\linyi\Desktop\reviews.csv", parse_dates=['Timestamp'])
data['Day']=data['Timestamp'].dt.date
day_average=data.groupby(['Day']).mean()
chart_def="""
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average rating of reviews'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'average rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""
def app():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp, text="Analysis of Reviews",classes= "text-h3 text-center q-pa-md")
    p1=jp.QDiv(a=wp, text="These graphs represent review analysis")
    hc=jp.HighCharts(a=wp, options=chart_def)
    hc.options.title.text="Average Rating by day"
    hc.options.xAxis.categories=list(day_average.index)
    hc.options.series[0].data=list(day_average['Rating'])
    return wp

jp.justpy(app)