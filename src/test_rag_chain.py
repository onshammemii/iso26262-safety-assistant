from rag_chain import query_rag

response = query_rag("What is the difference between ASIL A and ASIL D?")
print(response["answer"])
