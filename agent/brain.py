import requests
from core.config import settings

class AIBrain:
    def __init__(self):
        self.api_key = settings.LLM_API_KEY
        self.base_url = settings.LLM_BASE_URL
        self.memory = [{"role": "system", "content": "你是一个可爱的桌面虚拟宠物，性格活泼，乐于助人。你的回答应该简短且带有一些可爱的语气词。"}]

    def chat(self, user_input: str) -> str:
        """
        向云端大模型发送消息并获取回复
        """
        self.memory.append({"role": "user", "content": user_input})
        
        # 模拟 API 调用逻辑 (实际对接时解开注释并替换对应字段)
        '''
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {"model": "your-model-name", "messages": self.memory}
        try:
            response = requests.post(self.base_url, json=payload, headers=headers)
            reply = response.json()['choices'][0]['message']['content']
            self.memory.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            return "呜呜，我的大脑暂时连不上网了..."
        '''
        
        # 本地 Mock 回复
        reply = f"主人，我听到你说：{user_input}！我现在还在开发阶段哦~"
        self.memory.append({"role": "assistant", "content": reply})
        return reply

pet_agent = AIBrain()
