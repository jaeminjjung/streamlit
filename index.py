import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import plotly.figure_factory as ff
import plotly.express as px
import matplotlib.pyplot as plt
import squarify
"""
# Let's publish the result. :)
"""


# Load gapminder data and filter for year 2007
df = px.data.gapminder().query("year == 2007")

fig_treemap = px.treemap(
    df,
    path=[px.Constant("world"), "continent", "country"],
    values="pop",
    color="lifeExp",
    hover_data=["iso_alpha"],
    color_continuous_scale="RdBu",
    color_continuous_midpoint=np.average(df["lifeExp"], weights=df["pop"]),
    )

# Update layout for better presentation
fig_treemap.update_layout(margin=dict(t=50, l=25, r=25, b=25))

# Display the treemap using Streamlit
st.plotly_chart(fig_treemap)
