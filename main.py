from transformers import pipeline
import uvicorn
import os
from fastapi import FastAPI, File, UploadFile
from starlette.middleware.cors import CORSMiddleware
from keytotext import pipeline


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,

    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)
story_gen = pipeline("text-generation", "jcpwfloi/gpt2-story-generation", handle_long_generation="hole", early_stopping=False)


@app.post('/generate')
def sentence_generator(key_words: str = None):

    key_words[0]

    nlp = pipeline("k2t-base")  #loading the pre-trained model
    params = {"do_sample":True, "num_beams":4, "no_repeat_ngram_size":2, "early_stopping":True}    #decoding params


    sentence_one = nlp([key_words[0], 'morning', key_words[1]], **params)
    sentence_two = nlp(['Later', 'go to', key_words[2], key_words[3]], **params)
    sentence_three = nlp(['After', key_words[3], 'enjoy', key_words[4]], **params)
    sentence_four = nlp(['dinner', key_words[5]], **params)
    sentence_five = nlp(['night', key_words[6]], **params)

    return generate(sentence_one) 





async def generate(sentence):
    try:
        return story_gen(sentence)
    except Exception as e:
        LOGGER.error(e)
        return {'status': False, 'msg': e}, 400

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000)