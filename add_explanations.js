const fs = require('fs');
const readline = require('readline');

const files = [
    'd:\\MY_CODE\\GIFT_to_QTI\\WebTracNghiem\\DB\\MD3.csv',
    'd:\\MY_CODE\\GIFT_to_QTI\\WebTracNghiem\\DB\\MD4.csv',
    'd:\\MY_CODE\\GIFT_to_QTI\\WebTracNghiem\\DB\\MD5.csv',
    'd:\\MY_CODE\\GIFT_to_QTI\\WebTracNghiem\\DB\\MD6.csv'
];

function processString(str) {
    if (str.includes(',') || str.includes('"')) {
        return '"' + str.replace(/"/g, '""') + '"';
    }
    return str;
}

files.forEach(file => {
    try {
        if (!fs.existsSync(file)) {
            console.log(`File not found: ${file}`);
            return;
        }

        const content = fs.readFileSync(file, 'utf8');
        const lines = content.split(/\r?\n/);

        if (lines.length === 0 || !lines[0]) return;

        let headers = lines[0].split(',');
        let hasExplanation = headers.includes('Explanation');
        let needsWrite = false;

        if (!hasExplanation) {
            headers = lines[0].trimRight();
            headers = headers.replace(/,+$/, ''); // Remove trailing commas from header if any
            let headerArray = headers.split(',');
            headerArray.push('Explanation');

            let ansIndex = headerArray.indexOf('ResultAnswer');
            let expIndex = headerArray.length - 1;

            let newContent = [headerArray.join(',')];

            for (let i = 1; i < lines.length; i++) {
                let line = lines[i].trimRight();
                if (!line) continue;

                // Keep the simple split for reading since these csv files seem simple enough,
                // but proper quoting is needed for the Explanation!
                let parts = [];
                let current = '';
                let quotes = 0;

                for (let c of line) {
                    if (c === '"') {
                        quotes++;
                        current += c;
                    } else if (c === ',' && quotes % 2 === 0) {
                        parts.push(current);
                        current = '';
                    } else {
                        current += c;
                    }
                }
                parts.push(current);

                // Assuming ResultAnswer is at index 10 (AAnsver, B, C, D, Answer, ResultAnswer)
                // Let's just find the actual ResultAnswer from our split if possible
                let resAns = "";
                if (ansIndex !== -1 && ansIndex < parts.length) {
                    resAns = parts[ansIndex];
                    // remove outer quotes if they exist
                    if (resAns.startsWith('"') && resAns.endsWith('"')) {
                        resAns = resAns.substring(1, resAns.length - 1);
                    }
                }

                let explanation = `Đáp án chính xác là: ${resAns}. Vui lòng ôn tập lại nội dung Tiết học này để nắm vững kiến thức.`;
                let quotedExp = `"${explanation}"`;

                // Sometimes MD3 had trailing commas. Let's clean the parts up to expIndex
                while (parts.length < expIndex) parts.push('');
                // If parts had trailing commas making length > expIndex, we truncate
                parts = parts.slice(0, expIndex);

                parts.push(quotedExp);
                newContent.push(parts.join(','));
            }

            let fullFile = newContent.join('\n');
            fs.writeFileSync(file, fullFile, 'utf8');
            console.log(`Updated ${file}`);
        } else {
            console.log(`Already has Explanation: ${file}`);
        }

    } catch (err) {
        console.error(err);
    }
});
