# Movie Data Extraction Automation

## Project Overview
This project automates the process of extracting movie data from the Letterboxd website. The extracted data includes:
- Movie titles
- Links to the movie pages
- Synopses (if available)

The extracted information is organized into three lists:
1. **film_links**: Contains URLs of the movies.
2. **titles**: Contains the titles of the movies.
3. **synopses**: Contains the synopses of the movies.

The data is then stored in a structured format using a Pandas DataFrame and saved to a CSV file for further use.

---

## Prerequisites

### Python Environment
Ensure Python 3.6 or later is installed on your system.

### Dependencies
Install the required Python libraries using pip:
```bash
pip install selenium bs4 pandas webdriver-manager
```

### WebDriver
Download and set up the appropriate WebDriver for your browser. For Chrome users, this project uses the `webdriver-manager` library to handle the WebDriver installation automatically.

---

## Setup Instructions

### 1. Clone or Create Script File
Create a Python script or clone the project repository.

### 2. Update URL
The script extracts movie data from the Letterboxd popular films page. Ensure the URL is accurate:
```python
url = 'https://letterboxd.com/films/popular/'
```

### 3. Run the Script
Execute the script from your terminal or preferred IDE:
```bash
python script_name.py
```

### 4. Output
The extracted data is saved in a CSV file named `movie_data.csv` in the same directory as the script. This CSV file contains three columns:
- **Title**: The name of the movie.
- **Link**: The URL of the movie page on Letterboxd.
- **Synopsis**: The description or summary of the movie (if available).

Sample CSV structure:
| Title              | Link                          | Synopsis                  |
|--------------------|-------------------------------|---------------------------|
| Example Movie 1    | https://letterboxd.com/...    | An example synopsis.      |
| Example Movie 2    | https://letterboxd.com/...    | Another example synopsis. |

---

## Notes

- This script uses Selenium to interact with dynamic content and BeautifulSoup to parse the HTML structure.
- The script handles pop-up dialogs on the webpage automatically.
- Randomized delays are introduced between requests to prevent rate-limiting or bans.

---

## License
This project is open-source and available under the MIT License.

