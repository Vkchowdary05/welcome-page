"""
Automated Webpage Testing using Selenium
Lab Project 13: Welcome Webpage & Date Display
"""

import os
import sys
import time
import argparse
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def setup_driver(headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1280,800")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver


def run_tests(target_url=None):
    if not target_url:
        # Default to local file path if no URL specified
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        index_file = os.path.join(base_dir, "index.html")
        target_url = f"file:///{index_file.replace(os.sep, '/')}"

    print("=" * 65)
    print(" SELENIUM AUTOMATED TEST SUITE: PROJECT 13 (WELCOME WEBPAGE)")
    print(f" Target URL: {target_url}")
    print(f" Timestamp:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 65)

    driver = setup_driver(headless=True)
    tests_passed = 0
    tests_failed = 0

    try:
        # Load webpage
        driver.get(target_url)
        wait = WebDriverWait(driver, 10)

        # Test 1: Page Title
        print("\n[TEST 1] Verifying Page Title...")
        title = driver.title
        assert "Welcome Webpage" in title, f"Expected 'Welcome Webpage' in title, got: '{title}'"
        print(f"  [PASS] Page Title is valid: '{title}'")
        tests_passed += 1

        # Test 2: Welcome Message Element Presence and Content
        print("\n[TEST 2] Verifying Welcome Message...")
        welcome_elem = wait.until(EC.visibility_of_element_located((By.ID, "welcome-message")))
        welcome_text = welcome_elem.text
        assert "Welcome to DevOps Automation Portal" in welcome_text, (
            f"Unexpected welcome text: '{welcome_text}'"
        )
        print(f"  [PASS] Welcome Message detected: '{welcome_text}'")
        tests_passed += 1

        # Test 3: Current Date Element Verification
        print("\n[TEST 3] Verifying Current Date JavaScript Display...")
        date_elem = wait.until(EC.visibility_of_element_located((By.ID, "current-date")))
        date_text = date_elem.text.strip()
        assert date_text != "" and "Loading" not in date_text, (
            f"Date element not populated properly: '{date_text}'"
        )
        current_year = str(datetime.now().year)
        assert current_year in date_text, (
            f"Current year ({current_year}) not found in displayed date: '{date_text}'"
        )
        print(f"  [PASS] Date element verified: '{date_text}'")
        tests_passed += 1

        # Test 4: Toggle Date Format Button Action
        print("\n[TEST 4] Testing Toggle Format Button (ISO vs Readable)...")
        toggle_btn = driver.find_element(By.ID, "toggle-format-btn")
        toggle_btn.click()
        time.sleep(0.5)

        toggled_date_text = driver.find_element(By.ID, "current-date").text.strip()
        iso_today = datetime.now().strftime("%Y-%m-%d")
        assert toggled_date_text == iso_today, (
            f"Expected ISO date '{iso_today}', got '{toggled_date_text}'"
        )
        print(f"  [PASS] Toggle successfully changed format to ISO: '{toggled_date_text}'")
        tests_passed += 1

        # Test 5: Refresh Date Button Action
        print("\n[TEST 5] Testing Refresh Date Button...")
        refresh_btn = driver.find_element(By.ID, "refresh-btn")
        refresh_btn.click()
        time.sleep(0.5)
        refreshed_text = driver.find_element(By.ID, "current-date").text.strip()
        assert refreshed_text != "", "Date element became empty after refresh!"
        print(f"  [PASS] Refresh action completed successfully: '{refreshed_text}'")
        tests_passed += 1

    except AssertionError as ae:
        print(f"  [FAIL] Assertion failed: {ae}")
        tests_failed += 1
    except Exception as ex:
        print(f"  [ERROR] Test execution failed with exception: {ex}")
        tests_failed += 1
    finally:
        driver.quit()

    print("\n" + "=" * 65)
    print(f" TEST RUN SUMMARY: {tests_passed} PASSED | {tests_failed} FAILED")
    print("=" * 65)
    return tests_failed == 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automated Selenium tests for Welcome Webpage")
    parser.add_argument("--url", help="Target URL (e.g., http://localhost:8000 or http://localhost:30013)")
    args = parser.parse_args()

    success = run_tests(args.url)
    sys.exit(0 if success else 1)
