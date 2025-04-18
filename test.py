from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Test cases with different combinations of numbers
test_case = [
    {
        "num1": "7.8",
        "num2": "13"
    },
    {
        "num1": "7",
        "num2": "13.5"
    }
]

# Initialize the WebDriver (make sure ChromeDriver is installed)
driver = webdriver.Chrome()

# Update the path to your local HTML file
driver.get("file:///C:/Users/vinee/Desktop/project-%20root/Js_Testing/add.html")

# Loop through the test cases
for test in test_case:
    # Refresh the page for each test case (optional, but ensures fresh state)
    driver.refresh()

    # Find the input fields and insert values
    driver.find_element(By.ID, "num1").send_keys(test["num1"])
    driver.find_element(By.ID, "num2").send_keys(test["num2"])

    # Click the "Add" button
    driver.find_element(By.CSS_SELECTOR, "button[type='button']").click()

    # Wait for the result to appear
    time.sleep(3)

    # Capture the result from the <p> element with id "res"
    res = driver.find_element(By.ID, "res").text
    print(res)

# Close the browser after the test
driver.quit()
