import os
import shutil

# Consts
DB_SLIDE_DIR = r"D:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\Slide"
VIDEO_DIR = r"D:\MY_CODE\GIFT_to_QTI\WebTracNghiem\Video"

def final_sync():
    print("Starting Final Sync for 12 Lessons...")
    
    for i in range(1, 13):
        lesson_key = f"Chuong_1_Tiet_{i}"
        # Source is now standardized per user input
        source_pdf_name = f"{lesson_key}.pdf"
        source_path = os.path.join(DB_SLIDE_DIR, source_pdf_name)
        
        dest_folder = os.path.join(VIDEO_DIR, lesson_key)
        dest_pdf_path = os.path.join(dest_folder, "slide.pdf")
        
        print(f"Processing {lesson_key}...")
        
        # 1. Copy PDF
        if os.path.exists(source_path):
            if not os.path.exists(dest_folder):
                print(f"  [Skip] Folder {dest_folder} missing.")
            else:
                try:
                    shutil.copyfile(source_path, dest_pdf_path)
                    print(f"  [OK] Copied slide.pdf")
                except Exception as e:
                    print(f"  [Error] Copy failed: {e}")
        else:
            print(f"  [Error] Source missing: {source_path}")

        # 2. Update index.html
        index_path = os.path.join(dest_folder, "index.html")
        if os.path.exists(index_path):
            try:
                with open(index_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if button exists
                if 'id="download-btn"' in content:
                    print("  [Skip] Button already exists.")
                    continue
                
                # Insert Button
                btn_html = '''        <a href="slide.pdf" download style="text-decoration: none;" target="_blank">
          <button id="download-btn" title="Tải Slide PDF">📥</button>
        </a>'''
                
                # Insert before fullscreen-btn
                target = '<button id="fullscreen-btn"'
                if target in content:
                    new_content = content.replace(target, f'{btn_html}\n        {target}')
                    with open(index_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print("  [OK] Added Download Button.")
                else:
                    print("  [Error] Insertion point not found.")
            except Exception as e:
                print(f"  [Error] HTML update failed: {e}")

if __name__ == "__main__":
    final_sync()
