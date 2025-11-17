# Lesson 3 讲解脚本：LangChain框架入门

## 课程信息
- **课程名称**：Lesson 3 - LangChain框架入门
- **时长**：3小时（含实验）
- **难度**：中级
- **前置要求**：完成Lesson 1和Lesson 2

## 教学目标
学生完成本课后应能够：
1. 理解LangChain的核心概念和架构
2. 使用Prompt模板构建可重用的提示词
3. 通过链式调用组合复杂的AI工作流
4. 实现带记忆功能的对话系统
5. 使用免费的Ollama模型开发实际应用

---

## 第一部分：LangChain基础 (45分钟)

### 1.1 什么是LangChain (15分钟)

**开场白：**
"大家好！在前两节课中，我们学习了如何直接调用LLM的API。但你们可能已经发现，每次都要手动处理API调用、管理提示词、处理响应，代码会变得非常冗长。今天我们要学习的LangChain，就是为了解决这些问题而诞生的。"

**演示准备：**
- 打开两个代码窗口：一个使用纯Python + OpenAI API，另一个使用LangChain
- 展示相同功能的代码量对比

**讲解要点：**

1. **引入问题**
   - "假设我们要构建一个翻译应用，需要：保存历史对话、支持多种语言、可以调整翻译风格"
   - "不使用框架的话，我们需要自己管理所有这些状态和逻辑"
   - 展示不使用LangChain的复杂代码（30-50行）

2. **LangChain的解决方案**
   - "LangChain提供了现成的组件来处理这些常见需求"
   - 展示使用LangChain的简洁代码（10-15行）
   - **强调**："同样的功能，代码减少了60-70%！"

3. **核心优势讲解**
   ```
   ✅ 模型无关 - 支持OpenAI、Anthropic、Ollama等所有主流模型
   ✅ 可组合 - 像乐高积木一样组合功能
   ✅ 快速开发 - 专注业务逻辑，而非基础设施
   ```

**互动环节：**
- 问："大家在前两节课的作业中，遇到过哪些重复性的编程工作？"
- 收集学生反馈，说明LangChain如何解决这些问题

**过渡语：**
"现在大家理解了为什么要用LangChain，接下来我们看看它是如何构建的。"

---

### 1.2 核心架构 (15分钟)

**视觉辅助：**
- 展示slides上的架构图
- 使用不同颜色标注6个核心模块

**讲解策略 - 类比法：**

"LangChain就像一个完整的厨房，有6个核心区域："

1. **Models（模型）- 食材供应商**
   - "无论你想用什么食材（GPT、Claude、Ollama），都有统一的接口"
   - 代码示例：展示同一段代码如何轻松切换模型

2. **Prompts（提示）- 食谱**
   - "写一次食谱（提示模板），可以重复使用，只需改变配料（参数）"
   - 演示：相同模板，不同参数生成不同结果

3. **Chains（链）- 烹饪流程**
   - "就像做一道菜有多个步骤，链可以组合多个操作"
   - 示例：翻译 → 总结 → 评价（三步链）

4. **Memory（记忆）- 厨房日志**
   - "记录之前做过什么菜，下次可以改进"
   - 演示：对话机器人记住之前说过的话

5. **Agents（代理）- 智能助手**
   - "可以自己决定用哪些工具的AI助手"
   - 说明："这是高级功能，我们在Lesson 5会详细学习"

6. **Callbacks（回调）- 监控系统**
   - "监控每一步的执行情况，便于调试"
   - 快速演示：verbose=True的输出

**重点强调：**
"今天我们主要学习前4个模块：Models、Prompts、Chains和Memory。掌握这4个，你就能构建80%的实际应用了！"

**检查理解：**
- 快速提问："谁能用自己的话解释一下什么是Chain？"
- 找2-3位学生回答

---

### 1.3 安装与配置 (15分钟)

**实操演示：**

"现在我们一起来安装LangChain。请大家跟着我的步骤操作。"

**步骤1：安装LangChain**
```bash
# 大家注意，我们装的是langchain和langchain-ollama
python3 -m pip install langchain langchain-ollama
```

