def break_words(words):
    """Split the word passed as input"""
    return words.split(' ')

def sorted_words(words):
   return sorted(words)

words = "life is short"

print "Output %r", break_words(words)

print "Output in sorted order", sorted_words(break_words(words))