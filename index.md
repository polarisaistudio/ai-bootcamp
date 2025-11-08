---
layout: home
title: 首页
---

# 🚀 AI工程师训练营

## 从零开始，4周成为AI工程师

欢迎来到AI工程师训练营！这是一个为期**4周**的密集课程，专为想要快速掌握AI应用开发的工程师设计。无论你是否有编程基础，都能通过这个课程学会构建实用的AI应用。

---

## 💡 为什么选择这个课程？

<div class="features">
  <div class="feature-card">
    <h3>🎯 实战导向</h3>
    <p>每节课都包含实际项目，学完即可上手开发</p>
  </div>

  <div class="feature-card">
    <h3>💰 成本优化</h3>
    <p>学会如何降低90%的API成本，避免账单爆炸</p>
  </div>

  <div class="feature-card">
    <h3>🔧 完整工具链</h3>
    <p>掌握从模型选择到部署的完整技术栈</p>
  </div>

  <div class="feature-card">
    <h3>👥 社区支持</h3>
    <p>加入Discord社群，与同学们一起学习成长</p>
  </div>
</div>

---

## 📅 课程大纲

{% assign lessons = site.lessons | sort: 'order' %}
<div class="lessons-grid">
{% for lesson in lessons %}
  <div class="lesson-card">
    <div class="lesson-header">
      <span class="lesson-number">Lesson {{ lesson.order }}</span>
      <span class="lesson-duration">{{ lesson.duration }}</span>
    </div>
    <h3>
      <a href="{{ lesson.url | relative_url }}">{{ lesson.title }}</a>
    </h3>
    <p class="lesson-description">{{ lesson.description }}</p>
    <div class="lesson-meta">
      <span class="difficulty difficulty-{{ lesson.difficulty }}">
        📊 {{ lesson.difficulty }}
      </span>
    </div>
  </div>
{% endfor %}
</div>

---

## 🎯 你将学到什么？

<div class="learning-outcomes">
  <div class="outcome">
    <h3>🤖 LLM模型掌握</h3>
    <ul>
      <li>理解GPT、Claude、Gemini等模型特点</li>
      <li>学会根据场景选择最优模型</li>
      <li>掌握Token机制和成本优化</li>
    </ul>
  </div>

  <div class="outcome">
    <h3>✍️ Prompt工程</h3>
    <ul>
      <li>Zero-shot/Few-shot学习</li>
      <li>Chain-of-Thought推理</li>
      <li>Prompt模板设计与优化</li>
    </ul>
  </div>

  <div class="outcome">
    <h3>🔗 应用开发</h3>
    <ul>
      <li>使用LangChain构建应用</li>
      <li>实现RAG知识库系统</li>
      <li>部署生产级AI应用</li>
    </ul>
  </div>

  <div class="outcome">
    <h3>🛠️ 实战项目</h3>
    <ul>
      <li>智能客服系统</li>
      <li>文档分析助手</li>
      <li>AI驱动的内容创作平台</li>
    </ul>
  </div>
</div>

---

## 🛠️ 技术栈

<div class="tech-stack">
  <div class="tech-category">
    <h4>编程语言</h4>
    <span class="tech-badge">Python 3.11+</span>
  </div>

  <div class="tech-category">
    <h4>AI平台</h4>
    <span class="tech-badge">OpenAI API</span>
    <span class="tech-badge">Anthropic Claude</span>
    <span class="tech-badge">Google Gemini</span>
  </div>

  <div class="tech-category">
    <h4>框架</h4>
    <span class="tech-badge">LangChain</span>
    <span class="tech-badge">Streamlit</span>
    <span class="tech-badge">FastAPI</span>
  </div>

  <div class="tech-category">
    <h4>数据库</h4>
    <span class="tech-badge">ChromaDB</span>
    <span class="tech-badge">Pinecone</span>
    <span class="tech-badge">PostgreSQL</span>
  </div>
</div>

---

## 📚 课程要求

### 必需条件
- 💻 一台能上网的电脑（Mac/Windows/Linux均可）
- 🔑 OpenAI API密钥（会指导如何申请）
- ⏰ 每周投入8-12小时学习时间

### 推荐背景
- 有基础编程经验（Python最佳，但不强制）
- 对AI应用开发感兴趣
- 愿意动手实践

### 不需要
- ❌ 深度学习理论知识
- ❌ 数学/统计学背景
- ❌ AI研究经验

---

## 🎓 学习路径

```mermaid
graph LR
    A[Week 1: LLM基础] --> B[Week 2: Prompt工程]
    B --> C[Week 3: 应用开发]
    C --> D[Week 4: 项目实战]
    D --> E[🎉 毕业项目]
```

### Week 1: LLM生态认知
- Lesson 1: 认识LLM生态
- Lesson 2: Prompt工程基础

