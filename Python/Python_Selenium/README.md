# Web Scraping with Selenium and BeautifulSoup

## Project Overview
This project demonstrates how to use Selenium in Python to automate interactions with a webpage and retrieve specific information, such as a phone number. The script also integrates BeautifulSoup to parse the HTML source after the dynamic content has been loaded. Additionally, the project uses Docker and Scrapoxy for scaling requests and includes certificate handling for secure connections.

---

## Prerequisites

### Python Dependencies
- Python 3.6 or later
- Selenium
- BeautifulSoup4
- Requests

Install these dependencies using pip:
```bash
pip install selenium beautifulsoup4 requests
```

### Browser and WebDriver
- Firefox browser
- Geckodriver for Firefox

Ensure that Geckodriver is installed and available in your system's PATH.

### Docker and Scrapoxy
- Docker installed on your machine
- Scrapoxy image pulled from Docker Hub

### Certificates
- Ensure that the required certificates for Scrapoxy are downloaded and properly installed.

---

## Setup Instructions

### 1. Install Selenium WebDriver
Download and install the Geckodriver executable for Firefox. Ensure it is in your PATH so Selenium can locate it.

### 2. Configure Scrapoxy
Start a Scrapoxy instance in Docker by running:
```bash
docker run -d -p 8888:8888 -v /path/to/certificates:/certificates scrapoxy
```
Replace `/path/to/certificates` with the directory containing your certificates.

### 3. Download Certificates
To use Scrapoxy with HTTPS, you need valid certificates. Follow these steps:


![Download Certificates](path/to/screenshot_download_certificates.png)

### 4. Integrate with Docker
Set up Scrapoxy using Docker to handle proxy requests effectively. Follow these steps:
Step 1:


![image](https://github.com/user-attachments/assets/d72726b6-637d-4601-a3b4-7e387b773209)
Enter username as admin
Password as password
The first project is automatically created

Step 2:
![image](https://github.com/user-attachments/assets/bde1f84c-68da-4879-9af4-c3df722f7ed5)

click on create.


Step 3: Add a first connector and select any service to generate the secret key and API code

![image](https://github.com/user-attachments/assets/712cebc6-8279-4a48-badd-2f69334cd202)


(path/to/screenshot_integrate_docker.png)
![image](https://github.com/user-attachments/assets/429e10c2-2c79-4371-aa52-9de57e3cfe13)

Step 4: Make your first request with curl

![image](https://github.com/user-attachments/assets/6b0b8948-24b0-4ee1-8869-e1fdc359c7bb)
Step 5:Make a curl request- Run in cmd


curl -k -x http://localhost:8888 -U c0h8n4x5muk6yxpvli4e4l:zljtsrycyucl0xip3rl79 http://ipinfo.io


---

## Troubleshooting

### Common Issues
1. **Element Not Found**:
   Ensure the `attribute` value matches the target button. Use browser developer tools to verify.

2. **Certificate Errors**:
   Check that your Scrapoxy certificates are correctly installed.

3. **Docker Issues**:
   Ensure Docker is running, and the Scrapoxy container is properly configured.

---

## Notes

- This project is for educational purposes only. Ensure you comply with the website’s terms of service when scraping data.
- For robust scraping, consider adding error handling and rotating IP addresses using Scrapoxy.

---

## License
This project is open-source and available under the MIT License.

