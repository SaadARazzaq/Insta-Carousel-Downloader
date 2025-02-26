import streamlit as st
import instaloader
import os
import tempfile
import requests
from PIL import Image
from fpdf import FPDF

def download_insta_carousel(insta_url):
    """Download images from an Instagram carousel post and compile them into a PDF."""
    
    temp_dir = tempfile.mkdtemp()
    loader = instaloader.Instaloader()

    try:
        shortcode = insta_url.split("/")[-2]
    except IndexError:
        return None, "Invalid Instagram URL format."

    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
    except Exception as e:
        return None, f"Failed to load post: {e}"

    if post.typename != 'GraphSidecar':
        return None, "This is not a carousel post."

    pdf = FPDF()
    sidecar_nodes = list(post.get_sidecar_nodes())

    for index, slide in enumerate(sidecar_nodes):
        if slide.is_video:
            continue 

        image_url = slide.display_url
        image_path = os.path.join(temp_dir, f"slide_{index}.jpg")

        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(image_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)

            try:
                img = Image.open(image_path)
                img = img.convert('RGB')
                pdf.add_page()
                pdf.image(image_path, x=10, y=10, w=190)
                img.close()
            except Exception as e:
                return None, f"Error processing slide {index + 1}: {e}"
            finally:
                os.remove(image_path)

    pdf_file = os.path.join(temp_dir, f"{post.owner_username}_carousel.pdf")
    pdf.output(pdf_file)

    return pdf_file, None

st.title("📸 Instagram Carousel to PDF Downloader")

insta_url = st.text_input("Enter the Instagram post URL:")

if st.button("Download Carousel as PDF"):
    if insta_url:
        st.info("Processing... Please wait.")
        pdf_path, error = download_insta_carousel(insta_url)
        
        if pdf_path:
            st.success("Download Ready! Click below to save the PDF.")
            with open(pdf_path, "rb") as file:
                st.download_button(
                    label="Download PDF",
                    data=file,
                    file_name=os.path.basename(pdf_path),
                    mime="application/pdf"
                )
        else:
            st.error(f"Error: {error}")
    else:
        st.warning("Please enter a valid Instagram URL.")
