def count_vowels(s):

    ''' (str) -> int
    >>> count_vowels('Happy Anniversary!')
    5
    >>> count_vowels('xyz')
    0
    '''
    num_vowels = 0
    for char in s:
        if char in 'aeiouAEIOU':
                num_vowels = num_vowels + 1
    return num_vowels

def collect_vowels(s):

    ''' (str) -> str
    >>>collect_vowels('Happy Anniversary!')
    'aAiea'
    >>>collect_vowels('xyz')
    ''
    '''

    vowels_string = ''
    for char in s:
        if char in 'aeiouAEIOU':
            vowels_string +=char
    return vowels_string


def find_string(s1,s2):
    '''(str,str) -> int
    >>>find_string('banana','ana')
    3
    >>>find_string('apple','p')
    2
    '''
    return s1.find(s2,s1.find(s2)+1)

def common_chars(s1, s2):
    '''(str, str) -> str

    Return a new string containing all characters from s1 that appear at least once in s2.
    The characters in the result will appear in the same order as they appear in s1.

    >>> common_chars('abc', 'ad')
    'a'
    >>> common_chars('a', 'a')
    'a'
    >>> common_chars('abb', 'ab')
    'abb'
    >>> common_chars('abracadabra', 'ra')
    'araaara'
    '''
    res = ''

    for ch in s1:
        if ch in s2:
            res = res + ch

    return res


def count_repeats(string):
    repeats = 0
    index = 0
    while(index < len(string)-1):
        if string[index] == string[index + 1]:
            repeats = repeats + 1
        index = index + 1
    return repeats

    '''
    for i in range(len(s) - 1))
        if s[i] == s[i+1]:
            repeats = repeats + 1
    '''

def shift_left(l):
    first_item = l[0]

    for i in range(1,len(l)):
        l[i - 1] = l[i]

    l[-1] = first_item

def sum_list(list1,list2):
    sum_list = []
    for i in range(len(list1)):
        sum_list.append(list1[i] + list2[i])

    return sum_list


def revert_string(str):
    new_string = ''
    for i in range(1,len(str)+1):
        new_string += str[-i]
    return new_string


    
