import streamlit as st
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
import pandas as pd
import os
import subprocess


# List of notebook paths
NOTEBOOKS = [
    "1/1.ipynb",
    "2/2.ipynb",
    "3/3.ipynb",
    "4/4.ipynb",
    "5/5.ipynb",
    "6/6.ipynb",
    "7/7.ipynb",
    "8/8.ipynb",
    "9/9.ipynb",
    "10/10.ipynb"
]

# List of CSV file paths and descriptions
CSV_FILES = [
    # ("1/1_Yearly_absolute_change.csv", "This file contains yearly absolute change data."),
    # ("1/1_Yearly_percentage_change.csv", "This file shows yearly percentage change."),
    # ("1/5_Hi_lo_Abs_Pct_Month_change.csv", "This file highlights high and low absolute percentage changes by month."),
    ("1/1_Yearly_absolute_change.csv","Q1 : Yearly absolute change in incoming tourists. - Visualisation available"),
    ("1/1_Yearly_percentage_change.csv","Q1 : Yearly percentage change in incoming tourists. - Visualisation available"),
    ("1/2_Monthly_absolute_change.csv","Q1 : Monthly absolute change in incoming tourists. - Visualisation available"),
    ("1/2_Monthly_percent_change.csv","Q1 : Monthly precentage change in incoming tourists. - Visualisation available"),
    ("1/3_Hi_lo_Abs_Pct_Year_change.csv","Q1 : Yearly Highest and Lowest Change. - Visualisation available"),
    ("1/4_Change_from_prev_month.csv","Q1 : Change from Previous Month. - Visualisation available"),
    ("1/5_Hi_lo_Abs_Pct_Month_change.csv","Q1 : Month with Highest Positive and Negative Absolute and Percentage Change. - Visualisation available"),
    ("2/1_Lean_Peak_Months.csv","Q2 : Yearly Lean and Peak months in terms of fee received. - Visualisation available"),
    ("2/2_Countrywise_Quarter_Data.csv","Q2 : Country-wise lean and peak quarter in terms of no of visits visit"),
    ("2/2_continentwise_Quarter_Data.csv","Q2 : Continent-wise lean and peak quarter in terms of no of visits visit"),
    ("3/1_continent_age_distribution.csv","Q3. Yearly Continent-wise Age_category_wise Distribution Probabilities. - Visualisation available"),
    ("3/1_continent_distribution.csv","Q3. Yearly Continent-wise Distribution Probabilities for all 3 Features Combined. - Visualisation available"),
    ("3/1_continent_gender_distribution.csv","Q3. Yearly Continent-wise Genderwise Distribution Probabilities. - Visualisation available"),
    ("3/1_continent_purpose_distribution.csv","Q3. Yearly Continent-wise Purpose-wise Distribution Probabilities. - Visualisation available"),
    ("3/1_country_age_distribution.csv","Q3. Yearly Country-wise Age_category_wise Distribution Probabilities."),
    ("3/1_country_distribution.csv","Q3. Yearly Country-wise Distribution Probabilities for all 3 Features Combined"),
    ("3/1_country_gender_distribution.csv","Q3. Yearly Country-wise Genderwise Distribution Probabilities."),
    ("3/1_country_purpose_distribution.csv","Q3. Yearly Country-wise Purpose-wise Distribution Probabilities."),
    ("3/1_overall_age_distribution.csv","Q3. Yearly Age_categorical Distribution Probabilities"),
    ("3/1_overall_distribution.csv","Q3. Yearly Overall Distribution Probabilities for all 3 Features Combined"),
    ("3/1_overall_gender_distribution.csv","Q3. Yearly genderwise Distribution Probabilities"),
    ("3/1_overall_purpose_distribution.csv","Q3. Yearly purposewise Distribution Probabilities"),
    ("3/2_continent_min_max_entropy.csv","Q3. Continent-wise Year-wise Minimum and Maximum Entropy for all 3 Features"),
    ("3/2_country_min_max_entropy.csv","Q3. Country-wise Year-wise Minimum and Maximum Entropy for all 3 Features"),
    ("3/2_overall_min_max_entropy.csv","Q3. Overall Minimum and Maximum Entropy for all 3 Features"),
    ("4/1_Yearly_absolute_change.csv","Q4 : Yearly absolute change in outgoing tourists. - Visualisation available"),
    ("4/1_Yearly_percentage_change.csv","Q4 : Yearly percentage change in outgoing tourists. - Visualisation available"),
    ("4/2_Monthly_absolute_change.csv","Q4 : Monthly absolute change in outgoing tourists. - Visualisation available"),
    ("4/2_Monthly_percent_change.csv","Q4 : Monthly percentage change in outgoing tourists. - Visualisation available"),
    ("4/3_Hi_lo_Abs_Pct_Year_change.csv","Q4 : Yearly Highest and Lowest Change. - Visualisation available"),
    ("4/4_Change_from_prev_month.csv","Q4 : Change from Previous Month. - Visualisation available"),
    ("4/5_Hi_lo_Abs_Pct_Month_change.csv","Q4 : Month with Highest Positive and Negative Absolute and Percentage Change. - Visualisation available"),
    ("5/2_Countrywise_Quarter_Data.csv","Q5 : No data is available for part 1 of question.\n\nQ5 : Country-wise lean and peak quarter in terms of no of departures"),
    ("5/2_continentwise_Quarter_Data.csv","Q5 : Continent-wise lean and peak quarter in terms of no of departures"),
    ("6/1_overall_dvf_distribution.csv","Q6 : Overall Yearly Domestic vs Foreign Distribution Probability"),
    ("6/1_overall_mode_distribution.csv","Q6 : Overall Yearly Mode-wise Distribution Probability"),
    ("6/1_overall_port_distribution.csv","Q6 : Overall Yearly Port-wise Distribution Probability"),
    ("6/2_dvf_min_max_entropy.csv","Q6 : State-wise Domestic and Foreign Entropy"),
    ("6/2_dvf_overall_min_max_entropy.csv","Q6 : Overall Maximum and Minimum entropy for Domestic and Foreign tourists"),
    ("6/2_mode_min_max_entropy.csv","Q6 : Mode-wise Minimum and Maximum Entropy Year"),
    ("6/2_mode_overall_min_max_entropy.csv","Q6 : Overall Mode Year for Minimum and Maximum Entropy"),
    ("6/2_port_min_max_entropy.csv","Q6 : Port-wise Minimum and Maximum Entropy Year"),
    ("6/2_port_overall_min_max_entropy.csv","Q6 : Overall Port Year for Minimum and Maximum Entropy"),
    ("7/Difference_Continentwise.csv","Q7 : Continent-wise Differenece of incoming and outgoing tourists. Note - Incoming and outgojng data for year 2014 was the same in the give dataset. Somewhat similar applies to year 2017 too."),
    ("7/Difference_Countrywise.csv","Q7 : Country-wise Differenece of incoming and outgoing tourists. Note - Incoming and outgojng data for year 2014 was the same in the give dataset. Somewhat similar applies to year 2017 too."),
    ("8/1_top5_negative_country.csv","Q8 : Top 5 countries with lowest (incoming - outgoing) tourists value. - Visualisation available"),
    ("8/1_top5_positive_country.csv","Q8 : Top 5 countries with highest (incoming - outgoing) tourists value. - Visualisation available"),
    ("8/2_Orderd_Continent_balance.csv","Q8 : Ordered continents in terms of balance per year. - Visualisation available"),
    ("9/1_ffill_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'Purpose of Visit' using Forward Fill"),
    ("9/1_knn_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'Purpose of Visit' using KNN"),
    ("9/1_linear_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'Purpose of Visit' using Linear Interpolation"),
    ("9/1_mean_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'Purpose of Visit' using Mean Imputation"),
    ("9/1_rolling_mean_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'Purpose of Visit' using Time-Series Imputation with Rolling Mean"),
    ("9/1_seasonal_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'Purpose of Visit' using Seasonal Decomposition with Interpolation"),
    ("9/2_ffill_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'Total No of Incoming Tourists per Continents' using Forward Fill"),
    ("9/2_knn_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'Total No of Incoming Tourists per Continents' using KNN"),
    ("9/2_linear_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'Total No of Incoming Tourists per Continents' using Linear Interpolation"),
    ("9/2_mean_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'Total No of Incoming Tourists per Continents' using Mean Imputation"),
    ("9/2_rolling_mean_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'Total No of Incoming Tourists per Continents' using Time-Series Imputation with Rolling Mean"),
    ("9/2_seasonal_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'Total No of Incoming Tourists per Continents' using Seasonal Decomposition with Interpolation"),
    ("9/3_knn_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'No of Domestic Tourists per state' using KNN"),
    ("9/3_linear_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'No of Domestic Tourists per state' using Linear Interpolation"),
    ("9/3_mean_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'No of Domestic Tourists per state' using Mean Imputation"),
    ("9/3_seasonal_imputed_scores_with_threshold.csv","Q9 : Score for imputed values of 'No of Domestic Tourists per state' using Seasonal Decomposition with Interpolation"),
    ("9/4_df_comparison.csv","Q9 : Difference between the Imputation Techniques Used"),
    ("10/1_Gender_Average_difference_across_all_countries.csv","Q10 : Here is a Gender-wise and Total Absolute Differnence for all countries between the mean values the available years(except 2020 and 2021) and covid years(2020 and 2021)"),
    ("10/1_Gender_Avg_Largest_Pct_Change.csv","Q10 : Overall Percentge change and Country with Largest Percentage change for Male and Female"),
    ("10/1_Gender_Percentage_Change_for_All_Countries.csv","Q10 : Here is a Country-wise Gender-wise Percentage Differnence between the mean values the available years(except 2020 and 2021) and covid years(2020 and 2021)"),
    ("10/1_Gender_Top_5_countries_with_largest_differences_in_2020.csv","Q10 : Top 5 Countries (with Gender count) with Highest Differnece in no of tourists for year 2020"),
    ("10/1_Gender_Top_5_countries_with_largest_differences_in_2021.csv","Q10 : Top 5 Countries (with Gender count) with Highest Differnece in no of tourists for year 2021"),
    ("10/1_Gender_Yearwise_Avg_Difference.csv","Q10 : Here is a Country-wise Gender-wise and Total Absolute Differnence between the mean values the available years(except 2020 and 2021) and covid years(2020 and 2021)"),
    ("10/3_Age_Average_Percentage_Changes_by_Age_Group.csv","Q10 : Age-wise percentage change in no of tourists for all Age Groups"),
    ("10/3_Age_Top_Country_per_year.csv","Q10 : For all Age Group the country which had highest percentage change during covid years."),
    ("10/3_Age_per_Country.csv","Q10 : Here is a Country-wise Age-Group-wise Percentage Differnence between the mean values the available years(except 2020 and 2021) and covid years(2020 and 2021)"),
    ("10/4_Dom_Foreign_Statewise_pct.csv","Q10 : State-wise Percentage change in Domestic vs Foreign Tourists for Covid years i.e. 2020 and 2021"),
    ("10/4_Extreme_State_change.csv","Q10 : State/UT with Highest and Lowest Percentage change in Domestic and Foreign tourists for covid years i.e 2020 and 2021")
    # ("10/4_Overall_Change_in_Dom_Foreign_Tourist.csv","")
    # Add more CSV file paths and descriptions as needed
]

