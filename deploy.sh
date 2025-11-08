#!/bin/bash

# AI Bootcamp - Quick Deployment Script
# This script helps you quickly deploy your Jekyll site to GitHub Pages

echo "🚀 AI Bootcamp - Deployment Script"
echo "=================================="
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored messages
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if git is installed
if ! command -v git &> /dev/null; then
    print_error "Git is not installed. Please install Git first."
    exit 1
fi

print_info "Git is installed ✓"

# Check if we're in a git repository
if [ ! -d ".git" ]; then
    print_info "Initializing git repository..."
    git init
    print_info "Git repository initialized ✓"
else
    print_info "Already in a git repository ✓"
fi

# Check if remote origin exists
if ! git remote get-url origin &> /dev/null; then
    echo ""
    print_warning "No remote repository configured."
    echo ""
    echo "Please follow these steps:"
    echo "1. Create a new repository on GitHub"
    echo "2. Copy the repository URL"
    echo "3. Run: git remote add origin <your-repo-url>"
    echo ""
    read -p "Press Enter when you've added the remote, or Ctrl+C to exit..."
fi

# Get current branch
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo "main")

if [ -z "$BRANCH" ]; then
    print_info "Creating main branch..."
    git checkout -b main
    BRANCH="main"
fi

print_info "Current branch: $BRANCH"

# Add all files
print_info "Adding files to git..."
git add .

# Commit
echo ""
read -p "Enter commit message (or press Enter for default): " COMMIT_MSG
if [ -z "$COMMIT_MSG" ]; then
    COMMIT_MSG="Update course content - $(date +%Y-%m-%d)"
fi

print_info "Committing changes..."
git commit -m "$COMMIT_MSG" || print_warning "No changes to commit"

# Push
echo ""
print_info "Pushing to GitHub..."
if git push -u origin $BRANCH; then
    print_info "Successfully pushed to GitHub! ✓"
else
    print_error "Failed to push. Please check your remote configuration."
    exit 1
fi

# GitHub Pages information
echo ""
echo "=================================="
print_info "🎉 Deployment complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Go to your GitHub repository"
echo "2. Click on 'Settings'"
echo "3. Navigate to 'Pages' in the left sidebar"
echo "4. Under 'Source', select 'Deploy from a branch'"
echo "5. Select branch: $BRANCH and folder: / (root)"
echo "6. Click 'Save'"
echo ""
echo "Your site will be live in a few minutes at:"
REPO_URL=$(git remote get-url origin)
REPO_NAME=$(basename -s .git "$REPO_URL")
USERNAME=$(dirname "$REPO_URL" | xargs basename)
echo "https://${USERNAME}.github.io/${REPO_NAME}/"
echo ""
print_info "Happy teaching! 🎓"
