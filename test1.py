import os
from langgraph.prebuilt import create_react_agent
from langchain_community.chat_models import ChatTongyi
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

@tool
def get_weather(city: str) -> str:
    """获取指定城市的天气信息。"""
    return f"{city}今天阳光明媚！"

# ✅ 创建 Qwen 模型（使用 qwen-max，支持中文和工具调用）
llm = ChatTongyi(
    model_name="qwen-max",
    dashscope_api_key="sk-xxxx"  # 请替换为你的 DashScope API Key
)

# ✅ 创建 ReAct Agent
agent = create_react_agent(llm, [get_weather])

# 🇨🇳 用户用中文提问
result = agent.invoke({
    "messages": [HumanMessage(content="旧金山的天气怎么样？")]
})

# 输出中文回复
print(result["messages"][-1].content)
