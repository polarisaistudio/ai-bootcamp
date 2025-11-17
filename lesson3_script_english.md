# Lesson 3 Teaching Script: Introduction to LangChain Framework

## Course Information
- **Course Name**: Lesson 3 - Introduction to LangChain Framework
- **Duration**: 3 hours (including lab exercises)
- **Difficulty**: Intermediate
- **Prerequisites**: Completion of Lesson 1 and Lesson 2

## Learning Objectives
After completing this lesson, students should be able to:
1. Understand LangChain's core concepts and architecture
2. Use Prompt Templates to build reusable prompts
3. Combine complex AI workflows through chaining
4. Implement conversational systems with memory
5. Develop practical applications using free Ollama models

---

## Part 1: LangChain Fundamentals (45 minutes)

### 1.1 What is LangChain (15 minutes)

**Opening Statement:**
"Hello everyone! In the first two lessons, we learned how to directly call LLM APIs. But you may have already noticed that manually handling API calls, managing prompts, and processing responses can make your code quite verbose. Today we're going to learn about LangChain, which was created specifically to solve these problems."

**Demo Preparation:**
- Open two code windows: one using pure Python + OpenAI API, another using LangChain
- Display a code volume comparison for the same functionality

**Key Teaching Points:**

1. **Introduce the Problem**
   - "Suppose we want to build a translation app that needs to: save conversation history, support multiple languages, and adjust translation style"
   - "Without using a framework, we need to manage all this state and logic ourselves"
   - Show complex code without LangChain (30-50 lines)

2. **LangChain's Solution**
   - "LangChain provides ready-made components to handle these common needs"
   - Show concise code using LangChain (10-15 lines)
   - **Emphasize**: "Same functionality, 60-70% less code!"

3. **Core Advantages Explanation**
   ```
   ✅ Model-agnostic - Supports all major models: OpenAI, Anthropic, Ollama, etc.
   ✅ Composable - Combine features like LEGO blocks
   ✅ Rapid development - Focus on business logic, not infrastructure
   ```

**Interactive Session:**
- Ask: "In your homework from the first two lessons, what repetitive programming tasks did you encounter?"
- Collect student feedback and explain how LangChain solves these problems

**Transition Statement:**
"Now that you understand why we use LangChain, let's look at how it's built."

---

### 1.2 Core Architecture (15 minutes)

**Visual Aids:**
- Display the architecture diagram from the slides
- Use different colors to highlight the 6 core modules

**Teaching Strategy - Analogy Method:**

"LangChain is like a complete kitchen with 6 core areas:"

1. **Models - Ingredient Suppliers**
   - "No matter what ingredients you want (GPT, Claude, Ollama), there's a unified interface"
   - Code example: Show how the same code easily switches between models

2. **Prompts - Recipes**
   - "Write a recipe (prompt template) once, reuse it repeatedly, just change the ingredients (parameters)"
   - Demo: Same template, different parameters generate different results

3. **Chains - Cooking Process**
   - "Just like making a dish has multiple steps, chains can combine multiple operations"
   - Example: Translate → Summarize → Evaluate (three-step chain)

4. **Memory - Kitchen Log**
   - "Record what dishes you've made before, so you can improve next time"
   - Demo: Chatbot remembers previous conversations

5. **Agents - Smart Assistant**
   - "An AI assistant that can decide which tools to use on its own"
   - Note: "This is an advanced feature, we'll study it in detail in Lesson 5"

6. **Callbacks - Monitoring System**
   - "Monitor the execution of each step for easier debugging"
   - Quick demo: Output with verbose=True

**Key Emphasis:**
"Today we'll mainly learn the first 4 modules: Models, Prompts, Chains, and Memory. Master these 4, and you can build 80% of practical applications!"

**Comprehension Check:**
- Quick question: "Who can explain in their own words what a Chain is?"
- Have 2-3 students answer

---

### 1.3 Installation and Configuration (15 minutes)

**Hands-on Demonstration:**

"Now let's install LangChain together. Please follow my steps."

**Step 1: Install LangChain**
```bash
# Everyone pay attention, we're installing langchain and langchain-ollama
python3 -m pip install langchain langchain-ollama
```

