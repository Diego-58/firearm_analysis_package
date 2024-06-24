# firearm_analysis/map_generation.py

import folium
import pandas as pd
import selenium
import io
from PIL import Image


def create_maps(df):
    for column in ["permit_perc", "handgun_perc", "longgun_perc"]:
        # GeoJSON URL
        state_geo = "https://raw.githubusercontent.com/python-visualization/"
        state_geo += "folium/main/examples/data/us-states.json"
        # Initialize the map
        m = folium.Map(location=[40, -95], zoom_start=4)
        # Create Choropleth map
        folium.Choropleth(
            geo_data=state_geo,
            name="choropleth",
            data=df,
            columns=["code", column],
            key_on="feature.id",
            fill_color="YlGn",
            fill_opacity=0.7,
            line_opacity=0.1,
            legend_name=f"{' '.join(column.split('_'))}entage (%)",
        ).add_to(m)
        # Add layer control
        folium.LayerControl().add_to(m)
        # Save map as an image
        img_data = m._to_png(5)
        img = Image.open(io.BytesIO(img_data))
        img.save(f"{column}.png")
