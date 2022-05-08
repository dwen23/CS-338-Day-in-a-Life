from keytotext import pipeline

def sentence_generator(key_words):

    key_words[0]

    nlp = pipeline("k2t-base")  #loading the pre-trained model
    params = {"do_sample":True, "num_beams":4, "no_repeat_ngram_size":2, "early_stopping":True}    #decoding params


    sentence_one = nlp([key_words[0], 'morning', key_words[1]], **params)
    sentence_two = nlp(['Later', 'go to', key_words[2], key_words[3]], **params)
    sentence_three = nlp(['After', key_words[3], 'enjoy', key_words[4]], **params)
    sentence_four = nlp(['dinner', key_words[5]], **params)
    sentence_five = nlp(['night', key_words[6]], **params)


    
