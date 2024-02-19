# Python AI Code Generator

## Overview
This program is designed to automate the generation of Python code based on user input or randomly selected programming tasks.
It leverages the OpenAI API to generate Python code and unit tests for the given task. The program then attempts to execute the generated code,
providing feedback on any errors encountered during execution.
This automation aims to streamline the process of coding simple Python programs and testing them, making it an invaluable tool for both learning and rapid prototyping.

## Features
- **Code Generation:** Automatically generates Python code based on a predefined set of tasks or user input.
- **Unit Test Creation:** Generates unit tests for the produced code, ensuring functionality is as expected.
- **Execution and Feedback:** Attempts to execute the generated Python code, providing error feedback for debugging.
- **Multi-Attempt Execution:** Makes multiple attempts to generate and execute code, refining based on error feedback. If the program fails for 5 iterations to generate a functioning code that passes the unit tests it generates itelf as well - the program will admit it failed the task and stop.

## Requirements
- Python 3.11 or higher
- OpenAI API Key (for accessing GPT models)
- Internet connection (for API requests)

## Setup
1. **Clone the Repository:**
   git clone https://github.com/ofirmor15/Python-AI-Super-Code-Generator.git
2. **Install Dependencies:**
Ensure you have Python 3.11 or higher installed. Then, install the required Python packages:
  pip install openai
3. **Configure API Key:**
Set your OpenAI API key in the program by replacing `'KEY'` in the `openai.api_key = 'KEY'` line with your actual API key.

## Usage
To run the program, navigate to the directory containing the script and execute it with Python:
  python main.py
Upon running, the program will prompt you to enter a program idea. If you don't have one, simply press enter, and the program will select a random task to generate code for.


## Acknowledgments
- OpenAI for providing the GPT API used in this project.
- The Python community for continuous support and resources.

---

