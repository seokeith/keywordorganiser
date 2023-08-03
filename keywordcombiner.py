import streamlit as st
import itertools

# Define app title
st.title("Keyword Combiner")

# Define 5 columns of input
col1, col2, col3, col4, col5 = st.beta_columns(5)
with col1:
    keywords1 = st.text_input('Enter keywords for Column 1', '').split(',')
with col2:
    keywords2 = st.text_input('Enter keywords for Column 2', '').split(',')
with col3:
    keywords3 = st.text_input('Enter keywords for Column 3', '').split(',')
with col4:
    keywords4 = st.text_input('Enter keywords for Column 4', '').split(',')
with col5:
    keywords5 = st.text_input('Enter keywords for Column 5', '').split(',')

# Combine all keywords
all_keywords = [keywords1, keywords2, keywords3, keywords4, keywords5]

# Get all combinations
combinations = list(itertools.product(*all_keywords))

if st.button('Generate combinations'):
    # Display combinations
    for combination in combinations:
        st.write(' '.join(combination))
