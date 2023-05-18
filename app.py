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

  llm_predictor = LLMPredictor(llm=ChatOpenAI(temperature=0.2, model_name="gpt-3.5-turbo"))
 
  documents = SimpleDirectoryReader(directory_path).load_data()
  service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

  index = GPTVectorStoreIndex.from_documents(documents, service_context=service_context)
  return index  

if __name__ == "__main__":
  index = create_index()
  SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
