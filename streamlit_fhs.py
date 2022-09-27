import streamlit as st
import os

from gtts import gTTS
from io import BytesIO, StringIO

st.title("Text to speech")
text_or_document = st.selectbox("Input Text or Document?", ['Text', 'Document'])
if text_or_document == 'Text':
    text = st.text_input("Enter text:")
else:
    text = st.file_uploader("Upload file here (.txt only)", type=['txt'])

    if text:
        stringio = StringIO(text.getvalue().decode("utf-8"))
        string_data = stringio.read()
        text = string_data

def text_to_speech(text):
    tts = gTTS(text, lang='en', slow=False)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    return fp

if st.button("convert"):
    tts = text_to_speech(text)
    st.markdown(f"## Your audio:")
    st.audio(tts, format="audio/mp3", start_time=0)