# Feature Engineering and Polynomial Regression

This project demonstrates how linear regression can model non-linear relationships using feature engineering and polynomial features.

## Objectives

- Understand feature engineering
- Apply polynomial regression
- Learn why feature scaling is important
- Visualize model predictions

## Technologies Used

- Python
- NumPy
- Matplotlib
- Jupyter Notebook

## Project Steps

### 1. Data Creation
A simple dataset is generated using:

y = 1 + x²

This creates a non-linear relationship between x and y.

### 2. Linear Regression Without Feature Engineering
A simple linear regression model is trained using gradient descent.
Since the data is non-linear, the model fails to fit the curve properly.

### 3. Feature Engineering
A new feature **x²** is created to allow the model to learn the curved pattern.

### 4. Polynomial Regression
Polynomial features such as:

- x
- x²
- x³

are added to improve model flexibility.

### 5. Feature Scaling
Z-score normalization is applied to improve gradient descent convergence.

## Results

After feature engineering, the model successfully learns the non-linear relationship and produces accurate predictions.

## Key Concepts Learned

- Feature Engineering
- Polynomial Features
- Gradient Descent
- Feature Scaling
- Data Visualization

## Author

Muhammad Junaid
Software Engineering Student
Entrepreneurship and AI Enthusiast