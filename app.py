import streamlit as st
from PIL import Image
import os

cards = {
    '1': [
        {'month': 1, 'type': '광', 'image': 'images/Hwatu_January_Hikari.png'},
        {'month': 1, 'type': '띠', 'image': 'images/Hwatu_January_Tanzaku.png'},
        {'month': 1, 'type': '피', 'image': 'images/Hwatu_January_Kasu_1.png'},
        {'month': 1, 'type': '피', 'image': 'images/Hwatu_January_Kasu_2.png'},
    ],
    '2': [
        {'month': 2, 'type': '띠', 'image': 'images/Hwatu_February_Tanzaku.png'},
        {'month': 2, 'type': '피', 'image': 'images/Hwatu_February_Kasu_1.png'},
        {'month': 2, 'type': '피', 'image': 'images/Hwatu_February_Kasu_2.png'},
        {'month': 2, 'type': '끗', 'image': 'images/Hwatu_February_Tane.png'},
    ],
    '3': [
        {'month': 3, 'type': '광', 'image': 'images/Hwatu_March_Hikari.png'},
        {'month': 3, 'type': '띠', 'image': 'images/Hwatu_March_Tanzaku.png'},
        {'month': 3, 'type': '피', 'image': 'images/Hwatu_March_Kasu_1.png'},
        {'month': 3, 'type': '피', 'image': 'images/Hwatu_March_Kasu_2.png'},
    ],
    '4': [
        {'month': 4, 'type': '끗', 'image': 'images/Hwatu_April_Tane.png'},
        {'month': 4, 'type': '띠', 'image': 'images/Hwatu_April_Tanzaku.png'},
        {'month': 4, 'type': '피', 'image': 'images/Hwatu_April_Kasu_1.png'},
        {'month': 4, 'type': '피', 'image': 'images/Hwatu_April_Kasu_2.png'},
    ],
    '5': [
        {'month': 5, 'type': '끗', 'image': 'images/Hwatu_May_Tane.png'},
        {'month': 5, 'type': '띠', 'image': 'images/Hwatu_May_Tanzaku.png'},
        {'month': 5, 'type': '피', 'image': 'images/Hwatu_May_Kasu_1.png'},
        {'month': 5, 'type': '피', 'image': 'images/Hwatu_May_Kasu_2.png'},
    ],
    '6': [
        {'month': 6, 'type': '끗', 'image': 'images/Hwatu_June_Tane.png'},
        {'month': 6, 'type': '띠', 'image': 'images/Hwatu_June_Tanzaku.png'},
        {'month': 6, 'type': '피', 'image': 'images/Hwatu_June_Kasu_1.png'},
        {'month': 6, 'type': '피', 'image': 'images/Hwatu_June_Kasu_2.png'},
    ],
    '7': [
        {'month': 7, 'type': '끗', 'image': 'images/Hwatu_July_Tane.png'},
        {'month': 7, 'type': '띠', 'image': 'images/Hwatu_July_Tanzaku.png'},
        {'month': 7, 'type': '피', 'image': 'images/Hwatu_July_Kasu_1.png'},
        {'month': 7, 'type': '피', 'image': 'images/Hwatu_July_Kasu_2.png'},
    ],
    '8': [
        {'month': 8, 'type': '광', 'image': 'images/Hwatu_August_Hikari.png'},
        {'month': 8, 'type': '끗', 'image': 'images/Hwatu_August_Tane.png'},
        {'month': 8, 'type': '피', 'image': 'images/Hwatu_August_Kasu_1.png'},
        {'month': 8, 'type': '피', 'image': 'images/Hwatu_August_Kasu_2.png'},
    ],
    '9': [
        {'month': 9, 'type': '쌍', 'image': 'images/Hwatu_September_Tane.png'},
        {'month': 9, 'type': '띠', 'image': 'images/Hwatu_September_Tanzaku.png'},
        {'month': 9, 'type': '피', 'image': 'images/Hwatu_September_Kasu_1.png'},
        {'month': 9, 'type': '피', 'image': 'images/Hwatu_September_Kasu_2.png'},
    ],
    '10': [
        {'month': 10, 'type': '끗', 'image': 'images/Hwatu_October_Tane.png'},
        {'month': 10, 'type': '띠', 'image': 'images/Hwatu_October_Tanzaku.png'},
        {'month': 10, 'type': '피', 'image': 'images/Hwatu_October_Kasu_1.png'},
        {'month': 10, 'type': '피', 'image': 'images/Hwatu_October_Kasu_2.png'},
    ],
    '11': [
        {'month': 11, 'type': '광', 'image': 'images/Hwatu_November_Hikari.png'},
        {'month': 11, 'type': '피', 'image': 'images/Hwatu_November_Kasu_1.png'},
        {'month': 11, 'type': '쌍', 'image': 'images/Hwatu_November_Kasu_2.png'},
        {'month': 11, 'type': '피', 'image': 'images/Hwatu_November_Kasu_3.png'},
    ],
    '12': [
        {'month': 12, 'type': '광', 'image': 'images/Hwatu_December_Hikari.png'},
        {'month': 12, 'type': '끗', 'image': 'images/Hwatu_December_Tane.png'},
        {'month': 12, 'type': '띠', 'image': 'images/Hwatu_December_Tanzaku.png'},
        {'month': 12, 'type': '쌍', 'image': 'images/Hwatu_December_Kasu.png'},
    ],
}
import streamlit as st
from PIL import Image

