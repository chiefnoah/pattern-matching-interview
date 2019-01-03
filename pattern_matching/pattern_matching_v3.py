
def isMatch3(text, pattern):
    """
    Returns whether pattern fully matches text using the following rules:
    ? represents exactly 1 instance of any character
    * will match 0 or more of it's preceding character
    literals (any non ? or * character) will match exactly 1 instance of the same character
    """
    # Empty pattern can only match empty string
    if len(pattern) == 0:
        return len(text) == 0
    patternindex = textindex = 0 # all zeroes!
    while patternindex < len(pattern):

        if (patternindex < len(pattern) - 1) and pattern[patternindex + 1] == "*":
            # the current pattern character can repeat 0,n times

            #look ahead to get the first non text[textindex] character and the # of characters ahead it is
            future_text_literal, target_char = _scan_text_for_literal(
                text[textindex:], character=pattern[patternindex])
            #figure out how many instances of the x in x* we need to match, accounting for literals and ?s
            # and ensuring the ret of the pattern can match, even if it means this doesn't match every instance of current char
            future_pattern_literal = _scan_pattern_for_literal(
                pattern[patternindex+2:], character=pattern[patternindex], target=target_char)
            # match_count is the # of repeating chars this * group matches
            match_count = future_text_literal - future_pattern_literal
            # increase the current progress through text by the # of matched characters
            textindex = textindex + match_count
            patternindex = patternindex + 1
        elif pattern[patternindex] == "?":
            # if the current pattern character is a ?, we just increase the indexs by 1 (pattern is down at the bottom)
            textindex = textindex + 1
        elif textindex >= len(text):
                # we got to the end of the text before the end of the pattern, we're done here
                break
        else:
            if pattern[patternindex] != text[textindex]:
                # if literals don't match up, pattern doesn't match
                return False
            textindex = textindex + 1
        patternindex = patternindex + 1
    # if we managed to get here and go through every character in text, the strings match
    # if we didn't make it through every character in text, the pattern didn't match the entire string and we return False
    return textindex == len(text)


def _scan_pattern_for_literal(text, character=None, target=None):
    """returns the number of repeating <characters>, subtracting the # of '?' characters until <target> is hit"""
    count = 0
    qcount = 0
    for c in text:
        if c == "?":
            qcount = qcount + 1
        if c == target:
            return count
        if c not in ("?", "*", character):
            return count - qcount
        count = count + 1
    return count  # this happens if we get to the end of text


def _scan_text_for_literal(text, character):
    """scans a string until it finds an instance of character and returns the index of it"""
    count = 0
    for c in text:
        if c is not character:
            return count, c
        count = count + 1
    return count, None
