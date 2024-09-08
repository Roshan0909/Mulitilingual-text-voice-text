import speech_recognition as sr
from gtts import gTTS
import os

# Initialize recognizer
recognizer = sr.Recognizer()

# Function to convert Tamil text to voice using gTTS
def text_to_voice(text, language='ta'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("tamil_audio.mp3")
    # Play the generated speech
    os.startfile("tamil_audio.mp3")  # This works for Windows

# Function to convert voice to Tamil text
def voice_to_text():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for Tamil speech...")

        try:
            # Capture the audio
            audio = recognizer.listen(source)

            # Recognize and convert Tamil speech to text
            text = recognizer.recognize_google(audio, language='ta-IN')  # 'ta-IN' for Tamil (India)
            print(f"Recognized text (Tamil): {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Request error from Google Speech API: {e}")
        except Exception as e:
            print(f"Error: {e}")
        return None

# Main function to choose between voice-to-text or text-to-voice in Tamil
def main():
    while True:
        print("\nChoose an option:")
        print("1. Voice to Tamil Text")
        print("2. Tamil Text to Voice")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            # Perform voice to Tamil text
            print("You chose: Voice to Tamil Text")
            result = voice_to_text()
            if result:
                print(f"Recognized text (Tamil): {result}")
        elif choice == '2':
            # Perform Tamil text to voice
            print("You chose: Tamil Text to Voice")
            text = input("Enter the Tamil text you want to convert to speech: ")
            text_to_voice(text, language='ta')
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
