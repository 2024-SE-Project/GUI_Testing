from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (Make sure the path to your WebDriver is correct)
driver = webdriver.Chrome(executable_path='./chromedriver')

try:
    # Open the web application
    driver.get("http://localhost:3000/dashboard/myteam")  # Change URL to your application's URL

    # Wait for the team content to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "my-team"))
    )

    # Verify the presence of the team header
    header = driver.find_element(By.CLASS_NAME, "team-header").text
    assert "나의 팀" in header, "Team header not found or incorrect."

    # Verify the team details
    details = driver.find_element(By.CLASS_NAME, "team-details")
    professor_team_name = details.find_element(By.TAG_NAME, "h3").text
    rc = details.find_element(By.XPATH, ".//p[contains(text(), 'RC:')]").text
    semester = details.find_element(By.XPATH, ".//p[contains(text(), '학기:')]").text
    member_count = details.find_element(By.XPATH, ".//p[contains(text(), '멤버 수:')]").text

    # Verify the "탈퇴하기" button is present
    leave_team_button = details.find_element(By.CLASS_NAME, "leave-team").text
    assert leave_team_button == "탈퇴하기", "Leave team button is not present or incorrect."

    print("Test Passed: All elements are present and correct.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    # Close the browser window
    driver.quit()
