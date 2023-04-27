# This script imports the os and openai modules
import os
import openai

# The API key is set to the contents of the "this.txt" file
API_KEY = open("this.txt", "r").read()

# The API key is set as the default key for OpenAI API calls
openai.api_key = API_KEY

# This function takes an input file and reads its content
def add_comments_to_file(input_file):
    with open(input_file, 'r') as f:
        code = f.read()

    # An API call is made to OpenAI's chatbot for generating comments for the code
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "you are going to be passed some code from a file, you will read through this code and add comments to each function, function call, and variable inside the file and return only the code with comments"},
        {"role": "user", "content": code}
    ]
    )

    # The response from the API call is extracted and the generated comments are stored
    assistant_response = response['choices'][0]['message']['content']

    # The generated comments are stripped of newline and whitespace characters
    commented_code = assistant_response.strip("\n").strip()

    # The output file is created using the input file name with "COMM_" prefix and the generated comments are written to it
    output_file = "COMM_" + os.path.basename(input_file)

    with open(output_file, 'w') as f:
        f.write(commented_code)

    # Prints a message of completion
    print("All Done!")

# The script prompts the user for the input file name, which is then passed to the add_comments_to_file() function
if __name__ == "__main__":
    this_file = input("What is the file name?: ")
    add_comments_to_file(this_file)