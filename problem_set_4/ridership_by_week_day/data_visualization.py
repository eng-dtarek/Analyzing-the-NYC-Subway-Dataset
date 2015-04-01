import pandas
from ggplot import *
import datetime

def plot_weather_data(turnstile_weather):
    #Ridership by day of week
   
    turnstile_weather.is_copy = False
    turnstile_weather['weekday'] = turnstile_weather['DATEn'].map(lambda x: datetime.datetime.strptime(str(x), "%Y-%m-%d").strftime("%A"))
    ridership_grouped_by_dow = turnstile_weather.groupby('weekday',as_index=False).sum()
    plot=ggplot(ridership_grouped_by_dow, aes(x='weekday',y='ENTRIESn_hourly',fill='weekday')) + \
       geom_bar(stat='bar')+\
     xlab("Week Day") + ylab("Entries_hourly") +ggtitle("Ridership by week day")
    return plot
    
if __name__ == "__main__":
    image = "plot.png"
    with open(image, "wb"):
        turnstile_weather = pandas.read_csv('turnstile_data_master_with_weather.csv')
        plot_weather_data(turnstile_weather)
        gg =  plot_weather_data(turnstile_weather)
        ggsave(image, gg)
