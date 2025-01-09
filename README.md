# LinkedIn-ProfileProspector
LinkedIn ProfileProspector is a versatile tool designed to automate the process of extracting data from LinkedIn profiles. With this application, you can streamline the task of gathering information about LinkedIn users based on your search criteria. Whether for research, networking, or recruitment purposes, this tool simplifies the process by automating login, search, and data collection. The results are displayed in an organized tabular format and can be downloaded as an Excel file for further analysis. Users have the flexibility to customize the fields of data they wish to extract.

### Key Features
 - Seamless Login Automation: Automatically log in to LinkedIn using your credentials in a secure manner.
 - Intelligent Search Automation: Conduct searches on LinkedIn based on specific keywords or names and automate scrolling through multiple pages of results.
 - Dynamic Data Collection: Automatically extract essential profile details, such as name, location, profile tag, about section, and more. Users can customize the extracted data fields.
 - Export Results Effortlessly: Download the collected data as an Excel file for easy sharing and further processing.
 - Streamlined User Experience: Enjoy a user-friendly interface built with Streamlit, making it simple to configure and execute tasks.
 - Pagination Automation: Automatically navigate through multiple pages of LinkedIn search results.
### Why Use LinkedIn ProfileAutomator?
 - Save time by automating repetitive tasks such as logging in, searching, and scrolling.
 - Simplify data collection for research, recruitment, or lead generation.
 - Easily customize and expand the data fields you want to gather from profiles.
 - Export data in an accessible format for integration with other tools or workflows.

## Prerequisites
 - Python 3.7 or later: Ensure Python is installed on your system.
 - Libraries: Install required Python libraries using the following command:
  ```bash
  pip install pandas streamlit selenium openpyxl webdriver-manager
  ```
 - Chrome Browser: Make sure Google Chrome is installed.
 - WebDriver: This script uses webdriver_manager to manage the Chrome WebDriver.

## How to Use
 - Clone or download this repository.
 - Install the necessary dependencies listed in the requirements.txt file by running ((in terminal)):
  ```bash
  pip install -r requirements.txt
  ```
 - Run the Streamlit application (in terminal):
  ```bash
  streamlit run app.py
  ```
 - Provide the required details:
    - LinkedIn email and password.
    - The search query or name to scrape.
    - The number of result pages to scrape.
 - Click on the Scrape Profiles button to start the process.
 - View and download the results as an Excel file.

## File Structure
 - app.py: Main script for the Streamlit interface and scraper functionality.
 - requirements.txt: List of dependencies to install.

## Important Notes
 - LinkedIn Policies: Use this tool responsibly and ensure compliance with LinkedIn's terms of service. Excessive scraping may lead to account restrictions or bans.
 - Login Credentials: Be cautious while providing login credentials. Ensure the security of your account by not sharing your credentials with others.

 - Example Output
   The extracted data will include the following columns:
    - Name
    - Location
    - Tagline
    - About
    - Profile URL

## License
 - This script is provided as-is for educational and non-commercial use. Make sure to comply with all applicable legal and ethical guidelines.
