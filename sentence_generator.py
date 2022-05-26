from keytotext import pipeline

def sentence_generator(kw):

    nlp = pipeline('k2t-base')  #loading the pre-trained model
    params = {'do_sample':True, 'num_beams':4, 'no_repeat_ngram_size':2, 'early_stopping':True}    #decoding params

    spronoun = cleanPronoun(kw['sPronouns'])
    ppronoun = cleanPronoun(kw['pPronouns'])

    s1 = nlp([kw['name'], 'wakes up', kw['wake']], **params) + ' After that, ' + spronoun
 
    if kw['living'] == 'college':
        s2 = nlp([spronoun, 'student', kw['living'], 'at', kw['school']], **params) + ' Today at ' + kw['living'] + ', ' + kw['name']
        s4 = nlp([ppronoun, kw['college'], 'exam']) + ' Then ' + spronoun + ' went name'
    elif kw['living'] == 'high school':
        s2 = nlp([spronoun, kw['living'], 'student'], **params) + ' Today at school, ' + kw['name']
        s4 = nlp([spronoun, 'enjoyed', kw['high school'], 'and' 'test', kw['lSubject']], **params) + ' Then ' + spronoun + ' went name'
    elif kw['living'] == 'work':
        s2 = nlp([spronoun, 'works', kw['work']], **params) + ' Today at school, ' + kw['name']
        s4 = nlp([spronoun, kw['doWork']], **params) + ' Then ' + spronoun + ' went name'
    elif kw['living'] == 'nothing':
        s2 = nlp([spronoun, kw['nothing']], **params) + ' Today, ' + kw['name']
        s3 = nlp(['Today', 'fear', kw['fear']], **params) + ' It was ' + spronoun + ' worst nightmare'
        s4 = nlp([ppronoun, 'favorite thing to do is', kw['hobby']], **params) + ' ' + spronoun + ' had a great time'
        s5 = nlp([spronoun, 'lives', kw['city']] **params) + ' So, today'
        s6 = nlp([spronoun, 'eats', kw['food'], 'dinner'], **params) + ' ' + spronoun + ' enjoyed'
        s7 = nlp([spronoun, kw['bed'], 'at night before going to bed'], **params) + ' It was a good way to end the day'
        return [s1, s2, s3, s4, s5, s6, s7]


    s3 = nlp(['Today at', kw['living'], 'fear', kw['fear']], **params) + ' It was ' + spronoun + ' worst nightmare'
    s5 = nlp([spronoun, 'favorite thing to do after', kw['living'], 'is', kw['hobby']], **params) + kw['name'] + ' had a great time'
    s6 = nlp([spronoun, 'lives', kw['city']], **params) + ' So, today'
    s7 = nlp([spronoun, 'eats', kw['food'], 'dinner'], **params) + kw['name'] + ' enjoyed'
    s8 = nlp([spronoun, kw['bed'], 'at night before going to bed'], **params) + ' It was a good way to end the day'

    return [s1, s2, s3, s4, s5, s6, s7, s8]


    
def cleanPronoun(pronoun):
    pronoun = pronoun.split('/')[0]
    pronoun = pronoun.split(',')[0]
    pronoun = pronoun.split(' ')[0]
    return pronoun