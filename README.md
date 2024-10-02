#⁠Arrange words in a string in the order of their length

def sort_words_by_length(s):
    words = s.split()
    sorted_words = sorted(words, key=len)  
    return ' '.join(sorted_words)  
input_str = "This is a cool sentence"
output_str = words_by_length(input_str)
print(output_str)
