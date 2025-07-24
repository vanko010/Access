"""
HTML Report Generator Utility
============================

This module provides utilities for generating beautiful HTML test reports
that can be used across different test suites and test cases.

Author: Test Automation Team
Created: 2024
"""

from datetime import datetime


def generate_html_report(passed_tests, failed_tests, start_time, detailed_results, test_url=None, report_title="Test Report"):
    """
    Generate a beautiful HTML test report
    
    Args:
        passed_tests (int): Number of passed tests
        failed_tests (int): Number of failed tests  
        start_time (datetime): Test execution start time
        detailed_results (list): List of detailed test results with format:
                                [{'name': str, 'passed': bool, 'message': str, 'timestamp': str}, ...]
        test_url (str, optional): URL being tested (for display purposes)
        report_title (str): Title for the report (default: "Test Report")
    
    Returns:
        str: Filename of the generated HTML report
    """
    end_time = datetime.now()
    duration = end_time - start_time
    
    # Calculate statistics
    total_tests = passed_tests + failed_tests
    success_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0
    
    # Default URL display
    url_display = test_url if test_url else "N/A"
    
    # HTML template
    html_content = f"""
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{report_title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 300;
        }}
        
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        
        .stat-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            transition: transform 0.3s ease;
        }}
        
        .stat-card:hover {{
            transform: translateY(-5px);
        }}
        
        .stat-number {{
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        
        .stat-label {{
            color: #666;
            font-size: 1.1em;
        }}
        
        .passed {{ color: #27ae60; }}
        .failed {{ color: #e74c3c; }}
        .total {{ color: #3498db; }}
        .rate {{ color: #9b59b6; }}
        
        .results {{
            padding: 30px;
        }}
        
        .results h2 {{
            margin-bottom: 25px;
            color: #2c3e50;
            font-size: 1.8em;
        }}
        
        .test-item {{
            display: flex;
            align-items: center;
            padding: 15px 20px;
            margin-bottom: 10px;
            border-radius: 8px;
            border-left: 4px solid;
            transition: all 0.3s ease;
        }}
        
        .test-item:hover {{
            transform: translateX(5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        
        .test-pass {{
            background: #d5f4e6;
            border-left-color: #27ae60;
        }}
        
        .test-fail {{
            background: #fdeaea;
            border-left-color: #e74c3c;
        }}
        
        .test-status {{
            width: 60px;
            height: 25px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8em;
            font-weight: bold;
            color: white;
            margin-right: 15px;
        }}
        
        .status-pass {{ background: #27ae60; }}
        .status-fail {{ background: #e74c3c; }}
        
        .test-name {{
            flex: 1;
            font-weight: 500;
            color: #2c3e50;
        }}
        
        .test-message {{
            color: #666;
            font-size: 0.9em;
            margin-left: 10px;
        }}
        
        .test-time {{
            color: #999;
            font-size: 0.8em;
            margin-left: 10px;
        }}
        
        .footer {{
            background: #ecf0f1;
            padding: 20px 30px;
            text-align: center;
            color: #7f8c8d;
            border-top: 1px solid #bdc3c7;
        }}
        
        .progress-bar {{
            width: 100%;
            height: 8px;
            background: #ecf0f1;
            border-radius: 4px;
            overflow: hidden;
            margin: 20px 0;
        }}
        
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #27ae60, #2ecc71);
            width: {success_rate}%;
            transition: width 0.5s ease;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🧪 {report_title}</h1>
            <p>Automated Test Results for {url_display}</p>
            <div class="progress-bar">
                <div class="progress-fill"></div>
            </div>
        </div>
        
        <div class="stats">
            <div class="stat-card">
                <div class="stat-number total">{total_tests}</div>
                <div class="stat-label">Total Tests</div>
            </div>
            <div class="stat-card">
                <div class="stat-number passed">{passed_tests}</div>
                <div class="stat-label">Passed</div>
            </div>
            <div class="stat-card">
                <div class="stat-number failed">{failed_tests}</div>
                <div class="stat-label">Failed</div>
            </div>
            <div class="stat-card">
                <div class="stat-number rate">{success_rate:.1f}%</div>
                <div class="stat-label">Success Rate</div>
            </div>
        </div>
        
        <div class="results">
            <h2>📋 Test Results</h2>
"""
    
    # Add test results
    for result in detailed_results:
        status_class = "test-pass" if result['passed'] else "test-fail"
        status_badge = "status-pass" if result['passed'] else "status-fail"
        status_text = "PASS" if result['passed'] else "FAIL"
        
        html_content += f"""
            <div class="test-item {status_class}">
                <div class="test-status {status_badge}">{status_text}</div>
                <div class="test-name">{result['name']}</div>
                <div class="test-message">{result['message']}</div>
                <div class="test-time">{result['timestamp']}</div>
            </div>
"""
    
    # Close HTML
    html_content += f"""
        </div>
        
        <div class="footer">
            <p>📅 Generated on {end_time.strftime('%Y-%m-%d %H:%M:%S')} | ⏱️ Duration: {str(duration).split('.')[0]} | 🚀 Selenium WebDriver 4</p>
        </div>
    </div>
</body>
</html>
"""
    
    # Save to file
    report_filename = f"test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    with open(report_filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"\n📊 HTML Report generated: {report_filename}")
    return report_filename


def create_test_result_entry(name, passed, message="", timestamp=None):
    """
    Helper function to create a properly formatted test result entry
    
    Args:
        name (str): Test name
        passed (bool): Whether the test passed
        message (str): Additional message or error details
        timestamp (str, optional): Test timestamp (auto-generated if not provided)
    
    Returns:
        dict: Formatted test result entry
    """
    if timestamp is None:
        timestamp = datetime.now().strftime('%H:%M:%S')
    
    return {
        'name': name,
        'passed': passed,
        'message': message,
        'timestamp': timestamp
    }
