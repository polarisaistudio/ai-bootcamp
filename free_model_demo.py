# free_model_demo.py - 使用Ollama (完全免费)
import ollama
import time

# 测试prompt
test_prompt = "解释什么是递归，用一个简单的比喻"

print("🔬 使用免费本地模型实验")
print("=" * 50)

# 测试Llama 3.2 (免费)
print("\n1️⃣ 测试 Llama 3.2 (免费本地模型)...")
start = time.time()

response = ollama.chat(
    model='llama3.2',
    messages=[
        {'role': 'user', 'content': test_prompt}
    ]
)

time_taken = time.time() - start
print(f"⏱️ 响应时间: {time_taken:.2f}秒")
print(f"💰 成本: 免费！")
print(f"📝 回答: {response['message']['content'][:100]}...")

# 测试Qwen 2.5 (免费，中文更优)
print("\n2️⃣ 测试 Qwen 2.5 (免费，中文优化)...")
start = time.time()

response = ollama.chat(
    model='qwen2.5',
    messages=[
        {'role': 'user', 'content': test_prompt}
    ]
)

time_taken = time.time() - start
print(f"⏱️ 响应时间: {time_taken:.2f}秒")
print(f"💰 成本: 免费！")
print(f"📝 回答: {response['message']['content'][:100]}...")

print("\n✅ 所有测试完成，总成本: $0.00")
