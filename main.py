from transformers import pipeline
import uvicorn
import os
from fastapi import FastAPI, File, UploadFile
from starlette.middleware.cors import CORSMiddleware
from sentence_generator import sentence_generator



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
        LOGGER.error(e)
        return {'status': False, 'msg': e}, 400

@app.post('/input')
async def input(words: list = None):
    try:
        results = sentence_generator(words)
        return generate(results[0])
    except Exception as e:
        LOGGER.error(e)
        return {'status': False, 'msg': e}, 400

if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=8000)