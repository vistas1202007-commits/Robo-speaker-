# ============================================================
# Project  : Robo Speaker - Text to Speech Application
# Author   : Shivani Sharma
# Language : Python
# Library  : pyttsx3 (works offline, no internet needed)
# ============================================================

import pyttsx3  # Text-to-speech library

def initialize_engine():
    """
    Initialize the TTS engine and set properties.
    Returns the configured engine object.
    """
    engine = pyttsx3.init()  # Start the TTS engine

    # Set speech rate (default is 200, lower = slower)
    engine.setProperty('rate', 150)

    # Set volume (0.0 to 1.0)
    engine.setProperty('volume', 1.0)

    # Get available voices
    voices = engine.getProperty('voices')

    # Set voice: index 0 = Male, index 1 = Female (Windows)
    engine.setProperty('voice', voices[1].id)  # Female voice

    return engine


def speak_text(engine, text):
    """
    Convert given text to speech.
    
    Parameters:
        engine : pyttsx3 engine object
        text   : string to be spoken
    """
    if text.strip() == "":
        print("⚠️  Please enter some text to speak.")
        return

    print(f"\n🔊 Speaking: {text}\n")
    engine.say(text)        # Queue the text
    engine.runAndWait()     # Play the audio


def save_to_audio(engine, text, filename="output.mp3"):
    """
    Save spoken text to an audio file.
    
    Parameters:
        engine   : pyttsx3 engine object
        text     : string to be saved
        filename : output audio file name (default: output.mp3)
    """
    engine.save_to_file(text, filename)
    engine.runAndWait()
    print(f"✅ Audio saved as '{filename}'")


def main():
    """
    Main function - runs the Robo Speaker application.
    Provides a simple menu-driven interface.
    """
    print("=" * 45)
    print("     🤖 ROBO SPEAKER - Text to Speech App")
    print("=" * 45)

    # Initialize TTS engine once
    engine = initialize_engine()

    while True:
        print("\nOptions:")
        print("  1. Speak Text")
        print("  2. Save Text as Audio File")
        print("  3. Exit")

        choice = input("\nEnter your choice (1/2/3): ").strip()

        if choice == '1':
            # Get text from user and speak it
            text = input("Enter text to speak: ")
            speak_text(engine, text)

        elif choice == '2':
            # Get text and save as audio file
            text = input("Enter text to save as audio: ")
            filename = input("Enter filename (e.g. hello.mp3): ").strip()
            if filename == "":
                filename = "output.mp3"  # Default filename
            save_to_audio(engine, text, filename)

        elif choice == '3':
            print("\n👋 Goodbye! Exiting Robo Speaker...")
            break

        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")


# Entry point of the program
if __name__ == "__main__":
    main()
