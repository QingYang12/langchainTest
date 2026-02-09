import os
from langgraph.prebuilt import create_react_agent
from langchain_community.chat_models import ChatTongyi
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage

@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# ✅ 显式创建 Qwen 模型
llm = ChatTongyi(
    model_name="qwen-max",
    dashscope_api_key="sk-xxxx"
)

# ✅ 创建 agent（使用 langgraph）
agent = create_react_agent(llm, [get_weather])

# 执行
result = agent.invoke({"messages": [HumanMessage(content="what is the weather in sf")]})
print(result["messages"][-1].content)
