# from wordcloud import WordCloud, STOPWORDS
import wordcloud
from matplotlib import pyplot as plt

with open('The_Call_of_the_Wild.txt') as f:
    file_contents = f.read()


def calculate_frequencies(file_contents):
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    # uninteresting_words = ["a", "an", "at", "or", "by", "the", "to", "if", "of"]
    frequencies = {}
    for word in file_contents.lower().split():
        if word.isalpha() and word not in uninteresting_words:
            frequencies[word] = frequencies.setdefault(word, 0) + 1
    # print(frequencies)
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    # cloud.to_file("myfile.jpg")
    return cloud.to_array()


myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
