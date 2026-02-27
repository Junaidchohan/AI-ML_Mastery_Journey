# Linear Regression From Scratch

This project implements Linear Regression manually using NumPy.

## Model
f(x) = wx + b

- w = weight (slope)
- b = bias (intercept)

## Cost Function (Mean Squared Error)

J(w,b) = (1/2m) * Σ (prediction - actual)^2

Why square?
- Removes negative signs
- Penalizes large errors
- Makes function smooth for gradient descent

Why 1/2m?
- 1/m gives average error
- 1/2 simplifies derivative

## Gradient Descent

w = w - alpha * dJ/dw
b = b - alpha * dJ/db

Goal: Minimize cost by updating w and b.

## Observations

- Cost decreases over iterations.
- Model learns correct slope and intercept.
- Larger learning rate can cause divergence.
- Smaller learning rate slows training.