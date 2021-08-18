import pyperclip, nltk

def good_spacing(test_list):
    exceptions = [',', '.', ' ', '(', ')', '\'', '•', '"', '\'s', ';', ':', '-']
    special_exceptions = [',', ')', '\'s', ';', ':']

    for i, word in enumerate(test_list):
        if i != (len(test_list) - 1):
            if word in special_exceptions:
                if test_list[i + 1] in exceptions and word == ')':
                    continue
                if '—' in list(test_list[i + 1]) and word == ')':
                    continue
                if test_list[i + 1] in exceptions and word == ',':
                    continue
                test_list.insert(i + 1, ' ')
            if word[-1] == '-' and word[0] != word[-1]:
                continue
            if test_list[i + 1] not in exceptions and word not in exceptions:
                test_list.insert(i + 1, ' ')
            if word == '\'' and test_list[i - 1][-1] == 's':
                test_list.insert(i + 1, ' ')

    sentence = ''.join(test_list)
    return sentence
