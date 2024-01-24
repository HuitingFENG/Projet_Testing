import pytest
<<<<<<< HEAD
import requests
from playwright.sync_api import sync_playwright


def test_website_link():
    url = "https://i.hr.dmerej.info/"
    response = requests.get(url)
    assert response.status_code == 200, "Website is not accessible"
    
def test_add_employee():
    url = "https://i.hr.dmerej.info/add_employee"
    data = {"name": "Test Employee"}
    response = requests.post(url, data=data)
    assert response.status_code == 200, "Failed to add employee"
    
    
    
=======
from playwright.sync_api import sync_playwright

def test_firefox():
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto("https://i.hr.dmerej.info/add_employee")  # replace with your website link
        browser.close()
>>>>>>> 666b030ec18643c07b31760db2ff4e0104531913
