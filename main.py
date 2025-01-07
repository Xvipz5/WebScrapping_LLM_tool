import streamlit as st
from scrape import (
    scrape_website, 
    split_dom_content, 
    clean_body_content,
    extract_body_content
)

from parse import parse_with_ollama

#Streamlit UI title
st.title("AI Web Scrapper")
url = st.text_input("Enter a website URL: ")

#Scrapper
if st.button("Scrape Site"):
    st.write("Scrapping the website")

    #Scrape Action
    dom_content = scrape_website(url)
    body_content = extract_body_content(dom_content)
    cleaned_content = clean_body_content(body_content)

    #Storring DOM content
    st.session_state.dom_content = cleaned_content

    #Showing DOM Content
    with st.expander("view DDM Content"):
        st.text_area("DOM Content", cleaned_content, height = 300)


#Ask Ai what to Parse
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            #Parsing with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)