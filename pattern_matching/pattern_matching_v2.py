"""
THIS IS INCOMPLETE  AND DOESN'T WORK

"""

def isMatch2(s, p):
    groups = tokenize_pattern(p)
    index = 0
    matched_group = []
    for i, g in enumerate(groups):
        if "*" in g:
            c = g[0]  # this is the character that can be matched
            prev_index = index
            while p[index] == c:
                index = index + 1
            matched_group.append(s[prev_index:index])
        elif g == "?":
            matched_group.append(s[index])
            index = index + 1
        else:
            if g != s[index:index + len(g)]:
                return False
            else:
                matched_group.append(g)
                index = index + len(g)
    return True
    #return "".join(matched_group) == s


def tokenize_pattern(p):
    """
    :type p: str
    :rtype: list
    Tokenizes a pattern based on groups with ? and * characters for pattern matching. * characters will be grouped with their immediate preceding character
    """
    if not isinstance(p, str):
        raise TypeError("Pattern is not a string")
    output = []
    for g in _tokenize_questionmark(p):
        output.extend(_tokenize_star(g))
    return output


def _tokenize_questionmark(s):
    output = []
    groups = s.split("?")
    for i, x in enumerate(groups):
        if x != "":
            output.append(x)
        if i < len(groups) - 1:
            output.append("?")
    return output


def _tokenize_star(s):
    """
    :type s: str
    :rtype: list
    Tokenizes string on * characters for pattern matching
    Preserves character and trims empty groups
    """
    output = []
    groups = s.split("*")
    for x in groups[:-1:]:
        if x != "":
            if len(x) == 1:
                output.append(x + "*")
            else:
                output.append(x[:-1:])
                output.append(x[-1] + "*")
    if groups[-1] != "":
        output.append(groups[-1])
    return output
