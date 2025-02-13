import streamlit as st
from PIL import Image
import io
from transformers import pipeline

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Image Analysis Tool",
        layout="centered"
    )

    # Custom CSS to center elements and set background
    st.markdown("""
        <style>
        .uploadSection {
            display: flex;
            justify-content: center;
            margin-top: 50px;
        }
        .result {
            text-align: center;
            margin-top: 20px;
            padding: 20px;
            font-size: 18px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown("<h1 style='text-align: center;'>Image Analysis Tool</h1>", unsafe_allow_html=True)

    # Initialize image captioning pipeline
    image_captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    # File uploader
    with st.container():
        st.markdown('<div class="uploadSection">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])
        st.markdown('</div>', unsafe_allow_html=True)

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        
        # Center the image
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(image, use_container_width=True)

        # Process the image
        with st.spinner('Analyzing image...'):
            # Convert PIL Image to bytes
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format=image.format)
            img_byte_arr = img_byte_arr.getvalue()
            
            # Get image description
            result = image_captioner(image)
            description = result[0]['generated_text']

        # Display result
        st.markdown(f'<div class="result">{description}</div>', unsafe_allow_html=True)

if __name__ == '__main__':
    main()