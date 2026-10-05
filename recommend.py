import pickle


# ============================================================
# LOAD TRAINED MODEL
# ============================================================

MODEL_PATH = "models/similarity_model.pkl"

with open(MODEL_PATH, "rb") as file:
    similarity_df = pickle.load(file)


# ============================================================
# RECOMMENDATION FUNCTION
# ============================================================

def recommend_products(product_name, number_of_recommendations=5):

    # Check if product exists
    if product_name not in similarity_df.index:
        return []

    # Get similarity scores
    similarity_scores = similarity_df[product_name]

    # Sort products by similarity
    similar_products = similarity_scores.sort_values(
        ascending=False
    )

    # Remove the selected product
    similar_products = similar_products[
        similar_products.index != product_name
    ]

    # Select top recommendations
    recommendations = similar_products.head(
        number_of_recommendations
    )

    return list(recommendations.index)


# ============================================================
# TEST RECOMMENDATION SYSTEM
# ============================================================

if __name__ == "__main__":

    print("========================================")
    print("ONLINE RETAIL RECOMMENDATION SYSTEM")
    print("========================================")

    # Take the first product from the model
    product = similarity_df.index[0]

    print("\nSelected Product:")
    print(product)

    print("\nRecommended Products:")

    recommendations = recommend_products(
        product,
        5
    )

    if recommendations:

        for number, item in enumerate(
            recommendations,
            start=1
        ):
            print(
                f"{number}. {item}"
            )

    else:

        print("No recommendations found.")

        