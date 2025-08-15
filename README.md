# Vijay Pagare's Blog

This is the source code for my personal blog built with [Hugo](https://gohugo.io) and the [Hugo Bear Blog theme](https://github.com/janraasch/hugo-bearblog). Hosted on [GitHub Pages](https://github.com/pagarevijayy/vijay-pagare-blog).

## 🚀 Features

- Super lightweight & fast static site
- Minimalist design inspired by Bear Blog
- SEO-friendly and responsive
- Easy to maintain & deploy

## 🛠 Local Development

1. **Clone the repository**  
   ```bash
   git clone https://github.com/pagarevijayy/vijay-pagare-blog.git
   cd vijay-pagare-blog
   ```

2. **Install Hugo**  
   Follow [Hugo installation instructions](https://gohugo.io/getting-started/installing/).

3. **Start the development server**  
   ```bash
   hugo server -D
   ```
   Your site will be available at [http://localhost:1313](http://localhost:1313).

## 📦 Deployment

Run the following to generate a production build:

```bash
hugo --gc --cleanDestinationDir --minify
```

The output will be in the `public/` folder. You can deploy this to GitHub Pages, Netlify, Vercel, or any static hosting provider.

## 📄 License

This project is released under the MIT License.
