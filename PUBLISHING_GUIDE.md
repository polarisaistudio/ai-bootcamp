# 📚 Publishing AI Bootcamp to GitHub + Jekyll

This guide will help you publish your AI Bootcamp course content to GitHub Pages using Jekyll.

## 🎯 Overview

We'll set up a professional course website with:
- Course homepage
- Lesson pages with detailed content
- Code examples and demos
- Assignment pages
- Beautiful, responsive design

## 📋 Prerequisites

- GitHub account
- Git installed locally
- Basic command line knowledge

## 🚀 Quick Start (5 Steps)

### Step 1: Create GitHub Repository

```bash
# Create a new directory for your course
mkdir ai-bootcamp-website
cd ai-bootcamp-website

# Initialize git
git init

# Create initial structure
mkdir -p _lessons _includes _layouts assets/css assets/js assets/images
```

### Step 2: Set Up Jekyll Configuration

Create `_config.yml`:

```yaml
title: AI工程师训练营
description: 从零开始，4周成为AI工程师
url: "https://yourusername.github.io"
baseurl: "/ai-bootcamp"

# Build settings
markdown: kramdown
theme: minima
plugins:
  - jekyll-feed
  - jekyll-seo-tag
  - jekyll-sitemap

# Collections
collections:
  lessons:
    output: true
    permalink: /lessons/:path/

# Defaults
defaults:
  - scope:
      path: ""
      type: "lessons"
    values:
      layout: "lesson"
```

### Step 3: Create Layouts

Create `_layouts/default.html`:

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title }} | {{ site.title }}</title>
    <link rel="stylesheet" href="{{ '/assets/css/main.css' | relative_url }}">
    {% seo %}
</head>
<body>
    <header class="site-header">
        <div class="container">
            <nav>
                <a href="{{ '/' | relative_url }}" class="logo">{{ site.title }}</a>
                <ul class="nav-menu">
                    <li><a href="{{ '/' | relative_url }}">首页</a></li>
                    <li><a href="{{ '/lessons/' | relative_url }}">课程</a></li>
                    <li><a href="{{ '/assignments/' | relative_url }}">作业</a></li>
                    <li><a href="https://github.com/yourusername/ai-bootcamp">GitHub</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main class="content">
        {{ content }}
    </main>

    <footer class="site-footer">
        <div class="container">
            <p>&copy; 2024 {{ site.title }}. All rights reserved.</p>
        </div>
    </footer>

    <script src="{{ '/assets/js/main.js' | relative_url }}"></script>
</body>
</html>
```

Create `_layouts/lesson.html`:

```html
---
layout: default
---

<article class="lesson">
    <div class="container">
        <div class="lesson-header">
            <h1>{{ page.title }}</h1>
            <div class="lesson-meta">
                <span class="duration">⏱️ {{ page.duration }}</span>
                <span class="difficulty">📊 {{ page.difficulty }}</span>
            </div>
        </div>

        <div class="lesson-content">
            {{ content }}
        </div>

        <div class="lesson-nav">
            {% if page.previous.url %}
                <a href="{{ page.previous.url | relative_url }}" class="prev">← {{ page.previous.title }}</a>
            {% endif %}
            {% if page.next.url %}
                <a href="{{ page.next.url | relative_url }}" class="next">{{ page.next.title }} →</a>
            {% endif %}
        </div>
    </div>
</article>
```

### Step 4: Create Homepage

Create `index.md`:

```markdown
---
layout: default
title: 首页
---

# 🚀 AI工程师训练营

## 从零开始，4周成为AI工程师

欢迎来到AI工程师训练营！在这个为期4周的密集课程中，你将学习如何从零开始构建AI应用。

### 📅 课程大纲

<div class="course-outline">
    {% assign lessons = site.lessons | sort: 'order' %}
    {% for lesson in lessons %}
    <div class="lesson-card">
        <h3>
            <a href="{{ lesson.url | relative_url }}">
                {{ lesson.title }}
            </a>
        </h3>
        <p>{{ lesson.description }}</p>
        <div class="lesson-info">
            <span>⏱️ {{ lesson.duration }}</span>
            <span>📊 {{ lesson.difficulty }}</span>
        </div>
    </div>
    {% endfor %}
</div>

### 🎯 学习目标

- ✅ 掌握LLM模型选择和使用
- ✅ 精通Prompt工程技巧
- ✅ 学会构建AI应用
- ✅ 理解成本优化方法

### 🛠️ 技术栈

- Python 3.11+
- OpenAI API
- Anthropic Claude
- Streamlit
- LangChain

