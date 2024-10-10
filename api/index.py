import pymupdf4llm
import requests
import os

file_url = "https://egzfmwstzbapteywkqqq.supabase.co/storage/v1/object/public/techme_documents/181f9e334c-6ffa-4b31-80b2-9ac5028d9ffb.pdf"

response = requests.get(file_url)
file_buffer = response.content

with open("file.pdf", "wb") as f:
    f.write(file_buffer)

md_text = pymupdf4llm.to_markdown("file.pdf")
os.remove("file.pdf")
print(md_text)