**暂停点：**
- "等待安装完成...大家都装好了吗？有问题的举手。"
- 解决常见问题：网络慢、权限问题、版本冲突

**步骤2：安装Ollama模型**
```bash
ollama pull llama3.2
ollama list  # 验证
```

**重要提示：**
"我们使用Ollama的原因：
- ✅ 完全免费，无需API密钥
- ✅ 本地运行，数据安全
- ✅ 没有调用限制
- ✅ 适合学习和实验"

**步骤3：测试安装**
```python
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2")
response = llm.invoke("Say hello in Chinese!")
print(response)
```

**互动环节：**
- "请大家运行这个测试脚本，在聊天框分享运行结果"
- 检查：至少80%学生成功运行

**故障排除时间（预留5分钟）：**
- Ollama未启动
- 端口冲突
- 模型未下载

**过渡到Part 2：**
"好的！环境都配置好了。现在我们开始学习LangChain的核心组件。"

---

## 第二部分：核心组件 (75分钟)

### 2.1 LLM集成 (15分钟)

**学习重点：**
理解LangChain如何统一不同LLM的接口

**演示1：Ollama模型（免费）**

"我们先看最简单的用法："

```python
from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.7
)

result = llm.invoke("什么是机器学习？")
```

**讲解参数：**
- `model`: 选择模型
- `temperature`: 控制创造性（0=保守，2=创造）

**实验环节（5分钟）：**
"大家试试修改temperature，看看输出有什么变化"
- temperature=0.0 → 每次输出几乎相同
- temperature=1.5 → 输出更有创意

**演示2：批量调用**

"如果有多个问题要问，可以批量处理："

```python
questions = [
    "什么是深度学习？",
    "什么是神经网络？",
    "什么是反向传播？"
]
results = llm.batch(questions)
```

**性能对比：**
- 逐个调用：30秒
- 批量调用：8秒
- "提速75%！"

**可选：对比OpenAI API**
```python
# 只演示代码，说明需要API密钥
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4", temperature=0.7)
```

**总结：**
"LangChain最大的好处：代码几乎相同，只需改一行就能切换模型！"

---

### 2.2 提示模板 (20分钟)

**为什么需要模板？**

"我问大家一个问题：假设你要做一个教育应用，需要用不同风格解释概念（简单版、专业版、幽默版），不用模板你会怎么做？"

学生可能回答：复制粘贴prompt，改几个词

"问题是：
- ❌ 维护多个版本很麻烦
- ❌ 修改一处需要改多处
- ❌ 容易出错"

**解决方案：提示模板**

**示例1：基础模板**

```python
template = """你是一个专业的{role}。
请用{language}回答以下问题：
{question}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["role", "language", "question"]
)
```

**演示：一个模板，多种用法**

```python
# 用法1：中文教师
chain.invoke({
    "role": "Python教师",
    "language": "中文",
    "question": "什么是装饰器？"
})

# 用法2：英语科学家
chain.invoke({
    "role": "Computer Scientist",
    "language": "English",
    "question": "What is decorator?"
})
```

**强调优势：**
"看，同一个模板，改变参数就能适应不同场景！"

**示例2：聊天消息模板**

"更高级的用法：结构化的对话"

```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个{profession}，擅长{expertise}"),
    ("human", "{user_input}")
])
```

**实际应用展示：**
```python
# 编程助手
result = chain.invoke({
    "profession": "高级程序员",
    "expertise": "Python和算法",
    "user_input": "如何实现快速排序？"
})
```

**示例3：Few-shot学习**

"最强大的用法：通过示例教会AI"

```python
examples = [
    {"input": "快乐", "output": "悲伤"},
    {"input": "高", "output": "矮"},
]

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    # ...
)
```

**实验时间（8分钟）：**
"练习：创建一个将编程概念翻译成通俗语言的模板"

要求：
- 使用PromptTemplate
- 至少2个变量
- 测试3个不同的概念

**常见问题解答：**
Q: "变量名可以随意吗？"
A: "可以，但要有意义。推荐用英文，避免特殊字符。"