### 📚 开始学习

<a href="{{ '/lessons/lesson-01/' | relative_url }}" class="cta-button">
    开始第一课 →
</a>
```

### Step 5: Create Lesson Content

Create `_lessons/lesson-01.md`:

```markdown
---
layout: lesson
title: "Lesson 1: 认识LLM生态"
order: 1
duration: "3小时"
difficulty: "初级"
description: "全面认识LLM生态，掌握模型选择和参数优化"
---

## 📖 课程概述

本课程将带你全面认识LLM生态系统，学习如何选择合适的模型，优化参数设置，控制成本。

### 🎯 学习目标

1. 了解主流LLM模型（GPT、Claude、Gemini等）
2. 掌握Token机制和计费方式
3. 学会参数调优（Temperature、Top-p等）
4. 构建实际应用案例

---

## 🎬 Part 1: 开场与激发兴趣 (0-15分钟)

### [0:00-2:00] 开场白

大家好，欢迎来到AI工程师训练营的第一课！

我是[你的名字]，在接下来的4周里，我将带领大家从零开始，成为一名能够独立开发AI应用的工程师。

### [2:00-5:00] 痛点场景

让我给大家看一个真实的故事...

> 💡 **案例**: 创业公司的API账单惊魂

上个月，我的一个朋友开了一家创业公司，他兴奋地告诉我："我们用GPT-4做客服系统！"

一个月后，他收到了OpenAI的账单：**$3,847.52** 😱

#### 成本分析

```python
# 让我们算一下：
daily_users = 1000
conversations_per_user = 10
tokens_per_conversation = 500
gpt4_price = 0.03  # per 1K tokens

daily_cost = daily_users * conversations_per_user * (tokens_per_conversation / 1000) * gpt4_price
monthly_cost = daily_cost * 30

print(f"每天成本: ${daily_cost}")  # $150
print(f"每月成本: ${monthly_cost}")  # $4,500
```

💡 **互动问题**: 如果换成GPT-3.5，成本会是多少？

<details>
<summary>点击查看答案</summary>

使用GPT-3.5-turbo (价格: $0.001/1K tokens):
- 每天成本: **$5**
- 每月成本: **$150**
- **节省 96.7%!**

</details>

---

## 🎯 Part 2: 核心概念讲解 (15-45分钟)

### [15:00-25:00] 模型生态全景

就像选择交通工具一样：
- 去楼下买早餐 ≠ 开法拉利
- 简单任务 ≠ GPT-4

#### 模型对比表

| 模型 | 速度 | 质量 | 成本 | 最佳场景 |
|------|------|------|------|----------|
| GPT-4o | ⭐⭐ | ⭐⭐⭐⭐⭐ | $$$ | 复杂推理、代码生成 |
| GPT-4o-mini | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | $ | 平衡选择 |
| GPT-3.5 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | $ | 简单对话、客服 |
| Claude-Sonnet | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | $$ | 长文本、分析 |

### [25:00-35:00] Token深度理解

> 💡 **类比**: Token就像乐高积木
> - 英文：标准积木（1词 ≈ 1 token）
> - 中文：特殊积木（1字 ≈ 2-3 tokens）

#### Token计算示例

```python
import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

# 英文
english_text = "Hello World"
english_tokens = len(encoder.encode(english_text))
print(f"英文: {english_tokens} tokens")  # 2 tokens

# 中文
chinese_text = "你好世界"
chinese_tokens = len(encoder.encode(chinese_text))
print(f"中文: {chinese_tokens} tokens")  # 8 tokens

# 成本对比
gpt35_price = 0.001  # per 1K tokens
english_cost = (english_tokens / 1000) * gpt35_price
chinese_cost = (chinese_tokens / 1000) * gpt35_price

print(f"英文成本: ${english_cost:.6f}")
print(f"中文成本: ${chinese_cost:.6f}")
print(f"中文贵 {chinese_cost/english_cost:.1f}x")
```

### [35:00-45:00] Temperature参数实验

**Temperature 类比**:
- `Temperature = 0`: 严肃的会计师（确定性）
- `Temperature = 1`: 创意总监（创造性）
- `Temperature = 2`: 喝醉的诗人（随机性）

#### 实验代码

```python
import openai

client = openai.OpenAI()

prompt = "用一句话描述夕阳"

for temp in [0, 0.5, 1.0, 1.5]:
    print(f"\n🌡️ Temperature = {temp}")

    for i in range(3):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temp,
            max_tokens=30
        )
        print(f"  样本{i+1}: {response.choices[0].message.content}")
```

