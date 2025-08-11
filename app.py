import streamlit as st
import json
import os

DATA_PATH = os.path.join("data", "sacramentals.json")

def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    st.set_page_config(page_title="Catholic Sacramentals", layout="wide")
    st.title("🙏 Catholic Sacramentals")

    data = load_data()

    # Search & filter
    search = st.text_input("Search sacramentals:")
    categories = sorted(set(item["category"] for item in data))
    selected_category = st.selectbox("Filter by category", ["All"] + categories)

    filtered = [
        item for item in data
        if (search.lower() in item["name"].lower() or search.lower() in item["description"].lower())
        and (selected_category == "All" or item["category"] == selected_category)
    ]

    # Display results
    cols = st.columns(3)
    for idx, item in enumerate(filtered):
        with cols[idx % 3]:
            st.image(item["image"], caption=item["name"], use_container_width=True)
            st.write(item["description"])
            st.caption(f"Category: {item['category']}")

if __name__ == "__main__":
    main()
