import streamlit as st
from pathlib import Path

from faq import ingest_faq_data, faq_chain
from sql import sql_chain
from router import router


# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="ShopAssist AI",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------------
# Custom Styling
# ---------------------------------
st.markdown("""
<style>
    .main {
        padding-top: 1rem;
    }

    .block-container {
        max-width: 1000px;
        padding-top: 1rem;
    }

    .chat-title {
        text-align: center;
        padding-bottom: 10px;
    }

    .chat-subtitle {
        text-align: center;
        color: #888;
        margin-bottom: 20px;
    }

    footer {
        visibility: hidden;
    }

    #MainMenu {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# Load FAQ Data
# ---------------------------------
faqs_path = Path(__file__).parent / "resources/faq_data.csv"
ingest_faq_data(faqs_path)

# ---------------------------------
# Chatbot Logic
# ---------------------------------
def ask(query):
    route = router(query).name

    if route == "faq":
        return faq_chain(query)

    elif route == "sql":
        return sql_chain(query)

    return "Sorry, I couldn't understand your request."

# ---------------------------------
# Sidebar
# ---------------------------------
with st.sidebar:
    st.title("🛍️ ShopAssist AI")

    st.markdown("""
    ### Shopping Assistant

    Ask me about:

    • Products

    • Brands

    • Prices

    • Discounts

    • Refunds

    • Order Tracking

    • Payment Methods
    """)

    st.divider()

    st.caption("Powered by Semantic Routing + RAG")

# ---------------------------------
# Header
# ---------------------------------
st.markdown(
    """
    <div class='chat-title'>
        <h1>🛍️ ShopAssist AI</h1>
    </div>
    <div class='chat-subtitle'>
        Your Personal E-Commerce Shopping Assistant
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------
# Fresh Chat Every Refresh
# ---------------------------------
if "initialized" not in st.session_state:
    st.session_state.clear()
    st.session_state["initialized"] = True

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """
👋 Welcome to ShopAssist AI!

I can help you discover products, answer store-related questions, and provide shopping recommendations.

### Try asking:

• Show Nike products

• Find shoes under ₹3000

• What is your return policy?

• Which brand has the highest-rated sneakers?

• Do you offer cash on delivery?
"""
        }
    ]

# ---------------------------------
# Display Messages
# ---------------------------------
for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "🧑"

    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# ---------------------------------
# Chat Input
# ---------------------------------
query = st.chat_input(
    "Ask about products, brands, prices, orders..."
)

if query:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user", avatar="🧑"):
        st.markdown(query)

    with st.chat_message("assistant", avatar="🤖"):

        with st.spinner("Searching products and FAQs..."):
            response = ask(query)

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# ---------------------------------
# Footer
# ---------------------------------
st.divider()

st.caption(
    "ShopAssist AI • Product Discovery • FAQ Support • Semantic Search"
)