"""
This is the latest, and most correct  version!

"""
def isMatch2(s, p):

    # Tokenize the pattern into groups based on match groups
    # ex. a?b*cde will be split into a list consisting of ["a", "?", "b*", "cde"]
    groups = tokenize_pattern(p)
    index = 0
    matched_group = [] # The elements in this list will store the text matched by each group. When combined it should be identical to the provided string
    # Loop through the matcher groups
    for i, g in enumerate(groups):
        if "*" in g:
            c = g[0]  # this is the character that can be matched
            prev_index = index
            while index < len(s) and s[index] == c:
                index = index + 1
            if i < len(groups) - 1:
                lah = _look_ahead(groups[i + 1:], c, s[index:])
                index = index - lah
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

    return "".join(matched_group) == s

def _look_ahead(groups, c, text):
    """
    Looks ahead at provided groups and counts # of instances of something that could match c (literal or ?) in text and return that count
    """
    count = 0
    for group in groups:
        if group == "?":
            count = count + 1 # There's a bug here where the lookahead assumes the ? wildcard can match c and accounts for it, causing patterns that have a ? following a x* group to fail matches
        elif group[0] == c:
            counter = 0
            while counter < len(group) and group[counter] == c:
                counter = counter + 1
            count = count + counter
            if counter != len(group):
                break
        else:
            break
                
    return count


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
