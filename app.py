from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_nearby_hospitals(place_name):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/maps")

    try:
        
        search_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "searchboxinput")))
        
        
        search_box.clear()
        search_box.send_keys(place_name)
        search_box.send_keys(Keys.RETURN)

      
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "Z8fK3b")))
        
      
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')


        #list to store the values
        hospitals = []

       
        compart = soup.find_all('div', class_='Z8fK3b')
        def address():
            hospital_address = ""  
            compart2 = soup.find_all('div', class_='W4Efsd')
            for i in compart2:
                hospital_address = i.text.strip() + "\n"  
            return hospital_address

            
        for div in compart:
            name_element = div.find('div', class_='qBF1Pd fontHeadlineSmall')
            hospital_name = name_element.text.strip()
            rating_element = div.find('span', class_='MW4etd')
            rating = rating_element.text.strip() if rating_element else 'Not available'
            address_element = div.find('div', class_='W4Efsd')
            hospitals.append({
                'name': hospital_name,
                'rating': rating,
                'address':address()
                
            })
        



        return hospitals

    finally:
        driver.quit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_hospitals', methods=['POST'])
def get_hospitals():
    place = request.form['place']
    place_name = place + ' hospital'
    hospitals = get_nearby_hospitals(place_name)
    return render_template('result.html', hospitals=hospitals)

if __name__ == '__main__':
    app.run(debug=False)