### Week 2: 深入应用
- Lesson 3: LangChain框架
- Lesson 4: 向量数据库与RAG

### Week 3: 高级技能
- Lesson 5: Agent开发
- Lesson 6: 模型微调

### Week 4: 生产部署
- Lesson 7: 应用部署
- Lesson 8: 综合项目

---

## 🚀 开始学习

<div class="cta-section">
  <a href="{{ '/lessons/lesson-01/' | relative_url }}" class="cta-button primary">
    📖 开始第一课
  </a>
  <a href="{{ site.social.github }}" class="cta-button secondary">
    ⭐ Star on GitHub
  </a>
  <a href="{{ site.social.discord }}" class="cta-button secondary">
    💬 加入Discord
  </a>
</div>

---

## 💬 常见问题

<details>
<summary><strong>Q: 这个课程完全免费吗？</strong></summary>
<p>课程内容完全免费开源。但你需要自己准备OpenAI API密钥，会产生一些API调用费用（预计每周 $5-10）。</p>
</details>

<details>
<summary><strong>Q: 我没有编程基础可以学吗？</strong></summary>
<p>可以，但会比较有挑战。我们建议先学习Python基础（推荐资源见课程仓库）。如果你愿意投入时间，完全可以从零开始。</p>
</details>

<details>
<summary><strong>Q: 如何获得OpenAI API密钥？</strong></summary>
<p>访问 <a href="https://platform.openai.com" target="_blank">platform.openai.com</a>，注册账号后在API Keys页面创建。第一课会详细讲解。</p>
</details>

<details>
<summary><strong>Q: 完成课程后能做什么？</strong></summary>
<p>你将能够独立开发各种AI应用，如智能客服、文档分析工具、内容创作助手等。这些技能在当前就业市场非常抢手。</p>
</details>

<details>
<summary><strong>Q: 有结业证书吗？</strong></summary>
<p>完成所有作业并通过最终项目评审后，会获得课程结业证书（数字证书）。</p>
</details>

---

## 👨‍🏫 关于讲师

[在这里添加你的简介、经验、项目等]

---

## 📞 联系我们

- 📧 Email: {{ site.email }}
- 💬 Discord: [加入社群]({{ site.social.discord }})
- 🐙 GitHub: [提Issue]({{ site.repository }})
- 🐦 Twitter: [@{{ site.social.twitter }}](https://twitter.com/{{ site.social.twitter }})

---

<div class="footer-note">
  <p>⭐ 如果觉得课程有帮助，请在GitHub上给我们一个Star！</p>
  <p>📢 课程持续更新中，欢迎提供反馈和建议。</p>
</div>

<style>
.features {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

.feature-card {
  padding: 1.5rem;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.lessons-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.lesson-card {
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  padding: 1.5rem;
  transition: all 0.3s;
}

.lesson-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 16px rgba(37, 99, 235, 0.1);
  border-color: #2563eb;
}

.lesson-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.lesson-number {
  background: #2563eb;
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-size: 0.85rem;
  font-weight: 600;
}

.lesson-duration {
  color: #6b7280;
  font-size: 0.9rem;
}

.learning-outcomes {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

.outcome h3 {
  margin-bottom: 1rem;
  color: #2563eb;
}

.tech-stack {
  display: grid;
  gap: 1.5rem;
  margin: 2rem 0;
}

.tech-category {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
}

.tech-category h4 {
  width: 150px;
  margin: 0;
  color: #4b5563;
}

.tech-badge {
  background: #eff6ff;
  color: #2563eb;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  font-size: 0.9rem;
  border: 1px solid #bfdbfe;
}

.cta-section {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin: 3rem 0;
  flex-wrap: wrap;
}

.cta-button {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  border-radius: 6px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s;
}

.cta-button.primary {
  background: #2563eb;
  color: white;
}

.cta-button.primary:hover {
  background: #1d4ed8;
  transform: translateY(-2px);
}

.cta-button.secondary {
  background: white;
  color: #2563eb;
  border: 2px solid #2563eb;
}

.cta-button.secondary:hover {
  background: #eff6ff;
}

details {
  margin: 1rem 0;
  padding: 1rem;
  background: #f9fafb;
  border-radius: 4px;
  border-left: 4px solid #2563eb;
}

summary {
  cursor: pointer;
  font-weight: 600;
  user-select: none;
}

summary:hover {
  color: #2563eb;
}

.footer-note {
  text-align: center;
  margin-top: 4rem;
  padding: 2rem;
  background: #f9fafb;
  border-radius: 8px;
}

@media (max-width: 768px) {
  .lessons-grid {
    grid-template-columns: 1fr;
  }

  .features {
    grid-template-columns: 1fr;
  }
}
</style>
