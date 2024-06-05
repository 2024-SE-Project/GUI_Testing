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
    driver.get("http://localhost:3000/dashboard/main")  # Change URL to your application's URL

    # Wait for the main content to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "profile-page"))
    )

    # Verify the presence of the greeting text
    greeting_text = driver.find_element(By.TAG_NAME, "h4").text
    print(f"Greeting Text: {greeting_text}")

    # Scroll down to load more content if needed
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Wait for content to load

    # Verify that posts are present
    posts = driver.find_elements(By.CLASS_NAME, "post")  # Assuming posts have a class named 'post'
    assert len(posts) > 0, "No posts found on the page."

    print(f"Number of posts found: {len(posts)}")

    # Interact with a post (e.g., like a post)
    first_post_like_button = posts[0].find_element(By.CLASS_NAME, "like-button")  # Assuming a like button has a class named 'like-button'
    first_post_like_button.click()
    print("Clicked the like button on the first post.")

    # Wait and verify like count increased
    time.sleep(1)  # Wait for the like action to complete
    first_post_likes = posts[0].find_element(By.CLASS_NAME, "like-count").text  # Assuming like count has a class named 'like-count'
    print(f"First post like count: {first_post_likes}")

    print("Test Passed: All interactions and verifications completed successfully.")

except Exception as e:
    print(f"Test Failed: {e}")

finally:
    # Close the browser window
    driver.quit()
