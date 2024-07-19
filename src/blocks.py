def markdown_to_blocks(text):
    blockslist = []
    blocks = text.split("\n\n")
    clean_blocks = [block.strip() for block in blocks if block.strip()]
    return clean_blocks