**Pause Point:**
- "Waiting for installation to complete... Has everyone finished? Raise your hand if you have issues."
- Resolve common issues: slow network, permission issues, version conflicts

**Step 2: Install Ollama Model**
```bash
ollama pull llama3.2
ollama list  # Verify
```

**Important Notice:**
"Why we're using Ollama:
- ✅ Completely free, no API key needed
- ✅ Runs locally, data security
- ✅ No rate limits
- ✅ Ideal for learning and experimentation"

**Step 3: Test Installation**
```python
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2")
response = llm.invoke("Say hello in Chinese!")
print(response)
```

**Interactive Session:**
- "Please run this test script and share your results in the chat"
- Check: At least 80% of students successfully run it

**Troubleshooting Time (reserve 5 minutes):**
- Ollama not started
- Port conflicts
- Model not downloaded

**Transition to Part 2:**
"Great! The environment is all set up. Now let's start learning LangChain's core components."

---

## Part 2: Core Components (75 minutes)

### 2.1 LLM Integration (15 minutes)

**Learning Focus:**
Understand how LangChain provides a unified interface for different LLMs

**Demo 1: Ollama Model (Free)**

"Let's start with the simplest usage:"

```python
from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3.2",
    temperature=0.7
)

result = llm.invoke("What is machine learning?")
```

**Explain Parameters:**
- `model`: Select the model
- `temperature`: Control creativity (0=conservative, 2=creative)

**Experiment Session (5 minutes):**
"Try modifying temperature and see what changes in the output"
- temperature=0.0 → Output nearly identical each time
- temperature=1.5 → More creative output

**Demo 2: Batch Calling**

"If you have multiple questions to ask, you can batch process them:"

```python
questions = [
    "What is deep learning?",
    "What is a neural network?",
    "What is backpropagation?"
]
results = llm.batch(questions)
```

**Performance Comparison:**
- Sequential calls: 30 seconds
- Batch calls: 8 seconds
- "75% faster!"

**Optional: Compare with OpenAI API**
```python
# Just show the code, explain that an API key is needed
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4", temperature=0.7)
```

**Summary:**
"LangChain's biggest benefit: code is almost identical, just change one line to switch models!"

---

### 2.2 Prompt Templates (20 minutes)

**Why Do We Need Templates?**

"Let me ask you a question: Suppose you want to make an educational app that needs to explain concepts in different styles (simple version, professional version, humorous version), how would you do it without templates?"

Students might answer: Copy and paste prompts, change a few words

"The problem is:
- ❌ Maintaining multiple versions is troublesome
- ❌ Changing one place requires changing multiple places
- ❌ Easy to make errors"

**Solution: Prompt Templates**

**Example 1: Basic Template**

```python
template = """You are a professional {role}.
Please answer the following question in {language}:
{question}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["role", "language", "question"]
)
```

**Demo: One Template, Multiple Uses**

```python
# Usage 1: Chinese teacher
chain.invoke({
    "role": "Python teacher",
    "language": "Chinese",
    "question": "What is a decorator?"
})

# Usage 2: English scientist
chain.invoke({
    "role": "Computer Scientist",
    "language": "English",
    "question": "What is a decorator?"
})
```

**Emphasize Advantages:**
"See, same template, just change parameters to adapt to different scenarios!"

**Example 2: Chat Message Template**

"More advanced usage: structured conversations"

```python
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a {profession}, skilled in {expertise}"),
    ("human", "{user_input}")
])
```

**Practical Application Demo:**
```python
# Programming assistant
result = chain.invoke({
    "profession": "senior programmer",
    "expertise": "Python and algorithms",
    "user_input": "How to implement quicksort?"
})
```

**Example 3: Few-shot Learning**

"The most powerful usage: teach AI through examples"

```python
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "tall", "output": "short"},
]

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    # ...
)
```

**Experiment Time (8 minutes):**
"Practice: Create a template that translates programming concepts into plain language"

Requirements:
- Use PromptTemplate
- At least 2 variables
- Test 3 different concepts

**Common Q&A:**
Q: "Can variable names be arbitrary?"
A: "Yes, but they should be meaningful. English is recommended, avoid special characters."

