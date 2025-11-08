# 🚀 AI工程师训练营 | AI Engineering Bootcamp

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Jekyll](https://img.shields.io/badge/Jekyll-4.3-red)](https://jekyllrb.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

从零开始，4周成为AI工程师 | Zero to AI Engineer in 4 Weeks

## 📚 关于本课程

这是一个完全开源的AI工程师培训课程，专为想要快速掌握AI应用开发的工程师设计。课程内容包括：

- 🤖 LLM模型选择与使用
- ✍️ Prompt工程技巧
- 🔗 LangChain应用开发
- 📊 RAG系统构建
- 🚀 生产环境部署

## 🌐 在线访问

**课程网站**: [https://polarisaistudio.github.io/ai-bootcamp/](https://polarisaistudio.github.io/ai-bootcamp/)

## 📖 课程大纲

### Week 1: LLM基础
- **Lesson 1**: 认识LLM生态 (3小时)
- **Lesson 2**: Prompt工程基础 (3小时)

### Week 2: 应用开发
- **Lesson 3**: LangChain框架 (3小时)
- **Lesson 4**: 向量数据库与RAG (3小时)

### Week 3: 高级技能
- **Lesson 5**: Agent开发 (3小时)
- **Lesson 6**: 模型微调 (3小时)

### Week 4: 生产部署
- **Lesson 7**: 应用部署 (3小时)
- **Lesson 8**: 综合项目 (3小时)

## 🚀 快速开始

### 方法一：直接访问网站

访问 [课程网站](https://polarisaistudio.github.io/ai-bootcamp/) 开始学习。

### 方法二：本地运行

```bash
# 克隆仓库
git clone https://github.com/polarisaistudio/ai-bootcamp.git
cd ai-bootcamp

# 安装 Jekyll (如果还没安装)
gem install bundler jekyll

# 安装依赖
bundle install

# 启动本地服务器
bundle exec jekyll serve

# 访问 http://localhost:4000
```

### 方法三：运行Python代码

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 配置API密钥
cp .env.example .env
# 编辑 .env 文件，添加你的API密钥

# 运行示例代码
python examples/lesson01/first_api_call.py
```

## 📁 项目结构

```
ai-bootcamp/
├── _config.yml          # Jekyll配置
├── _layouts/            # 页面布局
│   ├── default.html
│   ├── lesson.html
│   └── assignment.html
├── _lessons/            # 课程内容
│   ├── lesson-01.md
│   ├── lesson-02.md
│   └── ...
├── assets/              # 静态资源
│   ├── css/
│   ├── js/
│   └── images/
├── examples/            # 代码示例
│   ├── lesson01/
│   ├── lesson02/
│   └── ...
├── assignments/         # 作业
├── index.md             # 首页
├── Gemfile              # Ruby依赖
├── requirements.txt     # Python依赖
├── deploy.sh            # 部署脚本
└── README.md            # 本文件
```

## 🛠️ 技术栈

### 网站
- [Jekyll](https://jekyllrb.com/) - 静态网站生成器
- [GitHub Pages](https://pages.github.com/) - 免费托管
- [Markdown](https://www.markdownguide.org/) - 内容编写

### 课程代码
- **Python** 3.11+
- **OpenAI API** - GPT模型
- **Anthropic Claude** - Claude模型
- **LangChain** - AI应用框架
- **Streamlit** - Web应用
- **FastAPI** - API服务

## 📝 贡献指南

我们欢迎各种形式的贡献！

### 报告问题

在 [Issues](https://github.com/polarisaistudio/ai-bootcamp/issues) 页面报告：
- 🐛 Bug报告
- 💡 功能建议
- 📝 内容改进
- ❓ 问题咨询

### 提交改进

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

### 内容贡献

- 修复错别字或语法错误
- 改进代码示例
- 添加新的练习题
- 完善文档说明

## 📋 课程要求

### 必需
- 💻 电脑 (Mac/Windows/Linux)
- 🔑 OpenAI API密钥
- ⏰ 每周8-12小时学习时间

### 推荐
- 基础Python知识
- 对AI感兴趣
- 愿意动手实践

### 不需要
- ❌ 深度学习背景
- ❌ 数学/统计学
- ❌ AI研究经验

## 💰 成本

- 课程内容：**完全免费**
- API调用费用：约 **$5-10/周**
  - OpenAI API使用费
  - 其他API服务（可选）

## 🎓 结业证书

完成以下要求可获得结业证书：
- ✅ 完成所有课程
- ✅ 提交所有作业
- ✅ 通过最终项目评审

## 📞 联系方式

- 📧 Email: your.email@example.com
- 💬 Discord: [加入社群](https://discord.gg/polarisai)
- 🐙 GitHub: [提交Issue](https://github.com/polarisaistudio/ai-bootcamp/issues)
- 🐦 Twitter: [@polarisaistudio](https://twitter.com/polarisaistudio)

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🙏 致谢

- OpenAI 团队的GPT模型
- Anthropic 团队的Claude模型
- LangChain 社区
- 所有贡献者和学员

## ⭐ Star历史

[![Star History Chart](https://api.star-history.com/svg?repos=polarisaistudio/ai-bootcamp&type=Date)](https://star-history.com/#polarisaistudio/ai-bootcamp&Date)

---

<p align="center">
  如果觉得课程有帮助，请给我们一个 ⭐ Star！
</p>

<p align="center">
  Made with ❤️ by AI教育社区
</p>
