import pandas as pd
import folium
from streamlit_folium import folium_static
import streamlit as st
import os

print(os.listdir())

# Load the disaster data from CSV
data = pd.read_csv('Top 9 Disasters Filtered.csv')

# Verify column names
print(data.columns.tolist())

# Set up the Streamlit app title
st.title("Disaster Dashboard")

# Create a sidebar for disaster type selection
st.sidebar.header("Filter Options")
selected_disaster_type = st.sidebar.selectbox("Select Disaster Type", data['Disaster Type'].unique())

# Add a year range slider
min_year = int(data['Start Year'].min())
max_year = int(data['Start Year'].max())
year_range = st.sidebar.slider("Select Year Range", min_year, max_year, (min_year, max_year))

# Filter data based on disaster type and year range
filtered_data = data[(data['Disaster Type'] == selected_disaster_type) &
                     (data['Start Year'] >= year_range[0]) &
                     (data['Start Year'] <= year_range[1])]

# Map height
map_height = 800

# Create a map centered on the average latitude and longitude of filtered data
m = folium.Map(location=[data['Latitude'].mean(), data['Longitude'].mean()], zoom_start=2, height=map_height)

# Add markers for each disaster in the filtered data
for _, row in filtered_data.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"{row.get('Event Name', 'N/A')}<br>Total Deaths: {row.get('Total Deaths', 'N/A')}<br>Total Affected: {row.get('Total Affected', 'N/A')}",
        icon=folium.Icon(color='red')
    ).add_to(m)

# CSS to set column width
st.markdown(
    """
    <style>
    .stColumn {
        width: fit-content !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create a layout with the map on the left and metadata on the right
col1, col2 = st.columns([3, 2])  # Adjust the ratio as needed (3:2 for more metadata space)

with col1:
    st.subheader("Disaster Map")
    folium_static(m)

with col2:
    st.subheader("Disaster Metadata")
    st.write(filtered_data[['Country', 'Total Deaths', 'Total Affected', 'Total Damage (\'000 US$)', 'Start Year']])

    # Summary statistics in the right sidebar
    st.subheader("Summary Statistics")
    st.write(filtered_data.describe())
    st.subheader("Number of Disasters")
    st.write(f"Total Disasters: {len(filtered_data)}")

    total_deaths = filtered_data['Total Deaths'].sum()
    total_affected = filtered_data['Total Affected'].sum()
    st.subheader("Total Deaths and Affected People")
    st.write(f"Total Deaths: {total_deaths}")
    st.write(f"Total Affected: {total_affected}")

    total_damage = filtered_data['Total Damage (\'000 US$)'].sum()
    st.subheader("Total Damage")
    st.write(f"Total Damage: {total_damage} '000 US$")

    average_damage = filtered_data['Total Damage (\'000 US$)'].mean()
    st.subheader("Average Damage per Disaster")
    st.write(f"Average Damage: {average_damage} '000 US$")

    average_deaths = filtered_data['Total Deaths'].mean()
    st.subheader("Average Deaths per Disaster")
    st.write(f"Average Deaths: {average_deaths}")

    average_affected = filtered_data['Total Affected'].mean()
    st.subheader("Average Affected People per Disaster")
    st.write(f"Average Affected: {average_affected}")

    st.subheader("Most Affected Countries")
    most_affected_countries = filtered_data.groupby('Country')['Total Affected'].sum().reset_index()
    most_affected_countries = most_affected_countries.sort_values(by='Total Affected', ascending=False)
    st.write(most_affected_countries.head(10))



    st.subheader("Most Damaging Disasters")
    most_damaging_disasters = filtered_data.sort_values(by='Total Damage (\'000 US$)', ascending=False)
    most_damaging_disasters = most_damaging_disasters[['Event Name', 'Country', 'Total Damage (\'000 US$)']]
    st.write(most_damaging_disasters.head(10))
