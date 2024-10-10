import pymupdf4llm
import requests
import os
import fastapi
from semantic_text_splitter import MarkdownSplitter
from tokenizers import Tokenizer

app = fastapi.FastAPI()

# file_url = "https://egzfmwstzbapteywkqqq.supabase.co/storage/v1/object/public/techme_documents/181f9e334c-6ffa-4b31-80b2-9ac5028d9ffb.pdf"

# # response = requests.get(file_url)
# # file_buffer = response.content

# with open("file.pdf", "wb") as f:
#     f.write(file_buffer)

# md_text = pymupdf4llm.to_markdown("file.pdf")
# os.remove("file.pdf")

# tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
# splitter = MarkdownSplitter.from_huggingface_tokenizer(tokenizer, 512)
# md_chunks = splitter.chunks(md_text)
# print(len(md_chunks))
# md_chunks


@app.post("/convert")
async def convert_pdf_to_markdown(file_url: str):
    response = requests.get(file_url)
    file_buffer = response.content

    with open("file.pdf", "wb") as f:
        f.write(file_buffer)

    md_text = pymupdf4llm.to_markdown("file.pdf")
    os.remove("file.pdf")

    tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
    splitter = MarkdownSplitter.from_huggingface_tokenizer(tokenizer, 512)
    md_chunks = splitter.chunks(md_text)

    return {"chunks": md_chunks}
