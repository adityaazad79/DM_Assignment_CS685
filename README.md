CS 685 - Data Mining

Overview

This project uses Python 3.9+ and Streamlit to execute a set of Jupyter notebooks, providing a user interface to run them and view the resulting .csv files. Follow the steps below to install dependencies, configure permissions, and launch the Streamlit app.

Requirements

	•	Python version: 3.9
	•	Dependencies: Listed in requirements.txt

Installation

	1.	pip install -r requirements.txt


2.	Ensure executable permissions for the script:
	The script 241110002.sh needs executable permissions to run. Set these by executing:
4.	    chmod +x 241110002.sh
    
Usage

Run the Streamlit App
 : Execute the script to start the app:

        ./241110002.sh

Once the script runs, your default web browser should open with the Streamlit app.

Running Notebooks and Viewing Results

	1.	In the Streamlit interface, click on “Run All Notebooks”. This will initiate the execution of 10 Jupyter notebooks.
	
	2.	Once the notebooks are processed, the resulting .csv files will be displayed in the browser interface for easy access and review.

Troubleshooting

If the app does not open automatically, try manually opening http://localhost:8501 in your browser.