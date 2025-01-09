# LinkedIn-ProfileProspector
This application, LinkedIn ProfileProspector, is a powerful tool for extracting information from LinkedIn profiles. It is designed to scrape user profiles based on your search query and provides insights such as name, location, tags, and about information. The results are displayed in a tabular format and can be downloaded as an Excel file. User can add or remove any addional insights from the profile.

### Key Features
 - Automated Login: Log in to LinkedIn with your credentials securely.
 - Customizable Search: Search for profiles using any keyword or name and select the number of pages to scrape.
 - Profile Data Extraction: Extract information such as name, location, profile tag, and about section.
 - Excel Download: Export scraped data to an Excel file for further analysis.
 - Streamlit Interface: User-friendly interface for easy configuration and operation.

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
