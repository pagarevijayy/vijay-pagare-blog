# Hugo + Vercel Deployment SOP

This document outlines the standard process for writing, previewing, and deploying blog posts.

---

## 1. Setup
- Hugo is installed locally.
- `/public` is in `.gitignore`.
- Vercel project is linked to your GitHub repo.
- Vercel build command: `hugo --gc --cleanDestinationDir --minify`
- Vercel output directory: `public`

---

## 2. Writing a New Post
1. Create a new branch (optional but clean):
   ```bash
   git checkout -b post/my-new-article
   ```
2. Create a new post file:
   ```bash
   hugo new blog/my-new-article.md
   ```
3. Write your content locally.
4. Preview with:
   ```bash
   hugo server -D
   ```
5. When ready to publish, set in front matter:
   ```yaml
   draft: false
   ```

---

## 3. Committing Changes
1. Stage and commit:
   ```bash
   git add .
   git commit -m "Add post: My New Article"
   ```
2. Push to GitHub:
   ```bash
   git push origin post/my-new-article
   ```
3. Merge branch into `main` (on GitHub or locally).

---

## 4. Deployment
- Once changes are pushed to `main`, Vercel automatically builds and deploys.
- No need to commit `/public` — Vercel builds it.

---

## 5. Editing Existing Posts
- Edit the `.md` file in `content/blog/` locally.
- Preview with `hugo server -D`.
- Commit & push — Vercel redeploys automatically.

---