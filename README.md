# 🛍️ Online Retail Recommendation System

## 📌 Project Overview

The **Online Retail Recommendation System** is a Machine Learning-based recommendation application that recommends products similar to a selected product.

The system uses **Item-Based Collaborative Filtering** and **Cosine Similarity** to analyze customer purchasing behavior and identify products with similar purchasing patterns.

The project includes an interactive **Streamlit web application** that allows users to search for or select a product and receive similar product recommendations with similarity scores.

---

## 🎯 Objectives

* Build a Machine Learning-based product recommendation system.
* Analyze customer purchasing behavior.
* Identify relationships between products.
* Implement Item-Based Collaborative Filtering.
* Use Cosine Similarity to measure product similarity.
* Develop an interactive Streamlit application.
* Display recommendation similarity scores.

---

## 🧠 Machine Learning Approach

This project uses **Item-Based Collaborative Filtering**.

### Workflow

```text
Online Retail Dataset
        ↓
Data Preprocessing
        ↓
Customer-Product Matrix
        ↓
Product-Customer Matrix
        ↓
Cosine Similarity
        ↓
Product Similarity Matrix
        ↓
Recommendation Engine
        ↓
Streamlit Web Application
```

### Cosine Similarity

Cosine Similarity is used to measure the similarity between products based on customer purchasing behavior.

Products with higher similarity scores are considered more similar and are recommended to the user.

---

## 📊 Dataset

The project uses the **Online Retail Dataset**, which contains retail transaction information.

Important columns include:

* InvoiceNo
* StockCode
* Description
* Quantity
* InvoiceDate
* UnitPrice
* CustomerID
* Country

### Data Preprocessing

The following preprocessing steps are performed:

* Remove records with missing Customer IDs.
* Remove records with missing product descriptions.
* Remove cancelled invoices.
* Remove negative or zero quantities.
* Remove invalid product prices.
* Clean product descriptions.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Cosine Similarity
* Machine Learning
* Collaborative Filtering
* Streamlit
* OpenPyXL
* Pickle

---

## 📁 Project Structure

```text
Online-Retail-Recommendation/
│
├── dataset/
│
├── models/
│
├── train_model.py
├── recommend.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

> The original dataset and trained model files are excluded from GitHub because of their large file sizes.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/prabhuti256-collab/Online-Retail-Recommendation.git
```

Move into the project directory:

```bash
cd Online-Retail-Recommendation
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## 📥 Dataset Setup

Download the **Online Retail Dataset** and place:

```text
Online Retail.xlsx
```

inside:

```text
dataset/
```

The dataset is not included in this GitHub repository because of GitHub's file-size limitations.

---

## 🤖 Train the Recommendation Model

After placing the dataset inside the `dataset` folder, run:

```bash
python train_model.py
```

This will create the trained recommendation files inside the `models` folder.

---

## 🔎 Test the Recommendation System

Run:

```bash
python recommend.py
```

The program will display recommended products for a selected product.

---

## 🌐 Run the Streamlit Application

Run:

```bash
streamlit run app.py
```

The application will open in your web browser.

---

## 🖥️ Application Features

### 🔍 Product Search

Search for products using the sidebar search box.

### 🛍️ Product Selection

Select a product from the available product list.

### 🎯 Product Recommendations

The system recommends products with similar purchasing patterns.

### 📊 Similarity Scores

Each recommendation displays its similarity score.

### ⚙️ Recommendation Control

Users can select the number of recommendations they want.

### 📱 Interactive Dashboard

The Streamlit interface provides an easy-to-use recommendation dashboard.

---

## 💡 Example

A user selects a product such as:

```text
I LOVE LONDON MINI RUCKSACK
```

The system analyzes its similarity with other products and returns products with the highest similarity scores.

Example:

```text
1. SET 36 COLOURING PENCILS DOILEY
2. SET 12 COLOURING PENCILS DOILEY
3. PLASTERS IN TIN SPACEBOY
4. BLUE BUNNY EASTER EGG BASKET
```

The recommendations may vary depending on the trained model.

---

## 🔄 Recommendation System Workflow

```text
User Selects Product
        ↓
Retrieve Product Vector
        ↓
Compare With Other Products
        ↓
Calculate Cosine Similarity
        ↓
Sort Similarity Scores
        ↓
Select Top Products
        ↓
Display Recommendations
```

---

## 📈 Future Improvements

Future versions can include:

* Customer-based recommendations.
* Hybrid recommendation systems.
* Popular-product fallback.
* Product sales analytics.
* Customer segmentation.
* Interactive charts.
* Recommendation history.
* Improved cold-start handling.
* Cloud deployment.
* Advanced personalization.

---

## 🎓 Internship Project

This project demonstrates practical implementation of:

* Machine Learning
* Recommendation Systems
* Data Preprocessing
* Collaborative Filtering
* Cosine Similarity
* Python Programming
* Streamlit Application Development

The project was developed as an **AI/ML internship project**.

---

## 👩‍💻 Author

**Prabhuti**

B.Tech – Artificial Intelligence & Machine Learning

---

## ⭐ Project Highlights

* End-to-end Machine Learning project
* Real-world retail transaction dataset
* Item-Based Collaborative Filtering
* Cosine Similarity
* Interactive Streamlit dashboard
* Product search functionality
* Similarity score display
* Internship-ready project structure

