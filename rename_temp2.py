import os

base = r'd:\MY_CODE\GIFT_to_QTI\WebTracNghiem\Video'
for i in range(1, 7):
    dir_path = os.path.join(base, f'Chuong_2_Tiet_{i}')
    if os.path.exists(dir_path):
        for f in os.listdir(dir_path):
            if f.endswith('.pdf') and f != 'slide.pdf':
                try:
                    os.rename(os.path.join(dir_path, f), os.path.join(dir_path, 'slide.pdf'))
                    print(f"Renamed {f} in {dir_path}")
                except Exception as e:
                    print(e)
