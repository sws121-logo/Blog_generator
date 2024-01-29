import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


# Function to get response from LLma2 model

def getLLamaResponse(input_text,no_words,blog_style):
# LLama 2 model
        llm=CTransformers(model="C:/Users/saura/OneDrive/Desktop/Mira/models/llama-2-7b-chat.ggmlv3.q8_0.bin",
                          model_type="llama",
                          config={'max_new_tokens':256,
                                  "temperature":0.02})
# prompt template
        template='''
             write a blog for {blog_style} job profile for a topic{input_text}
             within {no_words} words.
              '''
        prompt=PromptTemplate(input_variables=['blog_style','input_text','no_words'],
                              template=template)
        
#  GEnerate The Response From LLama2 model
        response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
        print(response)
        return response
        
        
        
        
st.set_page_config(page_title="Generate Blogs",
                     page_icon="🧊",
            layout="centered",
            initial_sidebar_state="collapsed")
st.header("Generate Blogs 🧊 ")

input_text=st.text_input("Enter The Blog Topic")

#  creating two more columns for additional two more fields
col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input("No Of Words")
with col2:
    blog_style=st.selectbox("writing the blog for",
                            ('Researchers','Data Scientist','Common People'),index=0)

submit=st.button("Generate")

# Final Response
if submit:
    st.write(getLLamaResponse(input_text,no_words,blog_style))