import streamlit as st
from langchain_aws import ChatBedrock
from langchain_community.chat_message_histories import DynamoDBChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatMessagePromptTemplate, MessagesPlaceholder


# セッションIDを定義
if "session_id" not in st.session_state:
    st.session_state.session_id = "session_id"

# セッションに会話履歴を定義
if "history" not in st.session_state:
    st.session_state.history = DynamoDBChatMessageHistory(
        table_name="bsc_db", session_id=st.session_state.session_id
    )

# セッションにLangChainの処理チェーンを定義
