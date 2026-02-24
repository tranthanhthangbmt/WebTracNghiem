import csv
import sys

def process_csv(csv_path):
    print(f"Processing {csv_path}...")
    
    rows = []
    headers = []
    try:
        with open(csv_path, 'r', encoding='utf-8-sig', newline='') as f:
            reader = csv.reader(f)
            try:
                 headers = next(reader)
            except StopIteration:
                 print("Empty file")
                 return
            
            has_explanation = 'Explanation' in headers
            if not has_explanation:
                 headers.append('Explanation')
                 
            for row in reader:
                 if not row: continue
                 rows.append(row)
    except Exception as e:
        print(f"Error reading {csv_path}: {e}")
        return
             
    try:
        q_idx = headers.index('QuestionContent')
        ans_idx = headers.index('ResultAnswer')
        exp_idx = headers.index('Explanation')
    except ValueError as e:
        print(f"Header missing in {csv_path}: {e}")
        return

    # Process each row
    count = 0
    for row in rows:
        while len(row) < len(headers):
             row.append('')
             
        if row[exp_idx].strip() == '':
             answer = row[ans_idx]
             
             # Create a simple, polite explanation pointing back to the lesson
             explanation = f"Đáp án chính xác là: {answer}. Vui lòng ôn tập lại nội dung Tiết học này để nắm vững kiến thức."
             row[exp_idx] = explanation
             count += 1
             
    # Write back
    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
        
    print(f"Finished {csv_path}. Added {count} generic explanations.")

process_csv('DB/MD1.csv')
process_csv('DB/Chuong_2_Tiet_2_30_cau.csv')
