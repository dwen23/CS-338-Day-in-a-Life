from keytotext import pipeline

def sentence_generator(key_words):

    nlp = pipeline("k2t-base")  #loading the pre-trained model
    params = {"do_sample":True, "num_beams":4, "no_repeat_ngram_size":2, "early_stopping":True}    #decoding params

    if key_words[2] == 'college' or key_words[2] == 'high school' or key_words[2] == 'school':
        fword1 = 'student'
    if key_words[2] == 'work':
        fword1 == 'job'




    s1 = nlp([key_words[0], 'wakes up', key_words[1]], **params) + ' After that, ' + key_words[0]
    s2 = nlp([key_words[0], fword1, key_words[2], 'at', key_words[3]], **params) + ' Today at ' + key_words[3] + ', ' + key_words[0]
    s3 = nlp([key_words[0], 'favorite thing to do after', key_words[2], 'is', key_words[4]], **params) + key_words[0] + ' had a great time'
    s4 = nlp([key_words[0], 'eats', key_words[5], 'for dinner'], **params) + key_words[0] + ' enjoyed'
    s5 = nlp([key_words[0], key_words[6], 'at night before going to bed'], **params) + ' It was a good way to end the day'

    return [s1, s2, s3, s4, s5]


    
