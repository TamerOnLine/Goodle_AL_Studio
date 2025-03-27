import os

import google.generativeai as genai
from dotenv import load_dotenv

def main():
    """
    Loads the Gemini API key from environment variables, configures the Generative AI client,
    and interacts with the user in a continuous chat loop using the Gemini model.
    """
    # Load environment variables from .env file
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")

    # Configure the API key for Generative AI
    genai.configure(api_key=api_key)

    # Test API connectivity and model functionality
    try:
        models = genai.list_models()
        print("API key is working! Available models:")
        for model in models:
            print(" -", model.name)

        # Create a chat session with the Gemini model
        model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
        chat = model.start_chat()

        print("\nYou can now chat with the Gemini model. Type 'exit' to quit.")
        while True:
            user_input = input("\nYou: ")
            if user_input.strip().lower() == 'exit':
                print("Exiting chat. Goodbye!")
                break

            response = chat.send_message(user_input)
            print("Gemini:", response.text)

    except Exception as e:
        print("An error occurred while connecting to the Gemini API:")
        print(e)


if __name__ == "__main__":
    main()
