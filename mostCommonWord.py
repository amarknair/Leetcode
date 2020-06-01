from collections  import defaultdict
banned = ",.?;"
stopword = ["a", "is", "the"]
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
paragraph = [s.strip(banned) for s in paragraph.lower().split(" ")]
paragraph = [s for s in paragraph if s not in stopword]
#word_count = {w:0 for w in paragraph}
word_count = defaultdict()
for word in paragraph:
    if word in word_count.keys():
        word_count[word] +=1
    else:
        word_count[word] = 1
test = max(word_count, key=lambda k: word_count[k])