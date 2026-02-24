import os
import glob
files = glob.glob(r'd:\MY_CODE\GIFT_to_QTI\WebTracNghiem\Video\Chuong_2_Tiet_*\*.pdf')
for f in files:
    if not f.endswith('slide.pdf'):
        new_name = os.path.join(os.path.dirname(f), 'slide.pdf')
        os.rename(f, new_name)
        print(f"Renamed {f} to {new_name}")
