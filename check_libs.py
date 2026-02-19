import sys
try:
    import fitz
    with open('libs_result.txt', 'w') as f:
        f.write('fitz')
    print("Found fitz")
except ImportError:
    try:
        import pdf2image
        with open('libs_result.txt', 'w') as f:
            f.write('pdf2image')
        print("Found pdf2image")
    except ImportError:
        with open('libs_result.txt', 'w') as f:
            f.write('none')
        print("Found none")