Q: "Can templates be nested?"
A: "Yes! We'll use this in advanced applications."

---

### 2.3 Chaining (20 minutes)

**Introduction:**
"Now we have models and templates, how do we combine them to complete complex tasks? The answer is: Chains"

**Core Concept:**
"A chain is like an assembly line, where each step processes a part, and you get the final product"

**Example 1: Simple Chain (LCEL Syntax)**

```python
chain = prompt | llm
```

"This pipe symbol | is a 'pipeline', meaning:
1. First execute prompt (format input)
2. Then execute llm (generate response)"

**Live Demo:**
```python
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

template = "Translate the following text into {target_language}:\n{text}"
prompt = PromptTemplate.from_template(template)
llm = OllamaLLM(model="llama3.2")

# Create chain
chain = prompt | llm

# Use chain
result = chain.invoke({
    "target_language": "English",
    "text": "Artificial intelligence is changing the world"
})
```

**Interaction:**
"Who can tell me what this chain.invoke() line actually does?"

Expected answer:
1. Pass parameters to prompt
2. Prompt generates complete prompt
3. Prompt is passed to llm
4. llm generates response
5. Return result

**Example 2: Sequential Chain (Multi-step)**

"Practical application: Content creation pipeline"

```python
# Step 1: Generate title
title_chain = PromptTemplate.from_template(
    "Generate an engaging title for the following topic: {topic}\nTitle:"
) | llm

# Step 2: Generate outline
outline_chain = PromptTemplate.from_template(
    "Generate a blog outline for the title '{title}':\nOutline:"
) | llm

# Step 3: Write article
article_chain = PromptTemplate.from_template(
    "Based on the following outline, write a 500-word article:\n{outline}\nArticle:"
) | llm
```

**Live Execution:**
"Let's create an article about 'AI Applications in Education'"

```python
topic = "AI Applications in Education"

# First step
title = title_chain.invoke({"topic": topic})
print(f"Generated title: {title}")

# Second step
outline = outline_chain.invoke({"title": title})
print(f"Generated outline:\n{outline}")

# Third step
article = article_chain.invoke({"outline": outline})
print(f"Complete article:\n{article}")
```

**Observation Points:**
- Each step's output becomes the next step's input
- The entire process is automated
- Can pause to check intermediate results at any time

**Advanced Technique: Custom Chain Logic**

```python
from langchain_core.runnables import RunnableLambda

# Custom processing function
def count_words(text):
    return {"text": text, "word_count": len(text.split())}

# Add to chain
chain = prompt | llm | RunnableLambda(count_words)
```

**Experiment Task (10 minutes):**
"Build a three-step chain:
1. Generate a joke
2. Translate it into English
3. Rate the humor of the joke (1-10 points)"

Hints:
- Use 3 PromptTemplates
- Connect with |
- Test run

**Debugging Tips:**
"What if the chain errors out?"
- Test each component step by step
- Print intermediate results
- Check if variable names match

---

### 2.4 Memory System (20 minutes)

**Introduction Story:**
"Imagine going to see a doctor and having to introduce your medical history from scratch every time - annoying, right? AI conversations are the same. By default, LLMs are 'forgetful' - each call is a fresh start."

**Demo Problem: Memory-less Conversation**

```python
llm = OllamaLLM(model="llama3.2")

print(llm.invoke("My name is Zhang San"))
# Reply: Hello Zhang San!

print(llm.invoke("What is my name?"))
# Reply: I don't know your name (forgot!)
```

"See, the AI completely forgot the previous conversation!"

**Solution: Memory System**

**Type 1: ConversationBufferMemory (Complete Memory)**

"The simplest memory: save all conversations"

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

memory = ConversationBufferMemory()
conversation = ConversationChain(
    llm=llm,
    memory=memory
)

