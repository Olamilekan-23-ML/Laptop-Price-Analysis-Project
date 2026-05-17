import pandas as pd 
import plotly.express as px
import streamlit as st
import plotly.figure_factory as ff
# LOADING DATASETS
laptop = pd.read_csv('laptop.csv')

# SETTING DASHBOARD PAGE
st.set_page_config(layout='wide')
# PAGE TITLE 

st.title(':computer: **LAPTOP PRICE DASHBOARD**')
# SIDE BAR
st.sidebar.header('**Choose your option:** ')
# FILTERING SIDE BAR
laptop['brand'] = laptop['brand'].str.strip().str.upper()
brand = st.sidebar.multiselect('Select your brand',sorted(laptop['brand'].unique()))
if not brand:
    lp = laptop.copy()
else:
    lp = laptop[laptop['brand'].isin(brand)] 
laptop['model'] = laptop['model'].str.strip().str.upper()   
model = st.sidebar.multiselect('Select your model',sorted(lp['model'].unique()))
if not model:
    lp2 = lp.copy()
else:
    lp2 = lp[lp['model'].isin(model)]
cpu = st.sidebar.multiselect("Central Processing Unit",sorted(lp2['cpu'].unique()))
if not cpu:
    lp3 = lp2.copy()
else:
    lp3 = lp2[lp2['cpu'].isin(cpu)]
#FILTERING PAGE 
if not brand and not model and not cpu:
    filtered = laptop
elif not model and not cpu:
    filtered = lp[lp['brand'].isin(brand)]
elif not brand and not cpu:
    filtered = lp2[lp2['model'].isin(model)]
elif not brand and not model:
    filtered = lp3[lp3['cpu'].isin(cpu)]
elif model and cpu:
    filtered = lp3[lp2['model'].isin(model) & lp3['cpu'].isin(cpu)]
elif brand and cpu:
    filtered = lp3[lp['brand'].isin(brand) & lp3['cpu'].isin(cpu)]
elif brand and model:
    filtered = lp2[lp['brand'].isin(brand) & lp2['model'].isin(model)]
else:
    filtered = lp3[lp['brand'].isin(brand) & lp2['model'].isin(model) & lp3['cpu'].isin(cpu)]


# VISUALIZATION
st.markdown('---')
col1, col2, col3 = st.columns(3)
with col1:
    total = filtered['price($)'].sum()
    if total >= 1_000_000:
        total_val = f"${total / 1_000_000:.1f}M"
    elif total >= 1_000:
        total_val = f"${total/1_000:.0f}K"
    else:
        total_val = f"${total:.2f}"
    with st.container(border=True):
        st.metric(
        label='TOTAL PRICE',
        value=total_val,
        delta="Live Update"
        )
with col2:
    mean = filtered['rating'].mean()
    average_rating = f"{mean:.1f}"
    with st.container(border=True):
        st.metric(
        label='AVERAGE RATING',
        value=average_rating,
        delta="Live Update"
        )
with col3:
    total_quantity = len(filtered['model'])
    with st.container(border=True):
        st.metric(
        label='LAPTOP QUANTITY',
        value=total_quantity,
        delta="Live Update"
        )
with st.expander("CLICK TABLE"):
    summary = filtered.groupby(['brand', 'model', 'screen_size(Inches)', 'cpu', 'ram(GB)',
    'operating_system'])[['price($)','rating']].mean().reset_index()
    sample = summary[0:10][['brand', 'model', 'screen_size(Inches)', 'cpu', 'ram(GB)',
    'operating_system','price($)','rating']]
    fig = ff.create_table(sample,colorscale='thermal') 
    st.plotly_chart(fig,use_container_width=True)
col1, col2 = st.columns(2)
with col1:
    price_category = filtered.groupby('model')['price($)'].sum().reset_index()
    fig = px.line(price_category, x='model', y='price($)', title='LAPTOP MODEL PRICE')
    fig.update_traces(
        line_color = 'blue',
        line_width = 1,
        line_shape = 'linear'
        )
    st.plotly_chart(fig, use_container_width=True)
with col2:
    rating_category = filtered.groupby(['brand'])['rating'].mean().reset_index().sort_values(by='rating', ascending=True)
    fig = px.bar(rating_category,x='brand',y='rating', title='AVERAGE BRAND RATING',color_discrete_sequence=['blue'])
    fig.update_traces(marker_color='blue')
    st.plotly_chart(fig,use_container_width=True)
col3, col4 = st.columns(2)
with col3:
    fig = px.strip(filtered, 
                    y='price($)',
                    x='rating',
                    hover_data={
                        'cpu': True,
                        'price($)':":$.2f",
                        'rating': True
                    },
                    title='PRICE VS. RATING',
                    color_discrete_sequence=["#3BEF3B"],
                    stripmode='overlay'
                    )
    fig.update_traces(jitter=0.01)
    st.plotly_chart(fig,use_container_width=True)
with col4:
    fig = px.strip(filtered, 
                    y='ram(GB)',
                    x='screen_size(Inches)',
                    hover_data={
                        'operating_system': True,
                        'screen_size(Inches)':":.2f",
                        'ram(GB)': True
                    },
                    title='RAM VS. SCREEN SIZE',
                    color_discrete_sequence=["#EF3B3B"],
                    stripmode='group'
                )
    fig.update_traces(jitter=0.7)
    st.plotly_chart(fig,use_container_width=True)

