# 切换到 VS Code
"让我们实际测试一下这些模型的差异"

# comparison_demo.py
import openai
import time
import anthropic
from datetime import datetime

# 配置客户端
openai_client = openai.OpenAI(api_key="sk-...")
claude_client = anthropic.Anthropic(api_key="sk-ant-...")

# 测试prompt
test_prompt = "解释什么是递归，用一个简单的比喻"

print("🔬 开始模型对比实验")
print("=" * 50)

# 测试GPT-3.5
print("\n1️⃣ 测试 GPT-3.5-turbo...")
start = time.time()

response_gpt35 = openai_client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": test_prompt}],
    temperature=0.7
)

time_gpt35 = time.time() - start
print(f"⏱️ 响应时间: {time_gpt35:.2f}秒")
print(f"💰 成本: ${0.001:.4f}")
print(f"📝 回答: {response_gpt35.choices[0].message.content[:100]}...")

# 测试GPT-4
print("\n2️⃣ 测试 GPT-4o...")
# ... 类似代码

# 运行代码，显示实时结果
