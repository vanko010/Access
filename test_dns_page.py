import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import config
from test_login_page import LoginPageTest


class DNSPageTest(LoginPageTest):
    """DNS Page Test class kế thừa từ LoginPageTest"""
    
    def __init__(self):
        """Khởi tạo class kế thừa từ LoginPageTest"""
        super().__init__()
        print("DNS Page Test initialized")
    
    def basic_login_and_verify(self):
        try:
            # Setup test - điều hướng đến trang login
            self.setup_test()
            
            # Tìm các element cần thiết
            username_field = self.driver.find_element(By.XPATH, config.xpathusername)
            password_field = self.driver.find_element(By.XPATH, config.xpathpassword)
            login_button = self.driver.find_element(By.XPATH, config.xpathloginbtn)
            
            # Nhập thông tin đăng nhập
            username_field.clear()
            username_field.send_keys(config.DOMAIN)
            print(f"Đã nhập username: {config.DOMAIN}")
            
            password_field.clear()
            password_field.send_keys(config.PASSWORD)
            print("Đã nhập password")
            
            # Click nút đăng nhập
            login_button.click()
            print("Đã click nút đăng nhập")
            
            # Chờ và verify đăng nhập thành công
            time.sleep(3)
            
            try:
                # Chờ element welcome message xuất hiện
                welcome_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//header[@class='section__header']//p[1]"))
                )
                
                if welcome_element.is_displayed():
                    print("Đăng nhập thành công! Welcome message đã xuất hiện.")
                    self.log_result("Basic Login and Verify", True, "Đăng nhập và verify thành công")
                    return True
                else:
                    print("Welcome message không hiển thị")
                    self.log_result("Basic Login and Verify", False, "Welcome message không hiển thị")
                    return False
                    
            except TimeoutException:
                print("Timeout: Không tìm thấy welcome message")
                self.log_result("Basic Login and Verify", False, "Timeout: Không tìm thấy welcome message")
                return False
                
        except Exception as e:
            print(f"Lỗi trong quá trình đăng nhập: {str(e)}")
            self.log_result("Basic Login and Verify", False, f"Lỗi: {str(e)}")
            return False
    
    def test_dns_page(self):
        dns_page = self.driver.get("https://access-ote.pavietnam.vn/dns")
        time.sleep(3)
        
        try:
            dns_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Cấu hình bản ghi tên miền')]"))
            )
            
            if dns_element.is_displayed():
                print("Truy cập DNS page - Cấu hình bản ghi tên miền thành công")
                self.log_result("test_dns_page", True, "Truy cập DNS page - Cấu hình bản ghi tên miền thành công")
                change_dns_button = self.driver.find_element(By.XPATH, "//div[@class='dns_tao']//a[@href='/name-server']")
                change_dns_button.click()
                time.sleep(3)
                change_dns_page = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//h4[contains(text(),'Thay đổi DNS')]")))
                if change_dns_page.is_displayed():
                    print("Truy cập DNS page - Thay đổi DNS thành công")
                    self.log_result("test_dns_page_change_dns", True, "Truy cập DNS page - Thay đổi DNS thành công")
                    return True
                else:
                    print("Truy cập DNS page - Thay đổi DNS không thành công")
                    self.log_result("test_dns_page_change_dns", False, "Truy cập DNS page - Thay đổi DNS không thành công")
                    return False
        except TimeoutException:
            print("Timeout: Không tìm thấy Cấu hình bản ghi tên miền")
            self.log_result("test_dns_page", False, "Timeout: Không tìm thấy Cấu hình bản ghi tên miền")
            return False
            
        except Exception as e:
            print(f"Lỗi trong quá trình đăng nhập: {str(e)}")
            self.log_result("test_dns_page", False, f"Lỗi: {str(e)}")
            return False

    def test_name_server_page(self):
        dns_page = self.driver.get("https://access-ote.pavietnam.vn/dns")
        time.sleep(3)
        
        try:
            dns_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Cấu hình bản ghi tên miền')]"))
            )
            change_dns_button = self.driver.find_element(By.XPATH, "//ul[@class='nav nav--tabs flex']//a[@href='/name-server']")
            change_dns_button.click()
            time.sleep(3)
            change_dns_page = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//h4[contains(text(),'Thay đổi DNS')]")))
            if change_dns_page.is_displayed():
                print("Truy cập DNS page - Thay đổi DNS thành công")
                self.log_result("test_dns_page_change_dns", True, "Truy cập DNS page - Thay đổi DNS thành công")
                return True

            else:
                print("Truy cập DNS page - Thay đổi DNS không thành công")
                self.log_result("test_dns_page_change_dns", False, "Truy cập DNS page - Thay đổi DNS không thành công")
                return False

        except TimeoutException:    
            print("Timeout: Không tìm thấy Thay đổi DNS")
            self.log_result("test_dns_page_change_dns", False, "Timeout: Không tìm thấy Thay đổi DNS")
            return False
            
        except Exception as e:
            print(f"Lỗi trong quá trình đăng nhập: {str(e)}")
            self.log_result("test_dns_page_change_dns", False, f"Lỗi: {str(e)}")
            return False

    def test_cns_page(self):
        dns_page = self.driver.get("https://access-ote.pavietnam.vn/dns")
        time.sleep(3)        
        try:
            dns_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Cấu hình bản ghi tên miền')]"))
            )
            cns_button = self.driver.find_element(By.XPATH, "//ul[@class='nav nav--tabs flex']//a[@href='/child-name-server']")
            cns_button.click()
            time.sleep(3)
            cns_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Tạo DNS con phụ')]"))
            )
            
            if cns_element.is_displayed():
                print("Truy cập DNS page - Tạo DNS con phụ thành công")
                self.log_result("test_dns_page_cns", True, "Truy cập DNS page - Tạo DNS con phụ thành công")
                return True
            else:
                print("Truy cập DNS page - Tạo DNS con phụ không thành công")
                self.log_result("test_dns_page_cns", False, "Truy cập DNS page - Tạo DNS con phụ không thành công")
                return False
                    
        except TimeoutException:
            print("Timeout: Không tìm thấy Cấu hình bản ghi tên miền")
            self.log_result("test_dns_page_cns", False, "Timeout: Không tìm thấy Cấu hình bản ghi tên miền")
            return False
                
        except Exception as e:
            print(f"Lỗi trong quá trình đăng nhập: {str(e)}")
            self.log_result("test_dns_page_cns", False, f"Lỗi: {str(e)}")
            return False

    def test_email_forwarding_page(self):
        dns_page = self.driver.get("https://access-ote.pavietnam.vn/dns")
        time.sleep(3)        
        try:
            dns_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Cấu hình bản ghi tên miền')]"))
            )
            email_forwarding_button = self.driver.find_element(By.XPATH, "//ul[@class='nav nav--tabs flex']//a[@href='/email-forwarding']")
            email_forwarding_button.click()
            time.sleep(3)
            email_forwarding_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Email chuyển tiếp')]"))
            )
            
            if email_forwarding_element.is_displayed():
                print("Truy cập DNS page - Email chuyển tiếp thành công")
                self.log_result("test_dns_page_email_forwarding", True, "Truy cập DNS page - Email chuyển tiếp thành công")
                return True
            else:
                print("Truy cập DNS page - Email chuyển tiếp không thành công")
                self.log_result("test_dns_page_email_forwarding", False, "Truy cập DNS page - Email chuyển tiếp không thành công")
                return False
                    
        except TimeoutException:
            print("Timeout: Không tìm thấy Cấu hình bản ghi tên miền")
            self.log_result("test_dns_page_email_forwarding", False, "Timeout: Không tìm thấy Cấu hình bản ghi tên miền")
            return False
                
        except Exception as e:
            print(f"Lỗi trong quá trình đăng nhập: {str(e)}")
            self.log_result("test_dns_page_email_forwarding", False, f"Lỗi: {str(e)}")
            return False

    def run_basic_test(self):
        """Chạy test cơ bản và tạo báo cáo"""
        print("\n=== Bắt đầu DNS Page Basic Test ===")
        
        # Chạy test login cơ bản
        success = self.basic_login_and_verify()
        success = self.test_dns_page()
        # Chạy test DNS page
        success = self.test_name_server_page()
        success = self.test_cns_page()
        success = self.test_email_forwarding_page()
        
        # In kết quả
        print(f"\n=== Kết quả test ===")
        print(f"Tổng số test: {self.passed_tests + self.failed_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.failed_tests}")
        
        # Tạo báo cáo HTML
        self.generate_html_report()
        
        self.teardown()
        return success

    def run_dns_record_tests(self):
        """Chạy test thêm DNS records và validation"""
        print("\n=== Bắt đầu DNS Record Tests ===")
        
        # Đăng nhập trước khi test
        login_success = self.basic_login_and_verify()
        if not login_success:
            print("Đăng nhập thất bại, không thể tiếp tục test DNS records")
            self.teardown()
            return False
        
        # Chạy test thêm các loại DNS records
        self.add_nameserver()
        
        # In kết quả
        print(f"\n=== Kết quả DNS Record Tests ===")
        print(f"Tổng số test: {self.passed_tests + self.failed_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.failed_tests}")
        
        # Tạo báo cáo HTML
        report_file = self.generate_html_report()
        
        self.teardown()
        return report_file

    def add_nameserver(self):
        """Test thêm nameserver và chức năng 'Sử dụng Nameserver mặc định'"""
        # Điều hướng đến trang name-server
        self.driver.get("https://access-ote.pavietnam.vn/name-server")
        time.sleep(3)
        
        # Kiểm tra domain hiện tại để xác định có IPv6 hay không
        current_domain = config.DOMAIN
        has_ipv6 = current_domain.endswith('.vn')
        
        # Expected default nameservers từ ảnh nameserver2.png  
        expected_nameservers = [
            {
                "name": "ns1.pavietnam.vn",
                "ipv4": "112.213.89.3",
                "ipv6": "2406:9c80::66" if has_ipv6 else None
            },
            {
                "name": "ns2.pavietnam.vn", 
                "ipv4": "222.255.121.247",
                "ipv6": "2406:9c80::9000:111" if has_ipv6 else None
            },
            {
                "name": "nsbak.pavietnam.net",
                "ipv4": "112.213.89.22", 
                "ipv6": "2406:9c80::9000:302" if has_ipv6 else None
            }
        ]
        
        try:
            # Kiểm tra trang "Thay đổi DNS" đã load
            dns_title = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//h4[contains(text(),'Thay đổi DNS')]"))
            )
            
            if dns_title.is_displayed():
                print("Truy cập trang Thay đổi DNS thành công")
                self.log_result("Trang Thay đổi DNS", True, "Trang đã load thành công")
            
                # Test 1: Kiểm tra nút "Sử dụng name server mặc định"
                try:
                    default_nameserver_button = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'js__btn-used-nameserver-default')]"))
                    )
                    
                    if default_nameserver_button.is_displayed():
                        self.log_result("Tìm thấy nút nameserver mặc định", True, "Nút tồn tại trên trang")
                        print("Tìm thấy nút nameserver mặc định")
                    else:
                        self.log_result("Tìm thấy nút nameserver mặc định", False, "Nút không hiển thị")
                        print("Nút nameserver mặc định không hiển thị")
                    
                    # Test 2: Kiểm tra cấu trúc bảng nameserver hiện tại
                    nameserver_table = self.driver.find_elements(By.XPATH, "//table//tr")
                    print(f"Tìm thấy {len(nameserver_table)} dòng trong bảng nameserver")
                    self.log_result("Kiểm tra bảng nameserver", True, f"Tìm thấy {len(nameserver_table)} dòng")
                    
                    # Verify các nameserver hiện tại (nếu có)
                    for i, expected_ns in enumerate(expected_nameservers, 1):
                        # Kiểm tra name server name
                        try:
                            nameserver_input = self.driver.find_element(By.XPATH, f"//tr[{i+1}]//input[contains(@placeholder, 'Nhập name server') or contains(@name, 'nameserver')]")
                            actual_nameserver = nameserver_input.get_attribute("value")
                            
                            if actual_nameserver == expected_ns["name"]:
                                self.log_result(f"Nameserver {i} - Name", True, f"Đúng: {actual_nameserver}")
                            else:
                                self.log_result(f"Nameserver {i} - Name", False, f"Sai - Mong đợi: {expected_ns['name']}, Thực tế: {actual_nameserver}")
                        except:
                            self.log_result(f"Nameserver {i} - Name", False, "Không tìm thấy trường nameserver")
                        
                        # Kiểm tra IPv4
                        try:
                            ipv4_input = self.driver.find_element(By.XPATH, f"//tr[{i+1}]//input[contains(@placeholder, 'Nhập địa chỉ IPv4')]")
                            actual_ipv4 = ipv4_input.get_attribute("value")
                            
                            if actual_ipv4 == expected_ns["ipv4"]:
                                self.log_result(f"Nameserver {i} - IPv4", True, f"Đúng: {actual_ipv4}")
                            else:
                                self.log_result(f"Nameserver {i} - IPv4", False, f"Sai - Mong đợi: {expected_ns['ipv4']}, Thực tế: {actual_ipv4}")
                        except:
                            self.log_result(f"Nameserver {i} - IPv4", False, "Không tìm thấy trường IPv4")
                        
                        # Kiểm tra IPv6 (chỉ cho domain .vn)
                        if has_ipv6 and expected_ns["ipv6"]:
                            try:
                                ipv6_input = self.driver.find_element(By.XPATH, f"//tr[{i+1}]//input[contains(@placeholder, 'Nhập địa chỉ IPv6')]")
                                actual_ipv6 = ipv6_input.get_attribute("value")
                                
                                if actual_ipv6 == expected_ns["ipv6"]:
                                    self.log_result(f"Nameserver {i} - IPv6", True, f"Đúng: {actual_ipv6}")
                                else:
                                    self.log_result(f"Nameserver {i} - IPv6", False, f"Sai - Mong đợi: {expected_ns['ipv6']}, Thực tế: {actual_ipv6}")
                            except:
                                self.log_result(f"Nameserver {i} - IPv6", False, "Không tìm thấy trường IPv6")
                        elif not has_ipv6:
                            # Kiểm tra không có trường IPv6 cho domain không phải .vn
                            try:
                                ipv6_input = self.driver.find_element(By.XPATH, f"//tr[{i+1}]//input[contains(@placeholder, 'Nhập địa chỉ IPv6')]")
                                if ipv6_input.is_displayed():
                                    self.log_result(f"Nameserver {i} - IPv6 hiển thị", False, "Trường IPv6 không nên hiển thị cho domain không phải .vn")
                                else:
                                    self.log_result(f"Nameserver {i} - IPv6 ẩn", True, "Trường IPv6 đã được ẩn đúng cho domain không phải .vn")
                            except:
                                self.log_result(f"Nameserver {i} - IPv6 ẩn", True, "Trường IPv6 không hiển thị cho domain không phải .vn")
                    
                    # Test 2: Thử thêm nameserver thủ công
                    try:
                        add_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Thêm') or contains(@class, 'btn-primary')]")
                        add_button.click()
                        time.sleep(2)
                        
                        # Tìm dòng trống mới được thêm
                        new_row_index = len(expected_nameservers) + 2  # +1 cho header, +1 cho dòng mới
                        
                        # Nhập nameserver tùy chỉnh
                        custom_ns_data = {
                            "name": "custom.example.com",
                            "ipv4": "8.8.8.8",
                            "ipv6": "2001:4860:4860::8888" if has_ipv6 else None
                        }
                        
                        # Nhập name server
                        nameserver_input = self.driver.find_element(By.XPATH, f"//tr[{new_row_index}]//input[contains(@placeholder, 'Nhập name server')]")
                        nameserver_input.clear()
                        nameserver_input.send_keys(custom_ns_data["name"])
                        
                        # Nhập IPv4
                        ipv4_input = self.driver.find_element(By.XPATH, f"//tr[{new_row_index}]//input[contains(@placeholder, 'Nhập địa chỉ IPv4')]")
                        ipv4_input.clear()
                        ipv4_input.send_keys(custom_ns_data["ipv4"])
                        
                        # Nhập IPv6 nếu có
                        if has_ipv6 and custom_ns_data["ipv6"]:
                            ipv6_input = self.driver.find_element(By.XPATH, f"//tr[{new_row_index}]//input[contains(@placeholder, 'Nhập địa chỉ IPv6')]")
                            ipv6_input.clear()
                            ipv6_input.send_keys(custom_ns_data["ipv6"])
                        
                        self.log_result("Thêm nameserver tùy chỉnh", True, f"Đã thêm {custom_ns_data['name']} thành công")
                        
                    except Exception as e:
                        self.log_result("Thêm nameserver tùy chỉnh", False, f"Lỗi khi thêm nameserver: {str(e)}")
                    
                    # Test 3: Kiểm tra nút "Lưu cấu hình"
                    try:
                        save_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Lưu cấu hình') or contains(text(), 'Lưu') or @type='submit']")
                        if save_button.is_displayed():
                            self.log_result("Nút Lưu cấu hình", True, "Nút Lưu cấu hình có hiển thị")
                            
                            # Click để test (nhưng không submit thực tế để tránh thay đổi cấu hình)
                            # save_button.click() - Comment out để không submit
                            
                        else:
                            self.log_result("Nút Lưu cấu hình", False, "Nút Lưu cấu hình không hiển thị")
                    except:
                        self.log_result("Nút Lưu cấu hình", False, "Không tìm thấy nút Lưu cấu hình")
                        
                except Exception as e:
                    self.log_result("Test nameserver mặc định", False, f"Lỗi khi test nameserver: {str(e)}")
                    
            else:
                self.log_result("Trang Thay đổi DNS", False, "Trang không load được")
                
        except TimeoutException:
            self.log_result("Trang Thay đổi DNS", False, "Timeout: Không tìm thấy trang Thay đổi DNS")
            
        except Exception as e:
            self.log_result("Test add_nameserver", False, f"Lỗi không mong đợi: {str(e)}")
            
        return True
            

if __name__ == "__main__":
    import sys
    
    # Tạo instance và chọn loại test
    dns_test = DNSPageTest()
    
    try:
        if len(sys.argv) > 1 and sys.argv[1] == "--records":
            # Chạy test DNS records (thêm, validation)
            print("Chạy DNS Record Tests...")
            dns_test.run_dns_record_tests()
        else:
            # Chạy test cơ bản (DNS page navigation)
            print("Chạy Basic DNS Page Tests...")
            dns_test.run_basic_test()
            
    except KeyboardInterrupt:
        print("\n=== Test bị gián đoạn bởi người dùng ===")
    except Exception as e:
        print(f"\n=== Lỗi không mong đợi: {str(e)} ===")
    finally:
        # Đảm bảo đóng browser
        try:
            dns_test.teardown()
        except:
            pass
        print("\n=== Test hoàn thành ===")