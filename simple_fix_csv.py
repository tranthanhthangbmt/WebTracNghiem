import csv
import io
import sys

files = [
    r"d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\MD3.csv",
    r"d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\MD4.csv",
    r"d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\MD5.csv",
    r"d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\MD6.csv"
]

for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        lines = content.split('\n')
        if not lines: continue
        
        header = lines[0]
        # remove trailing commas
        header = header.rstrip(',')
        if 'Explanation' in header:
            print(f"{f} already processed")
            continue
            
        new_header = header + ',Explanation'
        new_lines = [new_header]
        
        # parse the rest of the lines with csv reader
        # we don't pass the first line
        reader = csv.reader(lines[1:])
        for row in reader:
            if not row or not any(row): continue
            
            # remove empty trailing columns
            while row and row[-1] == '':
                row.pop()
                
            ans = row[9] if len(row) > 9 else ""
            res_ans = row[10] if len(row) > 10 else ""
            
            explanation = f'Đáp án chính xác là: {res_ans}. Vui lòng ôn tập lại nội dung Tiết học này để nắm vững kiến thức.'
            row.append(explanation)
            
            # format the row back to csv
            output = io.StringIO()
            writer = csv.writer(output, quoting=csv.QUOTE_MINIMAL)
            writer.writerow(row)
            new_lines.append(output.getvalue().strip())
            
        with open(f, 'w', encoding='utf-8', newline='') as file:
            file.write('\n'.join(new_lines) + '\n')
            
        print(f"Processed {f}")
    except Exception as e:
        print(f"Error processing {f}: {e}")
