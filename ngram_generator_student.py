# 1) ====================================
# read in the text from sample.txt and save it to a variable

def load_data(filename='sample.txt'):
    pass
# results1 = load_data()
# print(results1[:10])

# 2) ====================================
# clean the text:
#   -  any non-letter character (including punctuation, numbers, newlines) are removed 
#   - and everything is in lower case 

def clean_text(txt):
    pass
# results2 = clean_text("this i12s a@ test.\nHow's things?")
# print(results2,'=', "this is a test hows things")

#3) ====================================
# save all the bigrams in the document
# bonus: can you modify it from bigrams to trigrams?

def get_bigrams(txt):
    pass
# results3 = get_bigrams('this test is a test like no other test')
# print(results3)

#4) ====================================
# find all the bigrams matching a given first word

def find_bigrams(first_word,bigrams):
    pass
# results4 = find_bigrams('test',set(results3))
# print(results4)


#5) ====================================
# generate sentences by connecting random bigrams together

def generate_sentence(word, seq_len = 15):
    #store the generated string in a variable called "generated"
    #load in the raw text using your load_data() function
    #clean the raw text using your clean_text() function
    #turn the cleaned text into bigrams using your get_bigrams() function
    # create a loop that repeats for seq_len times, so that the generated string has seq_len words in it
        # use the find_bigrams() function to get only the bigrams that match the word stored in the variable "word"
        # choose a random word from those bigrams using the random.choice() function
        # add this word to the string of generated text
        # repeat using this word to find the next bigrams 
    # return the generated string
    pass
#results5 = generate_sentence('i')
#print(results5)

#6) ====================================
# save 10 generated sentences into a file called generated_text.txt
# make sure each sentence is on a new line
def save_to_file():
    pass
#save_to_file()
#print(load_data('generated_text.txt'))
