import streamlit as st
import pandas as pd
import os
import sys

from classification_face_stop_sign_recognition import run_classification

st.title('Bam\'s Stop Sign Detector')

uploaded_file = st.file_uploader("Upload a jpg/png file", type=["jpg", "png"])
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.image(bytes_data)
    # Ensure the src directory is in the path
    
    run_classification()

    st.image("Detected_Faces_and_Stop_Signs.png")

    
    
