CS 685 - Data Mining

- **Name**: Aditya Azad
- **Student ID**: 241110002
- **Dept** : Computer Science & Engineering
- **Course**: M.Tech - Y24


#### Overview

- This project uses Python 3.9+ and Streamlit to execute a set of Jupyter notebooks, providing a user interface to run them and view the resulting .csv files.

- Kindly follow the steps below to install dependencies, configure permissions, and launch the Streamlit app.

####  If you are using virtual environment, It's important to name the environment ".venv".

- I have deployed an app for easy evaluation. It doesn't requires any installation [Visit the App](https://adityaazad79-dm-assignment-cs685-app-7bqazr.streamlit.app)
- The app sources the files from this GitHub repo [Github](https://github.com/adityaazad79/DM_Assignment_CS685)

Requirements

	•	Python version: 3.9+
	•	Dependencies: Listed in requirements.txt

Installation

		pip install -r requirements.txt


Ensure executable permissions for the script:
	The script 241110002.sh needs executable permissions to run. Set these by executing:
    
	    chmod +x 241110002.sh
    
Usage

Run the Streamlit App
 : Execute the script to start the app:

        ./241110002.sh
        
If the above shellscript does not work, please run:
        
        streamlit run app.py

Once the script runs, your default web browser should open with the Streamlit app.

Running Notebooks and Viewing Results
    
    1.  In the Streamlit interface, click on "Delete Existing CSV Files".
        - This will delete all the existing csv files.

	2.  Click on “Run All Notebooks”.
        - This will initiate the execution of 10 Jupyter notebooks.
	
	3.  Once the notebooks are processed, the resulting .csv files will be displayed in the browser interface for easy access and review.

Troubleshooting

If the app does not open automatically, try manually opening http://localhost:8501 in your browser.