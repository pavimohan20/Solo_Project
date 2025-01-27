# Web Scraping with Shell Scripting

## Introduction
Web scraping is a method used to extract data from websites. This process can be invaluable when you need to gather information from web pages that do not provide an API. Although web scraping often involves using languages like Python, this exercise focuses on using shell scripting and tools like `curl`, `sed`, `cut`, and `awk` to extract useful information from a webpage.

## Objective
The goal of this project is to create a shell script that extracts laptop information (name, price, and description) from a webshop page. Each laptop’s details should be printed on a single line in the format:

```
Aspire E1-510 | 15.6", Pentium N3520 2.16GHz, 4GB, 500GB, Linux | $306.99
```

## Features
1. **HTML Extraction**
   - Use the `curl` command to fetch the HTML content of the webshop page.

2. **Data Parsing**
   - Utilize tools such as `sed`, `cut`, and `awk` to filter and extract relevant information (laptop name, price, and description) from the HTML.

3. **Formatted Output**
   - Display the extracted information in a clean, readable format, with each laptop’s details on a single line.

## Requirements
- Basic understanding of HTML structure.
- Familiarity with shell scripting and Linux commands.
- Tools: `curl`, `sed`, `cut`, and `awk`.

## Usage
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Make the script executable:
   ```bash
   chmod +x scrap.sh
   ```

3. Run the script:
   ```bash
   ./scrap.sh
   ```

4. The output will display each laptop’s details in the specified format.

## Example Output
```
Aspire E1-510 | 15.6", Pentium N3520 2.16GHz, 4GB, 500GB, Linux | $306.99
HP Pavilion 15 | 15.6", Core i5-1035G1, 8GB, 512GB SSD, Windows 10 | $549.99
Dell Inspiron 14 | 14", Core i7-1165G7, 16GB, 1TB SSD, Ubuntu | $799.99
```

## Tips
- Inspect the webshop page’s HTML structure to identify tags or attributes containing the required data.
- Use `curl` to fetch the page’s source code:
  ```bash
  curl -s <webshop-url> > page.html
  ```
- Experiment with `sed`, `cut`, and `awk` commands to isolate and extract the data.

## Challenges
- Web pages often contain complex and inconsistent HTML structures, which can make parsing challenging.
- Dynamic web pages that rely on JavaScript may not display all content in the HTML fetched by `curl`.

## Future Improvements
- Automate detection of relevant HTML tags or attributes.
- Handle dynamic web pages using tools like `selenium` or headless browsers (e.g., `puppeteer`).
- Migrate to a more robust language like Python for advanced web scraping needs.

## Conclusion
This project demonstrates how to use shell scripting tools to scrape and parse data from a webpage. While shell scripting is not the most efficient method for web scraping, this exercise provides valuable experience with tools like `curl`, `sed`, `cut`, and `awk`. It’s a stepping stone to more advanced scraping techniques in other programming languages.

