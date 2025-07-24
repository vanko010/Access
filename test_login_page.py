import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import config
import random
import string
from html_report_utils import generate_html_report


class LoginPageTest:
    """Test suite for login page using Selenium WebDriver 4"""
    
    def __init__(self):
        """Initialize WebDriver and test settings"""
        # Chrome options
        chrome_options = Options()
        # chrome_options.add_argument("--headless")  # Uncomment to run headless
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")
        
        # Initialize WebDriver
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.login_url = "https://access-ote.pavietnam.vn/dang-nhap"
        
        # Test results tracking
        self.test_results = []
        self.passed_tests = 0
        self.failed_tests = 0
        self.start_time = datetime.now()
        self.detailed_results = []  # For HTML report
    
    def setup_test(self):
        """Navigate to login page before each test"""
        print(f"Navigating to: {self.login_url}")
        self.driver.get(self.login_url)
        time.sleep(2)
    
    def teardown(self):
        """Close browser"""
        self.driver.quit()
    
    def log_result(self, test_name, passed, message=""):
        """Log test result"""
        status = "PASS" if passed else "FAIL"
        result = f"[{status}] {test_name}"
        if message:
            result += f" - {message}"
        
        print(result)
        self.test_results.append(result)
        
        # Store detailed result for HTML report
        self.detailed_results.append({
            'name': test_name,
            'status': status,
            'passed': passed,
            'message': message,
            'timestamp': datetime.now().strftime('%H:%M:%S')
        })
        
        if passed:
            self.passed_tests += 1
        else:
            self.failed_tests += 1
    
    def test_login_page_loads_successfully(self):
        """Test that login page loads and contains required elements"""
        test_name = "Login page loads successfully"
        try:
            self.setup_test()
            
            # Verify essential elements are present
            username_field = self.driver.find_element(By.XPATH, config.xpathusername)
            password_field = self.driver.find_element(By.XPATH, config.xpathpassword)
            login_button = self.driver.find_element(By.XPATH, config.xpathloginbtn)
            
            assert username_field.is_displayed()
            assert password_field.is_displayed()
            assert login_button.is_displayed()
            
            self.log_result(test_name, True, "All elements found and displayed")
            
        except Exception as e:
            self.log_result(test_name, False, str(e))
    
    def test_successful_login_scenarios(self):
        """Test Group 1: All successful login scenarios"""
        test_cases = [
            {"name": "Valid credentials", "username": config.DOMAIN, "password": config.PASSWORD},
            {"name": "Domain Việt Nam", "username": "autotest1.vn", "password": "16112001@Aii"},
            {"name": "Domain Việt Nam có dấu", "username": "autotesthả.vn", "password": "16112001@Aii"},
            {"name": "Domain Quốc tế", "username": "autotest2.com", "password": "16112001@Aii"},
            {"name": "Domain Quốc tế", "username": "autotest-vn.com", "password": "16112001@Aii"},
            {"name": "Domain Quốc tế", "username": "autotest--1.com", "password": "16112001@Aii"}
        ]
        
        for test_case in test_cases:
            test_name = f"Successful login - {test_case['name']}"
            self.driver.get(self.login_url)
            try:
                self.setup_test()
                
                # Enter credentials
                username_field = self.driver.find_element(By.XPATH, config.xpathusername)
                password_field = self.driver.find_element(By.XPATH, config.xpathpassword)
                login_button = self.driver.find_element(By.XPATH, config.xpathloginbtn)
                
                username_field.clear()
                username_field.send_keys(test_case["username"])
                password_field.clear()
                password_field.send_keys(test_case["password"])
                
                login_button.click()

                time.sleep(2)
                
                # Wait for redirect or success indicator
                try:
                    welcome_element = self.driver.find_element(By.XPATH, "//header[@class='section__header']//p[1]")
                    if welcome_element.is_displayed():
                        if test_case["name"] == "Domain Quốc tế":
                            assert welcome_element.text == "Xin chào, Le Doan Vu"
                            self.log_result(test_name, True, "Welcome element displayed")
                        else:
                            assert welcome_element.text == "Xin chào, Lê Đoàn Vũ"
                            self.log_result(test_name, True, "Welcome element displayed")
                    else:
                        self.log_result(test_name, False, "Welcome element not dis  played")
                        
                except TimeoutException:
                    # Check for welcome message
                    try:
                        welcome_element = WebDriverWait(self.driver, 5).until(
                            EC.presence_of_element_located((By.XPATH, "//header[@class='section__header']//p"))
                        )
                        if welcome_element.is_displayed():
                            self.log_result(test_name, True, "Welcome element displayed")
                        else:
                            self.log_result(test_name, False, "Welcome element not displayed")
                    except:
                        self.log_result(test_name, False, "No success indicator found")
                        
            except Exception as e:
                self.log_result(test_name, False, str(e))

    def test_failed_login_wrong_credentials(self):
        """Test Group 2: Login failures due to wrong credentials"""
        test_cases = [
            {"name": "Invalid username", "username": "invaliduserdomain.vn", "password": "16112001@Aii", "expected_error": "Đăng nhập không thành công. Vui lòng kiểm tra lại tên đăng nhập và mật khẩu, sau đó thử lại."},
            {"name": "Invalid password", "username": config.DOMAIN, "password": "wrongpassword", "expected_error": "Đăng nhập không thành công. Vui lòng kiểm tra lại tên đăng nhập và mật khẩu, sau đó thử lại."}
        ]
        
        for test_case in test_cases:
            test_name = f"Failed login - {test_case['name']}"
            try:
                self.setup_test()
                
                # Enter credentials
                username_field = self.driver.find_element(By.XPATH, config.xpathusername)
                password_field = self.driver.find_element(By.XPATH, config.xpathpassword)
                login_button = self.driver.find_element(By.XPATH, config.xpathloginbtn)
                
                username_field.clear()
                username_field.send_keys(test_case["username"])
                password_field.clear()
                password_field.send_keys(test_case["password"])
                
                login_button.click()
                
                # Wait for error message
                try:
                    error_message = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//div[@class='alert-description js__alert-description']"))
                    )
                    
                    if error_message.is_displayed():
                        error_text = error_message.text
                        if test_case["expected_error"] in error_text:
                            self.log_result(test_name, True, f"Error message: {error_message.text}")
                        else:
                            self.log_result(test_name, False, f"Unexpected error: {error_message.text}")
                    else:
                        self.log_result(test_name, False, "Error message not displayed")
                        
                except TimeoutException:
                    self.log_result(test_name, False, "No error message found")
                    
            except Exception as e:
                self.log_result(test_name, False, str(e))
    
    def test_failed_login_validation_errors(self):
        """Test Group 3: Login failures due to validation errors"""
        test_cases = [
            {"name": "Empty username", "username": "", "password": "validpassword123", "expected_error": "Tên người dùng không được để trống"},
            {"name": "Empty password", "username": config.DOMAIN, "password": "", "expected_error": "Mật khẩu không được để trống"},
            {"name": "Both fields empty", "username": "", "password": "", "expected_error": "Tên người dùng và mật khẩu không được để trống"},
            {"name": "Invalid domain format", "username": "testertestdomain123", "password": "16112001@Aii", "expected_error": "Tên miền không hợp lệ"},
            {"name": "Domain with special characters", "username": "testertestdomain@123.vn", "password": "16112001@Aii", "expected_error": "Tên miền không hợp lệ"},
            {"name": "Invalid domain format", "username": "testertestdomain123--1.vn", "password": "16112001@Aii", "expected_error": "Tên miền không hợp lệ"},
            {"name": "Domain with special characters", "username": "testertestdomain123-.vn", "password": "16112001@Aii", "expected_error": "Tên miền không hợp lệ"},
            {"name": "Invalid domain format", "username": "-testertestdomain123.vn", "password": "16112001@Aii", "expected_error": "Tên miền không hợp lệ"},
            {"name": "Invalid domain format", "username": "testertestdomain123_.vn", "password": "16112001@Aii", "expected_error": "Tên miền không hợp lệ"},
            {"name": "Invalid domain format", "username": "_testertestdomain123.vn", "password": "16112001@Aii", "expected_error": "Tên miền không hợp lệ"},
            {"name": "Invalid domain format", "username": "testertestd omain123.vn", "password": "16112001@Aii", "expected_error": "Tên miền không hợp lệ"}
        ]
        
        for test_case in test_cases:
            test_name = f"Validation error - {test_case['name']}"
            try:
                self.setup_test()
                
                # Enter credentials
                username_field = self.driver.find_element(By.XPATH, config.xpathusername)
                password_field = self.driver.find_element(By.XPATH, config.xpathpassword)
                login_button = self.driver.find_element(By.XPATH, config.xpathloginbtn)
                
                username_field.clear()
                if test_case["username"]:
                    username_field.send_keys(test_case["username"])
                    
                password_field.clear()
                if test_case["password"]:
                    password_field.send_keys(test_case["password"])
                
                login_button.click()
                time.sleep(2)
                
                # Check for validation error
                try:
                    error_message = self.driver.find_element(By.XPATH, "//div[@class='alert-description']")
                    if error_message.is_displayed():
                        error_text = error_message.text
                        if test_case["expected_error"] in error_text:
                            self.log_result(test_name, True, f"Validation message: {error_message.text}")
                        else:
                            self.log_result(test_name, False, f"Unexpected message:{testcase['username']} {error_message.text}")
                    else:
                        self.log_result(test_name, False, "Error message not displayed")
                        
                except TimeoutException:
                    # Check HTML5 validation for empty fields
                    if not test_case["username"] or not test_case["password"]:
                        if username_field.get_attribute("required") is not None or password_field.get_attribute("required") is not None:
                            self.log_result(test_name, True, "HTML5 validation found")
                        else:
                            self.log_result(test_name, False, "No validation found")
                    else:
                        self.log_result(test_name, False, "No validation error found")
                        
            except Exception as e:
                self.log_result(test_name, False, str(e))
    
    def test_additional_security_checks(self):
        """Additional security and UI tests"""
        # Test password field masking
        test_name = "Password field masking"
        try:
            self.setup_test()
            password_field = self.driver.find_element(By.XPATH, config.xpathpassword)
            
            if password_field.get_attribute("type") == "password":
                self.log_result(test_name, True, "Password field is properly masked")
            else:
                self.log_result(test_name, False, f"Password field type is '{password_field.get_attribute('type')}', expected 'password'")
                
        except Exception as e:
            self.log_result(test_name, False, str(e))
        
        # Test SQL injection prevention
        test_name = "SQL injection prevention"
        try:
            self.setup_test()
            sql_payload = "' OR '1'='1"
            
            username_field = self.driver.find_element(By.XPATH, config.xpathusername)
            password_field = self.driver.find_element(By.XPATH, config.xpathpassword)
            login_button = self.driver.find_element(By.XPATH, config.xpathloginbtn)
            
            username_field.clear()
            username_field.send_keys(sql_payload)
            password_field.clear()
            password_field.send_keys(sql_payload)
            
            login_button.click()
            time.sleep(3)
            
            current_url = self.driver.current_url
            if "dang-nhap" in current_url.lower():
                self.log_result(test_name, True, "SQL injection prevented - still on login page")
            else:
                self.log_result(test_name, False, f"Possible SQL injection vulnerability - redirected to: {current_url}")
                
        except Exception as e:
            self.log_result(test_name, False, str(e))
    
    def generate_html_report(self):
        """Generate beautiful HTML test report using the utility function"""
        return generate_html_report(
            passed_tests=self.passed_tests,
            failed_tests=self.failed_tests,
            start_time=self.start_time,
            detailed_results=self.detailed_results,
            test_url=self.login_url,
            report_title="Login Page Test Report"
        )
    
    def run_all_tests(self):
        """Run all test groups"""
        print("=" * 60)
        print("SELENIUM LOGIN PAGE TEST SUITE")
        print("=" * 60)
        print(f"Testing URL: {self.login_url}")
        print("-" * 60)
        
        # Run all test groups
        self.test_login_page_loads_successfully()
        self.test_successful_login_scenarios()
        self.test_failed_login_wrong_credentials()
        self.test_failed_login_validation_errors()
        self.test_additional_security_checks()
        
        # Print summary
        print("-" * 60)
        print("TEST SUMMARY:")
        print(f"Total Tests: {self.passed_tests + self.failed_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.failed_tests}")
        if (self.passed_tests + self.failed_tests) > 0:
            success_rate = (self.passed_tests / (self.passed_tests + self.failed_tests) * 100)
            print(f"Success Rate: {success_rate:.1f}%")
        print("=" * 60)
        
        # Generate HTML report
        report_file = self.generate_html_report()
        
        # Close browser
        self.teardown()
        
        return report_file


if __name__ == "__main__":
    # Create test instance and run all tests
    test_suite = LoginPageTest()
    test_suite.run_all_tests()
