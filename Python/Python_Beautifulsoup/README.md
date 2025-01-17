# Movie Extractor

This project automates the extraction of movie information from letterboxd.com. It retrieves movie links, titles, and synopses, organizes the data into lists, constructs a DataFrame using pandas, and saves the DataFrame to a CSV file.

## Project Structure

```
movie-extractor
├── src
│   ├── main.py          # Entry point of the application
│   └── utils
│       └── scraper.py   # Contains functions for web scraping
├── requirements.txt      # Lists project dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd movie-extractor
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will initiate the extraction process and save the movie data to a CSV file.

## Running the Script

To run the script, navigate to the `movie-extractor` directory and execute the following command:

```sh
python src/main.py
```

## Dependencies

- pandas
- requests
- BeautifulSoup4
- selenium

## License

This project is licensed under the MIT License.
