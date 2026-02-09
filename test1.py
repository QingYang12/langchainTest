import os
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_community.chat_models import ChatTongyi
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# ✅ 显式创建 Qwen 模型
llm = ChatTongyi(
    model_name="qwen-max",
    dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("chat_history"),
    ("user", "{input}"),
    MessagesPlaceholder("agent_scratchpad")
])

# ✅ 创建 agent（支持任意 LLM）
agent = create_tool_calling_agent(llm, [get_weather], prompt)
executor = AgentExecutor(agent=agent, tools=[get_weather], verbose=True)

result = executor.invoke({"input": "what is the weather in sf"})
print(result["output"])
