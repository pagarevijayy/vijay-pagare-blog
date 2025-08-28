# Hugo Notification Banner Integration Guide

## 1. File Structure
```
your-hugo-site/
├── config.yaml (or config.toml)
├── layouts/
│   └── partials/
│       └── notification-banner.html
└── content/
    └── your-pages.md
```

## 2. Integration Steps

### Step 1: Add the partial to your layout
Add this line to your `baseof.html` or wherever you want the banner to appear (typically right after the `<body>` tag):

```html
{{ partial "notification-banner.html" . }}
```

### Step 2: Add CSS to custom_head.html
Add the CSS code to your `layouts/partials/custom_head.html` file.

### Step 3: Configure site-wide banners
Update your `hugo.toml` with the banner settings (see the Hugo Config artifact).

## 3. Usage Examples

### Site-wide Banner (hugo.toml)
```toml
[params]
  banner_behavior = "stack"
  
  [params.notification]
    enabled = true
    message = "🚀 New feature launched! [Check it out](/features)"
    type = "success"
    auto_hide = false
    show_close_button = true
```

### Page-specific Banner (front matter)
Add to any page's front matter:

```toml
+++
title = "My Page"

[notification]
enabled = true
message = "⚠️ This page is under construction"
type = "warning"
auto_hide = true
auto_hide_delay = 3000
show_close_button = false
+++
```

### Both Banners with Override Behavior
```toml
# In hugo.toml
[params]
  banner_behavior = "override"  # Page banner will hide site banner
  
  [params.notification]
    enabled = true
    message = "Site-wide announcement"
    type = "info"
```

## 4. Banner Types
- `info` - Blue theme (default)
- `success` - Green theme
- `warning` - Yellow/orange theme
- `error` - Red theme

## 5. Configuration Options

### Site-wide (hugo.toml)
- `enabled`: Show/hide the banner
- `message`: Banner content (supports markdown)
- `type`: Banner color theme
- `auto_hide`: Auto-hide after delay?
- `auto_hide_delay`: Milliseconds to wait
- `show_close_button`: Show X button?

### Banner Behavior
- `stack`: Show both site and page banners
- `override`: Page banner hides site banner

## 6. JavaScript Functions

### Available Functions
- `closeBanner('banner-id')` - Manually close a banner
- `showBanner('banner-id')` - Re-show a dismissed banner

### Usage in Browser Console
```javascript
// Hide the site banner
closeBanner('site-banner');

// Show it again
showBanner('site-banner');
```

## 7. Customization Tips

### Custom Colors
Modify the CSS variables in the `:root` selector to change colors.

### Animation Duration
Change the `transition` property in `.notification-banner` class.

### Position
The banner uses `position: sticky` by default. Change to `fixed` for always-visible banners.

## 8. Troubleshooting

### Banner not showing?
1. Check if `enabled = true` in hugo.toml or front matter
2. Verify the partial is included in your layout
3. Check browser console for JavaScript errors

### Styling issues?
1. Ensure CSS is loaded in `custom_head.html`
2. Check if your theme has conflicting styles
3. Use browser dev tools to inspect elements

### Dark mode not working?
1. Check if your theme uses `prefers-color-scheme` or a `.dark` class
2. Adjust the CSS accordingly in the dark theme section