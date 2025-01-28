import requests
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = "https://www.jobly.fi/tyopaikat?search=it"
driver.get(url)

time.sleep(5)

soup = BeautifulSoup(driver.page_source, "html.parser")

driver.quit()

jobs = soup.find_all("article")

job_data = []

for job in jobs:
    title = job.find("h2")
    company = job.find("span", class_="recruiter-company-profile-job-organization")
    location = job.find("div", class_="location")
    date_posted = job.find("span", class_="date")
    logo = job.find("img")

    job_data.append({
        "Job Title": title.get_text(strip=True) if title else None,
        "Company": company.get_text(strip=True) if company else None,
        "Location": location.get_text(strip=True) if location else None,
        "Date Posted": date_posted.get_text(strip=True) if date_posted else None,
        "Company Logo": logo["data-src"] if logo and logo.has_attr("data-src") else None
    })

for job in job_data:
    print(f"Job Title: {job['Job Title']}")
    print(f"Company: {job['Company']}")
    print(f"Location: {job['Location']}")
    print(f"Date Posted: {job['Date Posted']}")
    print(f"Company Logo: {job['Company Logo']}\n")

df = pd.DataFrame(job_data)
df.to_excel("ITjobs.xlsx", index=False)

print("Data saved to ITjobs.xlsx")