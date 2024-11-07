###Speech-to-Text Transcription App
This project is a Speech-to-Text transcription application built with Streamlit and the Hugging Face Transformers library. It allows users to upload an MP3 audio file, processes it using a pre-trained automatic speech recognition (ASR) model, and displays the transcribed text on the screen.

##Features
Upload an MP3 audio file.
Process the audio file and transcribe it to text using the AudioSangraha-Audio_to_Text model from Hugging Face.
Display the transcribed text in a text area for easy manual copying.
Model Details
This app uses the AqeelShafy7/AudioSangraha-Audio_to_Text model available on Hugging Face. The model is a pre-trained automatic speech recognition (ASR) model that can transcribe audio to text. It was trained on a variety of audio datasets and supports a wide range of speech recognition tasks.

#Model repository on Hugging Face: AudioSangraha-Audio_to_Text

##Requirements
#To run this app locally, you need to have the following dependencies installed:
Python 3.x
Streamlit
Hugging Face Transformers
Installation

##Clone the repository
git clone <path>
cd speech-to-text-transcription

##Install dependencies
pip install -r requirements.txt

This will install the following dependencies:
streamlit
transformers

##Start the Streamlit app
streamlit run app.py
This will open the app in your default web browser.

##Usage
Upload an Audio File:

In the sidebar of the app, click the "Upload Audio File" button to upload an MP3 audio file.
Process the Audio:

After uploading the audio file, click the "Process Audio" button.
The app will process the audio and display the transcribed text in the main area of the app.
Copy the Transcription:

The transcribed text will appear in a text area. You can manually copy the text by selecting it and pressing Ctrl+C (or Cmd+C on Mac).

##Deployment
This app can be deployed on Streamlit Cloud for online access. To deploy it:

Push the repository to GitHub.
Go to Streamlit Cloud.
Link your GitHub repository.
Streamlit Cloud will automatically install the required dependencies and deploy your app.

