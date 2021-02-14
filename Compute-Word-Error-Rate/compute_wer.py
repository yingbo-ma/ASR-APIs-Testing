# import libraries
import re
import jiwer
from jiwer import wer

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
    # step 8: remove inner space
    phrase = jiwer.RemoveMultipleSpaces()(phrase)
    phrase = jiwer.RemoveWhiteSpace(replace_by_space=True)(phrase)

    return phrase

# read text from txt files
ground_truth = []
hypothesis = []

with open('transcript.txt','r') as f:
    ground_truth_text = f.read()
    ground_truth.append(ground_truth_text)
ground_truth = ground_truth[0]

with open('hypothesis_from_google_speech.txt','r') as f:
    hypothesis_text = f.read()
    hypothesis.append(hypothesis_text)
hypothesis = hypothesis[0]

# start preprocessing
ground_truth = text_preprocessing(ground_truth)
hypothesis = text_preprocessing(hypothesis)

print(ground_truth)
print(hypothesis)

error = wer(ground_truth, hypothesis)
print("The word error rate is: ", error)