Q: "可以嵌套模板吗？"
A: "可以！我们在高级应用中会用到。"

---

### 2.3 链式调用 (20分钟)

**引入：**
"现在我们有了模型和模板，如何组合它们完成复杂任务？答案是：Chains（链）"

**核心概念：**
"链就像工厂流水线，每个环节处理一部分，最终得到产品"

**示例1：简单链（LCEL语法）**

```python
chain = prompt | llm
```

"这个竖线符号|就是'管道'，意思是：
1. 先执行prompt（格式化输入）
2. 再执行llm（生成回答）"

**现场演示：**
```python
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

template = "将以下文本翻译成{target_language}：\n{text}"
prompt = PromptTemplate.from_template(template)
llm = OllamaLLM(model="llama3.2")

# 创建链
chain = prompt | llm

# 使用链
result = chain.invoke({
    "target_language": "英语",
    "text": "人工智能正在改变世界"
})
```

**互动：**
"谁能说说chain.invoke()这一行实际做了什么？"

预期回答：
1. 把参数传给prompt
2. prompt生成完整提示词
3. 提示词传给llm
4. llm生成回答
5. 返回结果

**示例2：顺序链（多步骤）**

"实际应用：内容创作流水线"

```python
# 步骤1：生成标题
title_chain = PromptTemplate.from_template(
    "为以下主题生成一个吸引人的标题：{topic}\n标题："
) | llm

# 步骤2：生成大纲
outline_chain = PromptTemplate.from_template(
    "为标题'{title}'生成博客大纲：\n大纲："
) | llm

# 步骤3：写文章
article_chain = PromptTemplate.from_template(
    "基于以下大纲写一篇500字的文章：\n{outline}\n文章："
) | llm
```

**现场执行：**
"我们来创作一篇关于'AI在教育中的应用'的文章"

```python
topic = "AI在教育中的应用"

# 第一步
title = title_chain.invoke({"topic": topic})
print(f"生成标题: {title}")

# 第二步
outline = outline_chain.invoke({"title": title})
print(f"生成大纲:\n{outline}")

# 第三步
article = article_chain.invoke({"outline": outline})
print(f"完整文章:\n{article}")
```

**观察点：**
- 每一步的输出成为下一步的输入
- 整个流程自动化
- 可以随时中断检查中间结果

**高级技巧：自定义链逻辑**

```python
from langchain_core.runnables import RunnableLambda

# 自定义处理函数
def count_words(text):
    return {"text": text, "word_count": len(text.split())}

# 加入链中
chain = prompt | llm | RunnableLambda(count_words)
```

**实验任务（10分钟）：**
"构建一个三步链：
1. 生成一个笑话
2. 翻译成英语
3. 评价这个笑话的幽默程度（1-10分）"

提示：
- 使用3个PromptTemplate
- 用 | 连接
- 测试运行

**调试技巧：**
"如果链出错了怎么办？"
- 逐步测试每个环节
- 打印中间结果
- 检查变量名是否匹配

---

### 2.4 记忆系统 (20分钟)

**引入故事：**
"想象你去看医生，每次都要从头介绍自己的病史，是不是很烦？AI对话也是如此。默认情况下，LLM是'健忘'的，每次调用都是全新的开始。"

**演示问题：无记忆对话**

```python
llm = OllamaLLM(model="llama3.2")

print(llm.invoke("我叫张三"))
# 回复：你好张三！

print(llm.invoke("我叫什么名字？"))
# 回复：我不知道你的名字（忘记了！）
```

"看，AI完全不记得刚才的对话！"

**解决方案：记忆系统**

**类型1：ConversationBufferMemory（完整记忆）**

"最简单的记忆：保存所有对话"

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=memory
)

# 现在有记忆了
print(conversation.predict(input="我叫张三，是程序员"))
print(conversation.predict(input="我的职业是什么？"))
# 正确回答：程序员
```

**演示：查看记忆内容**
```python
print(memory.load_memory_variables({}))
# 显示完整对话历史
```

**优缺点分析：**
- ✅ 优点：简单，记住所有信息
- ❌ 缺点：对话越长，token消耗越多，成本增加

**类型2：ConversationBufferWindowMemory（窗口记忆）**

"聪明的做法：只记住最近N轮对话"

```python
memory = ConversationBufferWindowMemory(k=2)  # 只记住最近2轮
```

**对比实验：**
```python
conversation = ConversationChain(llm=llm, memory=memory)

