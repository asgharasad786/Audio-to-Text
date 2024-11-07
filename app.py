import streamlit as st
from transformers import pipeline

# Load the speech recognition pipeline
pipe = pipeline("automatic-speech-recognition", model="AqeelShafy7/AudioSangraha-Audio_to_Text")

# Streamlit app layout
st.title("Speech to Text Transcription")

# Sidebar layout for uploading audio and processing it
st.sidebar.title("Upload Audio for Transcription")

# File uploader widget for the audio file in the sidebar
audio_file = st.sidebar.file_uploader("Upload Audio File (MP3 format)", type=["mp3"])

# Button to process the audio file
if st.sidebar.button("Process Audio"):
    if audio_file is not None:
        # Define a path for the uploaded file (within the app's directory)
        upload_path = "uploaded_audio.mp3"

        # Save the uploaded file to the defined path
        with open(upload_path, "wb") as f:
            f.write(audio_file.getbuffer())

        # Provide the file path to the pipeline
        result = pipe(upload_path)

        # Display the transcription result in the main area
        transcribed_text = result['text']
        st.text_area("Transcribed Text", transcribed_text, height=300)
    else:
        st.error("Please upload an audio file to process.")
