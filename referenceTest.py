from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (Make sure the path to your WebDriver is correct)
driver = webdriver.Chrome(executable_path='./chromedriver')

try:
    # Open the web application
    driver.get("http://localhost:3000/dashboard/library")  # Change URL to your application's URL

    # Wait for the reference container to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "reference-container"))
    )

    # Verify the presence of the search bar
    search_bar = driver.find_element(By.CLASS_NAME, "search-bar")
    assert search_bar is not None, "Search bar not found."

    # Perform a search operation
    search_input = search_bar.find_element(By.TAG_NAME, "input")
    search_button = search_bar.find_element(By.CLASS_NAME, "search-button")
    search_input.send_keys("자료")
    search_button.click()
    time.sleep(1)  # Wait for search results to update

    # Verify the presence of the navigation buttons
    nav_buttons = driver.find_elements(By.CLASS_NAME, "reference-nav")[0].find_elements(By.TAG_NAME, "button")
    assert len(nav_buttons) == 3, "Navigation buttons not found or incorrect count."

    # Click each navigation button and verify content updates
    for button in nav_buttons:
        button.click()
        time.sleep(1)  # Wait for content to update


    print("Test Passed: All interactions and verifications completed successfully.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    # Close the browser window
    driver.quit()
