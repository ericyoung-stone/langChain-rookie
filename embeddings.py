import requests
from langchain.embeddings.base import Embeddings

# 自定义嵌入类，用于向LM Studio的API发送请求获取嵌入向量
class LMStudioEmbeddings(Embeddings):
    def __init__(self, api_base="http://192.168.1.22:1234/v1", model_name="text-embedding-nomic-embed-text-v1.5-embedding"):
        self.api_base = api_base
        self.model_name = model_name
        self.headers = {
            "Authorization": "Bearer custom",
            "Content-Type": "application/json"
        }

    def embed_documents(self, texts: list[str]):
        response = requests.post(
            f"{self.api_base}/embeddings",
            json={
                "input": texts,
                "model": self.model_name
            },
            headers=self.headers
        )
        if response.status_code == 200:
            result = response.json()
            embeddings = []
            for e in result["data"]:
                embeddings.append(e["embedding"])
            return embeddings
        else:
            raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

    def embed_query(self, text):
        return self.embed_documents([text])[0]


if __name__ == "__main__":
    # 创建EmbeddingProcessor类的实例
    embedding = LMStudioEmbeddings()
    print(embedding.embed_documents(["你好", "好心情"]))
    print(embedding.embed_query("你好"))