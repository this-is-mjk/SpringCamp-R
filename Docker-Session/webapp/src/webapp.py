from flask import Flask, render_template, request, redirect, url_for
import os
import json
import random
import PIL.Image

app = Flask(__name__)
app.config

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/image')
def image():
    img_flag = True
    path = './pclub.png'
    try:
        img = PIL.Image.open(path)
        img_flag = True
    except:
        print(path, "Unable to find image ")
    width, height = img.size
    aspect_ratio = height/width
    new_width = 120
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))
    img = img.convert('L')
    chars = ["P", "B", "0", "u", "b", "P", ".", "L", "c", ",", "."]
    pixels = img.getdata()
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "<br>".join(ascii_image)
    return ascii_image

@app.route('/gaali')
def gaali():
    n = int(request.args.get('n', 1))
    html_response = "" 
    for i in range(n):
        with open('foo.txt','r') as f:
            t=f.read()
            lines = t.splitlines()
            html_response += random.choice(lines) + "<br>"

    return html_response
    


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')