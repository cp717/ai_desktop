import os

class Settings:
    # Agent API 配置 (例如对接 MiMo 或其他兼容接口)
    LLM_API_KEY = os.getenv("LLM_API_KEY", "your-api-key-here")
    LLM_BASE_URL = os.getenv("LLM_BASE_URL", "https://api.example.com/v1/chat/completions")
    
    # 宠物外观配置
    PET_SCALE = 1.0

settings = Settings()
