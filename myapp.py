import streamlit as st
from openai import OpenAI
from PIL import Image
import io
import requests

client = OpenAI(api_key="sk.......")

st.title('MyGPT')

# Create two columns
col1, col2 = st.columns(2)


def get_openai_response(prompt):
    response  = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"You are a 3 year old kid"},
            {"role":"user","content":prompt}
        ]

    )
    return response.choices[0].message.content

def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        n=1,
        size="256x256"
    )
    image_url = response.data[0].url
    return image_url

# Define a function to display the image
def display_image(image_url):
    image = Image.open(io.BytesIO(requests.get(image_url).content))
    st.image(image)

# Text generation column
with col1:
    st.header("Text Generation")
    text_input = st.text_input("Enter your text prompt:", "")
    if st.button("Generate Text"):
        response = get_openai_response(text_input)
        st.write("Response:")
        st.write(response)


# Image generation column
with col2:
    st.header("Image Generation")
    image_input = st.text_input("Enter your image prompt:", "")
    if st.button("Generate Image"):
        image_url = generate_image(image_input)
        display_image(image_url)
