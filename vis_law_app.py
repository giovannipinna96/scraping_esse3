import streamlit as st

from utils_law_app import read_json

json_data = read_json("clean_sentenze.json")

tot_num_sentences = len(json_data["b_llama-2-13b-law-gpt_train_500_base.json"])  # TODO generalize

change_name_dict = {
    "b_llama-2-13b-law-gpt_train_500_base.json": "LLaMA2 13B base",
    "b_llama-2-7b-law-gpt_train_500_base.json": "LLaMA2 7B base",
    "b_moe7summ__train_500_base.json": "MoE 8x7B (Mixtral of experts) base",
    "c_llamantino7summarization_train_500.json": "Llamantino 7B nostro",
    "c_llamantino13summarization_train_500.json": "Llamantino 13B nostro",
    "c_llama2_13b_summarization_train_500.json": "LLaMA2 13B nostro",
    "c_llama2_7b_summarization_train_500.json": "LLaMA2 7B nostro",
    "b_llamantino13summarization_train_500_evalita.json": "Llamantino 13B trained on EvalITA data (non nostro)",
    "b_llamantino7summarization_train_500_evalita.json": "Llamantino 7B trained on EvalITA data (non nostro)",
    "b_llama-2-13b-law-gpt_train_500_chat.json": "LLaMA2 13B Chat (non nostro)",
    "b_llama-2-7b-law-gpt_train_500_chat.json": "LLaMA2 7B Chat (non nostro)",
    "b_llamantino7summarization_train_500_chat.json": "Llamantino 7B Chat (non nostro)",
    "b_llamantino13summarization_train_500_chat.json": "Llamantino 13B Chat (non nostro)",
    "c_moe7summ__train_500.json": "MoE 8x7B (Mixtral of experts) nostro",

}

# st.write(json_data.keys())
# st.write(json_data["llama-2-7b-law-gpt_train_500.json"][0].keys())

# Set page title
st.title('LawGPT summarization')

# Sidebar
st.sidebar.title('Sentence Number')
# option = st.sidebar.selectbox(
#    'Select an option',
#    ('Option 1', 'Option 2', 'Option 3')
# )

num_sentence = st.sidebar.slider('Number', 0, tot_num_sentences - 1, 1)
st.divider()
# GOLD
with st.expander("Sentence"):
    st.write(json_data["c_llama-2-7b-law-gpt_train_500.json"][num_sentence]["request"][0])

with st.expander("Gold summary"):
    st.write(json_data["c_llama-2-7b-law-gpt_train_500.json"][num_sentence]["gold"])
st.divider()
for model in json_data.keys():
    try:
        with st.expander(change_name_dict[model]):
            st.write(json_data[model][num_sentence]['generated_clean'])
            # st.write(model)
    except:
        pass

# My models
# st.divider()
# with st.expander("llamantino 7B"):
#     st.write(json_data["b_llama-2-7b-law-gpt_train_500_base.json"][num_sentence]['generated_total'])
#
# with st.expander("llamantino 13B"):
#     st.write(json_data["b_llama-2-13b-law-gpt_train_500_base.json"][num_sentence]['generated_total'])

# with st.expander("llama 7B"):
#     st.write("This is a simple Streamlit app with a title, a description in a collapsed bar, and a sidebar.")
#
# with st.expander("llama 7B"):
#     st.write("This is a simple Streamlit app with a title, a description in a collapsed bar, and a sidebar.")
#
# with st.expander("MoE"):
#     st.write("This is a simple Streamlit app with a title, a description in a collapsed bar, and a sidebar.")
#
# # Base Models
# st.divider()
# with st.expander("llamantino 7B BASE"):
#     st.write("This is a simple Streamlit app with a title, a description in a collapsed bar, and a sidebar.")
#
# with st.expander("llamantino 13B BASE"):
#     st.write("This is a simple Streamlit app with a title, a description in a collapsed bar, and a sidebar.")
#
# with st.expander("llama 7B BASE"):
#     st.write("This is a simple Streamlit app with a title, a description in a collapsed bar, and a sidebar.")
#
# with st.expander("llama 7B BASE"):
#     st.write("This is a simple Streamlit app with a title, a description in a collapsed bar, and a sidebar.")
#
# with st.expander("MoE BASE"):
#     st.write("This is a simple Streamlit app with a title, a description in a collapsed bar, and a sidebar.")
#
# # Chat models
# st.divider()
# with st.expander("llamantino 7B CHAT"):
#     st.write("This is a simple Streamlit app with a title, a description in a collapsed bar, and a sidebar.")
#
# with st.expander("llamantino 13B CHAT"):
#     st.write("This is a simple Streamlit app with a title, a description in a collapsed bar, and a sidebar.")
#
# with st.expander("llama 7B CHAT"):
#     st.write("This is a simple Streamlit app with a title, a description in a collapsed bar, and a sidebar.")
#
# with st.expander("llama 7B CHAT"):
#     st.write("This is a simple Streamlit app with a title, a description in a collapsed bar, and a sidebar.")
#
# with st.expander("MoE CHAT"):
#     st.write("This is a simple Streamlit app with a title, a description in a collapsed bar, and a sidebar.")