def run_notebook(notebook_path):
    """
    Executes a Jupyter notebook and returns the updated notebook object.
    """
    with open(notebook_path, "r") as f:
        notebook = nbformat.read(f, as_version=4)
    
    # Set up the preprocessor with a kernel timeout of 600 seconds (10 minutes)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(notebook, {'metadata': {'path': os.path.dirname(notebook_path)}})

def run_all_notebooks():
    """
    Runs all notebooks in the NOTEBOOKS list and returns a message.
    """
    for notebook_path in NOTEBOOKS:
        st.write(f"Running {notebook_path}...")
        run_notebook(notebook_path)
    return "All notebooks have completed running. Now you may view the CSVs below"

def delete_csv_files():
    try:
        # Run the shell command
        subprocess.run("find . -type d -name '.venv' -o -type f -name '*.csv' -delete", shell=True, check=True)
        st.success("CSV files deleted successfully!")
    except subprocess.CalledProcessError as e:
        st.error(f"Error occurred: {e}")


# Streamlit app
st.title("CS 685 : Data Mining Assignment")

st.subheader('Delete All The Cached/Saved CSV Files')

if st.button('Delete Existing CSV Files'):
    delete_csv_files()

st.subheader('Run All 10 Notebooks')
# Section to run all notebooks
if st.button("Run All Notebooks"):
    with st.spinner("Running 10 notebooks, please wait..."):
        completion_message = run_all_notebooks()
    st.success(completion_message)

# Section to display CSV files with individual show/hide buttons and descriptions
st.header("CSV File Viewer")

# Loop through each CSV file, display the description, and add an expander for the table
for csv_file, description in CSV_FILES:
    # Display the description text above the expander
    st.write(f"**{description}**")
    with st.expander(f"View {os.path.basename(csv_file)}"):
        try:
            df = pd.read_csv(csv_file)
            st.write(df)  # Display the DataFrame in Streamlit
        except Exception as e:
            st.error(f"Failed to load {csv_file}: {e}")