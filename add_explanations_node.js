const fs = require('fs');
const readline = require('readline');

async function processCSV(filePath) {
    if (!fs.existsSync(filePath)) {
        console.log(`File not found: ${filePath}`);
        return;
    }

    const fileStream = fs.createReadStream(filePath, { encoding: 'utf8' });
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    let lines = [];
    let isFirstLine = true;
    let hasExplanation = false;

    for await (const line of rl) {
        if (!line.trim()) continue;

        let cols = line.split(','); // simple split, assumes no commas in quotes for now
        // A better approach is to use a proper CSV parser, but let's try a simple approach first

        // Actually, since the CSV has commas in quotes, simple split will break.
        // Let's just use regex to parse CSV
        const parseCSVRow = (str) => {
            const result = [];
            let inQuotes = false;
            let currentStr = "";
            for (let i = 0; i < str.length; i++) {
                if (str[i] === '"') {
                    inQuotes = !inQuotes;
                } else if (str[i] === ',' && !inQuotes) {
                    result.push(currentStr);
                    currentStr = "";
                } else {
                    currentStr += str[i];
                }
            }
            result.push(currentStr);
            return result;
        };

        const escapeCSV = (str) => {
            if (str.includes(',') || str.includes('"') || str.includes('\n')) {
                return `"${str.replace(/"/g, '""')}"`;
            }
            return str;
        };

        let parsedLine = parseCSVRow(line);

        if (isFirstLine) {
            // Remove BOM for checking
            let firstCol = parsedLine[0].replace(/^\uFEFF/, '');
            parsedLine[0] = firstCol;

            if (parsedLine.includes('Explanation')) {
                hasExplanation = true;
            } else {
                parsedLine.push('Explanation');
            }
            lines.push(parsedLine.map(escapeCSV).join(','));
            isFirstLine = false;
        } else {
            let explanationIndex = hasExplanation ? parsedLine.length - 1 : parsedLine.length;

            // Generate a generic explanation based on the answer
            let ansIdx = 9; // Assuming Answer is at index 9 (A, B, C, D)
            let answerTextIdx = 10; // ResultAnswer

            let answerStr = parsedLine[ansIdx] || '';
            let explanationText = `Đáp án đúng là ${answerStr}. Phần này được giải thích chi tiết trong bài giảng Tiết học này.`;

            if (hasExplanation && parsedLine[explanationIndex] && parsedLine[explanationIndex].trim() !== '') {
                // keep existing
                lines.push(parsedLine.map(escapeCSV).join(','));
            } else {
                if (!hasExplanation) {
                    parsedLine.push(explanationText);
                } else {
                    parsedLine[explanationIndex] = explanationText;
                }
                lines.push(parsedLine.map(escapeCSV).join(','));
            }
        }
    }

    // Write back with BOM
    const content = '\uFEFF' + lines.join('\n');
    fs.writeFileSync(filePath, content, 'utf8');
    console.log(`Processed ${filePath}`);
}

async function main() {
    await processCSV('DB/MD1.csv');
    await processCSV('DB/Chuong_2_Tiet_2_30_cau.csv');
}

main();