**观察规律**:
- Temperature ↓ → 输出更一致
- Temperature ↑ → 输出更多样

---

## 🛠️ Part 3: 动手实践 (45-120分钟)

### [45:00-60:00] 环境搭建

#### 1. 安装Python

```bash
# Mac用户
brew install python@3.11

# Windows用户
# 访问 https://python.org 下载安装
```

#### 2. 创建项目

```bash
# 创建项目文件夹
mkdir ai-bootcamp
cd ai-bootcamp

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Mac/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

#### 3. 安装依赖

创建 `requirements.txt`:

```txt
openai==1.12.0
anthropic==0.18.0
tiktoken==0.6.0
streamlit==1.31.0
pandas==2.2.0
plotly==5.18.0
python-dotenv==1.0.1
```

安装:

```bash
pip install -r requirements.txt
```

#### 4. 配置API密钥

创建 `.env`:

```bash
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here
```

⚠️ **重要**: 添加到 `.gitignore`:

```
.env
venv/
__pycache__/
*.pyc
```

### [60:00-75:00] 第一个程序

创建 `first_api_call.py`:

```python
import openai
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

# 初始化客户端
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def my_first_chat():
    """我的第一个AI对话"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个友好的AI助手"},
            {"role": "user", "content": "你好！请用一句话介绍自己。"}
        ],
        temperature=0.7,
        max_tokens=50
    )

    # 提取结果
    ai_message = response.choices[0].message.content
    tokens_used = response.usage.total_tokens
    cost = (tokens_used / 1000) * 0.001

    print(f"AI回复: {ai_message}")
    print(f"Token使用: {tokens_used}")
    print(f"成本: ${cost:.6f}")

if __name__ == "__main__":
    my_first_chat()
```

运行:

```bash
python first_api_call.py
```

---

## 📝 作业

### 必做题1: 模型对比报告 (30分)

选择一个业务场景，对比至少3个模型的性能。

**提交内容**:
1. 测试代码
2. 测试结果CSV
3. 分析报告（Markdown）

### 必做题2: Token优化 (30分)

优化一个长Prompt，减少至少50% tokens但保持效果。

### 选做题: 智能模型选择器 (40分)

实现一个函数，根据需求自动选择最优模型。

```python
def smart_model_selector(
    prompt: str,
    max_budget: float,
    quality_requirement: int  # 1-10
) -> dict:
    """
    返回推荐的模型和参数配置
    """
    pass
```

---

## 📚 资源链接

- [OpenAI API文档](https://platform.openai.com/docs)
- [Anthropic文档](https://docs.anthropic.com/)
- [课程GitHub仓库](https://github.com/yourusername/ai-bootcamp)
- [Discord讨论群](https://discord.gg/your-invite)

---

## 🎯 下节课预告

**Lesson 2: Prompt工程实战**

学习内容:
- Zero-shot vs Few-shot
- Chain-of-Thought推理
- Prompt模板设计
- 注入攻击防御

课前准备:
- 完成本节作业
- 准备3个想优化的Prompt
- 阅读推荐文章

---

<div class="lesson-footer">
    <p>💡 有问题？在 <a href="https://github.com/yourusername/ai-bootcamp/discussions">GitHub Discussions</a> 提问</p>
</div>
```

## 🎨 Styling

Create `assets/css/main.css`:

```css
/* Variables */
:root {
    --primary-color: #2563eb;
    --secondary-color: #7c3aed;
    --text-color: #1f2937;
    --bg-color: #ffffff;
    --border-color: #e5e7eb;
    --code-bg: #f3f4f6;
}

/* Base styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'PingFang SC', 'Hiragino Sans GB', sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background: var(--bg-color);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Header */
.site-header {
    background: white;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    position: sticky;
    top: 0;
    z-index: 100;
}

.site-header nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 0;
}

.logo {
    font-size: 1.5rem;
    font-weight: bold;
    color: var(--primary-color);
    text-decoration: none;
}

.nav-menu {
    display: flex;
    list-style: none;
    gap: 2rem;
}

.nav-menu a {
    color: var(--text-color);
    text-decoration: none;
    transition: color 0.3s;
}

.nav-menu a:hover {
    color: var(--primary-color);
}

/* Lesson cards */
.course-outline {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.lesson-card {
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 1.5rem;
    transition: transform 0.3s, box-shadow 0.3s;
}

.lesson-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.lesson-card h3 {
    margin-bottom: 0.5rem;
}

.lesson-card h3 a {
    color: var(--primary-color);
    text-decoration: none;
}

.lesson-info {
    display: flex;
    gap: 1rem;
    margin-top: 1rem;
    font-size: 0.9rem;
    color: #6b7280;
}

/* Code blocks */
pre {
    background: var(--code-bg);
    border-radius: 4px;
    padding: 1rem;
    overflow-x: auto;
    margin: 1rem 0;
}

code {
    background: var(--code-bg);
    padding: 0.2rem 0.4rem;
    border-radius: 3px;
    font-size: 0.9em;
}

pre code {
    background: none;
    padding: 0;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 2rem 0;
}

th, td {
    padding: 0.75rem;
    text-align: left;
    border-bottom: 1px solid var(--border-color);
}

th {
    background: var(--code-bg);
    font-weight: 600;
}

/* Buttons */
.cta-button {
    display: inline-block;
    background: var(--primary-color);
    color: white;
    padding: 0.75rem 1.5rem;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
    transition: background 0.3s;
}

.cta-button:hover {
    background: #1d4ed8;
}

/* Blockquotes */
blockquote {
    border-left: 4px solid var(--primary-color);
    padding-left: 1rem;
    margin: 1rem 0;
    color: #4b5563;
    background: #f9fafb;
    padding: 1rem;
    border-radius: 4px;
}

/* Details/Summary */
details {
    margin: 1rem 0;
    padding: 1rem;
    background: #f9fafb;
    border-radius: 4px;
}

summary {
    cursor: pointer;
    font-weight: 600;
    user-select: none;
}

/* Footer */
.site-footer {
    background: #f9fafb;
    padding: 2rem 0;
    margin-top: 4rem;
    text-align: center;
    color: #6b7280;
}

/* Responsive */
@media (max-width: 768px) {
    .nav-menu {
        gap: 1rem;
        font-size: 0.9rem;
    }

    .course-outline {
        grid-template-columns: 1fr;
    }
}
```

## 🚀 Deployment

### Option 1: GitHub Pages (Recommended)

1. **Create GitHub repository**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/ai-bootcamp.git
   git branch -M main
   git push -u origin main
   ```

2. **Enable GitHub Pages**:
   - Go to repository Settings
   - Navigate to Pages
   - Source: Deploy from branch
   - Branch: main / root
   - Save

3. **Your site will be live at**:
   `https://yourusername.github.io/ai-bootcamp/`

### Option 2: Custom Domain

1. Add `CNAME` file:
   ```
   courses.yourdomain.com
   ```

2. Configure DNS:
   ```
   Type: CNAME
   Name: courses
   Value: yourusername.github.io
   ```

## 📦 Complete File Structure

```
ai-bootcamp-website/
├── _config.yml
├── _layouts/
│   ├── default.html
│   └── lesson.html
├── _lessons/
│   ├── lesson-01.md
│   ├── lesson-02.md
│   └── ...
├── assets/
│   ├── css/
│   │   └── main.css
│   ├── js/
│   │   └── main.js
│   └── images/
├── index.md
├── assignments.md
├── .gitignore
├── Gemfile
└── README.md
```

## 🔧 Local Development

```bash
# Install Jekyll
gem install bundler jekyll

# Create Gemfile
cat > Gemfile << EOF
source "https://rubygems.org"
gem "jekyll"
gem "jekyll-seo-tag"
gem "jekyll-sitemap"
EOF

# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# Visit http://localhost:4000
```

## ✅ Checklist

- [ ] Repository created on GitHub
- [ ] Jekyll configuration complete
- [ ] Layouts created
- [ ] Homepage created
- [ ] Lesson 1 content added
- [ ] CSS styling applied
- [ ] Local testing successful
- [ ] Pushed to GitHub
- [ ] GitHub Pages enabled
- [ ] Site is live!

## 🎯 Next Steps

1. **Add more lessons**: Create files in `_lessons/` directory
2. **Add images**: Place in `assets/images/`
3. **Add code examples**: Create a `/code/` directory
4. **Enable comments**: Add Disqus or utterances
5. **Add analytics**: Google Analytics or Plausible

## 💡 Pro Tips

1. **Use GitHub Actions** for automated deployment
2. **Add search functionality** with Algolia
3. **Enable syntax highlighting** with Prism.js
4. **Add progress tracking** with localStorage
5. **Create PDF exports** for each lesson

---

Need help? Check the [Jekyll documentation](https://jekyllrb.com/docs/) or ask in the course Discord!
