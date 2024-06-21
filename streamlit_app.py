import streamlit as st
import pandas as pd
import os

st.title('Bam\'s Stop Sign Detector')

uploaded_file = st.file_uploader("Upload a jpg/png file", type=["jpg", "png"])
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.image(bytes_data)

    with open("Detected_Faces_and_Stop_Signs.png", "r") as output_file:
        bytes_data = output_file.read()
        st.image(bytes_data)

    
    
