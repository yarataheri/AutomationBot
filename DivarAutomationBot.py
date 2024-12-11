from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

social_name = "6182648397"
post_code = "5231457854" 
deposit = "100000000"    
rent = "10000000"       
meterage = "100"           
driver = webdriver.Chrome()
driver.maximize_window()

user_phone_number = "09123456789"

driver.get("https://divar.ir")

try:
    location_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )
    location_input.send_keys("تهران")
    time.sleep(2) 

    suggestion = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'تهران')]"))
    )
    ActionChains(driver).move_to_element(suggestion).click().perform()


    diwar_man_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'دیوار من')]"))
    )
    ActionChains(driver).move_to_element(diwar_man_button).click().perform()
    print("Clicked on 'دیوار من' successfully.")


    vorood_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'ورود')]"))
    )
    ActionChains(driver).move_to_element(vorood_button).click().perform()
    print("Clicked on 'ورود' successfully.")

    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='tel']"))
    )
    phone_input.send_keys(user_phone_number)
    print("Phone number entered successfully.")

    print("Waiting for 20 seconds for the user to enter the verification code...")
    time.sleep(20)

    sabt_agahi_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'ثبت آگهی')]"))
    )
    ActionChains(driver).move_to_element(sabt_agahi_button).click().perform()
    print("Clicked on 'ثبت آگهی' successfully.")

    search_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, "input"))
    )
    search_box.clear()
    search_box.send_keys("اجاره آپارتمان")
    print("Entered 'اجاره آپارتمان' in the search box.")
    time.sleep(2)

    first_search_suggestion = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='kt-search-result-row__title' and text()='اجارهٔ آپارتمان']"))
    )
    ActionChains(driver).move_to_element(first_search_suggestion).click().perform()
    print("Clicked on the first search suggestion for 'اجاره آپارتمان'.")

   
    try:

        neighborhood_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "Location___Input-neighborhood"))
        )
        driver.execute_script("arguments[0].click();", neighborhood_dropdown)
        print("Neighborhood dropdown opened.")

      
        time.sleep(2)

        chittgar_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'چیتگر')]"))
        )
        chittgar_option.click()
        print("Selected the 'چیتگر' option from the neighborhood dropdown.")
    
    except Exception as e:
        print(f"Error while selecting neighborhood: {e}")


    photo_directory = r"E:\env-1\photo"

    try:

        photo_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )

    
        valid_extensions = ('.jpg', '.jpeg', '.png')
        uploaded_files = set()
        for filename in os.listdir(photo_directory):
            file_path = os.path.join(photo_directory, filename)
            if (os.path.isfile(file_path) and 
                filename.lower().endswith(valid_extensions) and 
                os.path.getsize(file_path) > 0 and 
                filename not in uploaded_files):
                
                photo_input.send_keys(file_path)
                uploaded_files.add(filename)
                print(f"Uploading photo: {filename}")

                time.sleep(5)

        print("All photos uploaded successfully.")

    except Exception as e:
        print(f"Error while uploading photos: {e}")

    try:
        national_id_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'کد ملّی مالک')]/following::input[1]"))
        )
        national_id_label.send_keys(social_name)
        print("Entered National ID successfully.")

    except Exception as e:
        print(f"Error while entering National ID: {e}")

    try:
        postal_code_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'کد پستی ملک')]/following::input[2]"))
        )
        postal_code_label.send_keys(post_code)
        print("Entered Postal Code successfully.")
        
    except Exception as e:
        print(f"Error while entering Postal Code: {e}")
    
    try:
        deposit_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'ودیعه')]/following::input[1]"))
        )
        deposit_label.send_keys(deposit)
        print("Entered Deposit successfully.")
        
    except Exception as e:
        print(f"Error while entering Deposit: {e}")


    try:
        rent_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'اجارهٔ ماهانه')]/following::input[1]"))
        )
        rent_label.send_keys(rent)
        print("Entered Rent successfully.")
        
    except Exception as e:
        print(f"Error while entering Rent: {e}")

    try:
        meterage_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'متراژ')]/following::input[1]"))
        )
        meterage_label.clear()
        meterage_label.send_keys(meterage)
        print(f"Entered Meterage (متراژ) successfully: {meterage}")

    except Exception as e:
        print(f"Error while entering Meterage (متراژ): {e}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    time.sleep(5)
    driver.quit()
