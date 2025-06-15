import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

DATA_PATH = "data/klikindomaret_products.csv"

st.set_page_config(page_title="KlikIndomaret Coffee Insights", layout="wide")
st.title("☕ KlikIndomaret Coffee Product Dashboard")
st.markdown("Explore insights from scraped coffee products on KlikIndomaret.com")

# === Load Data ===
if not os.path.exists(DATA_PATH):
    st.warning("No data found. Please run the scraper first.")
else:
    df = pd.read_csv(DATA_PATH)

    # Clean price column
    df["price_clean"] = df["price"].str.replace("Rp", "").str.replace(".", "", regex=False).astype(float)

    # Sidebar
    st.sidebar.header("🔍 Filters")
    search_term = st.sidebar.text_input("Search by product name:")
    price_range = st.sidebar.slider(
        "Select Price Range (Rp)", 
        int(df["price_clean"].min()), 
        int(df["price_clean"].max()), 
        (int(df["price_clean"].min()), int(df["price_clean"].max()))
    )

    # Apply filters
    if search_term:
        df = df[df["name"].str.contains(search_term, case=False, na=False)]

    df = df[(df["price_clean"] >= price_range[0]) & (df["price_clean"] <= price_range[1])]

    # === Insights Section ===
    st.subheader("📊 Summary Insights")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Products", len(df))
    col2.metric("Min Price (Rp)", f"{int(df['price_clean'].min()):,}")
    col3.metric("Max Price (Rp)", f"{int(df['price_clean'].max()):,}")

    # Cheapest and Most Expensive
    st.subheader("🏷️ Price Extremes")
    col4, col5 = st.columns(2)
    cheapest = df.sort_values("price_clean").iloc[0]
    most_expensive = df.sort_values("price_clean", ascending=False).iloc[0]
    col4.markdown(f"**Cheapest Product**\n\n{cheapest['name']}  \n💰 Rp {int(cheapest['price_clean']):,}")
    col5.markdown(f"**Most Expensive Product**\n\n{most_expensive['name']}  \n💰 Rp {int(most_expensive['price_clean']):,}")

    # === Price Distribution Chart ===
    st.subheader("💰 Price Distribution")
    fig, ax = plt.subplots()
    df["price_clean"].plot(kind="hist", bins=20, ax=ax, color="#69b3a2", edgecolor="black")
    ax.set_xlabel("Price (Rp)")
    ax.set_ylabel("Number of Products")
    st.pyplot(fig)

    # === Product Table ===
    st.subheader("📋 Product Table")
    st.dataframe(df)

    # === Keyword Frequency ===
    st.subheader("🔤 Top Keywords in Product Names")
    from collections import Counter
    import re

    words = []
    for name in df["name"]:
        words.extend(re.findall(r"\b[a-zA-Z]+\b", name.lower()))

    stopwords = {"kopi", "gram", "ml", "isi", "pcs", "rasa", "botol", "pack"}
    word_freq = Counter([w for w in words if w not in stopwords and len(w) > 2])
    top_words = pd.DataFrame(word_freq.most_common(10), columns=["Keyword", "Count"])

    st.bar_chart(top_words.set_index("Keyword"))

