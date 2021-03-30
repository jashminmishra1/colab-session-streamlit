import streamlit as st


def get_dataset(data):

    if data == 'Diabetes.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/diabetes.csv'
    elif data == 'Breast-Cancer.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/breast-cancer.csv'
    elif data == 'Glass.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/glass_csv.csv'
    elif data == 'Waveform.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/waveform.csv'
    elif data == 'Image.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/image.csv'
    elif data == 'Heart.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/heart.csv'
    elif data == 'Segment.csv':
        dataset = 'https://raw.githubusercontent.com/bullet-ant/algorithmComparisionApp/main/Datasets/segment_csv.csv'
    else:
        dataset = None
    return dataset


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
