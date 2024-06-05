from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Initialize the WebDriver (Make sure the path to your WebDriver is correct)
driver = webdriver.Chrome(executable_path='./chromedriver')

try:
    # Open the web application
    driver.get("http://localhost:3000/dashboard/photo") 

    # Wait for the photo studio content to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "photo-studio"))
    )

    # Verify the presence of the photo header
    header = driver.find_element(By.CLASS_NAME, "photo-header").text
    assert "사진첩" in header, "Photo header not found or incorrect."

    # Verify the initial photo is displayed
    photo = driver.find_element(By.CLASS_NAME, "photo-item").find_element(By.TAG_NAME, "img")
    assert photo.get_attribute("src") == "https://storage.googleapis.com/raonz_post_image/cat.jpg", "Initial photo URL is incorrect."

    # Click the next button and verify the photo changes
    next_button = driver.find_element(By.CLASS_NAME, "right")
    next_button.click()
    time.sleep(1)  # Wait for the photo to change
    photo = driver.find_element(By.CLASS_NAME, "photo-item").find_element(By.TAG_NAME, "img")
    assert photo.get_attribute("src") == "https://storage.googleapis.com/raonz_post_image/cat1.jpg", "Next photo URL is incorrect."

    # Click the previous button and verify the photo changes back
    prev_button = driver.find_element(By.CLASS_NAME, "left")
    prev_button.click()
    time.sleep(1)  # Wait for the photo to change
    photo = driver.find_element(By.CLASS_NAME, "photo-item").find_element(By.TAG_NAME, "img")
    assert photo.get_attribute("src") == "https://storage.googleapis.com/raonz_post_image/cat.jpg", "Previous photo URL is incorrect."

    # Verify the download button is present and click it
    download_button = driver.find_element(By.CLASS_NAME, "download-button")
    download_button.click()
    time.sleep(1)  # Wait for the download to initiate


    print("Test Passed: All interactions and verifications completed successfully.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    # Close the browser window
    driver.quit()
