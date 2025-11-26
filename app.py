import streamlit as st
from rag import get_rag_chain, setup_env

def setup_chat():
    st.set_page_config(page_title="SecureGov RAG", page_icon="🛡️")
    st.title("SecureGov RAG Agent")

    if "chain" not in st.session_state:
        with st.spinner("Loading RAG Pipeline..."):
            try:
                setup_env()
                st.session_state.chain = get_rag_chain()
                st.success("System ready.")
            except Exception as e:
                st.error(f"Failed to load RAG chain: {e}")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask about your documents..."):
        if prompt.lower() in ["exit", "quit", "q"]:
            st.warning("Ending session... Refresh the page to start over.")
            st.stop()
                
        with st.chat_message("user"):
            st.markdown(prompt)
            
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Thinking...")
            
            try:
                response = st.session_state.chain.invoke({"input": prompt})
                answer = response["answer"]
                
                message_placeholder.markdown(answer)
                
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                message_placeholder.error(f"Error {e}")

def main():
    setup_chat()

if __name__ == "__main__":
    main()