# 카드 추가 함수
def add_card(selected_cards, card):
    selected_cards.append(card)

# 카드 제거 함수
def remove_card(selected_cards, card):
    selected_cards.remove(card)

# 카드 종류별 점수 계산 함수
def calculate_score(selected_cards):
    광 = [card for card in selected_cards if card['type'] == '광']
    끗 = [card for card in selected_cards if card['type'] == '끗']
    띠 = [card for card in selected_cards if card['type'] == '띠']
    피 = [card for card in selected_cards if card['type'] == '피']
    쌍 = [card for card in selected_cards if card['type'] == '쌍']

    score = 0
    광_count = len(광)
    끗_count = len(끗)
    띠_count = len(띠)
    피_count = len(피) + 2 * len(쌍)  # 쌍은 피 2장으로 계산

    # 광 점수 계산
    if any(card['month'] == 12 for card in 광):
        if 광_count >= 3:
            score += 2
        if 광_count >= 4:
            score += 1
        if 광_count == 5:
            score = 15
    else:
        if 광_count >= 3:
            score += 3
        if 광_count >= 4:
            score += 1
    
    # 끗 점수 계산
    if 끗_count >= 5:
        score += 끗_count - 4

    # 고도리 점수 계산
    고도리_월 = {2, 4, 8}
    고도리 = [card for card in selected_cards if card['type'] == '끗' and card['month'] in 고도리_월]
    if len(고도리) == 3:
        score += 5

    # 띠 점수 계산
    if 띠_count >= 5:
        score += 띠_count - 4
    
    # 홍단, 초단, 청단 점수 계산
    홍단_월 = {1, 2, 3}
    홍단 = [card for card in selected_cards if card['type'] == '띠' and card['month'] in 홍단_월]
    if len(홍단) == 3:
        score += 3

    초단_월 = {4, 5, 7}
    초단 = [card for card in selected_cards if card['type'] == '띠' and card['month'] in 초단_월]
    if len(초단) == 3:
        score += 3

    청단_월 = {6, 9, 10}
    청단 = [card for card in selected_cards if card['type'] == '띠' and card['month'] in 청단_월]
    if len(청단) == 3:
        score += 3
    
    # 피 점수 계산
    if 피_count >= 10:
        score += 피_count - 9
    
    return score

# Streamlit UI 구성
st.set_page_config(layout="wide")
col1, col2 = st.columns([8, 1])

with col1:
    st.title('고스톱 점수 계산기')

with col2:
    if st.button('초기화'):
        st.session_state.selected_cards = []

# 카드 선택 상태 유지
if 'selected_cards' not in st.session_state:
    st.session_state.selected_cards = []

# 선택한 카드 보여주기
st.subheader('내가 선택한 카드들:')

# 피, 띠, 끗, 광 순서대로 카드 분류
피 = [card for card in st.session_state.selected_cards if card['type'] == '피']
띠 = [card for card in st.session_state.selected_cards if card['type'] == '띠']
끗 = [card for card in st.session_state.selected_cards if card['type'] == '끗']
광 = [card for card in st.session_state.selected_cards if card['type'] == '광']

# 피 카드 표시
with st.expander("피", expanded=True):
    columns = st.columns(8)
    column_index = 0
    for card in 피:
        with columns[column_index]:
            st.image(card['image'], width=60)
            if st.button(f"제거", key=f"remove_{card['image']}"):
                remove_card(st.session_state.selected_cards, card)
                st.experimental_rerun()
        column_index = (column_index + 1) % 8

# 띠, 끗, 광 카드를 각각의 expander로 표시
cols = st.columns(3)

with cols[0]:
    with st.expander("띠", expanded=True):
        columns = st.columns(8)
        column_index = 0
        for card in 띠:
            with columns[column_index]:
                st.image(card['image'], width=60)
                if st.button(f"제거", key=f"remove_{card['image']}"):
                    remove_card(st.session_state.selected_cards, card)
                    st.experimental_rerun()
            column_index = (column_index + 1) % 8

with cols[1]:
    with st.expander("끗", expanded=True):
        columns = st.columns(8)
        column_index = 0
        for card in 끗:
            with columns[column_index]:
                st.image(card['image'], width=60)
                if st.button(f"제거", key=f"remove_{card['image']}"):
                    remove_card(st.session_state.selected_cards, card)
                    st.experimental_rerun()
            column_index = (column_index + 1) % 8

with cols[2]:
    with st.expander("광", expanded=True):
        columns = st.columns(8)
        column_index = 0
        for card in 광:
            with columns[column_index]:
                st.image(card['image'], width=60)
                if st.button(f"제거", key=f"remove_{card['image']}"):
                    remove_card(st.session_state.selected_cards, card)
                    st.experimental_rerun()
            column_index = (column_index + 1) % 8

# 현재 점수 보여주기
current_score = calculate_score(st.session_state.selected_cards)
st.write(f'현재 점수: {current_score} 점')

# 추가할 카드들 보여주기
st.subheader('추가할 카드들:')

# 두 개의 열로 나누어 카드 표시
num_columns = 8
columns = st.columns(num_columns)
column_index = 0

for month in cards:
    for card in cards[month]:
        if card not in st.session_state.selected_cards:
            card_image = Image.open(card['image'])
            with columns[column_index]:
                st.image(card_image, width=60)
                if st.button(f"{card['month']}월{card['type']}", key=card['image']):
                    add_card(st.session_state.selected_cards, card)
                    st.experimental_rerun()
            column_index = (column_index + 1) % num_columns

