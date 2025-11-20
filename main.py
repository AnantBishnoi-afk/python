import streamlit as st
import pandas as pd 
import numpy as np

st.title("hello streamlit")

# st.write("this is sample text")

# df = pd.DataFrame( {
#         'first_column':[1,2,3],
#         'second_column':[4,5,6]
#     } )

# st.write("this is the dataframe")
# st.write(df)

# chart_data = pd.DataFrame(
#     np.random.randn(20,3), columns=['a','b','c']
# )

# st.line_chart(chart_data)

name = st.text_input("Enter your name : ")

if name:
    st.write(f"Hello {name}, how are you")