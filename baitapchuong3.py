import schedule
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import os
import shutil
from dotenv import load_dotenv
load_dotenv(dotenv_path='D:/TĐHQT/information.env')

SENDER_EMAIL = os.getenv("Sender_email")
APP_PASSWORD = os.getenv("App_password")
RECEIVER_EMAIL = os.getenv("Receive_email")
backup_folder = "backup_database"
load_dotenv()

def gui_email_thong_bao(tieu_de, noi_dung):

    msg = MIMEText(noi_dung)
    msg["Subject"] = tieu_de
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SENDER_EMAIL, APP_PASSWORD)
            server.send_message(msg)
        print(f"Email '{tieu_de}' đã được gửi thành công!")
    except Exception as e:
        print(f"Lỗi khi gửi email '{tieu_de}': {e}")

def backup_database():
   
    os.makedirs(backup_folder, exist_ok=True)
    backup_time_str = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    backed_up_files = []
    failed_files = []
    for filename in os.listdir("."):
        if filename.endswith(".sql") or filename.endswith(".sqlite3"):
            source_path = os.path.join(".", filename)
            destination_path = os.path.join(backup_folder, f"{filename}_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
            try:
                shutil.copy2(source_path, destination_path)
                backed_up_files.append(filename)  
            except Exception as e:
                failed_files.append(f"{filename} ({e})")

    if backed_up_files:
        noi_dung_thanh_cong = f"Các file database sau đã được sao lưu thành công vào thư mục '{backup_folder}' vào lúc {backup_time_str}:\n" + "\n".join(backed_up_files)
        gui_email_thong_bao(f"Thông báo Backup Database Thành Công - {backup_time_str}", noi_dung_thanh_cong)

    else:
        gui_email_thong_bao(f"Thông báo Backup Database - {backup_time_str}", "Không có file database nào (.sql hoặc .sqlite3) được tìm thấy để sao lưu.")

    if failed_files:
        noi_dung_that_bai = f"Các file database sau không thể sao lưu vào lúc {backup_time_str}:\n" + "\n".join(failed_files)
        gui_email_thong_bao(f"Thông báo Lỗi Backup Database - {backup_time_str}", noi_dung_that_bai)

schedule.every().day.at("00:00").do(backup_database)



if __name__ == "__main__":
    print("Chương trình backup database tự động đã khởi chạy...")
    while True:
        schedule.run_pending()
        time.sleep(1)