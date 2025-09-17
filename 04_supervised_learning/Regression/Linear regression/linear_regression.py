import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# 📌 Step 1: Data (Hours studied vs Marks scored)
X = np.array([[1], [2], [3], [4], [5], [6]])  # Hours studied
y = np.array([20, 40, 60, 80, 100, 120])      # Marks scored

# 📌 Step 2: Create & Train Model
model = LinearRegression()
model.fit(X, y) # Train the model to learn the relationship between hours and marks. fit() is used for training

# 📌 Step 3: Make Prediction
hours = np.array([[7]])  # Predict marks for 7 hours study
predicted_marks = model.predict(hours) # It predict the output and store as array in predicted_marks variable
print(f"Predicted marks for 7 hours of study: {predicted_marks[0]}")
print(model.predict(X))

plt.scatter(X, y, color="blue", label="Actual Data")      # Training data plotting
plt.plot(X, model.predict(X), color="red", label="Line")  # Regression line
plt.scatter(hours, predicted_marks, color="green", label="Prediction")  # Predicted Data point in green color
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.legend()
plt.show()
