# ⚡ Quick Start Guide - 5 Minutes to Published!

This guide will get your AI Bootcamp course published to GitHub Pages in just 5 minutes.

## 🎯 Step-by-Step Instructions

### Step 1: Create GitHub Repository (2 minutes)

1. Go to [GitHub](https://github.com) and log in
2. Click the **"+"** icon → **"New repository"**
3. Fill in:
   - Repository name: `ai-bootcamp`
   - Description: "AI Engineering Bootcamp - Zero to Hero in 4 Weeks"
   - Public
   - ✅ Add a README file (uncheck this, we already have one)
4. Click **"Create repository"**

### Step 2: Update Configuration (1 minute)

Open `_config.yml` and replace these values:

```yaml
url: "https://YOUR-USERNAME.github.io"
baseurl: "/ai-bootcamp"
repository: YOUR-USERNAME/ai-bootcamp
email: your.email@example.com

# Social
social:
  github: YOUR-USERNAME
  twitter: YOUR-TWITTER
  discord: YOUR-DISCORD-INVITE
```

### Step 3: Deploy (1 minute)

Run the deployment script:

```bash
# Make sure you're in the project directory
cd "/Users/xinwang/Polaris AI Studio/youtube/AI/Bootcamp1/Class1"

# Run the deployment script
./deploy.sh
```

The script will:
- ✅ Initialize git (if needed)
- ✅ Add all files
- ✅ Create a commit
- ✅ Push to GitHub

**Follow the prompts** when asked for:
- Commit message (or use default)
- GitHub credentials

### Step 4: Enable GitHub Pages (1 minute)

1. Go to your repository on GitHub
2. Click **"Settings"** tab
3. Click **"Pages"** in the left sidebar
4. Under **"Source"**:
   - Branch: `main`
   - Folder: `/ (root)`
5. Click **"Save"**

### Step 5: Visit Your Site! (Wait ~2 minutes)

Your site will be live at:

```
https://YOUR-USERNAME.github.io/ai-bootcamp/
```

GitHub Pages takes about 1-2 minutes to build. Refresh the page until you see your course!

---

## 🚀 Alternative: One-Command Deploy

If you prefer a single command:

```bash
# Initialize and push to GitHub
git init
git add .
git commit -m "Initial course publish"
git remote add origin https://github.com/YOUR-USERNAME/ai-bootcamp.git
git branch -M main
git push -u origin main
```

Then enable GitHub Pages in Settings → Pages.

---

## 🛠️ Local Development

To preview your site locally before publishing:

### Option 1: Using Jekyll (Recommended for Mac/Linux)

```bash
# Install Jekyll (one-time setup)
gem install bundler jekyll

# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# Visit http://localhost:4000
```

### Option 2: Using Docker (Works everywhere)

```bash
# Run with Docker (no installation needed)
docker run --rm \
  --volume="$PWD:/srv/jekyll" \
  -p 4000:4000 \
  jekyll/jekyll \
  jekyll serve
```

### Option 3: Using GitHub Codespaces (Zero setup)

1. Go to your GitHub repository
2. Click **"Code"** → **"Codespaces"** → **"Create codespace on main"**
3. In the terminal:
   ```bash
   bundle install
   bundle exec jekyll serve
   ```
4. Click "Open in Browser" when prompted

---

## 📝 Making Updates

After making changes to your content:

```bash
# Option 1: Use the deploy script
./deploy.sh

# Option 2: Manual git commands
git add .
git commit -m "Update lesson content"
git push
```

GitHub Pages will automatically rebuild (takes 1-2 minutes).

---

## ✅ Verification Checklist

After deployment, verify:

- [ ] Homepage loads correctly
- [ ] Lesson 1 page is accessible
- [ ] Images display properly
- [ ] Code blocks have syntax highlighting
- [ ] Navigation links work
- [ ] Mobile view looks good
- [ ] All social links are correct

---

## 🐛 Troubleshooting

### Site not showing up?

1. **Wait 2-3 minutes** - GitHub Pages needs time to build
2. **Check Actions tab** - See if the build succeeded
3. **Verify Settings** - Make sure Pages is enabled with correct branch

### Page shows 404?

1. Check `_config.yml` → `baseurl` matches your repo name
2. Try accessing: `https://YOUR-USERNAME.github.io/ai-bootcamp/` (with trailing slash)

### CSS not loading?

1. Make sure `assets/css/main.css` exists
2. Check browser console for errors
3. Clear browser cache and hard reload (Cmd/Ctrl + Shift + R)

### Build failed?

1. Go to GitHub → Actions tab
2. Click on the failed build
3. Read error messages
4. Common issues:
   - Syntax error in `_config.yml`
   - Missing front matter in `.md` files
   - Invalid Liquid syntax

### Local preview not working?

```bash
# Clean and rebuild
bundle exec jekyll clean
bundle exec jekyll serve --trace
```

### Still having issues?

1. Check [GitHub Pages Documentation](https://docs.github.com/en/pages)
2. Search [Jekyll Issues](https://github.com/jekyll/jekyll/issues)
3. Ask in our [Discord](YOUR-DISCORD-LINK)

---

## 🎨 Customization Tips

### Change Theme Colors

Edit `assets/css/main.css`:

```css
:root {
    --primary-color: #2563eb;     /* Change to your color */
    --secondary-color: #7c3aed;   /* Change to your color */
}
```

### Add Your Logo

1. Add image to `assets/images/logo.png`
2. Edit `_layouts/default.html`:
   ```html
   <a href="/" class="logo">
     <img src="{{ '/assets/images/logo.png' | relative_url }}" alt="Logo">
   </a>
   ```

### Add Google Analytics

Edit `_config.yml`:

```yaml
google_analytics: UA-XXXXXXXXX-X
```

### Enable Comments

Edit `_config.yml`:

```yaml
disqus:
  shortname: your-disqus-shortname
```

---

## 📊 Next Steps

Now that your site is live:

1. ✅ **Share it!**
   - Tweet about your course
   - Post in relevant communities
   - Add to your resume/portfolio

2. ✅ **Add Content**
   - Create more lesson pages
   - Add assignments
   - Write blog posts

3. ✅ **Engage Students**
   - Set up Discord community
   - Create discussion forums
   - Host Q&A sessions

4. ✅ **Improve SEO**
   - Add meta descriptions
   - Submit to Google Search Console
   - Create a sitemap (automatically generated)

5. ✅ **Monitor**
   - Check GitHub Pages build status
   - Monitor site analytics
   - Gather student feedback

---

## 🎉 Congratulations!

Your AI Bootcamp course is now live on the internet!

**Share your course URL**:
```
https://YOUR-USERNAME.github.io/ai-bootcamp/
```

---

## 💬 Need Help?

- 📧 Email: your.email@example.com
- 💬 Discord: [Join our community](YOUR-DISCORD)
- 🐙 GitHub: [Open an issue](https://github.com/YOUR-USERNAME/ai-bootcamp/issues)

---

<p align="center">
  <strong>Happy Teaching! 🎓</strong>
</p>
