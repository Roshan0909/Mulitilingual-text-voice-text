import speech_recognition as sr
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert text to voice
def text_to_voice(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to convert voice to text
def voice_to_text():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust based on the surrounding noise level
        print("Listening...")

        try:
            # Capture the audio
            audio = recognizer.listen(source)
            # Recognize and convert speech to text
            text = recognizer.recognize_google(audio, language='en-US')  # Specify 'en-IN' for Indian English
            print(f"Recognized text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
        except sr.RequestError as e:
            print(f"Request error from Google Speech API: {e}")
        except Exception as e:
            print(f"Error: {e}")
        return None

# Main function to choose between voice-to-text or text-to-voice
def main():
    while True:
        print("\nChoose an option:")
        print("1. Voice to Text")
        print("2. Text to Voice")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            # Perform voice to text
            print("You chose: Voice to Text")
            result = voice_to_text()
            if result:
                print(f"Recognized text: {result}")
        elif choice == '2':
            # Perform text to voice
            print("You chose: Text to Voice")
            text = input("Enter the text you want to convert to speech: ")
            text_to_voice(text)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
