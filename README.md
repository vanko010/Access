# Login Page Test Suite

This project contains automated tests for a login page using Pytest and Selenium WebDriver 4.

## Test Cases Covered

The test suite includes the following test scenarios:

1. **Page Load Tests**
   - Verify login page loads successfully
   - Check all required elements are present

2. **Authentication Tests**
   - Valid login credentials
   - Invalid username
   - Invalid password
   - Empty username field
   - Empty password field
   - Both fields empty

3. **UI/UX Tests**
   - Password field masking
   - Remember me checkbox functionality
   - Forgot password link presence
   - Login button state changes

4. **Security Tests**
   - SQL injection prevention
   - XSS attack prevention

## Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install ChromeDriver**
   - Download ChromeDriver from https://chromedriver.chromium.org/
   - Or use webdriver-manager (already included in requirements)

3. **Configure Test Settings**
   - Update the `login_url` in the test file with your actual login page URL
   - Modify element selectors (ID, class names) to match your login page
   - Update test credentials as needed

## Running Tests

### Run All Tests
```bash
pytest test_login_page.py -v
```

### Run Specific Test
```bash
pytest test_login_page.py::TestLoginPage::test_successful_login_with_valid_credentials -v
```

### Run Tests with HTML Report
```bash
pytest test_login_page.py --html=report.html --self-contained-html
```

### Run Tests in Headless Mode
Tests are configured to run in headless mode by default. To see the browser:
- Comment out the `--headless` option in the `driver` fixture

## Configuration Notes

Before running tests, make sure to:

1. **Update URL**: Change `login_url` in the `login_page` fixture
2. **Update Selectors**: Modify element selectors to match your page:
   - Username field: `By.ID, "username"`
   - Password field: `By.ID, "password"`
   - Login button: `By.ID, "login-btn"`
   - Error message: `By.CLASS_NAME, "error-message"`

3. **Update Test Data**: Replace test credentials with valid ones for your application

## Test Structure

- **Fixtures**: Setup and teardown WebDriver, navigate to login page
- **Test Classes**: Organized test methods for different scenarios
- **Assertions**: Verify expected behavior and elements
- **Error Handling**: Graceful handling of missing elements

## Browser Support

Currently configured for Chrome browser. To use other browsers:
- Firefox: Replace `webdriver.Chrome()` with `webdriver.Firefox()`
- Edge: Replace with `webdriver.Edge()`

## Troubleshooting

- **Element not found**: Update selectors to match your page structure
- **Timeout errors**: Increase wait times in `WebDriverWait`
- **ChromeDriver issues**: Ensure ChromeDriver version matches Chrome browser version