conversation.predict(input="我最喜欢的颜色是蓝色")  # 第1轮
conversation.predict(input="我的爱好是游泳")      # 第2轮
conversation.predict(input="我今天吃了披萨")      # 第3轮
conversation.predict(input="我最喜欢的颜色是什么？")  # 测试

# 结果：不记得了（超过窗口）
```

"这就像短期记忆，只记住最近的事情"

**使用场景讨论：**
- ConversationBufferMemory → 短对话，注重质量
- ConversationBufferWindowMemory → 长对话，控制成本

**类型3：ConversationSummaryMemory（总结记忆）**

"高级技巧：不是保存原文，而是保存总结"

简单提及，不深入讲解（避免信息过载）

**自定义记忆示例**

"最灵活的做法：手动控制记忆"

```python
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import MessagesPlaceholder

memory = ConversationBufferMemory(return_messages=True)

# 手动保存对话
memory.save_context(
    {"input": "我叫李明"},
    {"output": "你好李明！"}
)

# 手动清除记忆
memory.clear()
```

**实战练习（10分钟）：**
"任务：创建一个能记住用户信息的个人助手"

要求：
- 能记住用户姓名、职业、爱好
- 至少进行5轮对话测试
- 验证记忆是否有效

**常见陷阱：**
1. 忘记初始化memory → 每次都是新对话
2. 窗口太小(k=1) → 几乎无记忆效果
3. 没有保存记忆到文件 → 程序重启后丢失

**高级话题（时间允许时）：**
- 如何持久化记忆（保存到数据库）
- 如何在不同会话间共享记忆
- 记忆的成本优化策略

---

## 第三部分：实战项目 (45分钟)

### 3.1 项目1：智能问答系统 (15分钟)

**项目目标：**
"构建一个能够以不同角色回答问题的AI系统"

**功能演示：**
同一个问题"什么是区块链？"，三种角色：
1. 教师版：用简单语言解释
2. 专家版：用专业术语
3. 喜剧版：用幽默方式

**代码讲解：**

```python
class QASystem:
    def __init__(self, model="llama3.2"):
        self.llm = OllamaLLM(model=model, temperature=0.7)

        self.roles = {
            "teacher": "你是一位耐心的教师...",
            "expert": "你是一位技术专家...",
            "comedian": "你是一位幽默的喜剧演员..."
        }

    def ask(self, question, role="teacher"):
        template = self.roles[role]
        prompt = PromptTemplate.from_template(template)
        chain = prompt | self.llm
        return chain.invoke({"question": question})
```

**设计亮点：**
1. **可扩展性** - 轻松添加新角色
2. **代码重用** - 所有角色共享同一个LLM
3. **参数化** - role作为参数传入

**学生实践（10分钟）：**
"任务：添加两个新角色"
- 诗人（用诗歌形式回答）
- 5岁小孩（用超级简单的语言）

**展示与讨论：**
- 邀请2-3位学生展示成果
- 讨论：哪种角色最难实现？为什么？

---

### 3.2 项目2：带记忆的聊天机器人 (20分钟)

**项目需求：**
"构建一个聊天机器人，能够：
- 记住用户说过的话
- 有自己的个性
- 维持连贯的对话"

**架构讲解：**

```
用户输入 → 记忆加载 → 提示模板 → LLM → 保存到记忆 → 返回
```

**代码实现：**

```python
class SmartChatbot:
    def __init__(self, name="小智", personality="友好、乐于助人"):
        self.name = name
        self.llm = OllamaLLM(model="llama3.2", temperature=0.8)
        self.memory = ConversationBufferWindowMemory(k=5)

        template = f"""你是{name}，一个{personality}的AI助手。

当前对话:
{{history}}

人类: {{input}}
AI助手:"""

        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            prompt=PromptTemplate.from_template(template)
        )

    def chat(self, user_input):
        return self.conversation.predict(input=user_input)

    def reset(self):
        """重置记忆"""
        self.memory.clear()
