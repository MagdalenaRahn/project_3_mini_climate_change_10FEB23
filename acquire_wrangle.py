import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import mean_squared_error
from math import sqrt 

from env import username, host, password




# this function returns the .csv file

def get_temp_data():
    
    temp = pd.read_csv('GlobalLandTemperaturesByMajorCity.csv')
    
    return temp
                       

        
def evaluate(target_var):
    
    '''
    This function will take the actual values of the target_var from validate, 
    and the predicted values stored in yhat_df, 
    and compute the rmse, rounding to 0 decimal places. 
    it will return the rmse. 
    '''
    
    rmse = round(sqrt(mean_squared_error(val[target_var], yhat_df[target_var])), 0)
    print(f'The RMSE on train is {rmse}.')
    
    return rmse



        
        
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
        
        

def append_eval_df(model_type, target_var):
    
    rmse = evaluate(target_var)
    
    f = {'model_type' : [model_type], 'target_var' : [target_var], 'RMSE' : [rmse]}
    
    f = pd.DataFrame(f)
    
    return eval_df.append(f, ignore_index = True)
        
        
        
# plotting and RMSE function

def plot_eval(train, val, yhat_df, target):
    
    '''
    This function takes in the target variable and returns a graph
    of the train, validate and predicted values from the yhat dataframe.
    It also labels the RMSE.
    '''
    
    plt.figure(figsize = (12, 6))
    
    plt.plot(train[target], label = 'Train', linewidth = 0.7, color = 'm')
    plt.plot(val[target], label = 'Validate', linewidth = 0.7, color = 'y')
    plt.plot(yhat_df[target], label = 'yhat', linewidth = 0.9, c = 'g')
    
    plt.legend()
    plt.title('Average Temperature')

    
    plt.show()
            