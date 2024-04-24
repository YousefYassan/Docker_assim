import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('stopwords')

with open("paragraphs.txt", 'r') as file:
    data = file.read()
    tokens = word_tokenize(data)
    stopword_list = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word.lower() not in stopword_list]
word_freq = Counter(filtered_tokens)

for word, count in word_freq.items():
    print(f"{word}: {count}")