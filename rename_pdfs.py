import os
import sys

# Windows console encoding fix
sys.stdout.reconfigure(encoding='utf-8')

base = r'd:\MY_CODE\GIFT_to_QTI\WebTracNghiem\Video'
files_to_rename = [
    (r'Chuong_2_Tiet_1\Phần 1_E-Contract_Essentials.pdf', r'Chuong_2_Tiet_1\slide.pdf'),
    (r'Chuong_2_Tiet_2\Phần 2_Electronic_Contract_Essentials.pdf', r'Chuong_2_Tiet_2\slide.pdf'),
    (r'Chuong_2_Tiet_3\Phần 2_Electronic_Contract_Essentials (1).pdf', r'Chuong_2_Tiet_3\slide.pdf'),
    (r'Chuong_2_Tiet_4\Phần 4_Electronic_Payment_Fundamentals.pdf', r'Chuong_2_Tiet_4\slide.pdf'),
    (r'Chuong_2_Tiet_5\Phần 5_Digital_Payment_Strategies.pdf', r'Chuong_2_Tiet_5\slide.pdf'),
    (r'Chuong_2_Tiet_6\Phần 6_Digital_Signatures_and_Authentication.pdf', r'Chuong_2_Tiet_6\slide.pdf')
]

for src, dst in files_to_rename:
    src_path = os.path.join(base, src)
    dst_path = os.path.join(base, dst)
    try:
        os.rename(src_path, dst_path)
        print(f"Renamed: {src}")
    except Exception as e:
        print(f"Failed {src}: {e}")