```

**关键点讲解：**

1. **个性设置** - 通过personality参数定制
2. **记忆窗口** - k=5，平衡效果和成本
3. **温度参数** - 0.8让对话更自然
4. **重置功能** - 允许清除历史

**互动演示：**
"我来和聊天机器人对话，大家观察它如何记忆"

```python
bot = SmartChatbot(name="小智", personality="友好、幽默")

# 第1轮
print(bot.chat("你好！我叫李明，是一名学生"))
# 小智记住：用户叫李明，是学生

# 第3轮（中间省略）
print(bot.chat("我叫什么名字？"))
# 小智回忆：你叫李明

# 第7轮（测试窗口限制）
print(bot.chat("我的职业是什么？"))
# 可能不记得（超过k=5的窗口）
```

**扩展功能讨论：**
"如果要改进这个机器人，你会加什么功能？"

学生可能的回答：
- 保存对话到文件
- 支持多用户
- 添加情感分析
- 连接数据库

**实践时间（15分钟）：**
"任务：改进聊天机器人"

选项A（简单）：
- 修改个性为"严肃的教授"
- 测试对话风格变化

选项B（中等）：
- 添加save_conversation()方法
- 保存对话到JSON文件

选项C（困难）：
- 实现多用户支持
- 每个用户有独立记忆

**成果展示：**
- 找2-3组展示改进
- 讨论实现难点

---

### 3.3 高级应用：多功能AI助手 (10分钟)

**最终项目演示：**
"把今天学的所有知识整合起来"

**功能列表：**
1. 翻译（translate:）
2. 总结（summarize:）
3. 代码生成（code:）
4. 聊天（默认）

**代码架构：**

```python
class AIAssistant:
    def __init__(self):
        self.llm = OllamaLLM(model="llama3.2")
        self.features = {
            "translate": self.translate,
            "summarize": self.summarize,
            "code": self.code_helper,
            "chat": self.chat
        }

    def execute(self, command):
        # 解析命令
        if ":" in command:
            feature, content = command.split(":", 1)
            return self.features[feature](content)
        else:
            return self.chat(command)
```

**现场演示：**

```bash
👤 你: translate: 人工智能正在改变世界
🤖 助手: Artificial Intelligence is changing the world

👤 你: code: 实现冒泡排序
🤖 助手: [生成Python代码]

