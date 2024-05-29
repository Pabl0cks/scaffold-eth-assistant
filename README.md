# Scaffold-ETH Docs & SRE Challenges assistant

Open source AI assistant based in RAG (Retrieval Augmented Generation), to help users resolve their SpeedRunEthereum questions, and let users "chat" with Scaffold-ETH docs.

![image](https://github.com/Pabl0cks/scaffold-eth-assistant/assets/55535804/2d956142-93bf-445b-995c-66592fcb5e5f)


## Tech stack

![image](https://github.com/Pabl0cks/scaffold-eth-assistant/assets/55535804/eea6af16-1fc5-43b7-bada-22155043c72a)
_Generic RAG Diagram_

This assistant MVP uses LangChain framework with these providers:

- __GroqCloud:__ to interact with LLM via API. We can easily plug different Models like:
   - __llama3-70b-8192__ (current model)
   - llama3-8b-8192
   - mixtral-8x7b-32768
   - gemma-7b-it
- __Google:__ to create the embeddings
- __FAISS:__ for vector store and to search for embeddings that are similar to user prompt

Everything is wrapped in Streamlit to transform the Python script into a web app.

## Knowledge base
Each Challenge will have it's own set of documents in a [Challenge #] folder. It will be loaded when the user selects the Challenge in the dropdown menu. By default, [Challenge 0] docs are loaded.

Document list for each challenge:
- Scaffold ETH docs
- Challenge readme
- Telegram Q/A extracted from Challenge chat group
