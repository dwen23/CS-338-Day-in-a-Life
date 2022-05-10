from keytotext import pipeline

def sentence_generator(kw):

    nlp = pipeline("k2t-base")  #loading the pre-trained model
    params = {"do_sample":True, "num_beams":4, "no_repeat_ngram_size":2, "early_stopping":True}    #decoding params

    if kw["occupation"] == 'college' or kw["occupation"] == 'high school' or kw["occupation"] == 'school':
        fword1 = 'student'
    if kw["occupation"] == 'work':
        fword1 = 'job'




    s1 = nlp([kw["name"], 'wakes up', kw["wakeup"]], **params) + ' After that, ' + kw["name"]
    s2 = nlp([kw["name"], fword1, kw["occupation"], 'at', kw["workplace"]], **params) + ' Today at ' + kw["occupation"] + ', ' + kw["name"]
    s3 = nlp([kw["name"], 'favorite thing to do after', kw[2], 'is', kw[4]], **params) + kw["name"] + ' had a great time'
    s4 = nlp([kw["name"], 'eats', kw["food"], 'dinner'], **params) + kw["name"] + ' enjoyed'
    s5 = nlp([kw["name"], kw["sleep"], 'at night before going to bed'], **params) + ' It was a good way to end the day'

    return [s1, s2, s3, s4, s5]


    
