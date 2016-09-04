import nltk
import glob as gb
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem import SnowballStemmer

stemmer = SnowballStemmer("spanish")

file_comment = gb.glob('comentario.txt')
nlp_words = []

for filename in file_comment:
	for sentence in open(filename, encoding="utf-8"):
		sentence_temp = sentence
		sentence = sentence.replace('.','')
		sentence = sentence.replace(',','')
		sentence = sentence.replace('"','')
		sentence = sentence.replace(':','')
		word = sentence.split()
		for word in word:
			nlp_words.append(word)

nlp_set = set()

for w in nlp_words:
	flag = True
	while flag:
		stem_temp = stemmer.stem(w)
		print(w+" / "+stem_temp+" / "+stemmer.stem(stem_temp))
		if ((w != stem_temp) and (stem_temp != stemmer.stem(stem_temp))):
			w = stemmer.stem(stem_temp)
		else:
			nlp_set.add(stem_temp)
			flag = False

print ("Comentario: '"+sentence_temp+"'")
print ("\nAbstracción de raíces del comentario:")
print (nlp_set)

dataset = gb.glob('dataset.txt')
nlp_words_ds = []

for filename_ds in dataset:
	for sentence_ds in open(filename_ds,encoding="utf-8"):
		sentence_ds = sentence_ds.strip('\n')
		nlp_words_ds.append(sentence_ds)

nlp_set_ds = set()
for w in nlp_words_ds:
	nlp_set_ds.add(stemmer.stem(w))

print ("\nRaíces del dataset:")
print (nlp_set_ds)

nlp_set_intersection = nlp_set & nlp_set_ds

print ("\nConjunto para análisis:")
print (nlp_set_intersection)