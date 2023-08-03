import streamlit as st
import itertools

# Define app title
st.title("Brand Combiner")

# Input for brands
brands_input = st.text_input('Enter brands separated by comma', '')
brands = brands_input.split(',')

# Get all combinations
combinations = list(itertools.combinations(brands, 2))

if st.button('Generate combinations'):
    # Display combinations
    for combination in combinations:
        st.write(' vs '.join(combination))
