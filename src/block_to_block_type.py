block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def block_to_block_type(block):
    if __is_heading_block__(block):
        return block_type_heading
    
    if __is_code_block__(block):
        return block_type_code

    if __is_quote_block__(block):
        return block_type_quote

    if __is_unordered_list_block__(block):
        return block_type_unordered_list

    if __is_ordered_list_block__(block):
        return block_type_ordered_list
    
    return block_type_paragraph

def __is_heading_block__(block):
    split = block.split("# ", 1)
    if len(split) == 1:
        return False
    
    if len(split[0]) == 0 or split[0].startswith('#'):
        return True
    
    return False

def __is_code_block__(block):
    return block.startswith("```") and block.endswith("```")

def __is_quote_block__(block):
    splits = block.split('\n')
    quote_lines = list(filter(lambda s: s.startswith('>'), splits))
    return len(quote_lines) == len(splits)
    
def __is_unordered_list_block__(block):
    splits = block.split('\n')
    quote_lines = list(
        filter(
            lambda s: s.startswith("* ") or s.startswith("- "), 
            splits
        )
    )
    return len(quote_lines) == len(splits)

def __is_ordered_list_block__(block):
    splits = block.split('\n')
    index = 1
    for s in splits:
        if not s.startswith(f"{index}. "):
            return False
        index += 1
    return True