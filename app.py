import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
from pyngrok import ngrok
import cv2
import tensorflow as tf
def predictImage():
    pass

st.sidebar.title('About HealthRice')
st.sidebar.info('''Rice is the most popular staple in the world. It is a crucial staple for almost 
4 billion people worldwide. Problem is, these crops can experience a variety of diseases. 
These diseases can cause sickness to humans when eaten. While these disease are quite hard to diagnose, HealthRice
is here to help! HealthRice utilizes the power of machine learning in order to diagnose BrownSpot and Hispa. Of course,
HealthRice can also diagnose healthy rice too.''')
st.sidebar.image('assets\Buford-FrenchRice.jpg')

st.sidebar.text('')
st.sidebar.title('How to use')
st.sidebar.info('''
    HealthRice is extremely easy to use! Simply hit the "Upload Image" button and select your picture
    of rice! Once your image is uploaded, simply hit 'Diagnose' and wait for your results to show!
''')

st.title('HealthRice')

upload = st.file_uploader('Upload a CT scan image', type=['png', 'jpg'])

if upload is not None:
  file_bytes = np.asarray(bytearray(upload.read()), dtype=np.uint8)
  opencv_image = cv2.imdecode(file_bytes, 1)
  opencv_image = cv2.cvtColor(opencv_image,cv2.COLOR_BGR2RGB) # Color from BGR to RGB
  img = Image.open(upload)
  st.image(img,caption='Uploaded Image',width=300)
  if(st.button('Predict')):
    model = tf.keras.models.load_model(model_path)
    x = cv2.resize(opencv_image,(100,100))
    x = np.expand_dims(x,axis=0)    
    y = model.predict(x)
    ans=np.argmax(y,axis=1)
    if(ans==0):
      st.title('COVID')
    elif(ans==1):
      st.title('Healthy')
    else:
      st.title('Other Pulmonary Disorder')