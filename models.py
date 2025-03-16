from langchain_openai import ChatOpenAI
from openai import OpenAI
import os

class MyOpenAIModel:
    def __init__(self):
        # 从环境变量读取配置
        self.base_url = os.getenv("LLM_BASE_URL", 'http://192.168.1.22:1234/v1') or "http://192.168.1.22:1234/v1"
        self.api_key = os.getenv("LLM_API_KEY", 'test') or "test"
        self.model = os.getenv("LLM_CHAT_MODEL", 'gemma-3-4b-it') or "gemma-3-4b-it"

        self.client = OpenAI(
            base_url=self.base_url,
            api_key=self.api_key
        )

    def generate(self, prompt: str, temperature: float = 0.7, stream: bool = True) -> str:
        """
        生成文本响应

        Args:
            prompt: 输入提示
            temperature: 温度参数
            stream: 是否使用流式输出

        Returns:
            生成的文本响应
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            stream=stream
        )

        # 处理流式响应
        if stream:
            result = ""
            for chunk in response:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    print(content, end="")
                    result += content
            return result

        return response.choices[0].message.content



"""
# ⭐️ChatOpenAI 使用自己的base_url,使本身不支持tool的模型,支持:
- 支持结构化输出, with_structured_output方法
- 支持使用工具, bind_tools方法
llm = ChatOpenAI(
                model="xxx",
                temperature=0,
                max_tokens=None,
                timeout=None,
                max_retries=2,
                # api_key="...",
                # base_url="...",
                # organization="...",
                # other params...
            )
"""
def get_base_url_model_with_tools(base_url: str="http://192.168.1.22:1234/v1", model: str="gemma-3-4b-it") -> ChatOpenAI:
    llm = ChatOpenAI(
        request_timeout=None,
        openai_api_base=base_url,
        model_name=model,
        openai_api_key="custom",
        max_retries=3,
        max_tokens=8064,
        temperature=0.7,
    )
    # openai_api_base 就是llama-server 部署时监听的地址
    # openai_api_key 必须要填 随便填就行 不能为 ""
    # print(llm.invoke("你是谁?").content)
    return llm