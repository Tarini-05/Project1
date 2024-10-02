
def sort_by_word_length():
    s = input("Enter a string: ")  
    words = s.split()  
    sorted_words = sorted(words, key=len)  
    return ' '.join(sorted_words)  \
