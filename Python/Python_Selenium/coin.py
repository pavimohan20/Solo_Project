from seleniumwire import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from selenium.common.exceptions import TimeoutException # type: ignore
from bs4 import BeautifulSoup # type: ignore
import time
import random
from webdriver_manager.chrome import ChromeDriverManager # type: ignore

url = "https://www.leboncoin.fr/sports_hobbies/1536839557.htm/"

# List of user agents to rotate
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    # Add more user agents as needed
]

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")

# Configure Scrapoxy proxy
proxy = "http://Project:Project#123@localhost:8888"  # Replace with your Scrapoxy proxy address and credentials
chrome_options.add_argument(f'--proxy-server={proxy}')

# Here, we create instance of Chrome WebDriver using webdriver-manager.
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.implicitly_wait(30)
driver.get(url)

# Wait for the "Accepter & Fermer" button to be present and click it
accept_button = WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Accepter & Fermer")]'))
)
accept_button.click()

# Pause to allow manual CAPTCHA solving
input("Please solve the CAPTCHA and press Enter to continue...")

# Introduce a random delay
time.sleep(random.uniform(2, 5))

# Wait for the element to be present
try:
    button = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH, '//div[@data-reactid="269"]'))
    )
    button.click()
except TimeoutException:
    print("Element not found or blocked.")
    driver.quit()
    exit()

# Introduce another random delay
time.sleep(random.uniform(2, 5))

# Now use BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.prettify())

driver.close()
for elem in soup.find_all("a", attrs={"data-qa-id": "adview_number_phone_contact"}):
    print(elem.text)