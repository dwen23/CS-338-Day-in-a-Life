from transformers import pipeline
import json
import uvicorn
import os
from fastapi import FastAPI, File, UploadFile
from starlette.middleware.cors import CORSMiddleware
from sentence_generator import sentence_generator

# from flask import Flask

# app = Flask(__name__)

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


def generate(sentence):
    try:
        return story_gen(sentence)
    except Exception as e:
        # LOGGER.error(e)
        return {'status': False, 'msg': e}, 400

@app.post('/generate')
def input(words:dict):
    # words = json.loads(words)
    results = sentence_generator(words)
    # print(results)
    try:
        results = sentence_generator(words)
        generate_text = ''
        for i, sentence in enumerate(results):
            if i != 0:
                prev_text = generate_text.rsplit('.', 2)[1]
                # print(prev_text)
                generate_text = generate_text.rsplit('.', 2)[0] + '.'
                raw_text = generate(prev_text + '. ' + sentence)[0]['generated_text'].rsplit('.', 1)[0] + '.'
            else:
                raw_text = generate(sentence)[0]['generated_text'].rsplit('.', 1)[0] + '.'
            generate_text += raw_text + ' '
        return {'text': generate_text}
    except Exception as e:
        # LOGGER.error(e)
        return {'status': False, 'msg': e}, 400

if __name__ == '__main__':
    # uvicorn.run(app=app, host='0.0.0.0', port=8000)
    print(input({"name": "Emily", "sPronouns": "she", "pPronouns": "her", "wake": "make breakfast", "living": "college",
                "school": "Northwestern", "college": "computer science", "fear": "tiger", "hobby": "hang out with my friends",
                "city": "Evanston", "food": "pasta", "bed": "finish my homework"}))
    # app.run(debug=True)

