# Resale Flat Price

By Tan Yu Xuan

email: yxtan92@hotmail.com

--------
## Project Organization


    ├── bash.sh            <- .sh file which preprocesses the raw data and performs predictions.
    |
    ├── README.md          <- The top-level README for users of this project.
    |
    ├── data               <- Where resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv should be placed in & processed results are stored in.
    │   ├── resale-flat-prices-based-on-registration-date-from-jan-2017-onwards.csv  <- data of resale flats from Jan 2017 onwards
    │   |
    |   └── clean_csv.csv  <- processed dataset.
    | 
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    |
    ├── eda.ipynb          <- Exploratory data analysis.
    |
    ├── src                <- Source code for use in this project.
    |   ├── __init__.py    <- Makes src a Python module
    |   |
    |   |── modelling.py   <- Script to perform predictions based on processed dataset.
    |   |
    |   └── models         <- Dumps of trained models
    |         ├── decision_tree_regressor.joblib
    |         |
    |         └── knn_regressor.joblib
    |
    └── algorithm_used.txt <- Input the algorithm to be used (decision tree / knn).
--------

# Instructions

## 1. Setting up the enviroment

### Install the required libraries from your terminal

- In your command shell/terminal locate the directory where requirements.txt is located and type in the following:

      conda create --name resaleflat --file requirements.txt

### Once all packages/libraries are installed activate the installed enviroment

- Key in the following code into your shell:

      conda activate resaleflat

## 2. Placing your data

- Place the data into the `data` folder of this directory

## 3. Running the model

- In your command shell/terminal move to where run.sh is located and key in the following command
    
      ./bash.sh
--------

# Engineering Pipeline

1. Import dataset
2. Checking for duplicates & missing values
3. Correcting abnormal data
4. Build additional features e.g. price_per_sqm
5. Converting categorical data into dummies & booleans
6. Saving processed dataset out as .csv
7. fit model & pickle it out
8. Predict with features & unpickled model
9. Output results in .csv file


# EDA Overview

The EDA contains overview of key findings from the dataset. Choices made in the pipeline are based on those findings, particularly any feature engineerings for modelling. Please keep the details of the EDA in the `.ipynb` which serves as a quick summary.


# Model choice

The following regression models are chosen for this project:
 
  1. Decision Tree Regressor
  2. K Nearest Neighbors Regressor

# Model Evaluation

For the regression models, baseline is set to be a simple linear regression model.

The goal is for the models to perform better than a simple straight line.

### Evaluation metrics

| model               | Explained Variance | Mean Absolute Error (MAE)| Root Mean Squared Error (RMSE)|
|---------------------|--------------------|--------------------------|-------------------------------|
|Linear Regression    |        0.975       |         17120.50         |           25732.62            |
|KNN (n_neighbors=5)  |        0.994       |         5094.87          |           12632.29            |
|`Decision Tree`      |       `0.9997`     |         `686.35`         |           `3032.38`           |

From the evaluation metrics we see that the decision tree regressor out performs baseline linear regression model and knn model. 

In addition, decision tree has the highest explained variance score of 99.97% (best possible score is 1.0) which means there is only 0.03% difference between the expected value and predicted value.

# Conclusion
Comparing the types of models the decision tree regressor is definitely the most accurate in predicting the resale flat prices.
