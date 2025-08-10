import streamlit as st

# Sample data embedded directly to avoid missing file errors
SACRAMENTALS = [
    {
        "name": "Holy Water",
        "category": "Blessed Objects",
        "description": "Water blessed by a priest for the purpose of sanctification.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f6/Holy_water_font.jpg/320px-Holy_water_font.jpg"
    },
    {
        "name": "Rosary",
        "category": "Prayer Beads",
        "description": "A string of beads used to keep count of prayers, especially the Hail Marys.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Rosary.jpg/320px-Rosary.jpg"
    },
    {
        "name": "Scapular",
        "category": "Devotional Wear",
        "description": "A sacramental worn as a sign of devotion and a reminder of the wearer's commitment to live a Christian life.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/ScapularOLMountCarmel.jpg/320px-ScapularOLMountCarmel.jpg"
    }
]

def main():
    st.set_page_config(page_title="Catholic Sacramentals", layout="wide")
    st.title("📿 Catholic Sacramentals Encyclopedia")
    
    # Sidebar filters
    search = st.sidebar.text_input("Search sacramentals")
    categories = sorted(set([item['category'] for item in SACRAMENTALS]))
    selected_category = st.sidebar.selectbox("Filter by category", ["All"] + categories)

    # Filter data
    filtered = [
        s for s in SACRAMENTALS
        if (search.lower() in s["name"].lower() or search.lower() in s["description"].lower())
        and (selected_category == "All" or s["category"] == selected_category)
    ]

    # Display cards
    cols = st.columns(3)
    for idx, sacramental in enumerate(filtered):
        with cols[idx % 3]:
            st.image(sacramental["image"], use_column_width=True)
            st.subheader(sacramental["name"])
            st.caption(sacramental["category"])
            st.write(sacramental["description"])

if __name__ == "__main__":
    main()
