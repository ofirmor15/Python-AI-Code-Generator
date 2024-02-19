import openai
import os
import subprocess
import random
import platform

openai.api_key = 'OPENAI_API_KEY'

# Remove common introductory phrases from the response
def clean_code(code):
    phrases_to_remove = ["Here's a Python code", "The following Python code", "```python", "```"]
    for phrase in phrases_to_remove:
        code = code.replace(phrase, "")
    return code.strip()

# Execute the generated Python code and return the error message if any
def execute_generated_code():
    try:
        subprocess.run(["python3.11", "generatedcode.py"], check=True)
        print("Code creation completed successfully!")
        return None  # No errors
    except subprocess.CalledProcessError as e:
        return str(e)  # Return the error message

# Generate Python code based on the user's request
def generate_python_code(user_input):
    try:
        full_prompt = (
            "You are an expert python developer. Create the following program:\n"
            + user_input
            + ". Make sure to include standard python indentation. Do not write any explanations,"
             + "how me the code itself."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the gpt-3.5-turbo model for chat
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant who generates Python code with standard indentation and without any explanations."
                },
                {
                    "role": "user",
                    "content": full_prompt
                }
            ]
        )

        # Extracting the Python code from the response
        code_content = response['choices'][0]['message']['content']

        return clean_code(code_content)

    except Exception as e:
        return str(e)

 # Generate Python unit tests for the code   
def generate_python_tests(user_input):
    try:
        test_prompt = (
            "You are an expert python developer. Based on the following Python program," 
            + "create unit tests using the unittest framework."
            + " Include tests that check the logic of the program with 5 different inputs and expected outputs:\n"
            + user_input
            + "\nAlso, make sure to include standard python indentation and do not write any explanations or Notes,"
            + " just the test code."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant who generates Python unittest code based on the given program."
                },
                {
                    "role": "user",
                    "content": test_prompt
                }
            ]
        )

        test_code_content = response['choices'][0]['message']['content']
        return clean_code(test_code_content)

    except Exception as e:
        return str(e)

# Chat with GPT-3 to generate Python code    
def chat_with_gpt3(prompt):
    try:
        # Constructing a prompt that explicitly asks for only Python code
        full_prompt = "Python code: " + prompt

        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the gpt-3.5-turbo model for chat
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant who provides Python code solutions without any additional comments or explanations."
                },
                {
                    "role": "user",
                    "content": full_prompt
                }
            ]
        )

        # Extracting only the Python code from the response
        response_content = response['choices'][0]['message']['content']

        # Write the code to a file
        with open('generatedcode.py', 'a') as file:
            file.write(response_content + "\n")

        return clean_code(response_content)

    except Exception as e:
        return str(e)
    
def get_random_program_idea():
    # List of random program ideas
    PROGRAMS_LIST = [
    "create a program that creates a simple game of tic tac toe",
    "a program that checks if a number is a palindrome",
    "A program that finds the kth smallest element in a given binary search tree.",
    "A program that creates a calculator",
    "A program that creates a to-do list"
]
    return random.choice(PROGRAMS_LIST)

# Main program
if __name__ == "__main__":
    attempt_count = 0
    max_attempts = 5
    user_input = input("Tell me, which program would you like me to code for you? If you don't have an idea, just press enter: ")

    while attempt_count < max_attempts:
        if not user_input.strip():
            user_input = get_random_program_idea()
            print(f"I have chosen to code:\n{user_input}")

        # Generate Python code based on the user's request or the random idea
        code_response = generate_python_code(user_input)
        cleaned_code = clean_code(code_response)
        with open('generatedcode.py', 'w') as file:
            file.write(cleaned_code + "\n")

        # Generate Python unit tests for the code
        test_response = generate_python_tests(cleaned_code)
        if test_response.strip():
            with open('generatedcode.py', 'a') as file:
                file.write("\n\n# Unit Tests\n" + test_response)

        # Execute the code and handle potential errors
        error_message = execute_generated_code()
        if error_message is None:
            break  # No errors, break the loop

        print(f"Error running generated code! Error: {error_message}")
        # Update the user_input to include the error for correction by ChatGPT
        user_input += f"\n\n# Error encountered: {error_message}\n# Please fix the code."
        attempt_count += 1

    if attempt_count >= max_attempts:
        print("Code generation FAILED")

    # Open the generated Python file as if it was double-clicked
    file_path = os.path.abspath('generatedcode.py')
    try:
        os_type = platform.system()
        if os_type == "Windows":
            subprocess.call(["start", file_path], shell=True)
        elif os_type == "Darwin":  # Darwin is the system name for macOS
            subprocess.call(["open", file_path])
        elif os_type == "Linux":
            subprocess.call(["xdg-open", file_path])
        else:
            print(f"Unsupported operating system: {os_type}")
    except Exception as e:
        print("Error occurred while opening the file:", e)
