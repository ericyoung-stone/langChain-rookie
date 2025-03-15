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