from seleniumwire import webdriver # type: ignore
from selenium.webdriver.chrome.service import Service as ChromeService # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.common.by import By # type: ignore

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    seleniumwire_options={
        'proxy': {
            'http': 'http://0prhlxwj1f3kmudcqm7das:dj5e2nxyevdfgslluhnj9@localhost:8888',  # Replace with your Scrapoxy credentials
            'verify_ssl': True,
            'ca_cert': 'D:/scrapoxy-ca.crt',  # Use forward slashes for the path
        },
    }
)

driver.get('https://fingerprint.scrapoxy.io')

print(driver.find_element(By.TAG_NAME, 'body').text)

driver.close()
