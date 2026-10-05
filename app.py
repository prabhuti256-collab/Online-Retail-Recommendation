import pickle
import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Retail Recommendation System",
    page_icon="🛍️",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>
    .main-title {
        font-size: 38px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .metric-card {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        border: 1px solid #ddd;
    }

    .recommendation-card {
        padding: 15px;
        margin: 8px 0;
        border-radius: 10px;
        border: 1px solid #ddd;
        font-size: 17px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    with open(
        "models/similarity_model.pkl",
        "rb"
    ) as file:

        similarity_df = pickle.load(file)

    return similarity_df


similarity_df = load_model()

products = list(similarity_df.index)

# =========================================================
# RECOMMENDATION FUNCTION
# =========================================================

def recommend_products(
    product_name,
    number_of_recommendations
):

    if product_name not in similarity_df.index:
        return []

    similarity_scores = similarity_df[
        product_name
    ]

    similar_products = (
        similarity_scores
        .sort_values(
            ascending=False
        )
    )

    similar_products = similar_products[
        similar_products.index != product_name
    ]

    return similar_products.head(
        number_of_recommendations
    )


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🛍️ AI Retail Recommendation System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Machine Learning based Product Recommendation using Collaborative Filtering</div>',
    unsafe_allow_html=True
)

st.divider()

# =========================================================
# DASHBOARD METRICS
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "🛒 Total Products",
        f"{len(products):,}"
    )

with col2:

    st.metric(
        "🤖 Recommendation Method",
        "Item-Based CF"
    )

with col3:

    st.metric(
        "📐 Similarity Algorithm",
        "Cosine Similarity"
    )

st.divider()

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚙️ Recommendation Settings")

search_text = st.sidebar.text_input(
    "🔍 Search Product",
    placeholder="Type product name..."
)

number_of_recommendations = st.sidebar.slider(
    "Number of Recommendations",
    min_value=1,
    max_value=10,
    value=5
)

# =========================================================
# PRODUCT SEARCH
# =========================================================

filtered_products = products

if search_text:

    filtered_products = [
        product
        for product in products
        if search_text.lower()
        in product.lower()
    ]

if not filtered_products:

    st.warning(
        "❌ No products found. Try another search."
    )

    st.stop()

# =========================================================
# PRODUCT SELECTION
# =========================================================

st.subheader("🔎 Select a Product")

selected_product = st.selectbox(
    "Choose a product for recommendation:",
    filtered_products
)

# =========================================================
# SELECTED PRODUCT
# =========================================================

st.info(
    f"🛍️ Selected Product: **{selected_product}**"
)

# =========================================================
# RECOMMEND BUTTON
# =========================================================

if st.button(
    "🚀 Generate Recommendations",
    use_container_width=True
):

    recommendations = recommend_products(
        selected_product,
        number_of_recommendations
    )

    st.divider()

    st.subheader(
        "🎯 Recommended Products"
    )

    if recommendations.empty:

        st.warning(
            "No recommendations found."
        )

    else:

        for number, (product, score) in enumerate(
            recommendations.items(),
            start=1
        ):

            percentage = score * 100

            st.markdown(
                f"""
                <div class="recommendation-card">

                <b>{number}. {product}</b>

                <br>

                Similarity Score:
                <b>{percentage:.2f}%</b>

                </div>
                """,
                unsafe_allow_html=True
            )

# =========================================================
# HOW IT WORKS
# =========================================================

st.divider()

st.subheader("🤖 How the Recommendation System Works")

st.write(
    """
    This project uses **Item-Based Collaborative Filtering**
    to recommend products.

    The system analyzes customer purchasing patterns and
    creates a product-customer interaction matrix.

    Then, **Cosine Similarity** is used to measure how similar
    products are based on customer purchasing behavior.

    When a user selects a product, the system recommends
    products that have the highest similarity scores.
    """
)

# =========================================================
# TECHNOLOGIES
# =========================================================

st.subheader("🛠️ Technologies Used")

tech1, tech2, tech3, tech4, tech5 = st.columns(5)

with tech1:
    st.write("🐍 Python")

with tech2:
    st.write("🐼 Pandas")

with tech3:
    st.write("🔢 NumPy")

with tech4:
    st.write("🤖 Scikit-learn")

with tech5:
    st.write("🌐 Streamlit")

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "AI Retail Recommendation System | "
    "Machine Learning Project | "
    "Item-Based Collaborative Filtering"
)

