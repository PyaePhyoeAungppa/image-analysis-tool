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

    try:
        # Initialize image captioning pipeline
        image_captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

        # File uploader
        uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

        if uploaded_file is not None:
            try:
                # Read the image
                image_bytes = uploaded_file.read()
                image = Image.open(io.BytesIO(image_bytes))
                
                # Display the image
                st.image(image_bytes, caption='Uploaded Image', use_column_width=True)

                # Process the image
                with st.spinner('Analyzing image...'):
                    # Get image description
                    result = image_captioner(image)
                    description = result[0]['generated_text']

                # Display result
                st.markdown(f'<div class="result">{description}</div>', unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Error processing image: Please try uploading a different image")
                st.exception(e)

    except Exception as e:
        st.error("Error initializing the model. Please try refreshing the page.")
        st.exception(e)

if __name__ == '__main__':
    main()