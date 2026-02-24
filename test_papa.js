const Papa = require('papaparse');
const fs = require('fs');

const fileContent = fs.readFileSync('DB/Chuong_2_Tiet_3.csv', 'utf8');

Papa.parse(fileContent, {
    header: true,
    skipEmptyLines: true,
    complete: function (results) {
        console.log("Errors:", results.errors);
    }
});
