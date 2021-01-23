# from wordcloud import WordCloud, STOPWORDS
import wordcloud

uninteresting_words = ["a", "an", "at", "or", "by", "the", "to", "if", "of"]
with open('The_Call_of_the_Wild.txt') as f:
    words = f.read()
    frequencies = {}
    for word in words.lower().split():
        if word.isalpha() and word not in uninteresting_words:
            frequencies[word] = frequencies.setdefault(word, 0) + 1
# print(frequencies)

cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(frequencies)
cloud.to_file("myfile.jpg")
