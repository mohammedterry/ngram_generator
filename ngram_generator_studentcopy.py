# 1) read in the text from sample.txt and save it to a variable
def load_data():
    pass

#results1 = load_data()
#print(results1[:10])

# 2) clean the text:
#   -  any non-letter character (including punctuation, numbers, newlines) are removed 
#   - and everything is in lower case 
def clean_text(txt):
    pass

#results2 = clean_text("this i12s a@ test.\nHow's things?")
#print(results2,'=', "this is a test hows things")

#3) create a dictionary containing each word and a count of how many times it occurs
def count_words(txt):
    pass

#results3 = count_words('this test is a test like no other test')
#print(results3)
        
#4) that was a unigram dictionary.  now create a bigram dictionary 
def count_bigrams(txt):
    pass

#results4 = count_bigrams('this test is a test like no other test')
#print(results4)

#5) find all the bigrams matching a given first word
def find_bigrams(first_word, bigrams):
    pass

#results5 = find_bigrams('test',set(results4))
#print(results5)


#6) take the last word from a bigram
#   if the bigram is empty, return fullstop
def last_word(bigram):
    pass

#results6 = last_word(('a','test'))
#print(results6,'=','test')

#7) generate sentences using bigrams 
# bonus: can you modify it from a bigram to a trigram model?

def generate_sentence(word, seq_len = 10):
    pass

#results7 = generate_sentence('i')
#print(results7)
