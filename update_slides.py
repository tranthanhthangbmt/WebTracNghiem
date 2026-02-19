import os
import shutil
import re

# Consts
DB_SLIDE_DIR = r"D:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\Slide"
VIDEO_DIR = r"D:\MY_CODE\GIFT_to_QTI\WebTracNghiem\Video"

# Define mappings for lessons
# Format: Lesson_Number: {'source_pdf': 'filename_in_db', 'dest_pdf': 'filename_in_video_dir'}
LESSON_MAP = {}

# 1-9: Simple mapping
for i in range(1, 10):
    LESSON_MAP[i] = {
        'source_pdf': f"Chuong_1_Tiet_{i}.pdf",
        'dest_pdf': "slide.pdf",
        'folder': f"Chuong_1_Tiet_{i}"
    }

# 10-12: Specific filenames
LESSON_MAP[10] = {
    'source_pdf': "Chuong_1_Tiet_10_E-Marketplace_Essentials.pdf",
    'dest_pdf': "E-Marketplace_Essentials.pdf",
    'folder': "Chuong_1_Tiet_10"
}
LESSON_MAP[11] = {
    'source_pdf': "Chuong_1_Tiet_11_E-commerce_Trading_Dynamics.pdf",
    'dest_pdf': "E-commerce_Trading_Dynamics.pdf",
    'folder': "Chuong_1_Tiet_11"
}
LESSON_MAP[12] = {
    'source_pdf': "Chuong_1_Tiet_12_E-commerce_Launch_Blueprint.pdf",
    'dest_pdf': "E-commerce_Launch_Blueprint.pdf",
    'folder': "Chuong_1_Tiet_12"
}

def update_slides():
    print("Starting slide update process...")
    
    for lesson_num, data in LESSON_MAP.items():
        folder_name = data['folder']
        source_pdf_name = data['source_pdf']
        dest_pdf_name = data['dest_pdf']
        
        source_path = os.path.join(DB_SLIDE_DIR, source_pdf_name)
        dest_folder = os.path.join(VIDEO_DIR, folder_name)
        dest_path = os.path.join(dest_folder, dest_pdf_name)
        
        print(f"\nProcessing Lesson {lesson_num}...")

        # 1. Copy File
        if not os.path.exists(source_path):
            print(f"Error: Source file not found: {source_path}")
            continue
            
        if not os.path.exists(dest_folder):
            print(f"Error: Destination folder not found: {dest_folder}")
            continue

        try:
            shutil.copy2(source_path, dest_path)
            print(f"Copied {source_pdf_name} to {dest_path}")
        except Exception as e:
            print(f"Error copying file: {e}")
            continue

        # 2. Update index.html
        index_path = os.path.join(dest_folder, "index.html")
        if not os.path.exists(index_path):
            print(f"Error: index.html not found in {dest_folder}")
            continue
            
        try:
            with open(index_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if button already exists
            if 'id="download-btn"' in content:
                print("Download button already exists in index.html. Skipping HTML update.")
            else:
                # Find the controls div
                # We look for <div class="controls"> ... <button id="fullscreen-btn"
                # And insert our button before the fullscreen button or just append to controls.
                
                # Regex to find the closing div of controls or insert before valid button
                # Let's insert before the fullscreen button, which is usually last.
                
                button_html = f'''
        <a href="{dest_pdf_name}" download style="text-decoration: none;" target="_blank">
          <button id="download-btn" title="Tải Slide PDF">📥</button>
        </a>'''
                
                # Pattern: Find the closing tag of controls div, usually </div> after buttons
                # Or find the fullscreen button and insert before it
                if 'id="fullscreen-btn"' in content:
                    # Insert before fullscreen button
                    new_content = content.replace(
                        '<button id="fullscreen-btn"', 
                        f'{button_html}\n        <button id="fullscreen-btn"'
                    )
                else:
                    # If fullscreen button not found (unlikely based on my view), append significantly
                    # Try to find end of controls
                    new_content = content.replace(
                        '</div>\n    </div>\n\n    <!-- Audio Element',
                        f'  {button_html}\n      </div>\n    </div>\n\n    <!-- Audio Element'
                    )
                    
                if new_content == content:
                     print("Could not find suitable location to insert button.")
                else:
                    with open(index_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated index.html for Lesson {lesson_num}")
                    
        except Exception as e:
            print(f"Error updating index.html: {e}")

if __name__ == "__main__":
    update_slides()
