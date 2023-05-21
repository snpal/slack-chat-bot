import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from llama_index import SimpleDirectoryReader, GPTListIndex, readers, LLMPredictor, PromptHelper, GPTVectorStoreIndex, ServiceContext
from llama_index.retrievers import VectorIndexRetriever
from llama_index.query_engine import RetrieverQueryEngine
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
import sys
import os

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.message()

def respond(message, say):
  query = message["text"]
  retriever = index.as_retriever()
  query_engine = RetrieverQueryEngine.from_args(retriever, response_mode='tree_summarize')
  response = query_engine.query(query)
  say(response.response)

def create_index():
  directory_path = "sitemap/"
  
  max_input_size = 4096
  max_tokens = 256
  max_chunk_overlap = 20
  chunk_size_limit = 600

  prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
  llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.2, model_name="gpt-3.5-turbo", max_tokens=max_tokens))
    
  documents = SimpleDirectoryReader(directory_path).load_data()
  service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

  index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
  return index  

if __name__ == "__main__":
  index = create_index()
  SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
