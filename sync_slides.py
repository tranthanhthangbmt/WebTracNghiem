import os
import shutil
import re

# Consts
DB_SLIDE_DIR = r"D:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\Slide"
VIDEO_DIR = r"D:\MY_CODE\GIFT_to_QTI\WebTracNghiem\Video"

def sync_slides_and_fix_links():
    print("Starting slide synchronization...")
    
    for i in range(1, 13):
        lesson_key = f"Chuong_1_Tiet_{i}"
        source_pdf_name = f"{lesson_key}.pdf"
        dest_folder = os.path.join(VIDEO_DIR, lesson_key)
        dest_pdf_name = "slide.pdf"
        dest_path = os.path.join(dest_folder, dest_pdf_name)
        source_path = os.path.join(DB_SLIDE_DIR, source_pdf_name)

        print(f"\nProcessing Lesson {i} ({lesson_key})...")

        # 1. Copy File
        if os.path.exists(source_path):
            if not os.path.exists(dest_folder):
                 print(f"  Warning: Destination folder {dest_folder} does not exist. Skipping.")
                 continue
            
            try:
                shutil.copy2(source_path, dest_path)
                print(f"  [OK] Copied {source_pdf_name} -> {dest_pdf_name}")
            except Exception as e:
                print(f"  [Error] Copy failed: {e}")
                continue
        else:
            print(f"  [Error] Source file not found: {source_path}")
            continue

        # 2. Update index.html link to point to slide.pdf
        index_path = os.path.join(dest_folder, "index.html")
        if os.path.exists(index_path):
            try:
                with open(index_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Regex to find the download link href
                # Pattern: href="[^"]*(\.pdf)" or similar. 
                # We specifically look for our download button structure or just any href ending in .pdf used for download?
                # Let's search for the ID we added: id="download-btn"
                # The parent <a> tag has the href.
                
                # <a href="OLD_NAME.pdf" download ....>
                
                # We can use regex to replace href=".*?" inside the link containing download-btn
                # Or simpler: replace strict substrings if we know what we put there.
                # In previous steps, 1-9 were "slide.pdf", 10-12 were specific names.
                
                # Universal fix: Regex replace
                # Match <a href="..." ... > ... id="download-btn"
                # This is multiline usually.
                
                # Let's try a robust regex replacement for the <a> tag wrapping the button.
                # Pattern: <a href="([^"]+)"[^>]*download[^>]*>\s*<button id="download-btn"
                
                new_content = re.sub(
                    r'<a href="[^"]+"([^>]*)download([^>]*)>\s*<button id="download-btn"',
                    r'<a href="slide.pdf"\1download\2>\n          <button id="download-btn"',
                    content,
                    flags=re.IGNORECASE | re.MULTILINE
                )
                
                if new_content != content:
                    with open(index_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print("  [OK] Updated index.html download link.")
                else:
                    print("  [Info] index.html content matches or link not found in expected format.")

            except Exception as e:
                print(f"  [Error] Updating HTML failed: {e}")
        else:
            print(f"  [Error] index.html not found.")

if __name__ == "__main__":
    sync_slides_and_fix_links()
