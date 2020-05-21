import os
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from statsmodels.tsa.seasonal import seasonal_decompose 
from sklearn.metrics import mean_squared_error 
from statsmodels.tools.eval_measures import rmse

url='https://raw.githubusercontent.com/saswatp99/umeed/master/carpets.csv'
airline = pd.read_csv(url, 
          index_col ='Month', 
          parse_dates = True)

# Print the first five rows of the dataset 
airline.head() 

# ETS Decomposition 
 
# Import the library 
from pmdarima import auto_arima 
  
# Ignore harmless warnings 
import warnings 
warnings.filterwarnings("ignore")  
# Split data into train / test sets 
train = airline.iloc[:len(airline)-12] 
test = airline.iloc[len(airline)-12:] # set one year(12 months) for testing 

# Fit a SARIMAX(0, 1, 1)x(2, 1, 1, 12) on the training set 
from statsmodels.tsa.statespace.sarimax import SARIMAX 

model = SARIMAX(train['#Passengers'], 
        order = (0, 1, 1), 
        seasonal_order =(2, 1, 1, 12)) 

result = model.fit() 
result.summary() 
start = len(train) 
end = len(train) + len(test) - 1
  
# Predictions for one-year against the test set 
predictions = result.predict(start, end, 
                             typ = 'levels').rename("Predictions") 
  
# Train the model on the full dataset 
model = model = SARIMAX(airline['#Passengers'],  
                        order = (0, 1, 1),  
                        seasonal_order =(2, 1, 1, 12)) 
result = model.fit() 
  
# Forecast for the next 3 years 
forecast = result.predict(start = len(airline),  
                          end = (len(airline)-1) + 12,  
                          typ = 'levels').rename('Forecast') 
rmse(test["#Passengers"], predictions) 
mean_squared_error(test["#Passengers"], predictions) 

  
# Plot the forecast values 
#airline['#Passengers'].plot(figsize = (12, 5), legend = True) 
#forecast.plot(legend = True)

plt.plot(airline['#Passengers'])
plt.xlabel('Number of People')
plt.ylabel('Expenses')
plt.plot(forecast*0.875)
plt.show()
