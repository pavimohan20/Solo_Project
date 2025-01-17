def extract_movie_data():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from bs4 import BeautifulSoup
    import time
    import random

    url = 'https://letterboxd.com/films/popular/'  # Updated URL to scrape data from Letterboxd

    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    # Handle the dialog box
    try:
        continue_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Continue without supporting us')]")
        continue_button.click()
        time.sleep(2)  # Wait for the dialog to close
    except Exception as e:
        print("Dialog box not found or could not be closed:", e)

    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    # Print the HTML content to debug the issue
    print(soup.prettify())

    # Update the selectors based on the HTML structure of the Letterboxd page
    film_links = []
    titles = []
    synopses = []

    movies = soup.select('li.poster-container')  # Updated selector for movie containers
    if not movies:
        print("No movies found on the page.")
        return [], [], []

    print(f"Found {len(movies)} movies on the page.")  # Log the number of movies found

    for movie in movies:
        title_element = movie.select_one('img[alt]')
        link_element = movie.select_one('a')
        synopsis_element = movie.select_one('p.synopsis')  # Updated selector for synopsis

        if title_element and link_element:
            title = title_element['alt']
            link = 'https://letterboxd.com' + link_element['href']
            synopsis = synopsis_element.text if synopsis_element else 'No synopsis available'

            titles.append(title)
            film_links.append(link)
            synopses.append(synopsis)

            # Print the extracted data for debugging
            print(f"Title: {title}, Link: {link}, Synopsis: {synopsis}")
        else:
            print("Missing title or link element in movie:", movie.prettify())  # Log the movie element if title or link is missing

        # Slow down the frequency of requests to avoid being identified and banned
        time.sleep(random.uniform(1.0, 2.0))

    return film_links, titles, synopses

# Add a call to the function to test it
if __name__ == "__main__":
    film_links, titles, synopses = extract_movie_data()
    print("Film Links:", film_links)
    print("Titles:", titles)
    print("Synopses:", synopses)