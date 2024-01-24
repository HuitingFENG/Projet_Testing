import pytest
from playwright.sync_api import sync_playwright

def test_firefox():
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto("https://i.hr.dmerej.info/add_employee")  # replace with your website link
        browser.close()
        
def test_add_employee():
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto("https://i.hr.dmerej.info/add_employee")  # replace with your actual URL
        page.fill("input[name='name']", "Test Employee")
        page.fill("input[name='email']", "test.employee@example.com")
        page.fill("input[name='address']", "123 Test St")
        page.fill("input[name='city']", "Test City")
        page.fill("input[name='zipcode']", "12345")
        page.fill("input[name='hiring_date']", "2022-01-01")
        page.fill("input[name='job_title']", "Test Job Title")
        page.click("button[type='submit']")
        assert page.url == "https://i.hr.dmerej.info/list_employee", "Failed to add employee"
        browser.close()
