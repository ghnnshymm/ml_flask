# Customer Churn Prediction Project

## Description

This project aims to develop a machine learning model for predicting customer churn based on historical customer data. Customer churn refers to the phenomenon where customers discontinue their services or subscriptions.


## Usage

1. Ensure you have the necessary dataset in the correct format (CSV).

2. Preprocess the data, including handling missing values, encoding categorical variables, and splitting into training and testing sets. You can use the provided Jupyter Notebook or Python script for this purpose.

3. Train and evaluate the machine learning model for customer churn prediction. You can choose from various algorithms, such as logistic regression, random forest, or neural networks.

4. Fine-tune the model's hyperparameters using techniques like cross-validation and grid search.

5. Deploy the final model into a production-like environment, allowing it to make predictions on new customer data.

## Data

The dataset used for this project contains historical customer information, including the following columns:

- `CustomerID`: Unique identifier for each customer.
- `Name`: Customer name.
- `Age`: Customer age.
- `Gender`: Customer gender.
- `Location`: Customer location.
- `Subscription_Length_Months`: Length of the subscription in months.
- `Monthly_Bill`: Monthly bill amount.
- `Total_Usage_GB`: Total data usage in gigabytes.
- `Churn`: Target variable indicating churn (1 for churned, 0 for not churned).

You can find the dataset in CSV format in the `data` directory.

## Features

- Exploratory data analysis (EDA) was performed to understand the data better.
- Data preprocessing steps included handling missing data, encoding categorical variables, and scaling numerical features.
- The main features used for modeling include customer demographics, subscription details, and usage data.

## Model

- The machine learning model used for customer churn prediction is a neural network built with TensorFlow and Keras.
- The model architecture consists of an input layer, hidden layers with ReLU activation, and an output layer with a sigmoid activation function for binary classification.
- The model was trained using binary cross-entropy loss and optimized using the Adam optimizer.

## Results

- The model's performance was evaluated using various metrics, including accuracy, precision, recall, and F1-score.
- Confusion matrices and visualizations were used to analyze the model's predictions.

## Acknowledgments

- We acknowledge the open-source community for providing valuable tools and libraries used in this project.

## Authors

(https://github.com/ghnnshymm) - Lead Developer