# Now it has memory
print(conversation.predict(input="My name is Zhang San, I'm a programmer"))
print(conversation.predict(input="What is my profession?"))
# Correct answer: Programmer
```

**Demo: View Memory Content**
```python
print(memory.load_memory_variables({}))
# Shows complete conversation history
```

**Pros and Cons Analysis:**
- ✅ Pros: Simple, remembers all information
- ❌ Cons: Longer conversations consume more tokens, increasing cost

**Type 2: ConversationBufferWindowMemory (Window Memory)**

"Smart approach: Only remember the last N conversation turns"

```python
memory = ConversationBufferWindowMemory(k=2)  # Only remember last 2 turns
```

**Comparison Experiment:**
```python
conversation = ConversationChain(llm=llm, memory=memory)

conversation.predict(input="My favorite color is blue")  # Turn 1
conversation.predict(input="My hobby is swimming")       # Turn 2
conversation.predict(input="I ate pizza today")          # Turn 3
conversation.predict(input="What is my favorite color?") # Test

# Result: Doesn't remember (exceeded window)
```

"This is like short-term memory, only remembers recent things"

**Use Case Discussion:**
- ConversationBufferMemory → Short conversations, focus on quality
- ConversationBufferWindowMemory → Long conversations, control cost

**Type 3: ConversationSummaryMemory (Summary Memory)**

"Advanced technique: Don't save original text, save summaries"

Briefly mention, don't dive deep (avoid information overload)

**Custom Memory Example**

"Most flexible approach: Manual memory control"

```python
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import MessagesPlaceholder

memory = ConversationBufferMemory(return_messages=True)

# Manually save conversation
memory.save_context(
    {"input": "My name is Li Ming"},
    {"output": "Hello Li Ming!"}
)

# Manually clear memory
memory.clear()
```

**Practical Exercise (10 minutes):**
"Task: Create a personal assistant that can remember user information"

Requirements:
- Can remember user's name, profession, hobbies
- Conduct at least 5 conversation turns for testing
- Verify if memory is effective

**Common Pitfalls:**
1. Forgetting to initialize memory → Every time is a new conversation
2. Window too small (k=1) → Almost no memory effect
3. Not saving memory to file → Lost after program restart

**Advanced Topics (if time permits):**
- How to persist memory (save to database)
- How to share memory between different sessions
- Memory cost optimization strategies

---

## Part 3: Practical Projects (45 minutes)

### 3.1 Project 1: Intelligent Q&A System (15 minutes)

**Project Goal:**
"Build an AI system that can answer questions in different roles"

**Feature Demo:**
Same question "What is blockchain?", three roles:
1. Teacher version: Explain in simple language
2. Expert version: Use professional terminology
3. Comedian version: Use humor

**Code Explanation:**

```python
class QASystem:
    def __init__(self, model="llama3.2"):
        self.llm = OllamaLLM(model=model, temperature=0.7)

        self.roles = {
            "teacher": "You are a patient teacher...",
            "expert": "You are a technical expert...",
            "comedian": "You are a humorous comedian..."
        }

    def ask(self, question, role="teacher"):
        template = self.roles[role]
        prompt = PromptTemplate.from_template(template)
        chain = prompt | self.llm
        return chain.invoke({"question": question})
```

**Design Highlights:**
1. **Extensibility** - Easily add new roles
2. **Code Reuse** - All roles share the same LLM
3. **Parameterization** - Role passed as a parameter

**Student Practice (10 minutes):**
"Task: Add two new roles"
- Poet (answer in poetry form)
- 5-year-old child (use super simple language)

**Show and Discuss:**
- Invite 2-3 students to showcase their work
- Discuss: Which role was hardest to implement? Why?

---

### 3.2 Project 2: Chatbot with Memory (20 minutes)

**Project Requirements:**
"Build a chatbot that can:
- Remember what the user said
- Have its own personality
- Maintain coherent conversations"

**Architecture Explanation:**

```
User Input → Load Memory → Prompt Template → LLM → Save to Memory → Return
```

**Code Implementation:**

```python
class SmartChatbot:
    def __init__(self, name="Xiaozhi", personality="friendly, helpful"):
        self.name = name
        self.llm = OllamaLLM(model="llama3.2", temperature=0.8)
        self.memory = ConversationBufferWindowMemory(k=5)

        template = f"""You are {name}, a {personality} AI assistant.

Current conversation:
{{history}}
Human: {input}
AI Assistant:"""

        self.conversation = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            prompt=PromptTemplate.from_template(template)
        )

    def chat(self, user_input):
        return self.conversation.predict(input=user_input)

    def reset(self):
        """Reset memory"""
        self.memory.clear()
