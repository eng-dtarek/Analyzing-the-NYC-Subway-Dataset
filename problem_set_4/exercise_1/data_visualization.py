import pandas
from ggplot import *
import datetime

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://www.dropbox.com/s/meyki2wl9xfa7yk/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
    
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    
    '''    
    #Ridership by week days
   
    turnstile_weather.is_copy = False
    turnstile_weather['weekday'] = turnstile_weather['DATEn'].map(lambda x: datetime.datetime.strptime(str(x), "%Y-%m-%d").strftime("%A"))
    ridership_grouped_by_dow = turnstile_weather.groupby('weekday',as_index=False).sum()
    plot=ggplot(ridership_grouped_by_dow, aes(x='weekday',y='ENTRIESn_hourly',fill='weekday')) + \
       geom_bar(stat='bar')+\
     xlab("Week Day") + ylab("Ridership Volume") +ggtitle("Ridership by day of week") 
    return plot

if __name__ == "__main__":
    image = "plot.png"
    with open(image, "wb"):
        turnstile_weather = pandas.read_csv('turnstile_data_master_with_weather.csv')
        plot_weather_data(turnstile_weather)
        gg =  plot_weather_data(turnstile_weather)
        ggsave(image, gg)
