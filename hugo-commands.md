# Common Hugo Commands

A quick reference for the most frequently used Hugo commands.

## 📝 Creating Content

```bash
# Create a new page
hugo new my-new-page.md

# Create a new blog post inside the 'content/blog' folder
hugo new blog/my-new-post.md
```

## 🚀 Running the Development Server

```bash
# Start the Hugo development server (with drafts enabled)
hugo server -D

# Start server with a custom source and themes directory
hugo server --source . --themesDir themes
```

## 🧹 Cleaning & Rebuilding

```bash
# Build site and clean the destination folder before writing
hugo --cleanDestinationDir

# Build the site with minified output
hugo --minify

# Build the site after garbage collection (clean up unused generated files).
hugo --gc
```

## 📦 Building for Production

```bash
# Build the site to the ./public folder
hugo

# Build the site with drafts disabled and output minified
hugo --minify

# Build optimised
hugo --gc --cleanDestinationDir --minify
```

## 🏷️ Helpful Flags

```bash
-D    # Include drafts in build or server
--cleanDestinationDir  # Remove old files from destination folder before building
--minify               # Minify HTML, CSS, JS in output
--themesDir            # Specify the themes directory
--source               # Specify an alternate source directory
```
