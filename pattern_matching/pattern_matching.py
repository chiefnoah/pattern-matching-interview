import re


def isMatch(text, pattern):
    """
    :type s: str
    :type p: str
    :rtype: bool
    isMatch will return whether a string matches a provided patter. The pattern supports literals, ?, and * wildcard characters with the following rules:
    ? matches exactly one of any character
    * matches 0 or more of any character (ex. "*a" will match "a", "aaa", and "")
    Cannot handle cases such as s = "aaaaaa" p = "?a*" because the "a*" will match all 'a' characters and will leave any other matches with no characters left to parse
    """
    # if empty s, every character must be optional
    if len(text) == 0:
        # funky python list comprehension
        return pattern == "*" or all([x == "*" for x in pattern[1::2]])

    if pattern == "*" and text != "":
        return False

    # Uncomment this to support multiple * characters in a row.
    # pattern = "*".join([x for x in pattern.split("*") if x != ''])


    # string is reversed, so start at the last index
    pattern_index = len(pattern) - 1
    prev_char = None
    # Loop through the reversed string
    for string_index, character in enumerate(reversed(text)):
        # if prev_char is set, it means we're currently matching against a * wildcard group
        if prev_char == character:
            continue
        elif prev_char != None:
            # we've hit the end of the repeating character match group
            prev_char = None
            pattern_index = pattern_index - 1
        # if we got to the end of the pattern, but not the end of the string, we don't match
        if pattern_index < 0:
            return False
        if pattern[pattern_index] == "*":
            # if the first character in the pattern...
            if pattern_index == 0 and string_index == len(text) - 1:
                return True
            pattern_index = pattern_index - 1
            if character == pattern[pattern_index]:
                prev_char = pattern[pattern_index]
            else:
                pattern_index = pattern_index - 1
        elif pattern[pattern_index] == "?":
            pattern_index = pattern_index - 1
        else:
            if character != pattern[pattern_index]:
                return False
            pattern_index = pattern_index - 1
    # This ensures we made it through all of the pattern and string...
    return pattern_index < 1 and string_index == len(text) - 1


def lazyIsMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    lazyIsMatch uses the build-in Python regex engine to do wildcard matching. It's the lazy approach, and the one that should actually be used 🙂 
    """
    try:
        # the replace lets ? match any character, but because ? does something else in pythons regex engine, I just replace it with the chars that do what I want
        return re.fullmatch(p.replace("?", ".{1}"), s) != None
    except re.error:
        return False
