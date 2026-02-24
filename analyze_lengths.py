import csv
import sys

files = [
    r"d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\MD1.csv",
    r"d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\Chuong_2_Tiet_2_30_cau.csv",
    r"d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\Chuong_2_Tiet_3.csv",
    r"d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\Chuong_2_Tiet_4.csv",
    r"d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\Chuong_2_Tiet_5.csv",
    r"d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\Chuong_2_Tiet_6.csv",
]

for file in files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            if "ResultAnswer" not in header:
                continue
            idx_A = header.index("AAnsver") if "AAnsver" in header else header.index("AAnswer") # typo in my header sometimes
            idx_B = header.index("BAnswer")
            idx_C = header.index("CAnswer")
            idx_D = header.index("DAnswer")
            idx_correct_letter = header.index("Answer")
            
            diffs = []
            for row in reader:
                if len(row) <= max(idx_A, idx_B, idx_C, idx_D, idx_correct_letter):
                    continue
                ans_letter = row[idx_correct_letter].strip()
                lengths = {
                    "A": len(row[idx_A]),
                    "B": len(row[idx_B]),
                    "C": len(row[idx_C]),
                    "D": len(row[idx_D]),
                }
                correct_len = lengths.get(ans_letter, 0)
                wrong_lens = [v for k, v in lengths.items() if k != ans_letter]
                if wrong_lens:
                    avg_wrong = sum(wrong_lens) / len(wrong_lens)
                    diffs.append(correct_len - avg_wrong)
            
            avg_diff = sum(diffs)/len(diffs) if diffs else 0
            import os
            basename = os.path.basename(file)
            print(f"{basename}: Avg (Correct - Wrong) length diff = {avg_diff:.2f} chars. Max diff = {max(diffs) if diffs else 0:.2f}")
    except Exception as e:
        print(f"Error on {file}: {e}")
