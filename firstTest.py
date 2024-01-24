import pytest
from playwright.sync_api import sync_playwright

def test_firefox():
    with sync_playwright() as p:
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto("https://i.hr.dmerej.info/add_employee") 
        browser.close()
