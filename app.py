from email import message
from lib2to3.pgen2 import token
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image, ImageOps
from pyngrok import ngrok
import cv2
from tensorflow import keras
from img_classification import machine_classification
import tensorflow as tf
from twilio.rest import Client

client = Client('**********************', '**************************')

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.sidebar.title('About HealthRice')
st.sidebar.info('''Rice is the most popular staple in the world. It is a crucial food for almost 
4 billion people worldwide. Problem is, these crops can experience a variety of diseases. 
These diseases can cause sickness to humans when eaten. While these disease are quite hard to diagnose, HealthRice
is here to help! HealthRice utilizes the power of machine learning in order to diagnose BrownSpot and Hispa. Of course,
HealthRice can also diagnose healthy rice too.''')
st.sidebar.image('assets\display\Buford-FrenchRice.jpg')

st.sidebar.text('')
st.sidebar.title('How to use')
st.sidebar.info('''
    HealthRice is extremely easy to use! Simply hit the "Browse files" button and select your picture! 
    Once your image is uploaded, HealthRice will automatically diagnose the leaf for you! Additionally, if you 
    would like to be further reminded through an SMS, all you have to do is input your phone number above the "Browse files" button!
''')

st.title('HealthRice')

st.image('assets\display\IMG_20190419_170439.jpg', caption='Here is what a healthy rice leaf looks like!', width=200,)
st.image('assets\display\IMG_2993.jpg', caption='Here is what a rice leaf with BrownSpot looks like!', width=200)
st.image('assets\display\IMG_20190419_094254.jpg', caption='This is what a rice leaf with Hispa looks like!', width=200)

st.write('')
st.write('')
st.write('')

phoneNumber = st.text_input(label='Enter in your phone number to be reminded of your leaves!'),

uploaded_file = st.file_uploader('Upload an image of rice leaves!', type=['png', 'jpg'])

if uploaded_file is not None:
      image = Image.open(uploaded_file)
      st.image(image, caption='Uploaded Rice Leaf Photo.', use_column_width=True)
      st.write("")
      label = machine_classification(image, 'keras_model.h5')
      if label == 0:
          st.write("The inputted rice leaf appears to have Brownspot. It is not recommendeed to sell this to the public.")
          if (phoneNumber is not None):
            message = client.messages.create(
                body='Your leaf appears to have BrownSpot!',
                from_ = '*********', 
                to=phoneNumber
            )
            print(message.body)
      elif label == 1:
          st.write("Congratulations! The inputted rice leaf is healthy!")
          if (phoneNumber is not None):
            message = client.messages.create(
                body='Congrats! Your leaf is healthy!',
                from_ = '*********', 
                to=phoneNumber
            )
            print(message.body)
      else: 
        st.write('The inputted rice leaf unfortunately has Hispa. It is not recommended to sell this to the public. ')
        if phoneNumber is not None:
            message = client.messages.create(
                body = 'The inputted rice leaf unfortunately appears to have Hispa', 
                from_ = '*********',
                to = phoneNumber
            )
            print(message.body)
