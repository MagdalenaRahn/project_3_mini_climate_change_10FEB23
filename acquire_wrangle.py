import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from env import username, host, password




# this function returns the .csv file

def get_temp_data():
    
    temp = pd.read_csv('GlobalLandTemperaturesByMajorCity.csv')
    
    return temp
                       

        
        
        
        
# datetime temp clean-up function

def temp_time(df):
    
    '''
    this function takes in a dataframe, renames the columns, changes the 'date' 
    col to datetime and then sets it as the index, then creates day and month
    columns, fills nulls with 0 and returns the 
    modified dataframe
    '''
    
    # renaming cols
    df = df.rename(columns = {'dt': 'date', 'AverageTemperature' : 'avg_temp', 
                              'AverageTemperatureUncertainty' : 'avg_temp_q', 
                              'City' : 'city', 'Country' : 'country', 
                              'Latitude': 'latitude', 'Longitude' : 'longitude'})

    # change 'Date' to datetime format
    df['date'] = pd.to_datetime(df['date'])

    # setting index to now-date-formated 'Date'
    df = df.set_index('date')
    
    df = df.drop(columns = ['latitude', 'longitude'])

    # creating month & year cols
    df['month'] = df.index.month_name()
    df['year'] = df.index.year
    
    #filling NaNs with 0
    df.dropna(axis = 0, inplace = True)
    
    return df        
        
        
