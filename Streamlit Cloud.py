# Deployment options#
# Now that we’ve gone through the steps of developing an application,
# it’s time to deploy it so users can interact with it.
#
# There are several options to deploy applications, including the following:
#
# Heroku
# AWS
# Streamlit Cloud
# In this lesson, we learn to deploy applications using Streamlit Cloud.

# Streamlit Cloud#
# Connect to the service#
# When we first access Streamlit Cloud, we see the page shown in the image above.
#
# You need a Github account where our repository (repo) will be situated to deploy on Streamlit Cloud.
# This is the advisable way to sign up for the service.
#
# The first time we do this, we go through the process of connecting our GitHub account to the service.
#
# The repo should contain the Python script file and a requirements.txt file containing
# packages needed to build and run our application successfully.
#
# Streamlit Cloud’s Community Tier allows the deployment of just one private repo and unlimited public repos.
#
# Required files#
# As a demonstration, we use the following script for the application to be deployed.
# This script sets up a basic photo editor application that lets users upload an image
# and perform basic manipulation on it:

import streamlit as st
import numpy as np
from PIL import Image

st.title("Super Basic Photo Editor")


def display_figures(img1, img2):
    fig1_left, fig2_right = st.columns(2)
    with fig1_left:
        st.markdown("### Original image")
        st.image(img1)
    with fig2_right:
        st.markdown("### Processed image")
        st.image(img2)


image_file = st.sidebar.file_uploader("Upload an image file", type=["jpg", "png", "tif"])

if image_file is not None:
    input_image = Image.open(image_file)

    effect = st.sidebar.selectbox("Select the type of image manipulation.",
                                  ["Rotate Image", "Flip Image", "Resize"])

    if effect == "Rotate Image":
        angle = st.sidebar.select_slider("Select the angle of rotation", [0, 90, 180, 270, 360])
        output_image = input_image.rotate(angle)

    if effect == "Flip Image":
        mirror_choice = st.sidebar.radio("Choose  how to flip the image",
                                         ["Horizontally", "Vertically"])
        if mirror_choice == "Horizontally":
            output_image = input_image.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            output_image = input_image.transpose(Image.FLIP_TOP_BOTTOM)

    if effect == "Resize":
        scale_factor = st.sidebar.slider("Select the percentage size", 5, 10, 6)
        output_image = input_image.resize((input_image.width // scale_factor, input_image.height // scale_factor))

    if st.button("Process image"):
        display_figures(input_image, output_image)