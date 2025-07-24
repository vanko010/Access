# File cấu hình cho thông tin đăng nhập và các selector

URL_LOGIN = "https://access-ote.pavietnam.vn/dang-nhap"  # Thay bằng URL thực tế
DOMAIN = "testertestdomain12.vn"
PASSWORD = "16112001@Aii"

# Các ID của trường nhập liệu và nút trên trang
xpathusername = "//input[@name='user']"
xpathpassword = "//input[@name='password']"
xpathloginbtn = "//button[@class='button__sign']"
xpathwelcomemessage = "//p[contains(text(),'Xin chào, Lê Đoàn Vũ')]"  # Phần tử xác nhận đăng nhập thành công 