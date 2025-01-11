AI Agent Project
Overview
This project is a simple command-line AI Agent with the following features:

Weather Information:
Fetches the current weather for any city using the OpenWeatherMap API.
To-Do List Management:
Add, view, and remove tasks from a to-do list.
The project is modular, with each feature implemented in its own file:

weather.py: Handles weather-related functionality.
todo.py: Handles to-do list functionality.
main.py: Integrates everything and provides a user-friendly interface.
Project Structure
bash
Copy code
AI_AGENT_PROJECT/
├── __pycache__/          # Auto-generated cache files (can be ignored)
├── .env                  # Stores the OpenWeatherMap API key
├── main.py               # Entry point of the program
├── todo.py               # To-do list functionality
├── weather.py            # Weather-related functionality
└── README.md             # Project documentation
Setup Instructions
1. Prerequisites
Python 3.7 or higher installed on your system.
Internet connection (required to fetch weather data).
2. Clone or Download the Project
Clone the repository or download the ZIP file and extract it:
bash
Copy code
git clone <repository-url>
cd AI_AGENT_PROJECT
3. Create a Virtual Environment
Create and activate a virtual environment for the project:
bash
Copy code
python -m venv ai_agent_env
ai_agent_env\Scripts\activate   # On Windows
source ai_agent_env/bin/activate  # On macOS/Linux
4. Install Dependencies
Install the required Python libraries:
bash
Copy code
pip install requests python-dotenv
5. Get an OpenWeatherMap API Key
Sign up at OpenWeatherMap.
Go to the API Keys section in your account and generate an API key.
6. Create a .env File
In the root directory (AI_AGENT_PROJECT/), create a file named .env:
makefile
Copy code
OPENWEATHER_API_KEY=your_actual_api_key_here
Replace your_actual_api_key_here with your OpenWeatherMap API key. Do not include spaces or quotes.
How to Run
Activate your virtual environment:

bash
Copy code
ai_agent_env\Scripts\activate   # On Windows
source ai_agent_env/bin/activate  # On macOS/Linux
Run the program:

bash
Copy code
python main.py
Follow the on-screen instructions to:

Fetch weather information for any city.
Add, view, or remove tasks from your to-do list.
Common Issues and Debugging
1. .env File Not Loading
Symptom: API key is None or not found.
Fix:
Ensure the .env file is in the same directory as weather.py and main.py.
Ensure the .env file contains:
makefile
Copy code
OPENWEATHER_API_KEY=your_actual_api_key
Ensure load_dotenv() is called at the start of the program.
2. Invalid API Key
Symptom: 401 Unauthorized when fetching weather data.
Fix:
Verify your API key on OpenWeatherMap.
Ensure it is activated (some keys take a few minutes to activate).
Regenerate the key if necessary.
3. Invalid City Name
Symptom: 404 Not Found when fetching weather data.
Fix:
Check the city name spelling.
Try adding the country code (e.g., London,GB).
4. ModuleNotFoundError
Symptom: Errors like ModuleNotFoundError: No module named 'dotenv'.
Fix:
Ensure the virtual environment is activated.
Install dependencies:
bash
Copy code
pip install requests python-dotenv
5. General Debugging
Add debug statements to check variable values, such as:
python
Copy code
print(f"Loaded API Key: {api_key}")
How It Works
Weather Functionality (weather.py)
Loads the API key from the .env file.
Fetches weather data from OpenWeatherMap using the city name.
Returns the weather description and temperature.
To-Do List Functionality (todo.py)
Uses a simple in-memory list to manage tasks.
Functions:
add_task(task): Adds a task to the list.
remove_task(task): Removes a task from the list.
view_tasks(): Displays all tasks.
Main Program (main.py)
Provides a user interface to interact with the weather and to-do list functionalities.
Lets users choose from a menu of options.
Extending the Project
Add More Features:

Integration with other APIs (e.g., News, Time, or Currency Conversion).
Persistent storage for the to-do list (e.g., save to a file or database).
Improve the Interface:

Create a GUI using tkinter or a web interface using Flask.
Error Handling:

Add more robust error handling for invalid input or API errors.
Contact and Contributions
If you encounter any issues or have suggestions, feel free to open an issue or submit a pull request.