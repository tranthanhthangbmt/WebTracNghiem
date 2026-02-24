import csv
import os
import google.generativeai as genai
import time
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("GEMINI_API_KEY not found in environment")
    exit(1)

genai.configure(api_key=api_key)

def generate_explanation(question, options, answer, context_script):
    prompt = f"""Bạn là một chuyên gia về Thương mại điện tử.
Dựa vào kịch bản bài học dưới đây, hãy viết MỘT CÂU GIẢI THÍCH NGẮN GỌN (dưới 30 từ) giải thích tại sao đáp án '{answer}' là đúng cho câu hỏi sau.

Kịch bản bài học (tham khảo, có thể không chứa toàn bộ nhưng dùng định hướng):
{context_script[:2000]} # Limit context to save tokens if it's too long, but for these scripts 2000 chars is usually enough for the gist if the question is specific, or we just rely on general knowledge. actually, let me just give the whole script if it fits. 
# actually the previous quiz generation proved we don't always need the full script for a simple explanation.
# Let's provide the question and options.
Câu hỏi: {question}
Các lựa chọn:
{options}
Đáp án đúng: {answer}

Yêu cầu: Chỉ trả về nội dung câu giải thích, KHÔNG có tiền tố như 'Giải thích:' hay 'Vì'. Giải thích ngắn gọn, súc tích, dễ hiểu. Nếu trong kịch bản không đề cập rõ ràng, dùng kiến thức chung quy định của TMĐT Việt Nam để giải thích ngắn gọn."""
    
    # We will use gemini-2.5-flash for speed
    model = genai.GenerativeModel('gemini-2.0-flash')
    try:
        response = model.generate_content(prompt)
        return response.text.strip().strip('"').strip("'")
    except Exception as e:
        print(f"Error generating for question: {question[:30]}... - {e}")
        time.sleep(2) # wait and retry once
        try:
             response = model.generate_content(prompt)
             return response.text.strip().strip('"').strip("'")
        except:
             return "Giải thích đang được cập nhật."

def process_csv(csv_path, script_path):
    print(f"Processing {csv_path}...")
    
    # Read script content
    script_content = ""
    try:
        with open(script_path, 'r', encoding='utf-8') as f:
            script_content = f.read()
    except Exception as e:
        print(f"Warning: Could not read script file: {e}")
    
    # Read CSV
    rows = []
    headers = []
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
             
    # Find indices
    try:
        q_idx = headers.index('QuestionContent')
        ans_idx = headers.index('ResultAnswer')
        a_idx = headers.index('AAnsver') if 'AAnsver' in headers else headers.index('AAnswer')
        b_idx = headers.index('BAnswer')
        c_idx = headers.index('CAnswer')
        d_idx = headers.index('DAnswer')
        exp_idx = headers.index('Explanation')
    except ValueError as e:
        print(f"Header missing in {csv_path}: {e}")
        return

    # Process each row
    count = 0
    for row in rows:
        # Extend row if it doesn't have explanation column yet
        while len(row) < len(headers):
             row.append('')
             
        if row[exp_idx].strip() == '':
             question = row[q_idx]
             options = f"- {row[a_idx]}\n- {row[b_idx]}\n- {row[c_idx]}\n- {row[d_idx]}"
             answer = row[ans_idx]
             
             explanation = generate_explanation(question, options, answer, script_content)
             row[exp_idx] = explanation
             count += 1
             print(f"Generated explanation {count}/{len(rows)}")
             time.sleep(2) # rate limiting for gemini api
             
    # Write back
    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
        
    print(f"Finished {csv_path}. Added {count} explanations.")

# Process Lesson 1
process_csv('DB/MD1.csv', 'Video/Chuong_2_Tiet_1/Kịch bản Chương 2_Tiết 1.txt')

# Process Lesson 2
process_csv('DB/Chuong_2_Tiet_2_30_cau.csv', 'Video/Chuong_2_Tiet_2/Kịch bản Chương 2_Tiết 2.txt')
