import pandas as pd
import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import io



st.title("LinkedIn Profile Scraper")
st.write("Please provide following details to proceed:")

pages = st.number_input("How many pages of results do you want to scrape?", min_value=1, max_value=100,value=1)
search_query = st.text_input("Enter name/character you want to search:")
mail = st.text_input("Enter your LinkedIn email:")
psd = st.text_input("Enter your LinkedIn password:", type="password")

if st.button("Scrape Profiles"):

    website = "https://www.linkedin.com/home"
    driver = webdriver.Chrome()
    driver.get(website)
    driver.maximize_window()

    def login(email,password):
        try:
            driver.find_element(By.XPATH, '//input[@id="session_key"]').send_keys(email)
            driver.find_element(By.XPATH, '//input[@id="session_password"]').send_keys(password)
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            WebDriverWait(driver, 10).until(EC.url_changes(website))
        except Exception as e:
            st.error(f"Error during login: {e}")
            st.stop()

    login(mail,psd)

    def Search(name):
        Find= driver.find_element(By.XPATH, '//*[@id="global-nav-typeahead"]/input')
        Find.send_keys(name)
        Find.send_keys(Keys.RETURN)
    Search(search_query)

    time.sleep(5)

    buttons = driver.find_elements(By.CSS_SELECTOR, '#search-reusables__filters-bar > ul > li > button')
    for button in buttons:
        if button.text == "People":
            button.click()
            break
    
    time.sleep(5)
    
    profileLinks = []
    for i in range(1,pages+1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(5)
        mainSearchCon = driver.find_element(By.CLASS_NAME, "reusable-search__entity-result-list")
        lis = mainSearchCon.find_elements(By.CSS_SELECTOR,".reusable-search__result-container")
        for li in lis:
            div= li.find_element(By.CSS_SELECTOR,".entity-result__title-text")
            anchor = div.find_element(By.TAG_NAME,"a")
            profileLinks.append(anchor.get_attribute('href'))
        driver.find_element('xpath','//button[@class="artdeco-pagination__button artdeco-pagination__button--next artdeco-button artdeco-button--muted artdeco-button--icon-right artdeco-button--1 artdeco-button--tertiary ember-view"]').click()
        
    data_list = []

    for url in profileLinks:
        driver.get(url)
        time.sleep(5)
        try:
            mainDiv = driver.find_element(By.CSS_SELECTOR,".pv-top-card")
            name = mainDiv.find_element(By.TAG_NAME,"h1").text
            tag = mainDiv.find_element(By.CSS_SELECTOR,"div.text-body-medium.break-words").text
            loc = mainDiv.find_element(By.XPATH,'//*[@id="profile-content"]/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[2]/span[1]').text
            try:    
                ul= mainDiv.find_element(By.CSS_SELECTOR,"ul.pv-top-card--list").find_element(By.CSS_SELECTOR,"span.t-bold").text
            except:
                ul=""
        except:
            continue
        try:
            about = driver.find_element(By.CSS_SELECTOR, '#profile-content > div > div:nth-child(2) > div > div > main > section:nth-child(n) > div:nth-child(3) > div > div > div > span:nth-child(1)').text                  
        except:
            about=""


        profile_data = {
            'Name': name,
            'Location': loc,
            'Tag': tag,
            'About': about,
            'Url': url,
        }
        data_list.append(profile_data)

    df = pd.DataFrame(data_list)
    st.write("Scraping finished!")
    st.dataframe(df)

    if not df.empty:
        st.write("Download Excel File")
        excel_file = io.BytesIO()
        df.to_excel(excel_file, index=False, header=True)
        excel_file.seek(0)
        st.download_button(label="Download Excel", data=excel_file, file_name='profile_data.xlsx', key='profile_data_excel')

    driver.quit()
    
