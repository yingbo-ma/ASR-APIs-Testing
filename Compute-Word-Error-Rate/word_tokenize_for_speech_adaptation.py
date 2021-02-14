# import libraries
import re
import nltk
from nltk import ngrams, FreqDist
from nltk.corpus import stopwords

# define support functions
def decontracted(phrase):
    # specific
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)

    return phrase

def remove_symbols(utterance):
    utterance = re.sub(r'[--]', '', utterance)  # remove '--'
    utterance = re.sub(r'[(]', '', utterance)  # remove '('
    utterance = re.sub(r'[?]', '', utterance)  # remove '?'
    utterance = re.sub(r'[\\]', '', utterance)  # remove '\'
    utterance = re.sub(r'[\']', '', utterance)  # remove '''
    utterance = re.sub(r'[!]', '', utterance)  # remove '!'
    utterance = re.sub(r'["]', '', utterance)  # remove '"'
    utterance = re.sub(r'[{]', '', utterance)  # remove '{"}'
    utterance = re.sub(r'[}]', '', utterance)  # remove '}'
    utterance = re.sub(r'[,]', '', utterance)  # remove '}'
    utterance = re.sub(r'[.]', '', utterance)  # remove '}'
    utterance = re.sub(r'[\n]', ' ', utterance)  # remove '\n'
    utterance = re.sub(r'[#]', '', utterance)  # remove '\n'

    return utterance

def text_preprocessing(phrase):
    # step 1: replace all digital numbers with consistent string of 'number'
    phrase = re.sub(r'\d+', 'number', phrase)
    # step 2: convert text to lowercase
    phrase = phrase.lower()
    # step 3: solve contractions
    phrase = decontracted(phrase)
    # step 4: remove '()' several times. '((())) happens in text corpus'
    for i in range(7):
        phrase = re.sub(r'\([^()]*\)', '', phrase)
    # step 5: remove '[]' and contents inside it
    phrase = re.sub("([\[]).*?([\]])", "", phrase)
    # step 6: remove specific symbols
    phrase = remove_symbols(phrase)
    # step 7: remove leading and ending white spaces
    phrase = phrase.strip()
    # step 8: we first word tokenize then join, in this way we could eliminate inner white spaces

    return phrase

# read text from txt files
ground_truth = []

with open('transcript.txt','r', encoding="utf8") as f:
    ground_truth_text = f.read()
    ground_truth.append(ground_truth_text)
ground_truth = ground_truth[0]

# word tokenize and remove stop words
ground_truth = text_preprocessing(ground_truth)
tokens = nltk.word_tokenize(ground_truth)
stop_words = set(stopwords.words('english'))
filtered_words = [w for w in tokens if not w in stop_words]

all_counts = dict()
speech_adaptation_corpus = []

for size in 1, 2:
    all_counts[size] = FreqDist(ngrams(filtered_words, size))
    most_common_list = all_counts[size].most_common(20)
    # least_common_list = all_counts[size].most_common()[-10:]
    # print(most_common_list)
    # print(least_common_list)

    for item in most_common_list:
        phrase_list = list(item[0])
        phrase = ' '.join(phrase_list)
        speech_adaptation_corpus.append(phrase)
    #
    # for item in least_common_list:
    #     phrase_list = list(item[0])
    #     phrase = ' '.join(phrase_list)
    #     speech_adaptation_corpus.append(phrase)

print(speech_adaptation_corpus)

