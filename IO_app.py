import streamlit as st
import base64
import json, os
import pandas as pd

from io import BytesIO
from openai import OpenAI
from PIL import Image

from ollama import Client

from  dotenv import load_dotenv

load_dotenv()

def intro():
    import streamlit as st

    st.write("# 欢迎来到IO的世界")
    st.sidebar.success("选择一个功能.")

    st.markdown(
        """
        IO并不是Input output的缩写。而是Inner Orientation的缩写，向心所求。创造这个应用的初衷是将太多的复杂概念简单话，直面个体内向所需与的功能。而不是为了概念化而概念化。
        引发我思考的是多年前阅读的一本介绍悖论的小书庞德斯通的《推理的迷宫》，它让我思考过度的概念会导致的悖论将以怎么样的面目示人。
    """
    )

page_names_to_funcs = {
    "—": intro,
}



demo_name = st.sidebar.selectbox("选择功能", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
