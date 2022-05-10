from transformers import pipeline
import uvicorn
import os
from fastapi import FastAPI, File, UploadFile
from starlette.middleware.cors import CORSMiddleware
from sentence_generator import sentence_generator



# app = FastAPI()
# origins = ["*"]
# app.add_middleware(
#     CORSMiddleware,

#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],

# )

story_gen = pipeline("text-generation", "jcpwfloi/gpt2-story-generation", handle_long_generation="hole", early_stopping=False)


def generate(sentence):
    try:
        return story_gen(sentence)
    except Exception as e:
        # LOGGER.error(e)
        return {'status': False, 'msg': e}, 400

def input(words: list = None):
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
        return generate_text
    except Exception as e:
        # LOGGER.error(e)
        return {'status': False, 'msg': e}, 400

if __name__ == '__main__':
    # uvicorn.run(app=app, host='0.0.0.0', port=8000)
    ex = {"name": "Emily", "wakeup": "take a shower", "occupation": "college", "workplace": "Northwestern", "hobbies": "hang out with friends", "food": "pasta", "sleep": "finish homework"}

    print(input(ex))