
# Cost Function in Linear Regression

This project explains and implements the Cost Function used in Linear Regression.

The goal of the cost function is to measure how wrong our model predictions are.

---

## 1. Linear Model

We use the hypothesis:

f(x) = w*x + b

Where:
- w = weight (slope)
- b = bias (intercept)
- x = input feature
- y = actual value

---

## 2. Cost Function Formula

We use Mean Squared Error (MSE):

J(w, b) = (1 / 2m) * Σ (f(xᵢ) - yᵢ)²

Where:
- m = number of training examples
- f(xᵢ) = predicted value
- yᵢ = actual value

The goal is to minimize J(w, b).

---

## 3. Why Divide by 2m?

- Dividing by m gives the average error
- Dividing by 2 simplifies gradient calculation later

---

## 4. Python Implementation

```python
import numpy as np

def compute_cost(x, y, w, b):
    m = len(x)
    cost = 0

    for i in range(m):
        f_wb = w * x[i] + b
        cost += (f_wb - y[i]) ** 2

    total_cost = cost / (2 * m)
    return total_cost
```

---

## 5. Example

Training data:

| Size (1000 sqft) | Price (1000 dollars) |
|------------------|----------------------|
| 1                | 300                  |
| 2                | 500                  |

Initial parameters:

w = 0
b = 0

Cost will be large because predictions are far from actual values.

---

## 6. Key Insight

- High cost = model predictions are bad
- Low cost = model predictions are good
- Minimum cost = best fit line

Cost function creates a bowl shaped curve.
The lowest point of the bowl is the optimal solution.

---

## 7. Next Step

To minimize this cost automatically, we use Gradient Descent.
