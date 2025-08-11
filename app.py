import streamlit as st
import json
import os

# Get absolute path to the data file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "sacramentals.json")

def load_data():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    st.title("Catholic Sacramentals Encyclopedia")

    data = load_data()

    for item in data:
        st.subheader(item["name"])
        st.image(os.path.join(BASE_DIR, "assets", item["image"]),
                 caption=item["name"], use_container_width=True)
        st.write(item["description"])

if __name__ == "__main__":
    main()

