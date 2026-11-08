def retrieve_case(db, query):
    docs = db.similarity_search(query, k=2)
    return "\n".join([d.page_content for d in docs])