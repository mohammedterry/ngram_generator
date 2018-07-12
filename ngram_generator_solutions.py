# 1) read in the text from sample.txt and save it to a variable

def load_data():
    with open('sample.txt') as f:
        lines = f.readlines()
    return ' '.join(lines)

results1 = load_data()
print(results1[:10])

# 2) clean the text:
#   -  any non-letter character (including punctuation, numbers, newlines) are removed 
#   - and everything is in lower case 

def clean_text(txt):
    cleaned = ''
    for letter in txt.lower():
        if ord('a') <= ord(letter) <= ord('z') or letter.isspace():
            cleaned += letter
    return cleaned.replace('\n',' ')

results2 = clean_text("this i12s a@ test.\nHow's things?")
print(results2,'=', "this is a test hows things")

#3) save all the bigrams in the document

def get_bigrams(txt):
    bigrams = []
    for bigram in zip(txt.split(), txt.split()[1:]):
        bigrams.append(bigram)
    return bigrams

results3 = get_bigrams('this test is a test like no other test')
print(results3)

#4) find all the bigrams matching a given first word

def find_bigrams(first_word,bigrams):
    bag = []
    for bigram in bigrams:
        word1,word2 = bigram
        if word1 == first_word:
            bag.append(bigram)
    return bag

results4 = find_bigrams('test',set(results3))
print(results4)


#5) get only the last word from a bigram
#   if the bigram is empty, return fullstop
    
def last_word(bigram):
    if len(bigram) > 0:
        return bigram[-1]
    else:
        return '.'

results5 = last_word(('a','test'))
print(results5,'=','test')

#6) generate sentences using bigrams 
# bonus: can you modify it from a bigram to a trigram model?

def generate_sentence(word, seq_len = 10):
    from random import choice
    generated = word
    raw_text = load_data()
    text = clean_text(raw_text)
    bigrams = get_bigrams(text)
    for _ in range(seq_len):
        candidate_grams = find_bigrams(word,bigrams)
        chosen_gram = choice(candidate_grams)
        word = last_word(chosen_gram)
        generated += ' ' + word 
    return generated

results6 = generate_sentence('i')
print(results6)