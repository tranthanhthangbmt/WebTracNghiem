import csv
import re
import os

files = [
    "MD1.csv",
    "Chuong_2_Tiet_2_30_cau.csv",
    "Chuong_2_Tiet_3.csv",
    "Chuong_2_Tiet_4.csv",
    "Chuong_2_Tiet_5.csv",
    "Chuong_2_Tiet_6.csv"
]

for file in files:
    path = rf"d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\{file}"
    fixed_rows = []
    
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    header = next(csv.reader([lines[0]]))
    fixed_rows.append(header)
    
    for line in lines[1:]:
        if not line.strip(): continue
        
        row = next(csv.reader([line]))
        if len(row) == 12:
            fixed_rows.append(row)
            continue
            
        # We have > 12 fields
        # Find the answer letter (A, B, C, or D) which is usually around index -3, -4
        possible_answers = []
        for i, val in enumerate(row):
            if val in ['A', 'B', 'C', 'D']:
                possible_answers.append(i)
        
        # We take the last one that makes sense (before Explanation and ResultAnswer)
        # Since ResultAnswer can contain A, B, C, D as words, the letter is likely the one before ResultAnswer parts
        # Explanation is row[-1]
        ans_idx = possible_answers[-1] if possible_answers else -1
        
        if ans_idx == -1:
            print("Failed to find answer index for row", row[0])
            continue
            
        letter = row[ans_idx]
        
        result_ans = ",".join(row[ans_idx+1:-1])
        explanation = row[-1]
        
        left_str = ",".join(row[4:ans_idx])
        
        # Now we need to split left_str into QContent, A, B, C, D
        # Let's use a very reliable regex since we generated the answers to end in periods mostly
        # Or we can just split by ','
        # Actually, let's use the simplest regex: find the last 4 comma-separated parts that don't contain other answers
        # A more robust approach:
        # Since we know ResultAnswer exactly matches the correct choice,
        # we can isolate it! But what about the other 3?
        
        # Let's try splitting by looking for common answer endings: 
        # A, B, C, D often end in a period or exclamation or parenthesis.
        # But wait, we can just split `left_str` from the right 4 times? 
        # No, because some choices have commas inside them.
        
        # Let's just fix the files manually by writing a smarter splitter:
        # We know that the choices are relatively short. 
        # Let's find all commas. Which commas are field separators?
        # Let's use AI! Wait, I can just use a local workaround:
        # For each choice, it normally starts right after a comma.
        
        def split_left(s, num_parts=5):
            # Try to split by ', ' (comma followed by space is usually text, comma followed by no space is usually separator?)
            # Actually, standard CSV generation joins fields with just ',' without space.
            # So a separator is just `,`. Text commas are often `, ` (with space).
            
            parts = []
            current = ""
            for i, char in enumerate(s):
                if char == ',':
                    # If the next char is a space, it's probably text
                    if i + 1 < len(s) and s[i+1] == ' ':
                        current += char
                    else:
                        # It might be a separator!
                        parts.append(current)
                        current = ""
                else:
                    current += char
            parts.append(current)
            
            # If we exactly have 5 parts, great!
            if len(parts) == 5:
                return parts
                
            # If we have more than 5 parts, we need to merge intelligently
            # This happens if there are commas without spaces in the text
            # e.g., (B2B),doanh nghiệp
            return s.rsplit(',', 4) # fallback to right split

        split_parts = split_left(left_str)
        if len(split_parts) != 5:
            # Fallback
            split_parts = left_str.rsplit(',', 4)
            
        QContent, A, B, C, D = split_parts
        
        # If ResultAnswer doesn't match the designated letter, our fallback rsplit might have been wrong,
        # but ResultAnswer is reconstructed fully! We can override the designated choice with ResultAnswer to be safe.
        if letter == 'A': A = result_ans
        elif letter == 'B': B = result_ans
        elif letter == 'C': C = result_ans
        elif letter == 'D': D = result_ans
        
        new_row = row[:4] + [QContent, A, B, C, D, letter, result_ans, explanation]
        fixed_rows.append(new_row)
        
    # Write back
    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        writer.writerows(fixed_rows)
        
print("Fixed files.")
