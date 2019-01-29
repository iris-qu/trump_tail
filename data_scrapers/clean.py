years = '1851-1899'

file = open('./cleaned_data/'+years+'.txt', 'w')  

source = open('./data_dump/'+years+'.txt').read()
source_sentences = source.splitlines()

for sentence in source_sentences[:]:
    if sentence.startswith(('Paid Notice:', 'Marriage Announcement', 'Article')):
        print('bad start')
        continue
    elif sentence.endswith('No Title'):
        print('no title')
        continue
    else: 
        file.write(sentence + '\n')

file.close()
