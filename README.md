# Jobly IT Job Scraper  
This Python script scrapes **IT job listings** from the Jobly website and saves the data into an **Excel file**. The script extracts details like **job title, company name, location, posting date, and company logo**.  

---

## Features  
- Fetches **IT job listings** from [Jobly.fi](https://www.jobly.fi/)  
- Extracts details: **Job Title, Company Name, Location, Posting Date, and Company Logo URL**  
- Saves the data into an **Excel file** for easy analysis  
- Displays extracted job details in the **console for quick reference**  

---

## Requirements  
To run this script, ensure you have the following Python libraries installed:  

- `selenium`  
- `beautifulsoup4`  
- `pandas`  
- `openpyxl`  
- `requests`  
- `webdriver-manager`  

### Install Dependencies  
Use the following command to install all required libraries:  
```sh  
pip install selenium beautifulsoup4 pandas openpyxl requests webdriver-manager  
```

---

## How to Use  

### 1️ Download the Script  
Clone or download the `jobly_scraper.py` file to your local machine.  

### 2️ Run the Script 
Execute the script using Python:  
```sh  
python jobly_scraper.py  
```

### 3️ If the script runs successfully, it will:  
- **Print job details** in the terminal  
- **Save the data** to an Excel file named **IT_job_listings.xlsx** in the current directory  

---

##  Script Behavior  
1. Sends a **request** to the Jobly **IT jobs** page.  
2. Parses the **HTML content** of the page using **BeautifulSoup**.  
3. Extracts **job details** for all listings, including:  
   - **Job Title**  
   - **Company Name**  
   - **Location**  
   - **Posting Date**  
   - **Company Logo URL**  
4. Saves the extracted data to an **Excel file** for further use.  

---

##  Output  

###  Console Output Example  
```
Job Title: Software Developer  
Company: Google  
Location: Helsinki  
Date Posted: 25.01.2025  
Company Logo: https://www.jobly.fi/logo_google.png  

Job Title: IT Support Specialist  
Company: Microsoft  
Location: Tampere  
Date Posted: 24.01.2025  
Company Logo: https://www.jobly.fi/logo_microsoft.png  

Data saved to IT_job_listings.xlsx  
```

### Excel File (`IT_job_listings.xlsx`)  
An Excel file will be created with the following columns:  
- **Job Title**  
- **Company Name**  
- **Location**  
- **Date Posted**  
- **Company Logo URL**  

---

## Error Handling  
- If the script **fails to load Jobly**, it prints an error message.  
- Missing data fields are **handled gracefully** with `None` values.  
- If a company **doesn’t have a logo**, the script **leaves it blank**.  

---

## Limitations  
- The script scrapes **all IT job listings** from the **first page** of Jobly.  
- It depends on the **current HTML structure** of Jobly.fi. If the website changes, the script might need updates.  
- Ensure compliance with **Jobly's terms of service** regarding web scraping.  

---

## Example of the excel 
![image](https://github.com/user-attachments/assets/6f4e2ac3-6ef7-40ad-ac61-feee71030cbd)

