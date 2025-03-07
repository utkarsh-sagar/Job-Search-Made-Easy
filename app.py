import streamlit as st
import os
import time 
from utils import save_files
import json
import pandas as pd
import shutil  # Import the shutil module for file/directory operations
import numpy as np  # Import numpy


st.set_page_config(
    page_title='Job Search Made Easy ',
    layout="centered",
    
)

st.markdown('<h1>Job Seekers : Job Search Made Easy</h1>', unsafe_allow_html=True)

Job_role = st.text_input( ":information_source: Enter the job role you want to look for")

Job_experience = st.text_input( ":information_source: Enter the experience level you want to look for")

Job_location = st.text_input( ":information_source: Enter the job location you want to look for")

main_uploaded_files = st.file_uploader(":information_source:   Upload a PDF of the candidate resume/CV.", accept_multiple_files=False, type=["pdf"] )

if main_uploaded_files:
    main_saved_status = save_files(main_uploaded_files)

#we'll first look for linkedin roles.
abcs
#lets check how to scrape 