```

**Key Points Explanation:**

1. **Personality Setting** - Customize through personality parameter
2. **Memory Window** - k=5, balance effectiveness and cost
3. **Temperature Parameter** - 0.8 makes conversation more natural
4. **Reset Function** - Allows clearing history

**Interactive Demo:**
"Let me have a conversation with the chatbot, everyone observe how it remembers"

```python
bot = SmartChatbot(name="Xiaozhi", personality="friendly, humorous")

# Round 1
print(bot.chat("Hello\! My name is Li Ming, I'm a student"))
# Xiaozhi remembers: User is called Li Ming, is a student

# Round 3 (middle rounds omitted)
print(bot.chat("What is my name?"))
# Xiaozhi recalls: Your name is Li Ming

# Round 7 (testing window limits)
print(bot.chat("What is my profession?"))
# Might not remember (exceeds k=5 window)
```

**Extended Functionality Discussion:**
"If you wanted to improve this chatbot, what features would you add?"

Students might answer:
- Save conversations to file
- Support multiple users
- Add sentiment analysis
- Connect to database

**Practice Time (15 minutes):**
"Task: Improve the chatbot"

Option A (Simple):
- Change personality to "serious professor"
- Test conversation style changes

Option B (Medium):
- Add save_conversation() method
- Save conversation to JSON file

Option C (Difficult):
- Implement multi-user support
- Each user has independent memory

**Showcase Results:**
- Have 2-3 groups present improvements
- Discuss implementation challenges

---

### 3.3 Advanced Application: Multi-functional AI Assistant (10 minutes)

**Final Project Demo:**
"Integrate all the knowledge we learned today"

**Feature List:**
1. Translation (translate:)
2. Summarization (summarize:)
3. Code generation (code:)
4. Chat (default)

**Code Architecture:**

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
        # Parse command
        if ":" in command:
            feature, content = command.split(":", 1)
            return self.features[feature](content)
        else:
            return self.chat(command)
```

**Live Demo:**

```bash
👤 You: translate: Artificial intelligence is changing the world
🤖 Assistant: 人工智能正在改变世界

👤 You: code: Implement bubble sort
🤖 Assistant: [Generates Python code]

👤 You: The weather is really nice today
🤖 Assistant: Yes, I hope it stays nice\!
```

**Design Pattern Explanation:**
1. **Command Pattern** - Parse commands through ":"
2. **Strategy Pattern** - Different features use different strategies
3. **Factory Pattern** - features dictionary manages functionality

**If Time Permits:**
Let students try adding new features, such as:
- weather: Query weather
- calculate: Solve math problems
- joke: Tell jokes

---

## Course Summary (15 minutes)

### Knowledge Review

**Interactive Q&A:**

1. "Who can explain why we use LangChain?"
   - Expected answer: Simplify development, code reuse, rapid application building

2. "What are the main benefits of Prompt Templates?"
   - Expected answer: Reusable, parameterized, easy to maintain

3. "What's the difference between Chains and regular function calls?"
   - Expected answer: Declarative programming, automatic pipelines, composable

4. "When do you need Memory?"
   - Expected answer: Multi-turn conversations, need context, personalized interactions

### Today's Achievements

"Today we completed:
✅ Understanding LangChain architecture
✅ Mastering 4 core components
✅ Completing 3 practical projects
✅ Learning to use free Ollama models"

### Homework Instructions

**Required Homework (40 points):**
"Personalized Learning Assistant - Comprehensive use of Prompt Template and Memory"

**Optional Homework (30 points):**
"Content Creation Pipeline - Practice combining Chains"

**Challenge Homework (30 points):**
"Intelligent Customer Service System - Complete practical application"

**Emphasis:**
- All homework uses free Ollama, zero cost\!
- Complete reference code provided
- Submit to GitHub within 7 days

### Next Lesson Preview

"Lesson 4: Vector Databases and RAG

