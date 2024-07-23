def extract_title(markdown):
    lines = markdown.split()

    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
        
    raise Exception("No H1 title found in markdown")