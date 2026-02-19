import os

VIDEO_DIR = r"D:\MY_CODE\GIFT_to_QTI\WebTracNghiem\Video"
# 1-9: slide.pdf
# 10: E-Marketplace_Essentials.pdf
# 11: E-commerce_Trading_Dynamics.pdf
# 12: E-commerce_Launch_Blueprint.pdf

LESSON_MAP = {}
for i in range(1, 10):
    LESSON_MAP[i] = "slide.pdf"
LESSON_MAP[10] = "E-Marketplace_Essentials.pdf"
LESSON_MAP[11] = "E-commerce_Trading_Dynamics.pdf"
LESSON_MAP[12] = "E-commerce_Launch_Blueprint.pdf"

def fix_html():
    print("Fixing index.html files...")
    for i in range(1, 13):
        folder = f"Chuong_1_Tiet_{i}"
        pdf_name = LESSON_MAP[i]
        index_path = os.path.join(VIDEO_DIR, folder, "index.html")

        if not os.path.exists(index_path):
            print(f"Skipping {folder}: index.html not found")
            continue

        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'id="download-btn"' in content:
            print(f"Lesson {i}: Button already exists.")
            continue

        # BUTTON HTML
        btn_html = f'''        <a href="{pdf_name}" download style="text-decoration: none;" target="_blank">
          <button id="download-btn" title="Tải Slide PDF">📥</button>
        </a>'''

        # We will insert it right before the closing </div> of <div class="controls">
        # To be safe, look for the closing div tag that follows the last expected button or just the end of the controls div.
        # The file has:
        # <div class="controls">
        # ...
        # </div>
        
        # Let's try to find the last button in the controls and append after it.
        # Common last button is fullscreen-btn
        
        target_str = '<button id="fullscreen-btn" title="Toàn màn hình">🖼️</button>'
        
        if target_str in content:
            # Insert BEFORE the fullscreen button
            new_content = content.replace(target_str, f'{btn_html}\n        {target_str}')
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Lesson {i}: Updated successfully (method 1).")
        else:
             # Fallback: Look for just id="fullscreen-btn" if title changed
             if 'id="fullscreen-btn"' in content:
                 # Regex replace to handle attributes
                 import re
                 new_content = re.sub(r'(<button id="fullscreen-btn"[^>]*>.*?<\/button>)', f'{btn_html}\n        \\1', content, count=1)
                 with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                 print(f"Lesson {i}: Updated successfully (method 2).")
             else:
                 print(f"Lesson {i}: Could not find insertion point.")

if __name__ == "__main__":
    fix_html()
