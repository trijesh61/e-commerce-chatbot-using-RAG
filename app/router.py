from semantic_router import Route
from semantic_router.routers import SemanticRouter 
from semantic_router.encoders import HuggingFaceEncoder


encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)


faq = Route(
    name='faq',
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
        "What is your policy on damaged product?",
        "what is your Refund Policy",
        "What is your return policy?",
        "Can I return a product?",
        "How do returns work?",
        "What is the refund policy?",
        "How long does a refund take?",
        "When will I get my money back?",
        "How can I track my order?",
        "Where is my order?",
        "How do I check my order status?",
        "What payment methods do you accept?",
        "Can I pay using UPI?",
        "Do you support credit cards?",
        "Do you offer cash on delivery?",
        "What if I receive a damaged product?",
        "What should I do if the product is defective?",
        "How do exchanges work?",
        "Can I replace an item?",
        "Do you provide free shipping?",
        "How much is the delivery charge?",
        "Do you have any bank offers?"
    ]
)

sql = Route(
    name='sql',
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
        "show me top 3 nike shoes with rating higher than 4.5",
        "Show me Nike shoes",
        "Show Puma shoes",
        "Find Adidas shoes",
        "I want running shoes",
        "Shoes under 3000",
        "Shoes below 5000",
        "Top rated Nike shoes",
        "Show me discounted shoes",
        "Products with 50 percent discount",
        "Show shoes with rating above 4",
        "Find black shoes",
        "Find white sneakers",
        "Show me size 9 shoes",
        "What is the price of Puma shoes?",
        "Show top 5 products",
        "Recommend some sports shoes",
        "Show men's shoes",
        "Show women's shoes",
        "Find casual shoes",
        "Find formal shoes"
    ]
)


router = SemanticRouter(routes=[faq, sql], encoder=encoder, auto_sync="local")

if __name__ == "__main__":
    print(router("What is your policy on defective product?").name)
    print(router("Pink Puma shoes in price range 5000 to 1000").name)