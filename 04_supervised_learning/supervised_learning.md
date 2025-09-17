# Supervised Learning:

---

## 1. What Is Supervised Learning?

Supervised learning is a type of machine learning where the model is trained (learned) using dataset which includes
input data and the correct output (label)

* The goal is for the model to learn the relationship between the input & Output.
* Once trained, the model can predict the output for **new, unseen inputs**.

Example :
I want to predict House price. Using this model, i will give my dataset like,
* **Input** -> Size of House, Number of Bedrooms & Location of House (These are **Features**. Here 3 Features mentioned)
* **Output** -> Actual price of House
You give the model many examples like this during training. After trained, you can give
the model to new house features and it will predict the price of House.
---

## 2. Why "Supervised"?

Think of it like a student learning with a teacher. The teacher gives the correct answers and helps fix any mistakes. During training,
the model learns by looking at the correct answers (called labels) and improving from them.

---

## 3. How Does It Work?

### Step 1: Collect Labeled Data

You start with a dataset:

| Input (Features)        | Output (Label) |
| ----------------------- | -------------- |
| Height = 170 cm, Age=30 | Male           |
| Height = 160 cm, Age=25 | Female         |
| Height = 180 cm, Age=40 | Male           |

---

### Step 2: Choose a Model

This can be:

* Linear Regression
* Logistic Regression etc

---

### Step 3: Train the Model

The model uses the input data and labels to **learn patterns**.
It adjusts its internal parameters to minimize the difference between its predictions and the actual labels.

---

### Step 4: Evaluate the Model

Once trained, the model is tested on new data it hasn’t seen to check how well it predicts.

---

### Step 5: Use the Model

If it performs well, you use the model to predict labels for future data.

---

## 4. Types of Supervised Learning Problems

### A. Classification

* Output is a **category or class**.
* Using classification model or algorithm to predict the output is spam or not spam (we will finding the new email(we are not pass this
email during training) is spam or not spam. Hence, it is countable class so it is category)
* Examples:

  * Email spam detection (spam or not spam)
  * Disease diagnosis (sick or healthy)
  * Image recognition (cat, dog, bird)

### B. Regression

* Output is a **continuous number**.
* We use regression when we want to predict numbers that can change — like prices, temperatures, or sales — over time or based on other things.
* Examples:

  * Predict house prices
  * Forecast stock prices
  * Predict temperature
  * Sales prediction

---

## 5. Examples Explained

### Example 1: Email Spam Classifier (Classification)

* Input: Email text features (words, sender info)
* Output: Spam or Not Spam
* The model learns from many emails labeled “spam” or “not spam” and predicts for new emails whether it is spam or not spam

---

### Example 2: House Price Prediction (Regression)

* Input: Size, location, number of rooms
* Output: Price in dollars
* The model learns from past house data with prices to predict prices of new houses.

---

## 6. Common Algorithms in Supervised Learning

| Algorithm                     | Use Case             | Description                                         |
| ----------------------------- | -------------------- | --------------------------------------------------- |
| Linear Regression             | Regression           | Fits a straight line to predict a number            |
| Logistic Regression           | Classification       | Predicts probability of a class (e.g., spam or not) |
| Decision Trees                | Both                 | Splits data based on questions to make decisions    |
| Random Forest                 | Both                 | Many decision trees combined for better accuracy    |
| Support Vector Machines (SVM) | Classification       | Finds the best boundary to separate classes         |
| Neural Networks (Deep learning)      | Both (often complex) | Layers of neurons learn complex patterns            |

---

## 7. How to Measure Performance?

* For **classification**: Accuracy, Precision, Recall, F1-score
* For **regression**: Mean Squared Error (MSE), Root Mean Squared Error (RMSE), R-squared

---

## 8. Simple Python Example (Using Scikit-learn)

Here’s a quick example of supervised learning using a classification algorithm:

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset (flowers with features and species labels)
iris = load_iris()
X = iris.data       # features
y = iris.target     # labels

# Split data: 70% train, 30% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# random_state=42 ensures the data split is the same every time you run the code. So it is reproducible way by fixing the randomness.


# Create Logistic Regression model
model = LogisticRegression(max_iter=200) # max_iter=200 limits how many times the model tries to learn

# Train the model on the training data (learn patterns from X and y)
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Measure accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

## 9. Some common algorithm in supervised learning

| Regression           | Classification                         |
| -------------------- | -------------------------------------- |
| 1. Linear Regression | 1. Logistic Regression                 |
| 2. Decision tree     | 2. K-nearest neighbour                 |
| 3. Random Forest     | 3. Support vector machine              |


---

## 10. Summary

| Step                 | What happens?                          |
| -------------------- | -------------------------------------- |
| Collect labeled data | Gather examples with correct answers   |
| Choose model         | Pick an algorithm to learn the pattern |
| Train model          | Model learns from data and labels      |
| Evaluate model       | Test on new data to check accuracy     |
| Predict              | Use the trained model for new inputs   |

---