import ipdb

DEBUG = False
def isMatch3(text, pattern):

    # Empty pattern can only match empty string
    if len(pattern) == 0:
        return len(text) == 0
    patternindex = textindex = 0
    while patternindex < len(pattern):
        if (patternindex < len(pattern) - 1) and pattern[patternindex + 1] == "*":
            # the current character can repeat 0,n times
            if DEBUG:
                ipdb.set_trace()
            future_text_literal, target_char = _scan_text_for_literal(
                text[textindex:], character=pattern[patternindex])
            future_pattern_literal = _scan_pattern_for_literal(
                pattern[patternindex+2:], character=pattern[patternindex], target=target_char)
            match_count = future_text_literal - future_pattern_literal
            if match_count > 0 and pattern[patternindex] != text[textindex]:
                return False
            textindex = textindex + match_count
            patternindex = patternindex + 1
        elif pattern[patternindex] == "?":
            textindex = textindex + 1
        elif textindex >= len(text):
                # we got to the end of the text before the end of the pattern, False
                if DEBUG:
                    ipdb.set_trace()
                break
        else:
            if pattern[patternindex] != text[textindex]:
                if DEBUG:
                    ipdb.set_trace()
                return False
            textindex = textindex + 1
        patternindex = patternindex + 1
    if DEBUG:
        ipdb.set_trace()
    return textindex == len(text)


def _scan_pattern_for_literal(text, character=None, target=None):
    """returns index of first literal found in text, or the length of text if it doesn't exist"""
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
