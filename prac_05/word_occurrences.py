import operator

TEXT = "this is a collection of words of nice words this is a fun thing it is"
word_to_count = {}
for word in TEXT.split():
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
word_width = max((len(word) for word in word_to_count.keys()))
for word, count in sorted(word_to_count.items(), key=operator.itemgetter(0), reverse=False):
    print(f"{word:{word_width}} : {count}")
