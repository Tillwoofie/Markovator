'''
Written by Jeff Hickson.

License is GPLv2 as described by LICENCE file.

'''
import random

class Markov(object):
	def __init__(self):
		self.cache = {}

	def split_file(self, infile):
		words = []
		with open(infile, 'r') as inf:
			data = inf.read()
			words = data.split()
		return words
	
	def gen_triplets(self, words):
		for i in range(len(words)-2):
			yield (words[i], words[i+1], words[i+2])
	
	def add_cache(self, infile):
		words = self.split_file(infile)
		for w1, w2, w3 in self.gen_triplets(words):
			m_key = (w1, w2)
			if m_key in self.cache:
				self.cache[m_key].append(w3)
			else:
				self.cache[m_key] = [w3]
	
	def gen_out_text(self, size=25):
		seed = random.choice(self.cache.keys())
		w1, w2 = seed[0], seed[1]
		gend_words = []
		for i in range(0, size):
			gend_words.append(w1)
			w1, w2 = w2, random.choice(self.cache[(w1, w2)])
		gend_words.append(w2)
		return ' '.join(gend_words)
