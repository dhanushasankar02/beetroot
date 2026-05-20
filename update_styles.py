import os
import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update H2 and H3 font sizes
    # We look for h2 { ... } and h3 { ... }
    
    # Simple regex to find the h2 and h3 rules and replace font-size
    # Wait, it's safer to just replace font-size specifically inside h2 and h3 blocks.
    # Actually, we can just replace 'font-size: 3.5rem;' with 'font-size: 48px;' inside h2 { ... } 
    # But since they can vary, let's use a regex that matches `h2 { ... }` and replaces font-size inside it.
    # A simpler way:
    content = re.sub(r'(h2\s*\{[^}]*?font-size:\s*)[^;]+(;)', r'\g<1>48px\g<2>', content, flags=re.IGNORECASE)
    content = re.sub(r'(h3\s*\{[^}]*?font-size:\s*)[^;]+(;)', r'\g<1>24px\g<2>', content, flags=re.IGNORECASE)
    
    # We might also want to catch things like `.cta-inner h2 { font-size: 4rem; ... }` if they are meant to be 48px.
    # The prompt says "Maintain all H2 headings size 48px and H3 headings 24 px in above footer section, process section ,liquid gold section and also the source section ,store page and home1 and 2"
    # This implies ALL h2 and h3 in those files.
    # Let's replace any `h2 { font-size: ... }` and `.some-class h2 { font-size: ... }`
    content = re.sub(r'(h2\s*\{[^\}]*?font-size:\s*)[^;]+(;)', r'\g<1>48px\g<2>', content)
    content = re.sub(r'(h3\s*\{[^\}]*?font-size:\s*)[^;]+(;)', r'\g<1>24px\g<2>', content)
    
    # Also replace instances like `h2, .h2 { font-size: ... }`?
    # Let's just find all `font-size: .*?` inside any block that targets `h2` or `h3`.
    # A more brutal approach: replace all base `h2 { font-size: X; }` and `h3 { font-size: Y; }`
    
    # Update .login-btn to be primary
    login_btn_css = """    .login-btn {
      background: linear-gradient(105deg, var(--accent), #9E2C46) !important;
      color: white !important;
      border: none !important;
      box-shadow: 0 4px 10px rgba(188, 47, 76, 0.3);
    }
    .login-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 15px rgba(188, 47, 76, 0.4);
    }"""
    
    # Replace existing .login-btn block
    content = re.sub(r'\.login-btn\s*\{[^\}]*\}', login_btn_css, content)
    
    # Update Hero Image in index.html
    if 'index.html' in filepath:
        old_img = r'<img src="\./image/Fresh beetroot and juice\.jpg" alt="Fresh beetroot and juice"[^>]*>'
        new_img = r'<img src="./image/organic_juice_hero.png" alt="Fresh organic juice" fetchpriority="high" decoding="async" style="max-height: 450px; width: 100%; object-fit: contain; border-radius: 20px;">'
        content = re.sub(old_img, new_img, content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

files_to_update = ['index.html', 'home2.html', 'store.html']
for f in files_to_update:
    if os.path.exists(f):
        update_file(f)
        print(f"Updated {f}")

# The prompt also says "Nav bar- make login CTA as primary button" -> implies all pages with navbar
# Let's apply the login-btn CSS to all HTML files in the folder
for f in os.listdir('.'):
    if f.endswith('.html') and f not in files_to_update:
        update_file(f)
        print(f"Updated {f} for navbar")
