import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image, ImageOps
from pyngrok import ngrok
import cv2
from tensorflow import keras
from img_classification import teachable_machine_classification
import tensorflow as tf

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

def predictImage():
    pass

st.sidebar.title('About HealthRice')
st.sidebar.info('''Rice is the most popular staple in the world. It is a crucial staple for almost 
4 billion people worldwide. Problem is, these crops can experience a variety of diseases. 
These diseases can cause sickness to humans when eaten. While these disease are quite hard to diagnose, HealthRice
is here to help! HealthRice utilizes the power of machine learning in order to diagnose BrownSpot and Hispa. Of course,
HealthRice can also diagnose healthy rice too.''')
st.sidebar.image('assets\display\Buford-FrenchRice.jpg')

st.sidebar.text('')
st.sidebar.title('How to use')
st.sidebar.info('''
    HealthRice is extremely easy to use! Simply hit the "Browse files" button and select your picture! 
    Once your image is uploaded, HealthRice will automatically diagnose the leaf for you!
''')

st.title('HealthRice')

st.image('assets\display\IMG_20190419_170439.jpg', caption='Here is what a healthy rice leaf looks like!', width=200,)
st.image('assets\display\IMG_2993.jpg', caption='Here is what a rice leaf with BrownSpot looks like!', width=200)
st.image('assets\display\IMG_20190419_094254.jpg', caption='This is what a rice leaf with Hispa looks like!', width=200)

st.write('')
uploaded_file = st.file_uploader('Upload an image of rice leaves!', type=['png', 'jpg'])

if uploaded_file is not None:
      image = Image.open(uploaded_file)
      st.image(image, caption='Uploaded Rice Leaf Photo.', use_column_width=True)
      st.write("")
      label = teachable_machine_classification(image, 'keras_model.h5')
      if label == 0:
          st.write("The inputted rice leaf appears to have Brownspot. It is not recommendeed to sell this to the public.")
      elif label == 1:
          st.write("Congratulations! The inputted rice leaf is healthy!")
      else: 
        st.write('The inputted rice leaf unfortunately has Hispa. It is not recommended to sell this to the public. ')