import io
import uvicorn
import pathlib

from PIL import Image


from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as tf_image


app = FastAPI()
# Загрузка предварительно обученной модели
model = load_model('model_I.h5')

class_labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

app.mount("/static", StaticFiles(directory="static"), name="static")

BASE_DIR = pathlib.Path(__file__).parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get('/', response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/uploadfile/")
async def upload_photo(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    resized_image = image.resize((32, 32))
    img_array = tf_image.img_to_array(resized_image)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)
    predicted_class = class_labels[predicted_class_index]
    img_byte_array = io.BytesIO()
    resized_image.save(img_byte_array, format='JPEG')
    img_byte_array = img_byte_array.getvalue()
    print(predicted_class)
    return StreamingResponse(io.BytesIO(contents), media_type="image/jpeg", headers={"Predicted-Class": predicted_class}) #, content_type="image/jpeg"


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)



# @app.post("/uploadfile/")
# async def upload_photo(file: UploadFile = File(...)):
#     contents = await file.read()
#     image = Image.open(io.BytesIO(contents))
#     resized_image = image.resize((32, 32))
#     output_buffer = io.BytesIO()
#     resized_image.save(output_buffer, format="JPEG", quality=95)
#     compressed_contents = output_buffer.getvalue()
#     return StreamingResponse(io.BytesIO(compressed_contents), media_type="image/jpeg")