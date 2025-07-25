#!/usr/bin/env python3
# Test đơn giản cho nameserver functionality

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import config
from test_login_page import LoginPageTest


class SimpleNameserverTest(LoginPageTest):
    """Test đơn giản cho nameserver"""
    
    def __init__(self):
        super().__init__()
        print("Simple Nameserver Test initialized")
    
    def test_nameserver_page(self):
        """Test truy cập trang nameserver và kiểm tra UI"""
        try:
            # Login
            self.setup_test()
            
            # Đăng nhập
            username_field = self.driver.find_element(By.XPATH, config.xpathusername)
            password_field = self.driver.find_element(By.XPATH, config.xpathpassword)
            login_button = self.driver.find_element(By.XPATH, config.xpathloginbtn)
            
            username_field.clear()
            username_field.send_keys(config.DOMAIN)
            password_field.clear()
            password_field.send_keys(config.PASSWORD)
            login_button.click()
            time.sleep(3)
            
            # Điều hướng đến nameserver page
            self.driver.get("https://access-ote.pavietnam.vn/name-server")
            time.sleep(3)
            
            # Kiểm tra trang đã load
            title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Thay đổi DNS')]"))
            )
            
            if title.is_displayed():
                print("Trang Thay đổi DNS load thành công")
                self.log_result("Trang Thay đổi DNS", True, "Load thành công")
            
            # Kiểm tra nút nameserver mặc định
            try:
                default_btn = self.driver.find_element(By.XPATH, "//a[@id='useDefaultNameServerBtn']")
                if default_btn.is_displayed():
                    print("Tìm thấy nút 'Sử dụng nameserver mặc định'")
                    self.log_result("Nút nameserver mặc định", True, "Tồn tại và hiển thị")
                else:
                    print("Nút nameserver mặc định không hiển thị")
                    self.log_result("Nút nameserver mặc định", False, "Không hiển thị")
            except:
                print("Không tìm thấy nút nameserver mặc định")
                self.log_result("Nút nameserver mặc định", False, "Không tìm thấy")
            
            # Kiểm tra bảng nameserver
            try:
                table_rows = self.driver.find_elements(By.XPATH, "//table//tr")
                print(f"Tìm thấy {len(table_rows)} dòng trong bảng nameserver")
                self.log_result("Bảng nameserver", True, f"{len(table_rows)} dòng")
            except:
                print("Không tìm thấy bảng nameserver")
                self.log_result("Bảng nameserver", False, "Không tìm thấy")
            
            # Kiểm tra các input field
            nameserver_inputs = self.driver.find_elements(By.XPATH, "//input[contains(@placeholder, 'Nhập name server')]")
            ipv4_inputs = self.driver.find_elements(By.XPATH, "//input[contains(@placeholder, 'Nhập địa chỉ IPv4')]")
            ipv6_inputs = self.driver.find_elements(By.XPATH, "//input[contains(@placeholder, 'Nhập địa chỉ IPv6')]")
            
            print(f"Tìm thấy {len(nameserver_inputs)} trường nameserver")
            print(f"Tìm thấy {len(ipv4_inputs)} trường IPv4")
            print(f"Tìm thấy {len(ipv6_inputs)} trường IPv6")
            
            self.log_result("Input fields", True, f"NS: {len(nameserver_inputs)}, IPv4: {len(ipv4_inputs)}, IPv6: {len(ipv6_inputs)}")
            
            # Kiểm tra domain và IPv6 logic
            current_domain = config.DOMAIN
            has_ipv6 = current_domain.endswith('.vn')
            
            if has_ipv6:
                print(f"Domain {current_domain} là .vn - nên có IPv6")
                if len(ipv6_inputs) > 0:
                    print("IPv6 fields hiển thị đúng cho domain .vn")
                    self.log_result("IPv6 logic", True, "Domain .vn có IPv6 fields")
                else:
                    print("Domain .vn nhưng không có IPv6 fields")
                    self.log_result("IPv6 logic", False, "Domain .vn thiếu IPv6 fields")
            else:
                print(f"Domain {current_domain} không phải .vn - không nên có IPv6")
                if len(ipv6_inputs) == 0:
                    print("IPv6 fields ẩn đúng cho domain không phải .vn")
                    self.log_result("IPv6 logic", True, "Domain không .vn không có IPv6 fields")
                else:
                    print("Domain không phải .vn nhưng vẫn có IPv6 fields")
                    self.log_result("IPv6 logic", False, "Domain không .vn có IPv6 fields")
            
            # In summary
            print(f"\n=== Test Summary ===")
            print(f"Domain: {current_domain}")
            print(f"IPv6 Expected: {has_ipv6}")
            print(f"Nameserver inputs: {len(nameserver_inputs)}")
            print(f"IPv4 inputs: {len(ipv4_inputs)}")
            print(f"IPv6 inputs: {len(ipv6_inputs)}")
            
            return True
            
        except Exception as e:
            print(f"Lỗi: {str(e)}")
            self.log_result("Test nameserver page", False, f"Lỗi: {str(e)}")
            return False

    def test_validate_nameserver(self):
        """Test validation của nameserver inputs"""
        try:
            # Login và điều hướng đến nameserver page
            self.setup_test()
            
            # Đăng nhập
            username_field = self.driver.find_element(By.XPATH, config.xpathusername)
            password_field = self.driver.find_element(By.XPATH, config.xpathpassword)
            login_button = self.driver.find_element(By.XPATH, config.xpathloginbtn)
            
            username_field.clear()
            username_field.send_keys(config.DOMAIN)
            password_field.clear()
            password_field.send_keys(config.PASSWORD)
            login_button.click()
            time.sleep(3)
            
            # Điều hướng đến nameserver page
            self.driver.get("https://access-ote.pavietnam.vn/name-server")
            time.sleep(3)
            
            # Kiểm tra trang đã load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Thay đổi DNS')]"))
            )
            
            print("\n=== Test Validation Nameserver ===")
            
            # Test case 1: Nameserver hợp lệ - nhập đủ 2 nameserver
            try:
                # Nameserver 1
                nameserver1_input = self.driver.find_element(By.XPATH, "(//input[@name='name_server[1][name]'])[1]")
                ipv4_1_input = self.driver.find_element(By.XPATH, "(//input[@name='name_server[1][ipv4]'])[1]")
                
                # Nameserver 2
                nameserver2_input = self.driver.find_element(By.XPATH, "(//input[@name='name_server[2][name]'])[1]")
                ipv4_2_input = self.driver.find_element(By.XPATH, "(//input[@name='name_server[2][ipv4]'])[1]")
                
                # Nhập thông tin nameserver 1
                nameserver1_input.clear()
                nameserver1_input.send_keys("ns1.example.com")
                ipv4_1_input.clear()
                ipv4_1_input.send_keys("8.8.8.8")
                
                # Nhập thông tin nameserver 2
                nameserver2_input.clear()
                nameserver2_input.send_keys("ns2.example.com")
                ipv4_2_input.clear()
                ipv4_2_input.send_keys("8.8.4.4")

                save_button = self.driver.find_element(By.XPATH, "//a[contains(text(),'Lưu cấu hình')]")
                
                
                # Nếu là domain .vn thì nhập IPv6
                current_domain = config.DOMAIN
                if current_domain.endswith('.vn'):
                    try:
                        ipv6_1_input = self.driver.find_element(By.XPATH, "(//input[@name='name_server[1][ipv6]'])[1]")
                        ipv6_2_input = self.driver.find_element(By.XPATH, "(//input[@name='name_server[2][ipv6]'])[1]")
                        ipv6_1_input.clear()
                        ipv6_1_input.send_keys("2001:4860:4860::8888")
                        ipv6_2_input.clear()
                        ipv6_2_input.send_keys("2001:4860:4860::8844")
                        save_button.click()
                        print(" Đã nhập IPv6 cho domain .vn")
                    except:
                        print(" Không tìm thấy trường IPv6")
                
                time.sleep(2)
                
                # Kiểm tra validation message
                validation_msg = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'invalid-feedback') or contains(@class, 'error')]")
                if not validation_msg or not any(msg.is_displayed() for msg in validation_msg):
                    print(" 2 Nameserver hợp lệ được chấp nhận")
                    self.log_result("2 Nameserver hợp lệ", True, "ns1.example.com và ns2.example.com được chấp nhận")
                else:
                    print(" 2 Nameserver hợp lệ bị từ chối")
                    self.log_result("2 Nameserver hợp lệ", False, "ns1.example.com và ns2.example.com bị từ chối")
            except Exception as e:
                print(f" Lỗi test 2 nameserver hợp lệ: {str(e)}")
                self.log_result("2 Nameserver hợp lệ", False, f"Lỗi: {str(e)}")
            
            # Test case 2: Nameserver không hợp lệ - format sai
            try:
                nameserver_input = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Nhập name server')][1]")
                nameserver_input.clear()
                nameserver_input.send_keys("invalid-nameserver")
                time.sleep(1)
                
                # Click ra ngoài để trigger validation
                self.driver.find_element(By.TAG_NAME, "body").click()
                time.sleep(1)
                
                # Kiểm tra validation message
                validation_msg = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'invalid-feedback') or contains(@class, 'error')]")
                if validation_msg and any(msg.is_displayed() for msg in validation_msg):
                    print("✓ Nameserver không hợp lệ bị từ chối")
                    self.log_result("Nameserver không hợp lệ", True, "invalid-nameserver bị từ chối")
                else:
                    print("✗ Nameserver không hợp lệ được chấp nhận")
                    self.log_result("Nameserver không hợp lệ", False, "invalid-nameserver được chấp nhận")
            except Exception as e:
                print(f"✗ Lỗi test nameserver không hợp lệ: {str(e)}")
                self.log_result("Nameserver không hợp lệ", False, f"Lỗi: {str(e)}")
            
            # Test case 3: IPv4 address hợp lệ
            try:
                ipv4_input = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Nhập địa chỉ IPv4')][1]")
                ipv4_input.clear()
                ipv4_input.send_keys("8.8.8.8")
                time.sleep(1)
                
                # Click ra ngoài để trigger validation
                self.driver.find_element(By.TAG_NAME, "body").click()
                time.sleep(1)
                
                validation_msg = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'invalid-feedback') or contains(@class, 'error')]")
                if not validation_msg or not any(msg.is_displayed() for msg in validation_msg):
                    print("✓ IPv4 hợp lệ được chấp nhận")
                    self.log_result("IPv4 hợp lệ", True, "8.8.8.8 được chấp nhận")
                else:
                    print("✗ IPv4 hợp lệ bị từ chối")
                    self.log_result("IPv4 hợp lệ", False, "8.8.8.8 bị từ chối")
            except Exception as e:
                print(f"✗ Lỗi test IPv4 hợp lệ: {str(e)}")
                self.log_result("IPv4 hợp lệ", False, f"Lỗi: {str(e)}")
            
            # Test case 4: IPv4 address không hợp lệ
            try:
                ipv4_input = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Nhập địa chỉ IPv4')][1]")
                ipv4_input.clear()
                ipv4_input.send_keys("999.999.999.999")
                time.sleep(1)
                
                # Click ra ngoài để trigger validation
                self.driver.find_element(By.TAG_NAME, "body").click()
                time.sleep(1)
                
                validation_msg = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'invalid-feedback') or contains(@class, 'error')]")
                if validation_msg and any(msg.is_displayed() for msg in validation_msg):
                    print("✓ IPv4 không hợp lệ bị từ chối")
                    self.log_result("IPv4 không hợp lệ", True, "999.999.999.999 bị từ chối")
                else:
                    print("✗ IPv4 không hợp lệ được chấp nhận")
                    self.log_result("IPv4 không hợp lệ", False, "999.999.999.999 được chấp nhận")
            except Exception as e:
                print(f"✗ Lỗi test IPv4 không hợp lệ: {str(e)}")
                self.log_result("IPv4 không hợp lệ", False, f"Lỗi: {str(e)}")
            
            # Test case 5: IPv6 validation (nếu có)
            current_domain = config.DOMAIN
            if current_domain.endswith('.vn'):
                try:
                    ipv6_input = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Nhập địa chỉ IPv6')][1]")
                    ipv6_input.clear()
                    ipv6_input.send_keys("2001:4860:4860::8888")
                    time.sleep(1)
                    
                    # Click ra ngoài để trigger validation
                    self.driver.find_element(By.TAG_NAME, "body").click()
                    time.sleep(1)
                    
                    validation_msg = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'invalid-feedback') or contains(@class, 'error')]")
                    if not validation_msg or not any(msg.is_displayed() for msg in validation_msg):
                        print("✓ IPv6 hợp lệ được chấp nhận")
                        self.log_result("IPv6 hợp lệ", True, "2001:4860:4860::8888 được chấp nhận")
                    else:
                        print("✗ IPv6 hợp lệ bị từ chối")
                        self.log_result("IPv6 hợp lệ", False, "2001:4860:4860::8888 bị từ chối")
                except Exception as e:
                    print(f"✗ Lỗi test IPv6 hợp lệ: {str(e)}")
                    self.log_result("IPv6 hợp lệ", False, f"Lỗi: {str(e)}")
                
                # Test IPv6 không hợp lệ
                try:
                    ipv6_input = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Nhập địa chỉ IPv6')][1]")
                    ipv6_input.clear()
                    ipv6_input.send_keys("invalid-ipv6-address")
                    time.sleep(1)
                    
                    # Click ra ngoài để trigger validation
                    self.driver.find_element(By.TAG_NAME, "body").click()
                    time.sleep(1)
                    
                    validation_msg = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'invalid-feedback') or contains(@class, 'error')]")
                    if validation_msg and any(msg.is_displayed() for msg in validation_msg):
                        print("✓ IPv6 không hợp lệ bị từ chối")
                        self.log_result("IPv6 không hợp lệ", True, "invalid-ipv6-address bị từ chối")
                    else:
                        print("✗ IPv6 không hợp lệ được chấp nhận")
                        self.log_result("IPv6 không hợp lệ", False, "invalid-ipv6-address được chấp nhận")
                except Exception as e:
                    print(f"✗ Lỗi test IPv6 không hợp lệ: {str(e)}")
                    self.log_result("IPv6 không hợp lệ", False, f"Lỗi: {str(e)}")
            
            # Test case 6: Kiểm tra required fields
            try:
                # Clear tất cả fields
                nameserver_inputs = self.driver.find_elements(By.XPATH, "//input[contains(@placeholder, 'Nhập name server')]")
                for inp in nameserver_inputs[:2]:  # Clear 2 nameserver đầu tiên
                    inp.clear()
                
                # Thử submit form (nếu có nút submit)
                submit_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Lưu') or contains(text(), 'Cập nhật') or @type='submit']")
                if submit_buttons:
                    submit_buttons[0].click()
                    time.sleep(2)
                    
                    # Kiểm tra validation message cho required fields
                    validation_msg = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'invalid-feedback') or contains(@class, 'error')]")
                    if validation_msg and any(msg.is_displayed() for msg in validation_msg):
                        print("✓ Required field validation hoạt động")
                        self.log_result("Required field validation", True, "Hiển thị lỗi khi thiếu nameserver")
                    else:
                        print("✗ Required field validation không hoạt động")
                        self.log_result("Required field validation", False, "Không hiển thị lỗi khi thiếu nameserver")
                else:
                    print("⚠ Không tìm thấy nút submit để test required fields")
                    self.log_result("Required field validation", False, "Không tìm thấy nút submit")
            except Exception as e:
                print(f"✗ Lỗi test required fields: {str(e)}")
                self.log_result("Required field validation", False, f"Lỗi: {str(e)}")
            
            print("\n=== Hoàn thành test validation nameserver ===")
            return True
            
        except Exception as e:
            print(f"Lỗi trong test_validate_nameserver: {str(e)}")
            self.log_result("Test validate nameserver", False, f"Lỗi: {str(e)}")
            return False
            
    
    def run_test(self):
        """Chạy test và tạo báo cáo"""
        print("\n=== Simple Nameserver Test ===")
        
        success = self.test_nameserver_page()
        
        # In kết quả
        print(f"\n=== Kết quả ===")
        print(f"Tổng số test: {self.passed_tests + self.failed_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.failed_tests}")
        
        # Tạo báo cáo HTML
        self.generate_html_report()
        
        self.teardown()
        return success


if __name__ == "__main__":
    test = SimpleNameserverTest()
    try:
        test.run_test()
    except KeyboardInterrupt:
        print("\n=== Test bị gián đoạn ===")
    except Exception as e:
        print(f"\n=== Lỗi: {str(e)} ===")
    finally:
        try:
            test.teardown()
        except:
            pass
        print("\n=== Test hoàn thành ===")