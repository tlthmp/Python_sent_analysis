#/usr/bin/python
#honestTapir
#2/27/2017
#Challenge 2
#
#
#
# Paul helped me
#
#
#How to set bar width - http://matthiaseisen.com/pp/patterns/p0176/
#How to convert to lowercase - http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python
from __future__ import division

import matplotlib.pyplot as mplot



d1_lines = []
filename = input('What file would you like to read? ')
print(filename)
demSpeech1 = open(filename,"r")
d1_data = demSpeech1.read()
d1_data = d1_data.lower()
#http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python
d1_data = d1_data.replace("...",".").replace(",", ".").replace("..",".").replace("...... ", ".").replace(".....",".")
d1_data = d1_data.replace(". ", ".").replace("? ", "?").replace("?",".").replace("; ",";").replace(";",".").replace("."," ")

d1_data = d1_data.split(" ")


d1_unique = {}
d1_unique_count = {}

sum = {}

diction = []
for index in range(0, len(d1_data)):
    
    
    diction = d1_data[index]
   
    try:
        
        d1_unique[diction] += diction
        d1_unique_count[diction] += 1
    except:
        d1_unique[diction] = diction
        d1_unique_count[diction] =1
        


sent_lexicon = open("sent_lexicon.csv","r")
lexemes = sent_lexicon.read()
lexemes = lexemes.split("\n")


lexicon = {}



for index in range(0, len(lexemes)):
    if len(lexemes[index]) == 0:
        del(lexemes[index])
        continue

    
    lexemes[index] = lexemes[index].split(",")
    lexemes[index][1] = float(lexemes[index][1])
    word = lexemes[index][0]
    value = lexemes[index][1]

    lexicon[word] = value

d1_strong_pos_count = 0
d1_weak_pos_count = 0
d1_weak_neg_count = 0 
d1_strong_neg_count = 0
d1_neutral_count = 0
totalSum = 0

strong_pos_count = 0
weak_pos_count = 0
strong_neg_count = 0
neutral_count = 0
weak_neg_count = 0

for word,value in d1_unique_count.items():
    

    if(word in lexicon.keys()):
        #d1_strong_pos_count
        sent_value = lexicon[word]
        if (sent_value <= 1.0 and sent_value > 0.6):
            d1_strong_pos_count += value
            totalSum += value
        elif(sent_value <= 0.6 and sent_value > 0.2):
            d1_weak_pos_count += value
            
            totalSum += value
        elif(sent_value <= 0.2 and sent_value >= -0.2):
            d1_neutral_count += value
            
            totalSum += value
        elif (sent_value < -0.2 and sent_value >= -0.6):
            d1_weak_neg_count += value
            
            totalSum += value
        elif (sent_value >= -1.0 and sent_value < -0.6):
            d1_strong_neg_count += value
            
            totalSum += value
#print ("Strong Pos - ",d1_strong_pos_count)
#print ("Weak Pos - ",d1_weak_pos_count)
#print ("Weak Neg - ",d1_weak_neg_count)
#print ("Strong Neg - ",d1_strong_neg_count)
#print ("Neutral - ",d1_neutral_count)
bar_width = 1.6
xtick_data =["Negative", "Weak Negative", "Neutral", "Weak Postive", "Positive"]

#the histogram of the data
#print (totalSum)
xaxis = [0.1,1.1,2.1,3.1,4.1]

xticks = [-3, -1, 1, 3, 5]

strong_neg_percent = d1_strong_neg_count/totalSum
weak_neg_percent = d1_weak_neg_count/totalSum
neutral_percent = d1_neutral_count/totalSum
weak_pos_percent =d1_weak_pos_count/totalSum
strong_pos_percent = d1_strong_pos_count/totalSum


bins=[strong_neg_percent,weak_neg_percent,neutral_percent,weak_pos_percent,strong_pos_percent]

percent_of_words = [strong_neg_percent, weak_neg_percent, neutral_percent, weak_pos_percent, strong_pos_percent]
#http://matthiaseisen.com/pp/patterns/p0176/
mplot.bar(xticks,bins,bar_width, color ="blue", align = 'center')

mplot.xticks((xticks),xtick_data)



mplot.xlabel("Sentiment")
mplot.ylabel("Percent of Words")
mplot.title("Sentiment Distribution for challenge_2_" + filename)




mplot.show()





