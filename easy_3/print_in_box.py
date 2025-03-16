# def print_in_box(string):
#     border_length = len(string) + 2
#     border = f'+{'-' * border_length}+'
#     empty_line = f'|{' ' * border_length}|'

#     print(border)
#     print(empty_line)
#     print(f'| {string} |')
#     print(empty_line)
#     print(border)


# print_in_box('To boldly go where no one has gone before.')
# print_in_box('Hello world!!!')
# print_in_box('')
# output:
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

# Further exploration 1:
# def print_truncated(string, width=None):
#     if width > 0:
#         border_length = width
#         if width == 1:
#             string = ''
#         else:
#             string = string[:width - 2]
#     elif width == None:
#         border_length = len(string) + 2
#     else:
#         border_length = 0
#         string = ''

#     border = f'+{'-' * border_length}+'
#     empty_line = f'|{' ' * border_length}|'

#     print(border)
#     print(empty_line)
#     print(f'|{string.center(border_length, ' ')}|')
#     print(empty_line)
#     print(border)

# print_truncated('To boldly go where no one has gone before', 10)
# print_truncated('To boldly go where no one has gone before', 50)
# print_truncated('To boldly go where no one has gone before', 0)
# print_truncated('To boldly go where no one has gone before', 1)
# print_truncated('To boldly go where no one has gone before', 3)
# print_truncated('To boldly go where no one has gone before', -10)

# Further exploration 2:

def print_word_wrapped(string, width=None):
    MAX_BORDER_LENGTH = 80
    if width == None:
        width = MAX_BORDER_LENGTH

    BORDER = f'+{'-' * width}+'
    EMPTY_LINE = f'|{' ' * width}|'

    words_list = string.split()
    result = ''
    MAX_WORD_LENGTH = len(max(words_list, key=len))

    if MAX_WORD_LENGTH < width - 1:
        print(BORDER)
        print(EMPTY_LINE)
    
        for word in words_list:
            if len(result) + len(word) <= width - 2:
                result += word
                if len(result) + 1 <= width - 2:
                    result += ' '
            else:
                print(f'| {result.ljust(width - 1, ' ')}|')
                result = word + ' '

        print(f'| {result.ljust(width - 1, ' ')}|')
        print(EMPTY_LINE)
        print(BORDER)

    else:
        print('Words in paragraph exceed minimum border width limit!')

print_word_wrapped('When Mr. Bilbo Baggins of Bag End announced that he would'
                   ' shortly be celebrating his eleventy-first birthday with a'
                   ' party of special magnificence, there was much talk and'
                   ' excitement in Hobbiton.')
print_word_wrapped('Bilbo was very rich and very peculiar, and had been the'
                   ' wonder of the Shire for sixty years, ever since his'
                   ' remarkable disappearance and unexpected return.', 50)
print_word_wrapped('The riches he had brought back from his travels had now'
                   ' become a local legend, and it was popularly believed,'
                   ' whatever the old folk might say, that the Hill at Bag'
                   ' End was full of tunnels stuffed with treasure.', 20)
print_word_wrapped('And if that was not enough for fame, there was also his'
                   ' prolonged vigour to marvel at.', 5)
print_word_wrapped('Time wore on, but it seemed to have little effect on Mr.'
                   ' Baggins.', -2)