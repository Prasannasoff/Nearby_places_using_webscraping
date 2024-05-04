from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup
import requests
def get_nearby_hospitals(place_name):
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/maps")

    try:
        # Wait for the search box to be visible
        search_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "searchboxinput")))
        
        # Search for the place on Google Maps
        search_box.clear()
        search_box.send_keys(place_name)
        search_box.send_keys(Keys.RETURN)
        
        # Wait for the search results to load completely
        time.sleep(20)
        # Get the current URL after search
        current_url = driver.current_url
        print(current_url)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')
        
        hospital_links = soup.find_all('a', class_='hfpxzc')
        
        # Iterate over each <a> tag to extract hospital name and address
        # for link in hospital_links:
        #     # Extract hospital name from 'aria-label' attribute
        #     hospital_name = link['aria-label']
        #     print(hospital_name)
        compart = soup.find_all('div', class_='Z8fK3b')
        #name=compart.find_all('div',class_='qBF1Pd fontHeadlineSmall ')
        # Iterate over each <div> tag to extract additional information
        for div in compart:
            # Extract text content from the <div> tag
            name_element = div.find('div', class_='qBF1Pd fontHeadlineSmall')
            hospital_name = name_element.text.strip()
            div_text = div.get_text(separator=' ', strip=True)
            print(div_text)
            # address_element = div.find('div', class_='W4Efsd')
            # hospital_address = address_element.text.strip()
            rating_element = div.find('span', class_='MW4etd')
           
            print("Hospital Name:", hospital_name)
            # print("Address:", hospital_address)
            print("Rating:", rating_element)
            
            print()
      #  print(soup)
        compart2=soup.find_all('div',class_='W4Efsd')
        for i in compart2:
            hospital_address = i.text.strip()
            print("Address",hospital_address)
            print()
    
    finally:
        # Close the browser
        driver.quit()

# Example usage
place = input("Enter the name of the place: ")
place_name = place + ' hospital'  # Assuming 'hospital' needs to be appended for searching hospitals
get_nearby_hospitals(place_name)



# from selenium import webdriver
# from bs4 import BeautifulSoup

# url = 'https://www.google.com/maps/search/erode+hospital/@11.2641874,77.4542895,12z/data=!3m1!4b1?entry=ttu'


# driver = webdriver.Chrome()
# driver.get(url)




# driver.quit()