We will learn:
- How to convert documents into vectors
- Using ChromaDB to store knowledge
- Building AI that can answer questions about documents
- Implementing a true 'knowledge base Q&A system'"

### Q&A Time (10 minutes)

Prepared common questions:
1. Q: "Compared to using APIs directly, is LangChain slower?"
   A: "Almost no performance loss, LangChain is a lightweight wrapper"

2. Q: "Can free Ollama be used in production?"
   A: "Yes\! Many companies use Ollama to deploy private AI services"

3. Q: "Does Memory consume a lot of RAM?"
   A: "Depends on window size, ConversationBufferWindowMemory is lightweight"

4. Q: "How to debug when Chain errors out?"
   A: "Use verbose=True, test each component step by step"

---

## Teaching Techniques Suggestions

### Pacing Control
- ⏱️ One interactive session every 15-20 minutes
- 🎯 Theory explanations no more than 10 minutes
- 💻 Every concept paired with a practical demo
- 🤝 Student practice every 30 minutes

### Student Engagement
- Questions: Random call on students to answer (not always those who raise hands)
- Programming: Have students share screens to showcase code
- Discussion: Group discussions (2-3 people per group)
- Voting: Use chat to vote on next example

### Anticipating Common Student Questions
1. "Why isn't my code working?"
   → Check: Is Ollama running, is model downloaded, syntax errors

2. "Memory doesn't seem to be working?"
   → Check: Is memory initialized, using same conversation instance

3. "Output results are different every time?"
   → Explain: temperature parameter effect, reduce or set to 0 for stable output

4. "Code running very slow?"
   → Explain: Local LLM is slower the first time, faster afterwards; can reduce max_tokens

### Classroom Management
- 📱 Remind students to turn off notifications
- ⏰ Start on time, end on time
- 🍵 Arrange 5-minute break at the 90-minute mark
- 💾 Remind to save code regularly

### Lab Environment Preparation
- Ensure all computers have Ollama installed
- Pre-download llama3.2 model (avoid network congestion)
- Prepare GitHub repository links for all example code
- Test projector and code demonstration effects

---

## Contingency Plans

### Technical Issues
- **Ollama service down** → Prepare OpenAI API as backup (provide temporary key)
- **Network failure** → All materials downloaded locally in advance
- **Code examples error** → Prepare multiple versions of code

### Insufficient Time
**Priority Ranking:**
1. Must cover: LangChain intro, Prompt Template, Memory basics
2. Important: Chain basics, chatbot project
3. Optional: Advanced applications, in-depth parameter tuning

**Compression Strategy:**
- Reduce lab time (compress from 15 minutes to 10 minutes)
- Skip OpenAI API demo (only teach Ollama)
- Advanced applications as post-class materials

### Student Progress Variation
- **Fast students** → Provide bonus challenge questions
- **Slow students** → Arrange TA for one-on-one tutoring
- **Overall slow** → Extend lab time, compress theory explanation

---

## Post-Class Follow-up

### Learning Resource Distribution
- LangChain official documentation links
- Recommended YouTube tutorials
- Showcase of excellent student homework
- FAQ document for common questions

### Discussion Group Management
- Post homework link within 24 hours after class
- Collect student feedback (anonymous survey)
- Answer 3-5 group questions daily
- Share relevant technical articles

### Homework Grading
- Complete grading within 72 hours
- Provide detailed improvement suggestions
- Showcase excellent homework in next class
- Record common errors to improve teaching

---

## Teaching Effectiveness Evaluation

### Class Checkpoints
- [ ] 80% of students successfully install LangChain
- [ ] 60% of students can independently create Prompt Templates
- [ ] 50% of students can build simple Chains
- [ ] 40% of students can implement conversations with memory

### Post-Class Survey (5 questions)
1. What was your biggest takeaway today?
2. Which part was most difficult to understand?
3. Was the lab time sufficient?
4. How was the course pace (too fast/appropriate/too slow)?
5. What are your expectations for the next lesson?

### Improvement Directions
- Adjust difficulty based on survey
- Increase/decrease lab time
- Optimize code examples
- Update outdated content

---

**Wishing you successful teaching\!**
