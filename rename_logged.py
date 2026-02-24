import os
import glob

base = r'd:\MY_CODE\GIFT_to_QTI\WebTracNghiem\Video'

with open("rename_log.txt", "w", encoding="utf-8") as f:
    f.write("Starting rename\n")
    for i in range(1, 7):
        dir_path = os.path.join(base, f'Chuong_2_Tiet_{i}')
        if os.path.exists(dir_path):
            f.write(f"Directory {dir_path} exists\n")
            for file_name in os.listdir(dir_path):
                if file_name.endswith('.pdf') and file_name != 'slide.pdf':
                    src = os.path.join(dir_path, file_name)
                    dst = os.path.join(dir_path, 'slide.pdf')
                    try:
                        os.rename(src, dst)
                        f.write(f"SUCCESS: renamed {file_name} to slide.pdf in {dir_path}\n")
                    except Exception as e:
                        f.write(f"ERROR: {file_name} - {str(e)}\n")
        else:
            f.write(f"Directory {dir_path} DOES NOT EXIST\n")
    f.write("Finished rename\n")
