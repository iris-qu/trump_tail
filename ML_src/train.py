from textgenrnn import textgenrnn
import random
textgen = textgenrnn(name="NYT")

years = '2000-2019'
file_path = 'cleaned_data/' + years + '.txt'

source = open(file_path).read()
source_sentences = source.splitlines()
print(random.sample(source_sentences, 5))

textgen.train_on_texts(source_sentences, 
                        new_model = True, num_epochs = 10, gen_epochs = 2, word_level = True,
                        max_length = 40, max_words = 10000, max_gen_length = 300, train_size=0.8, dropout=0.2)