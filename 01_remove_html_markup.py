def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<':    # Start of markup
            tag = True
        elif c == '>':  # End of markup
            tag = False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c
        
    return out

print (remove_html_markup('<a href=">">foo</a>'))
print (remove_html_markup('"<b>foo</b>'))


"""
THE DEVIL'S GUIDE TO DEBUGGING:

1. Scatter output statements everywhere
2. Debug the program into existence
3. Never back up earlier versions
4. Don't bother understanding what the program should do
5. Use the most obvious fix
"""

"""
THE SCIENTIFIC METHOD:

It provides a systematic process by turning some aspect
of reality into a theory that explains how this aspect 
of reality works. And that makes exact predictions on 
this reality.

INITIAL OBSERVATION -> HYPOTHESIS -> PREDICTION -> EXPERIMENT ->
-> OBSERVATION (it supports the hypothesis or it rejects it)
rejecting a hypothesis means we need to create a new hypothesis
until a hypothesis becames a THEORY (a predictive and 
comprehensive description of some aspect of REALITY).

A THEORY is:
 * a framework that explains and predicts observations
 * a particularly useful hypothesis
 * the outcome of THE SCIENTIFIC METHOD.
"""