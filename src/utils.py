def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line.lstrip('# ').strip()  # Strip leading '# ' and any extraneous whitespace
    raise Exception("No H1 title found in markdown")