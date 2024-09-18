import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to convert text to voice using gTTS
def text_to_voice(text, language):
    tts = gTTS(text=text, lang=language, slow=False)
    file_name = f"{language}_audio.mp3"
    tts.save(file_name)
    playsound(file_name)
    os.remove(file_name)  # Optional: Remove the file after playing

# Function to convert voice to text
def voice_to_text(language):
    with sr.Microphone() as source:
        st.write("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        st.write(f"Listening for {language} speech...")

        try:
            # Capture the audio
            audio = recognizer.listen(source)

            # Recognize and convert speech to text
            text = recognizer.recognize_google(audio, language=language)
            st.write(f"Recognized text ({language}): {text}")
            return text
        except sr.UnknownValueError:
            st.write("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            st.write(f"Request error from Google Speech API: {e}")
        except Exception as e:
            st.write(f"Error: {e}")
        return None

# Language code mapping
LANGUAGE_CODES = {
    "English": "en",
    "Tamil": "ta",
    "Kannada": "kn",
    "Telugu": "te",
    "Hindi": "hi"
}

# Function to handle text-to-voice UI
def handle_text_to_voice(language):
    st.write(f"Text to Voice - {language}")
    text_input = st.text_input(f"Enter the text in {language}:")
    
    if st.button("Convert to Voice"):
        if text_input:
            st.write(f"Converting text to voice for {language}: {text_input}")
            text_to_voice(text_input, LANGUAGE_CODES[language])
        else:
            st.write("Please enter some text.")

# Function to handle voice-to-text UI
def handle_voice_to_text(language):
    st.write(f"Voice to Text - {language}")
    
    if st.button("Start Listening"):
        st.write("Listening for your speech...")
        result = voice_to_text(LANGUAGE_CODES[language])
        if result:
            st.write(f"Recognized text ({language}): {result}")

# Main function to handle the app
def main():
    st.title("Voice-to-Text and Text-to-Voice App")

    # Step 1: Ask for operation (Voice-to-Text or Text-to-Voice)
    operation = st.radio("Choose Operation", ("Voice to Text", "Text to Voice"))

    if operation == "Voice to Text":
        st.write("You chose: Voice to Text")

        # Step 2: Language selection for Voice-to-Text
        language = st.selectbox("Select Language", ("English", "Tamil", "Kannada", "Telugu", "Hindi"))
        
        if language:
            handle_voice_to_text(language)

    elif operation == "Text to Voice":
        st.write("You chose: Text to Voice")

        # Step 2: Language selection for Text-to-Voice
        language = st.selectbox("Select Language", ("English", "Tamil", "Kannada", "Telugu", "Hindi"))
        
        if language:
            handle_text_to_voice(language)

if __name__ == "__main__":
    main()
