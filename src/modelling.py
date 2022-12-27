from joblib import load
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

print('Importing dataset from ./data...')

df = pd.read_csv('C:/Users/Tan Yu Xuan/Desktop/resale-flat/data/clean_csv.csv', index_col=[0])

print('Preprocessing dataset for predictions...')

# Ranking storey range
storey_range_dict = {'01 TO 03':0, '04 TO 06':1, '07 TO 09':2, '10 TO 12':3, '13 TO 15':4, '16 TO 18':5, '19 TO 21':6, '22 TO 24':7, '25 TO 27':8, '28 TO 30':9, '31 TO 33':10, '34 TO 36':11, '37 TO 39':12, '40 TO 42':13, '43 TO 45':14, '46 TO 48':15, '49 TO 51':16}
df['storey_range_rank'] = df['storey_range'].replace(storey_range_dict)
print('Ranking storey_range from lowest (0) to highest floor (16).')

# Dropping unused columns
df.drop(columns = ['month', 'flat_type', 'block', 'street_name', 'storey_range', 'remaining_lease', 'units', 'latitude', 'longitude', 'address', 'town_rank', 'units_rank'], inplace=True)
print('DataFrame processed sucessfully!')

# Get dummies
df = pd.get_dummies(data=df, columns=['town'])
print('Convert categorical variable into dummy/indicator variables')

# Import resale prices dataset
df_resale = pd.read_csv('C:/Users/Tan Yu Xuan/Desktop/resale-flat/data/resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv', index_col=[0])
df_resale.reset_index(drop=True, inplace = True)

X = df.drop('resale_price', axis=1).values

model = input('Which algorithm is to be used? (decision tree / knn)')

if model.lower() == 'decision tree':
    print(f'Loading {model.lower()} model...')
    dtr = load('C:/Users/Tan Yu Xuan/Desktop/resale-flat/src/models/decision_tree_regressor.joblib')
    y_pred = dtr.predict(X)
    y_pred_df = pd.DataFrame(data=y_pred, columns=["predicted_resale_price"])
    results = df_resale.join(y_pred_df)
    results.to_csv(r'C:/Users/Tan Yu Xuan/Desktop/resale-flat/data/decision_tree_results.csv')
    print('Results saved into csv format!')

elif model.lower() == 'knn':
    print(f'Loading {model.lower()} model...')
    knn = load('C:/Users/Tan Yu Xuan/Desktop/resale-flat/src/models/knn_regressor.joblib')
    y_pred = knn.predict(X)
    y_pred_df = pd.DataFrame(data=y_pred, columns=["predicted_resale_price"])
    results = df_resale.join(y_pred_df)
    results.to_csv(r'C:/Users/Tan Yu Xuan/Desktop/resale-flat/data/knn_regressor_results.csv')
    print('Results saved into csv format!')

else:
    print('Please select a valid option. (decision tree / knn)')
