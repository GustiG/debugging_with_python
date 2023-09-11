def remove_html_markup(s):
    tag   = False
    quote = False
    out   = ""    

    for c in s:
        assert not tag
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            tag = False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c

    return out