from keytotext import pipeline

def sentence_generator(key_words):

    nlp = pipeline("k2t-base")  #loading the pre-trained model
    params = {"do_sample":True, "num_beams":4, "no_repeat_ngram_size":2, "early_stopping":True}    #decoding params


    s1 = nlp([key_words[0], 'starts the morning', key_words[1]], **params)
    s2 = nlp([key_words[0], 'goes to', key_words[2], 'at', key_words[3]], **params)
    s3 = nlp([key_words[0], key_words[4], 'after', key_words[2]], **params)
    s4 = nlp([key_words[0], 'eats', key_words[5], 'for dinner after', key_words[4]], **params)
    s5 = nlp([key_words[0], key_words[6], 'before going to bed', 'night'], **params)

    return [s1, s2, s3, s4, s5]


    
