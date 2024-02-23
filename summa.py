from keras.models import load_model
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import cv2
from PIL import Image
import numpy as np
import os
from braintumorchk import getResult

st.title('Brain Tumor detection using ML from MRI image')
Patient_Name = st.text_input('Patient Name')
Phone_number = st.text_input('Mobile Number')
Email = st.text_input('Email')
Age = st.text_input('Age')
upload_file = st.file_uploader('Upload MRI image', type=['jpg', 'png', 'jpeg'])
tumor_diagnosis = ''
if st.button('Predict'):
        if upload_file is not None:
            media_folder = "media"
            os.makedirs(media_folder, exist_ok=True)
            file_path = os.path.join(media_folder, upload_file.name)
            with open(file_path, 'wb') as f:
                f.write(upload_file.getbuffer())
            
            Tumor_Prediction = getResult(file_path)
            print(Tumor_Prediction)
            if Tumor_Prediction==1:
                tumor_diagnosis = "The person has Brain Tumor"
            elif Tumor_Prediction==0:
                tumor_diagnosis = "The person did not have Brain Tumor"
st.markdown(f'### {tumor_diagnosis}')