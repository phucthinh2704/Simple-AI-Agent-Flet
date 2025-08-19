# Langchain
from langchain_ollama import OllamaLLM  # Ollama model
from langchain_ollama.llms import BaseLLM  # Lớp cơ sở của LLM
from langchain.chains.llm import LLMChain  # xử lí chuỗi các LLM
from langchain.chains.sql_database.query import (
    create_sql_query_chain,
)  # tạo câu truy vấn cơ sở dữ liệu từ llm
from langchain.prompts import PromptTemplate  # tạo câu truy vấn từ mẫu
from langchain_community.tools import (
    QuerySQLDataBaseTool,
)  # công cụ truy vấn cơ sở dữ liệu
from langchain_core.output_parsers import (
    StrOutputParser,
    PydanticOutputParser,
)  # xử lí kết quả trả về là kiểu dữ liệu chuỗi
from langchain_core.runnables import RunnablePassthrough  # truyền đa dạng đối số
from operator import itemgetter  # lấy giá trị từ dict
from langchain_community.cache import InMemoryCache  # bộ nhớ đệm trong langchain 
from langchain_community.utilities import SQLDatabase  

# Cache
from langchain.globals import set_llm_cache

llm = OllamaLLM(model="qwen3:8b")

set_llm_cache(InMemoryCache())

template = PromptTemplate.from_template(
    """
 Tôi là chuyên gia về Công nghệ thông tin, bạn có thể hỏi tôi về các vấn đề liên quan đến CNTT.
 Câu trả lời phải đúng các tiêu chí sau:
    - Câu trả lời phải chính xác
    - Câu trả lời phải dễ hiểu
    - Câu trả lời phải đầy đủ
    - Câu trả lời phải hợp lý
    - Câu trả lời phải đúng với câu hỏi
    - Câu trả lời phải chính xác về mặt ngữ cảnh
    - Câu trả lời phải chính xác về mặt kiến thức
    - Câu trả lời phải chính xác về mặt ngữ pháp
    - Câu trả lời phải chính xác về mặt từ vựng

 Câu hỏi:
 {question}
"""
)

llm_chain = template | llm | StrOutputParser()


def get_answer(question: str):
    return llm_chain.invoke({"question": question})
