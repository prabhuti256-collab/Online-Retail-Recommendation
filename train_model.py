import os
import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# CONFIGURATION
# ============================================================

DATASET_PATH = "dataset/Online Retail.xlsx"
MODEL_FOLDER = "models"

SIMILARITY_MODEL_PATH = os.path.join(
    MODEL_FOLDER,
    "similarity_model.pkl"
)

PRODUCT_MODEL_PATH = os.path.join(
    MODEL_FOLDER,
    "products.pkl"
)


# ============================================================
# LOAD DATASET
# ============================================================

print("========================================")
print("ONLINE RETAIL RECOMMENDATION SYSTEM")
print("========================================")

print("\nLoading dataset...")

df = pd.read_excel(DATASET_PATH)

print("Dataset loaded successfully!")
print("Original dataset shape:", df.shape)

print("\nDataset columns:")
print(df.columns.tolist())


# ============================================================
# DATA PREPROCESSING
# ============================================================

print("\n========================================")
print("DATA PREPROCESSING")
print("========================================")

# Remove missing CustomerID
df = df.dropna(subset=["CustomerID"])

# Remove missing product descriptions
df = df.dropna(subset=["Description"])

# Remove cancelled transactions
df = df[
    ~df["InvoiceNo"]
    .astype(str)
    .str.startswith("C")
]

# Keep positive quantities
df = df[df["Quantity"] > 0]

# Keep positive prices
df = df[df["UnitPrice"] > 0]

# Clean product names
df["Description"] = (
    df["Description"]
    .astype(str)
    .str.strip()
)

print(
    "Dataset shape after preprocessing:",
    df.shape
)


# ============================================================
# CREATE CUSTOMER-PRODUCT MATRIX
# ============================================================

print("\n========================================")
print("CREATING CUSTOMER-PRODUCT MATRIX")
print("========================================")

customer_product_matrix = df.pivot_table(
    index="CustomerID",
    columns="Description",
    values="Quantity",
    aggfunc="sum",
    fill_value=0
)

print(
    "Customer-product matrix shape:",
    customer_product_matrix.shape
)


# ============================================================
# PRODUCT-CUSTOMER MATRIX
# ============================================================

product_customer_matrix = customer_product_matrix.T

print(
    "Product-customer matrix shape:",
    product_customer_matrix.shape
)


# ============================================================
# COSINE SIMILARITY
# ============================================================

print("\n========================================")
print("CALCULATING PRODUCT SIMILARITY")
print("========================================")

similarity_matrix = cosine_similarity(
    product_customer_matrix
)

similarity_df = pd.DataFrame(
    similarity_matrix,
    index=product_customer_matrix.index,
    columns=product_customer_matrix.index
)

print("Cosine similarity calculated successfully!")


# ============================================================
# CREATE MODELS FOLDER
# ============================================================

os.makedirs(
    MODEL_FOLDER,
    exist_ok=True
)


# ============================================================
# SAVE SIMILARITY MODEL
# ============================================================

with open(
    SIMILARITY_MODEL_PATH,
    "wb"
) as file:

    pickle.dump(
        similarity_df,
        file
    )


# ============================================================
# SAVE PRODUCT LIST
# ============================================================

products = list(
    product_customer_matrix.index
)

with open(
    PRODUCT_MODEL_PATH,
    "wb"
) as file:

    pickle.dump(
        products,
        file
    )


# ============================================================
# FINAL RESULT
# ============================================================

print("\n========================================")
print("MODEL TRAINING COMPLETED SUCCESSFULLY")
print("========================================")

print(
    "Number of customers:",
    customer_product_matrix.shape[0]
)

print(
    "Number of products:",
    len(products)
)

print(
    "\nSimilarity model saved at:",
    SIMILARITY_MODEL_PATH
)

print(
    "Product list saved at:",
    PRODUCT_MODEL_PATH
)

print("========================================")

