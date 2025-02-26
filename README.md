# Instagram Carousel to PDF Downloader

This Streamlit application allows users to download images from an Instagram carousel post and compile them into a PDF.

## Features
- Extracts images from an Instagram carousel post.
- Converts the images into a single PDF file.
- Provides a downloadable link to the generated PDF.

## Requirements
Ensure you have the following dependencies installed before running the script:

```bash
pip install -r requirements.txt
```

## How to Run
1. Clone this repository or save the script locally.
2. Install the required dependencies as listed above.
3. Run the Streamlit application with the following command:

```bash
streamlit run app.py
```

4. Enter the Instagram carousel post URL and click the "Download Carousel as PDF" button.
5. Download the generated PDF file.

## Usage
1. Enter a valid Instagram carousel post URL.
2. Click the "Download Carousel as PDF" button.
3. Wait for the processing to complete.
4. Click the "Download PDF" button to save the file.

## Limitations
- Only works with Instagram carousel posts (not single images or videos).
- Requires internet access to fetch Instagram images.
- May break if Instagram changes its API or structure.

## Dependencies
- `streamlit` - For creating the web interface.
- `instaloader` - For scraping Instagram posts.
- `requests` - For downloading images.
- `pillow` - For handling image processing.
- `fpdf` - For generating PDFs.

## Disclaimer
This tool is for educational purposes only. Use it responsibly and ensure compliance with Instagram's terms of service.
