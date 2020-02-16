import streamlit as st
import os
import numpy as np
import pandas as pd
import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from PIL import Image
import streamlit as st 


st.title("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type="png")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    st.write(type(uploaded_file))
    authenticator = IAMAuthenticator('pROvzH_YxoX5akTMjSOWXh9sWyAAdXjKbkOWYLs3VnRS')
    visual_recognition = VisualRecognitionV3(
        version='2018-03-19',
        authenticator=authenticator
    )

    visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/')

    with open(str(uploaded_file), 'rb') as images_file:
        classes = visual_recognition.classify(
            images_file = images_file,
            threshold='0.6',
            classifier_ids='DefaultCustomModel_1389832688').get_result()
    # filename = file_selector()
    st.write('You selected `%s`' % uploaded_file)
    st.write('The predicted type of lung disease is`%s`' % classes['images'][0]['classifiers'][0]['classes'][0]['class'])


# def file_selector(folder_path='.'):
#     filenames = os.listdir(folder_path)
#     selected_filename = st.file_uploader('Please upload a X-Ray picture of lung', filenames)
#     if not selected_filename:
#         selected_filename = '00030780_000.png'
#     uploaded_file = os.path.join(folder_path, selected_filename)
#     image = Image.open(uploaded_file)
#     st.image(image, caption=None, width=None, use_column_width=False, clamp=False, channels='RGB', format='png')



# authenticator = IAMAuthenticator('pROvzH_YxoX5akTMjSOWXh9sWyAAdXjKbkOWYLs3VnRS')
# visual_recognition = VisualRecognitionV3(
#     version='2018-03-19',
#     authenticator=authenticator
# )

# visual_recognition.set_service_url('https://api.us-south.visual-recognition.watson.cloud.ibm.com/')

# with open(display, 'rb') as images_file:
#         classes = visual_recognition.classify(
#             images_file = images_file,
#             threshold='0.6',
#             classifier_ids='DefaultCustomModel_1389832688').get_result()
# # filename = file_selector()
# st.write('You selected `%s`' % display)
# st.write('The predicted type of lung disease is`%s`' % classes['images'][0]['classifiers'][0]['classes'][0]['class'])
