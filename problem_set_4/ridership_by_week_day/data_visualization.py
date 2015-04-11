import pandas
from ggplot import *
import datetime
import numpy as np
def sort_pd(key=None,reverse=False,cmp=None):
    def sorter(series):
        series_list = list(series)
        return [series_list.index(i) 
           for i in sorted(series_list,key=key,reverse=reverse,cmp=cmp)]
    return sorter
def plot_weather_data(turnstile_weather):
    #Ridership by day of week
   
    turnstile_weather.is_copy = False
    turnstile_weather['weekday'] = turnstile_weather['DATEn'].map(lambda x: datetime.datetime.strptime(str(x), "%Y-%m-%d").strftime("%A"))
    ridership_grouped_by_dow = turnstile_weather.groupby('weekday',as_index=False,sort=False).mean()
    plot=ggplot(ridership_grouped_by_dow,aes(x='weekday',y='ENTRIESn_hourly',fill='weekday')) + \
       geom_bar(stat='bar',labels=ridership_grouped_by_dow["weekday"].tolist())+\
     xlab("Week Day") + ylab("Mean Ridership") +ggtitle("Mean Ridership by day of week")
    return plot
    
if __name__ == "__main__":
    image = "plot.png"
    with open(image, "wb"):
        turnstile_weather = pandas.read_csv('turnstile_data_master_with_weather.csv')
        plot_weather_data(turnstile_weather)
        gg =  plot_weather_data(turnstile_weather)
        ggsave(image, gg)
