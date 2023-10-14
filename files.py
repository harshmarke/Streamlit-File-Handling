# import streamlit as st
# import pandas as pd


# st.subheader('Uploading the CSV File')
# df = st.file_uploader("Upload the CSV file : ", type = ['csv', 'xlsx'])

# st.subheader('Loading the CSV File')
# df = pd.read_csv('Products.csv')
# if df is not None:
#     st.table(df.head())

# st.subheader('Working with Images')
# img_file = st.file_uploader("Upload the Image file : ", type = ['png', 'jpeg'])
# if img_file is not None:
#     st.image(img_file)

# st.subheader('Working with Videos')
# video_file = st.file_uploader("Upload the Video file : ", type = ['mkv', 'mp4'])
# if video_file is not None:
#     st.video(video_file, start_time = 0)

# st.subheader('Working with Audio')
# audio_file = st.file_uploader("Upload the audio file : ", type = ['mp3', 'wav'])
# if audio_file is not None:
#     st.audio(audio_file.read())


import streamlit as st
import pandas as pd

# Uploading the csv file
st.subheader('Uploading the CSV File')
df = st.file_uploader('Upload the csv file', type = ['csv','xlsx'])
# st.table(df)

# Loading the csv file
df = pd.read_csv('./Products.csv')
if df is not None:
    st.table(df.head())


# dealing with images
st.subheader('Dealing with images while uploading')
img_file = st.file_uploader('Upload the image', type = ['png','jpg','jpeg'])
if img_file is not None:
    st.image(img_file)



# working with videos
video_file = st.file_uploader('Upload the video', type = ['mkv','mp4'])
if video_file is not None:
    st.video(video_file,start_time = 0)


# working with audio
audio_file = st.file_uploader('Upload the audio', type = ['mp3'])
if audio_file is not None:
    st.audio(audio_file.read())

