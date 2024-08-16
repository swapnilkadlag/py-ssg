
def markdown_to_blocks(text):
    return list(
        filter(
            lambda t: len(t) > 0,
            map(
                lambda s: s.strip().strip('\n'),
                text.split("\n\n")
            )
        )
    )