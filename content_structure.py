from __future__ import division
from __future__ import unicode_literals
import os
import re
import math
import nltk
from nltk.corpus import stopwords
from textstat.textstat import textstat
from datetime import datetime
from wikiclass.features import wikitext_and_infonoise
from wikiclass.languages import english
language = english.English

data_dir = "./29097/test_29097"
MAX_FILE_ID = 3025

#get 9 readability scores of a revision page given its name
def readability_structure(filename):
	wiki = wikitext_and_infonoise.WikitextAndInfonoise(language)
	file_object = open(filename)
	try:
		text = file_object.read()
	finally:
		file_object.close()
	score1 = textstat.flesch_reading_ease(text)
	#print textstat.flesch_reading_ease(text)
	score2 = textstat.flesch_kincaid_grade(text)
	#print textstat.flesch_kincaid_grade(text)
	score3 = textstat.smog_index(text)	
	#print textstat.smog_index(text)
	score4 = textstat.coleman_liau_index(text)
	#print textstat.coleman_liau_index(text)
	score5 = textstat.automated_readability_index(text)
	#print textstat.automated_readability_index(text)
	score6 = textstat.dale_chall_readability_score(text)
	#print textstat.dale_chall_readability_score(text)
	score7 = textstat.difficult_words(text)
	#print textstat.difficult_words(text)
	score8 = textstat.linsear_write_formula(text)
	#print textstat.linsear_write_formula(text)
	score9 = textstat.gunning_fog(text)
	#print textstat.gunning_fog(text)
	score10 = textstat.text_standard(text)
	#print textstat.text_standard(text)
	#print textstat.char_count(text)

	#get the structure info
	resources = wiki.extract(text)
	return score1, score2, score3, score4, score5, score6, score7, score8, score9, score10, resources["infonoisescore"], \
		resources["loglength"], resources["logreferences"], resources["logpagelinks"], resources["numimageslength"], \
		resources["num_citetemplates"], resources["lognoncitetemplates"], resources["num_categories"], resources["hasinfobox"], \
		resources["lvl2headings"], resources["lvl3headings"]


#read data to get the readability scores and structure info, then store these info into the output file
def  read_write_file(output):
	res = ''
	with open(output, "w") as myfile:
		for i in range (MAX_FILE_ID):
# 			print(i)
			file_name = data_dir + '/' + str(i+1)
			if(i%1000 ==0):
				print("deal with %d file: " %i)
				print(datetime.now()) 
			score1, score2, score3, score4, score5, score6, score7, score8, score9, score10, \
			infonoisescore, loglength, logreferences, logpagelinks, numimageslength, num_citetemplates, lognoncitetemplates, num_categories, \
			hasinfobox, lvl2headings, lvl3headings = readability_structure(file_name)
			res+=str(score1)
			res+='\t'
			res+=str(score2)
			res+='\t'
			res+=str(score3)
			res+='\t'
			res+=str(score4)
			res+='\t'
			res+=str(score5)
			res+='\t'
			res+=str(score6)
			res+='\t'
			res+=str(score7)
			res+='\t'
			res+=str(score8)
			res+='\t'
			res+=str(score9)
			res+='\t'
			res+=str(score10)
			res+='\t'
			res+=str(infonoisescore)
			res+='\t'
			res+=str(loglength)
			res+='\t'
			res+=str(logreferences)
			res+='\t'
			res+=str(logpagelinks)
			res+='\t'
			res+=str(numimageslength)
			res+='\t'
			res+=str(num_citetemplates)
			res+='\t'
			res+=str(lognoncitetemplates)
			res+='\t'
			res+=str(num_categories)
			res+='\t'
			if hasinfobox == True:
				res+=str(1)
			else:
				res+=str(0)
# 			res+=str(hasinfobox)
			res+='\t'
			res+=str(lvl2headings)
			res+='\t'
			res+=str(lvl3headings)
			res+='\n'
			if i%100 ==0:
				myfile.write(res)
				myfile.flush()
				res=''
# 		print(res)
		myfile.write(res)

print("start time: ", datetime.now())
read_write_file("features_29097_test.txt") 
print("end time: ", datetime.now())
print("feature extraction finished")

