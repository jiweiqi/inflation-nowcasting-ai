from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import plotly.express as px

"""
# Project Inflation using AI

With historically high inflation rates, it is important to understand how inflation will evolve. 
This project aims to use economic models, machine learning and statistics to predict inflation rates.

"""

df = px.data.stocks()
fig = px.line(df, x="date", y=df.columns,
              hover_data={"date": "|%B %d, %Y"},
              title=None)
fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y")
st.plotly_chart(fig, use_container_width=True)


"""
disclaimer: this is a work in progress and should not be used for any financial decisions.
"""
