#===============================================================================================#

# Imports

#===============================================================================================#

import streamlit as sl

import pandas as pd
import numpy as np

import pickle

from nltk.tokenize import RegexpTokenizer

from tensorflow.keras.models import load_model
from keras.preprocessing import sequence

#===============================================================================================#

# Functions and Models Prepared

#===============================================================================================#

word_index_dict = pickle.load(open('Models/word_index_dict.pkl','rb'))

neural_net_model = load_model('Models/Neural_Network.h5')

tokenizer = RegexpTokenizer(r'[a-zA-Z]+')

def index_review_words(text):
    review_word_list = []
    for word in text.lower().split():
        if word in word_index_dict.keys():
            review_word_list.append(word_index_dict[word])
        else:
            review_word_list.append(word_index_dict['<UNK>'])

    return review_word_list 

def add_sum_suffix(text):
    
    token_list = tokenizer.tokenize(text.lower())
    new_text = ''
    for word in token_list:
        word = word + '_sum'
        new_text += word + ' '
        
    return new_text

def text_cleanup(text):
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    token_list = tokenizer.tokenize(text.lower())
    new_text = ''
    for word in token_list:
        new_text += word + ' '
        
    return new_text
#===============================================================================================#

# Streamlit

#===============================================================================================#

sl.title("Hotel Review Classifier Application")
page_bg_img = '''
<style>
body {
background-image: url('https://images.unsplash.com/photo-1454388683759-ee76c15fee26?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80');
background-repeat: no-repeat;
background-size: cover;
}
.block-container {
    backdrop-filter: blur(0px);
}
.markdown-text-container > h1{text-align:center}
.css-1sls4c0 {
    background:none;
        backdrop-filter: blur(10px);
}
.stApp {
    background:transparent;
}
.st-cn {
    background-color: aliceblue;
</style>


'''


sl.markdown(page_bg_img, unsafe_allow_html=True)


review_summary_text = sl.text_input('Enter Your Review Summary Here')
review_text = sl.text_area('Enter Your Review Here')

if sl.button('Predict'):
    
    result_review_sum = review_summary_text.title()
    
    result_review = review_text.title()

    review_summary_text = add_sum_suffix(review_summary_text)

    review_text = text_cleanup(review_text)

    review_text = index_review_words(review_text)

    review_summary_text = index_review_words(review_summary_text)

    all_review_text = review_text + review_summary_text

    all_review_text = sequence.pad_sequences([all_review_text],value=word_index_dict['<PAD>'],padding='post',maxlen=250)

    prediction = neural_net_model.predict(all_review_text)
    
    prediction = np.argmax(prediction)
    
    sl.success(prediction+1)
import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb


def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1
    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        hr(
            style=style_hr
        ),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)


# def footer():
#     myargs = [
#         "Made in ",
#         image('https://avatars3.githubusercontent.com/u/45109972?s=400&v=4',
#               width=px(25), height=px(25)),
#         " with ❤️ by Avinash Nair",
#         link("https://www.linkedin.com/in/avinash-nair-299b72157/", "@AvinashNair"),
#         br(),
        
#     ]
#     layout(*myargs)


# if __name__ == "__main__":
#     footer()
