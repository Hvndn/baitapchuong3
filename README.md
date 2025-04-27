# baitapchuong3
# Auto Backup Database Script

Một script Python đơn giản để tự động sao lưu các file database (`.sql`, `.sqlite3`) và gửi thông báo qua email.

## Mô tả

Script Python này được thiết kế để tự động sao lưu các file database có phần mở rộng `.sql` hoặc `.sqlite3` trong thư mục hiện tại. Các bản sao lưu sẽ được lưu trữ trong thư mục `backup_database` (tự động tạo nếu chưa tồn tại) với tên file bao gồm thời gian sao lưu. Sau mỗi lần sao lưu, script sẽ gửi một email thông báo (thành công, thất bại hoặc không tìm thấy file nào) đến địa chỉ email người nhận đã được cấu hình.

## Hướng dẫn sử dụng

**Yêu cầu:**

* Python 3.x đã được cài đặt.
* Đã cài đặt các thư viện được liệt kê trong `requirements.txt`.

**Cài đặt:**

1.  Clone repository này về máy của bạn (nếu bạn có repository trên GitHub):
    ```bash
    git clone <link_repository_github_cua_ban>
    cd <ten_repository_cua_ban>
    ```
2.  Tạo một file `.env` trong cùng thư mục với script `Baimau.py` và điền các thông tin email cần thiết:
    ```
    SENDER_EMAIL="your_email@gmail.com"
    RECEIVER_EMAIL="recipient_email@example.com"
    APP_PASSWORD="your_app_password"
    ```
    **Quan trọng:** Tuyệt đối không commit và push file `.env` lên GitHub để bảo mật thông tin email của bạn. File `.gitignore` đã được cấu hình để bỏ qua file này.
3.  Cài đặt các thư viện cần thiết từ file `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

**Chạy script:**

Để chạy script và kích hoạt lịch trình backup (hiện tại đang được đặt để chạy mỗi phút cho mục đích thử nghiệm), sử dụng lệnh sau trong terminal:

```bash
python Baimau.py
