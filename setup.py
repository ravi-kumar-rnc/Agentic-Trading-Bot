from setup.tools import setup, find_packages

setup(
    name = "Agentic_Trading_Bot",
    version = "1.0.0",
    author = "Ravi Kumar",
    author_email = "ravi.kumar.rnc@gmail.com",
    description = "An autonomous trading bot that leverages AI to execute trades based on market analysis.",
    packages = find_packages(),
    install_requires = [
        "langchain",
        "langgraph",
        "tavily-python",
        "langchain_community",
        "langchain_google_genai",
        "langchain-pinecone"        
    ] 
)