import csv
import os

files = [
    r'd:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\MD3.csv',
    r'd:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\MD4.csv',
    r'd:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\MD5.csv',
    r'd:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\MD6.csv'
]

for file_path in files:
    print(f"Processing {file_path}")
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
        
    updated_rows = []
    headers = []
    
    with open(file_path, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f)
        try:
            headers = next(reader)
        except StopIteration:
            continue
            
        # Add Explanation column if it doesn't exist
        if 'Explanation' not in headers:
            headers.append('Explanation')
            
        ans_idx = -1
        if 'ResultAnswer' in headers:
            ans_idx = headers.index('ResultAnswer')
        elif 'AAnsver' in headers:
            # Try to guess based on 'Answer' column (A, B, C, D)
            # This is a fallback if ResultAnswer is missing, but usually it's there.
            pass
            
        exp_idx = headers.index('Explanation')
        
        for row in reader:
            if not row or not any(row):
                continue
                
            # Pad row if it's shorter than headers
            while len(row) < len(headers):
                row.append('')
                
            if ans_idx != -1 and ans_idx < len(row):
                correct_ans_text = row[ans_idx].strip()
                explanation = f"Đáp án chính xác là: {correct_ans_text}. Vui lòng ôn tập lại nội dung Tiết học này để nắm vững kiến thức."
                row[exp_idx] = explanation
            
            updated_rows.append(row)
            
    # Write back
    with open(file_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(updated_rows)
        
    print(f"Successfully updated {file_path}")
