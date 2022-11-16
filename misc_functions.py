import numpy as np
from Data_Formation import get_dataframe
import streamlit as st


def calculate_class_weights(y):
    unique_categories, counts = np.unique(y, return_counts=True)
    counts = counts/counts.sum()
    weights_dict = {i: j for i, j in enumerate(counts)}
    return weights_dict

def select_columns(file):
    if file is not None:
        train_dataframe, _ = get_dataframe(file)
        dataset_columns = st.sidebar.multiselect("Выберите столбцы для обучения нейросети",
                       options=train_dataframe.columns.values, default=train_dataframe.columns.values
                       )
    return file, dataset_columns

def train_buttons_callback():
    st.session_state.train_button_clicked = True
    st.session_state.model_trained = False

def test_buttons_callback():
    st.session_state.train_button_clicked = True