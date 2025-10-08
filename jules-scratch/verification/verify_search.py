import os
from playwright.sync_api import sync_playwright, expect

def run_verification():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get the absolute path to the index.html file
        file_path = os.path.abspath('index.html')

        # Go to the local index.html file
        page.goto(f'file://{file_path}')

        # Input a classmark that was previously problematic
        page.locator("#classmarkInput").fill("HD 9744")

        # Click the find button
        page.locator("#findButton").click()

        # Wait for the result to be displayed
        expect(page.locator("#resultArea .bg-green-100")).to_be_visible()

        # Take a screenshot of the result
        page.screenshot(path="jules-scratch/verification/verification.png")

        browser.close()

if __name__ == "__main__":
    run_verification()