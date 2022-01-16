from statistics import quantiles
import streamlit as st
from annotated_text import annotated_text
from random import choice as grand
import gen


st.set_page_config(page_title="Генератор отзывов", page_icon=":pleading_face:")

@st.cache
def read_templates():
    return gen.read_templates("templates.json")

templates = read_templates()

@st.cache
def read_words():
    return gen.read_words_dict("words.csv")

words = read_words()

st.title("Генератор отзывов")

fields = dict()

fields["name"] = st.text_input("Имя")
fields["marks"] = str(st.slider("Успеваемость", value=5, min_value=1, max_value=5, step=1))
fields["work_class"] = str(st.slider("Работа в классе", value=5,
                       min_value=1, max_value=5, step=1))
fields["work_home"] = str(st.slider("Работа дома", value=5, min_value=1, max_value=5, step=1))
fields["discipline"] = str(st.slider("Дисциплина", value=5, min_value=1, max_value=5, step=1))
fields["qualities"] = st.text_input("Особые качества (в винительном падеже)")
fields["additional"] = " " + st.text_input("Дополнительный комментарий (в конец отзыва)")


if st.button("Сгенерировать"):
    st.code(str(gen.Review(words, grand(templates), fields)))
