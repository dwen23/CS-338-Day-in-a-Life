from keytotext import pipeline

def sentence_generator(key_words):

    key_words[0]

    nlp = pipeline("k2t-base")  #loading the pre-trained model
    params = {"do_sample":True, "num_beams":4, "no_repeat_ngram_size":2, "early_stopping":True}    #decoding params


    s1 = nlp([key_words[0], 'morning', key_words[1]], **params)
    s2 = nlp(['Later', 'go to', key_words[2], key_words[3]], **params)
    s3 = nlp(['After', key_words[2], 'enjoy', key_words[4]], **params)
    s4 = nlp(['dinner', key_words[5]], **params)
    s5 = nlp(['night', key_words[6]], **params)

    return [s1, s2, s3, s4, s5]


    
