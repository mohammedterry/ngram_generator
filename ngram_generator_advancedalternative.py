# Alternative generator using word vectors (more advanced)

from random import choice, shuffle

def load_data(filename='sample.txt'):
    with open(filename) as f:
        lines = f.readlines()
    return ' '.join(lines)

def clean_text(txt):
    cleaned = ''
    for letter in txt.lower():
        if ord('a') <= ord(letter) <= ord('z') or letter.isspace():
            cleaned += letter
    return cleaned.replace('\n',' ')

def vocabulary(txt):
    w_idx,idx_w = {},{}
    for i,w in enumerate(set(txt.split())):
        w_idx[w] = i
        idx_w[i] = w
    return w_idx,idx_w

def create_vectors(txt,w_idx):
    vectors = {w:[0 for _ in range(len(w_idx))] for w in txt.split()}
    for w1,w2 in zip(txt.split(), txt.split()[1:]):
        vectors[w1][w_idx[w2]] += 1
    return vectors

def next_word(word,vectors,idx_w):
    next_words = []
    vector = vectors[word]
    for i,v in enumerate(vector):
        next_words.extend([idx_w[i] for _ in range(v)])
    shuffle(next_words)
    return choice(next_words)

def generate(w,sen_len = 15):
    generated = w
    x = clean_text(load_data())
    y,z = vocabulary(x)
    v = create_vectors(x,y)
    for _ in range(sen_len):
        w = next_word(w,v,z)
        generated += ' ' + w
    return generated

def save_to_file(seed, n_examples = 10):
    with open('generated_text.txt','w') as f:
        for _ in range(n_examples):
            f.write('\n')
            f.write(generate(seed))
            f.write('\n')

# save_to_file('i')
# print(load_data('generated_text.txt'))


def dot(A,B): 
    return (sum(a*b for a,b in zip(A,B)))

def cosine_similarity(vec1,vec2): #1.0 = 100% identical
    return dot(vec1,vec2) / ( (dot(vec1,vec1) **.5) * (dot(vec2,vec2) ** .5) + 1e-8 )

def visualise_vectors(v):
    import matplotlib.pyplot as plt
    from sklearn.manifold import TSNE
    from mpl_toolkits.mplot3d import Axes3D

    tsne = TSNE(n_components = 2, random_state = 0)
    wordvecs = tsne.fit_transform(list(v.values()))
    xs,ys = wordvecs[:,0], wordvecs[:,1]
    for label, x, y in zip(v ,xs, ys):
        plt.annotate(label, (x, y))
        plt.scatter(x,y)
    plt.show()

def find_synonym(w,vectors,most_similar = .5):
    synonyms = []
    v = vectors[w]
    for word,vector in vectors.items():
        if word != w:
            similarity = cosine_similarity(v,vector)
            if similarity > most_similar:
                most_similar = similarity
                synonyms = [word]
            elif similarity == most_similar:
                synonyms.append(word)
    return synonyms,most_similar

def test_synonyms(testset):
    x = clean_text(load_data())
    y,z = vocabulary(x)
    v = create_vectors(x,y)
    for w in testset:
        print(w,find_synonym(w,v))
    visualise_vectors(v)

# t = ('in','dark','game','his')
# test_synonyms(t)



