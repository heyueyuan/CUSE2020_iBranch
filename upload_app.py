import streamlit as st
import os

def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.file_uploader('Please upload a X-Ray picture of lung', filenames)
    return os.path.join(folder_path, selected_filename)


#streamlit.image(image, caption=None, width=None, use_column_width=False, clamp=False, channels='RGB', format='JPEG')

display = file_selector()
#filename = file_selector()
filename = 100
st.write('You selected `%s`' % filename)

st.write('The probability of this lung could be infected by coronvirus is `%s`' % filename)

