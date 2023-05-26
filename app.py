# import gradio as gr


# def greet(name):
#     return "Hello " + name + "!!!"


# iface = gr.Interface(fn=greet, inputs="text", outputs="text")
# iface.launch()

# AUTOGENERATED! DO NOT EDIT! File to edit: ../cat-vs-dog.ipynb.

# %% auto 0
__all__ = [
    "learn",
    "categories",
    "image",
    "label",
    "examples",
    "intf",
    "is_cat",
    "classify_image",
]

# %% ../cat-vs-dog.ipynb 3
from fastai import *
from fastai.vision.all import *
import gradio as gr


# %% ../cat-vs-dog.ipynb 4
# Define function to label the data based on filename rule from dataset creators
def is_cat(x):
    return "cat" if x.name[0].isupper() else "dog"


# %% ../cat-vs-dog.ipynb 18
learn = load_learner("export.pkl")

# %% ../cat-vs-dog.ipynb 19
categories = ("Cat", "Dog")


def classify_image(img):
    pred, idx, probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))


# %% ../cat-vs-dog.ipynb 20
image = gr.Image(shape=(192, 192))
label = gr.Label()
examples = ["dog.jpg", "cat.jpg"]

intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)
intf.launch(inline=False, share=True)
