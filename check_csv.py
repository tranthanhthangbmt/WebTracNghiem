import csv
import sys
import json

files = [
    "MD1.csv",
    "Chuong_2_Tiet_2_30_cau.csv",
    "Chuong_2_Tiet_3.csv",
    "Chuong_2_Tiet_4.csv",
    "Chuong_2_Tiet_5.csv",
    "Chuong_2_Tiet_6.csv"
]
output = r"d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\csv_errors.json"

errors = []
for file in files:
    filename = rf"d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\{file}"
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            expected = len(header)
            for i, row in enumerate(reader, start=2):
                if len(row) != expected:
                    errors.append(f"{file} Line {i} has {len(row)} fields instead of {expected}")
    except Exception as e:
        errors.append(f"{file} has error: {str(e)}")

with open(output, 'w', encoding='utf-8') as out:
    json.dump(errors, out)
