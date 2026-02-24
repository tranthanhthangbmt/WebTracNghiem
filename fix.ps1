$files = @("d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\MD3.csv", "d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\MD4.csv", "d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\MD5.csv", "d:\MY_CODE\GIFT_to_QTI\WebTracNghiem\DB\MD6.csv")

foreach ($file in $files) {
    if (-Not (Test-Path $file)) {
        Write-Output "File not found: $file"
        continue
    }

    $lines = Get-Content -LiteralPath $file -Encoding UTF8
    if ($lines.Length -eq 0) { continue }

    $header = $lines[0].TrimEnd(',')
    if ($header -match '.*Explanation.*') {
        Write-Output "Already has Explanation: $file"
        continue
    }

    $newLines = @()
    $newLines += "$header,Explanation"

    for ($i = 1; $i -lt $lines.Length; $i++) {
        $line = $lines[$i].TrimEnd(',')
        if ([string]::IsNullOrWhiteSpace($line)) { continue }

        # Simple split because we know the structure has no internal commas that matter for the last few basic columns
        # Actually ResultAnswer is the last non-empty column.
        $parts = $line -split ','
        
        $res = ""
        # The result answer is usually part 10 (index 10)
        if ($parts.Length -gt 10) {
            $res = $parts[10]
        }
        elseif ($parts.Length -gt 0) {
            $res = $parts[$parts.Length - 1]
        }
        
        # Remove quotes if they exist around the result answer
        $res = $res -replace '^"|"$', ''

        $explanation = '"' + "Đáp án chính xác là: $res. Vui lòng ôn tập lại nội dung Tiết học này để nắm vững kiến thức." + '"'
        
        # We must preserve the whole line exactly, and just append exactly one comma and explanation
        $newLine = $line + "," + $explanation
        $newLines += $newLine
    }

    [System.IO.File]::WriteAllLines($file, $newLines, [System.Text.Encoding]::UTF8)
    Write-Output "Successfully updated: $file"
}
Write-Output "Done processing all files."
