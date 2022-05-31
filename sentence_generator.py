from torch import _standard_gamma_grad
from keytotext import pipeline

def sentence_generator(kw):

    nlp = pipeline('k2t-base')  #loading the pre-trained model
    params = {'do_sample':True, 'num_beams':4, 'no_repeat_ngram_size':2, 'early_stopping':True}    #decoding params

    spronoun = cleanPronoun(kw['sPronouns'])
    ppronoun = cleanPronoun(kw['pPronouns'])

    # print(spronoun) 

    for key in kw:
        kw[key] = changePronouns(kw[key], spronoun, ppronoun)
 
    if kw['living'] == 'college':
        s1 = kw['name'] + ' wakes up this morning and has to go to school. ' + nlp(['This morning,', spronoun, 'starts the day by', kw['wake']], **params) + ' ' + spronoun.capitalize() + ' gets ready for school by'
        s2 = nlp([spronoun, 'student', 'at', kw['school']], **params) + ' Today at school, ' + kw['name']
        s3 = 'While ' + spronoun + ' is at school, ' + spronoun + ' sees a ' + kw['fear'] + ' running towards ' + ppronoun + ' friend. ' + spronoun.capitalize()
        s4 = 'After the incident with the ' + kw['fear'] + ', ' + kw['name'] + ' goes to class. ' + nlp([ppronoun, 'favorite class', kw['college']]) + ' During class,'
        s5 = nlp([ppronoun, 'favorite thing to do after school is', kw['hobby']], **params) + ' Today, ' + kw['name'] + ' had a great time'
    elif kw['living'] == 'high school':
        s1 = kw['name'] + ' wakes up this morning and has to go to school. ' + nlp(['This morning,', spronoun, 'starts the day by', kw['wake']], **params) + ' ' + spronoun.capitalize() + ' gets ready for school by'
        s2 = nlp([spronoun, 'is', kw['living'], 'student'], **params) + ' Today at school, ' + kw['name']
        s3 = 'While ' + spronoun + ' is at school, ' + spronoun + ' sees a ' + kw['fear'] + ' running towards ' + ppronoun + ' friend. ' + spronoun.capitalize()
        s4 = 'After the incident with the ' + kw['fear'] + ', ' + kw['name'] + ' goes to ' + kw['high school'] + ' class. Later ' + ppronoun + ' has a test in ' + kw['lSubject']
        s5 = nlp([ppronoun, 'favorite thing to do after school is', kw['hobby']], **params)  + ' Today, ' + kw['name'] + ' had a great time'
    elif kw['living'] == 'work':
        s1 = kw['name'] + ' wakes up this morning and has to go to work. ' + nlp(['This morning,', spronoun, 'starts the day by', kw['wake']], **params) + ' ' + spronoun.capitalize() + ' gets ready for work by'
        s2 = nlp([spronoun, 'works', kw['work']], **params) + ' Today while ' + spronoun + ' is at work, ' + spronoun
        s3 = 'While ' + spronoun + ' is at work ' + spronoun + ' sees a ' + kw['fear'] + ' coming towards ' + ppronoun + ' coworker. ' + spronoun.capitalize()
        s4 = 'After the incident with the ' + kw['fear'] + ', ' + kw['name'] + ' keeps working. ' +  nlp(['At work', spronoun, 'her boss tells her to', kw['doWork']], **params) + ' Today,'      
        s5 = nlp(['After work,', ppronoun, 'favorite thing to do is', kw['hobby']], **params)  + ' Today, ' + kw['name'] + ' had a great time'

    elif kw['living'] == 'nothing':
        s1 = nlp([kw['name'], 'wakes up', kw['wake']], **params) + ' As ' + spronoun + ' gets ready for the day' 
        s2 = nlp([spronoun, kw['nothing']], **params) + ' Today, ' + kw['name']
        s3 = nlp(['Today', 'fear', kw['fear']], **params) + ' It was ' + spronoun + ' worst nightmare'
        s4 = nlp([ppronoun, 'favorite thing to do is', kw['hobby']], **params) + " " + spronoun + ' had a great time'
        s5 = nlp([spronoun, 'lives', kw['city']] **params) + ' So, today'
        s6 = nlp([spronoun, 'eats', kw['food'], 'dinner'], **params) + ' ' + spronoun + ' enjoyed'
        s7 = nlp([spronoun, kw['bed'], 'at night before going to bed'], **params) + ' It was a good way to end the day'
        s_list = [s1, s2, s3, s4, s5, s6, s7]
        for i, s in enumerate(s_list):
            s_list[i] = wasToIs(s)
            s_list[i] = noSheena(s_list[i])
        return s_list

    s6 = nlp([spronoun, 'lives', kw['city']], **params) + ' ' + spronoun.capitalize() + ' likes the area because'
    s7 = spronoun.capitalize() + ' eats ' + kw['food'] + ' for dinner today. She enjoyed' 
    s8 = nlp(['Before going to bed,', kw['name'], 'likes to', kw['bed']], **params) + ' Today as she gets ready for bed,'

    s_list = [s1, s2, s3, s4, s5, s6, s7, s8]
    for i, s in enumerate(s_list):
        s_list[i] = wasToIs(s)
        s_list[i] = noSheena(s_list[i])
    return s_list

def changePronouns(phrase, spronoun, ppronoun):
    phrase_list = phrase.split(' ')
    for i, word in enumerate(phrase_list):
        word = word.lower()
        if word == "my":
            phrase_list[i] = ppronoun
        if word == "my,":
            phrase_list[i] = ppronoun + ","
        if word == "i":
            phrase_list[i] = spronoun
        if word == "i,":
            phrase_list[i] = spronoun + ","
    phrase = " ".join(phrase_list)
    return phrase

    
def cleanPronoun(pronoun):
    pronoun = pronoun.split('/')[0]
    pronoun = pronoun.split(',')[0]
    pronoun = pronoun.split(' ')[0]
    return pronoun

def wasToIs(s):
    s = s.split(' ')
    for i, word in enumerate(s):
        # print(word)
        if word == "was":
            s[i] = "is"
    s = " ".join(s)
    return s

def noSheena(s):
    s = s.split(' ')
    for i, word in enumerate(s):
        # print(word)
        if word == "Sheena":
            s[i] = "She"
        if word == "sheena":
            s[i] = "she"
        if word == "Sheena's":
            s[i] = "She"
        if word == "sheena's":
            s[i] = "she"
        if word == "Shepars":
            s[i] = "She"
        if word == "shepars":
            s[i] = "she"
    s = " ".join(s)
    return s