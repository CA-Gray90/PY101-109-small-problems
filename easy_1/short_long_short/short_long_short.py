# def short_long_short(string_1, string_2):
#     if len(string_1) < len(string_2):
#         return string_1 + string_2 + string_1
#     else:
#         return string_2 + string_1 + string_2

def short_long_short(str1, str2):
    short_string = min(str1, str2, key=len)
    long_string = max(str1, str2, key=len)
    return short_string + long_string + short_string

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")