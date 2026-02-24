const fs = require('fs');
const path = require('path');
const base = 'd:\\MY_CODE\\GIFT_to_QTI\\WebTracNghiem\\Video';
for (let i = 1; i <= 6; i++) {
    const dir = path.join(base, `Chuong_2_Tiet_${i}`);
    if (fs.existsSync(dir)) {
        const files = fs.readdirSync(dir);
        for (const file of files) {
            if (file.endsWith('.pdf') && file !== 'slide.pdf') {
                try {
                    fs.renameSync(path.join(dir, file), path.join(dir, 'slide.pdf'));
                    console.log(`Renamed in ${dir}`);
                } catch (e) {
                    console.error(e);
                }
            }
        }
    }
}
