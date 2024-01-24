import pytest
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
    
    
    