import openai
import os
from datetime import datetime

# Function to get chat completion from OpenAI
def get_chat_completion(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # Ensure to use the correct model name
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=0.7,
            max_tokens=2000,
            top_p=1
        )
        return response.choices[0].message.content
    except openai.APIError as e:
        return f"An error occurred: {str(e)}"

# Main function to drive the script
def main():
    name = input("What is your name? ")
    profession = input("Enter your profession (e.g., family lawyer, financial advisor): ")
    topic = input("Enter a topic you want to cover in your video (e.g., divorce checklist, court tips): ")
    user_input = f"Create a short video script for a {profession} discussing '{topic}'. Include scene directions and dialogue."
    response = get_chat_completion(user_input)
    print("AI Response:", response)

    # Create a timestamp
    timestamp = datetime.now().strftime("%Y-%d-%m-%H%M")

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Write the response to a file in the same directory as the script
    with open(os.path.join(script_dir, f'{name}_{timestamp}.txt'), 'a') as f:
        f.write(f"Profession: {profession}\n")
        f.write(f"Topic: {topic}\n")
        f.write(f"AI Response: {response}\n\n")

# Set the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client
client = openai.OpenAI()

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
