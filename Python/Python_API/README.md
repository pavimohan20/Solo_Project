# Fetch and Save Last Ten News Articles

## Project Overview
This project demonstrates how to fetch the latest ten news articles from a news source and store the details in a structured CSV file. The news articles are retrieved using the News API, and the project focuses on providing an easy way to access and store relevant information for further analysis or sharing.

---

## Prerequisites

### Python Dependencies
- Python 3.6 or later
- `requests`
- `csv`

Install the required dependencies using pip:
```bash
pip install requests
```

### API Key
You will need an API key from [News API](https://newsapi.org). Sign up for a free API key and replace the placeholder in your script with your actual API key.

---

## Setup Instructions

### 1. Clone the Repository
Clone this project or create a new Python script file to integrate the solution.

### 2. Add Your API Key
Update the script with your News API key in the following format:
```python
key = "your_api_key_here"
```

### 3. Define News Source
Modify the `url` variable to specify the desired news source. For example:
```python
url = "https://newsapi.org/v2/top-headlines?sources=lequipe&apiKey=" + key
```

---

## Output
The output of the script will be a CSV file named `last_ten_news.csv`, containing the following columns:
- **Title**: The headline of the news article
- **Description**: A brief summary of the news article
- **URL**: A direct link to the full article
- **Published At**: The publication date and time of the article

Sample output:
| Title                               | Description                | URL                            | Published At       |
|-------------------------------------|----------------------------|--------------------------------|--------------------|
| Example News Title 1               | Example description 1      | https://example.com/news1      | 2025-01-01T12:00Z |
| Example News Title 2               | Example description 2      | https://example.com/news2      | 2025-01-01T13:00Z |

---

## How to Run
1. Ensure you have Python installed and the necessary dependencies (`requests` and `csv`) in your environment.
2. Run the script in your terminal or preferred IDE:
   ```bash
   python script_name.py
   ```
3. Check the output CSV file (`last_ten_news.csv`) in the same directory as the script.

---

## Notes

- This script is designed for educational purposes. Ensure compliance with [News API Terms of Use](https://newsapi.org/terms).
- The script can be extended to include additional fields or support other output formats like Excel or JSON.

---

## License
This project is open-source and available under the MIT License.