👤 你: 今天天气真好
🤖 助手: 是啊，希望能一直保持好天气！
```

**设计模式讲解：**
1. **命令模式** - 通过":"解析命令
2. **策略模式** - 不同功能不同策略
3. **工厂模式** - features字典管理功能

**时间允许的话：**
让学生尝试添加新功能，如：
- weather: 查询天气
- calculate: 计算数学问题
- joke: 讲笑话

---

## 课程总结 (15分钟)

### 知识回顾

**互动问答：**

1. "谁能解释为什么要用LangChain？"
   - 预期回答：简化开发、代码复用、快速构建应用

2. "Prompt Template的主要好处是什么？"
   - 预期回答：可重用、参数化、易维护

3. "Chain和普通函数调用有什么区别？"
   - 预期回答：声明式编程、自动管道、可组合

4. "什么时候需要Memory？"
   - 预期回答：多轮对话、需要上下文、个性化交互

### 今日成果

"今天我们完成了：
✅ 理解LangChain架构
✅ 掌握4个核心组件
✅ 完成3个实战项目
✅ 学会使用免费的Ollama模型"

### 作业说明

**必做作业（40分）：**
"个性化学习助手 - 综合运用Prompt Template和Memory"

**选做作业（30分）：**
"内容创作流水线 - 练习Chain的组合使用"

**挑战作业（30分）：**
"智能客服系统 - 完整的实际应用"

**强调：**
- 所有作业都使用免费的Ollama，零成本！
- 提供完整的参考代码
- 7天内提交到GitHub

### 下节预告

"Lesson 4: 向量数据库与RAG

我们将学习：
- 如何把文档转换为向量
- 使用ChromaDB存储知识
- 构建能回答文档内容的AI
- 实现真正的'知识库问答系统'"

### 答疑时间（10分钟）

常见问题准备：
1. Q: "LangChain和直接用API比，速度会慢吗？"
   A: "几乎没有性能损失，LangChain是轻量级封装"

2. Q: "能在生产环境用免费的Ollama吗？"
   A: "可以！很多公司用Ollama部署私有化AI服务"

3. Q: "Memory会占用很多内存吗？"
   A: "取决于窗口大小，ConversationBufferWindowMemory很轻量"

4. Q: "如何调试Chain出错？"
   A: "使用verbose=True，逐步测试每个组件"

---

## 教学技巧建议

### 节奏控制
- ⏱️ 每15-20分钟一个互动环节
- 🎯 理论讲解不超过10分钟
- 💻 每个概念配一个实际演示
- 🤝 每30分钟一次学生实践

### 学生参与
- 提问：随机点名回答（不是总找举手的）
- 编程：让学生分享屏幕展示代码
- 讨论：分组讨论（2-3人一组）
- 投票：用聊天框投票选择下一个示例

### 常见学生问题预判
1. "为什么我的代码不工作？"
   → 检查：Ollama是否运行、模型是否下载、语法错误

2. "记忆好像不起作用？"
   → 检查：是否初始化memory、是否使用同一个conversation实例

3. "输出结果每次都不一样？"
   → 解释：temperature参数的作用，降低或设为0可以稳定输出

4. "代码运行很慢？"
   → 说明：本地LLM第一次较慢，后续会快；可以减小max_tokens

### 课堂管理
- 📱 提醒学生关闭通知
- ⏰ 准时开始、准时结束
- 🍵 在90分钟处安排5分钟休息
- 💾 提醒定期保存代码

### 实验室环境准备
- 确保所有电脑都安装了Ollama
- 预先下载llama3.2模型（避免网络拥堵）
- 准备好所有示例代码的GitHub仓库链接
- 测试投影仪和代码演示效果

---

## 应急预案

### 技术问题
- **Ollama服务挂了** → 准备OpenAI API作为备用（提供临时密钥）
- **网络故障** → 所有材料提前下载到本地
- **代码示例出错** → 准备多个版本的代码

### 时间不足
**优先级排序：**
1. 必讲：LangChain简介、Prompt Template、Memory基础
2. 重要：Chain基础、聊天机器人项目
3. 可选：高级应用、深入的参数调优

**压缩策略：**
- 减少实验时间（从15分钟压缩到10分钟）
- 跳过OpenAI API演示（只讲Ollama）
- 高级应用作为课后材料

### 学生进度差异
- **快的学生** → 提供加分挑战题
- **慢的学生** → 安排助教一对一辅导
- **整体偏慢** → 延长实验时间，压缩理论讲解

---

## 课后跟进

### 学习资源推送
- LangChain官方文档链接
- 推荐YouTube教程
- 优秀学生作业展示
- 常见问题FAQ文档

### 讨论群管理
- 课后24小时内发布作业链接
- 收集学生反馈（匿名问卷）
- 每天回答3-5个群内问题
- 分享相关技术文章

### 作业批改
- 72小时内完成批改
- 提供详细的改进建议
- 优秀作业在下节课展示
- 记录常见错误用于改进教学

---

## 教学效果评估

### 课堂检查点
- [ ] 80%学生成功安装LangChain
- [ ] 60%学生能独立创建Prompt Template
- [ ] 50%学生能构建简单的Chain
- [ ] 40%学生能实现带记忆的对话

### 课后问卷（5个问题）
1. 今天最大的收获是什么？
2. 哪个部分最难理解？
3. 实验时间是否充足？
4. 课程节奏如何（太快/合适/太慢）？
5. 对下节课的期待？

### 改进方向
- 根据问卷调整难度
- 增加/减少实验时间
- 优化代码示例
- 更新过时的内容

---

**祝教学顺利！🎉**