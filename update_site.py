import os
import re
import glob

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Branding: "Beetroot Detox" -> "Pure Cleanse"
    content = content.replace("Beetroot Detox", "Pure Cleanse")
    content = content.replace("Beetroot Vitality", "Organic Vitality")
    content = content.replace("Earth’s Crimson Energy", "Organic Juice Delivery")
    content = content.replace("Earth's Crimson Energy", "Organic Juice Delivery")
    content = content.replace("Why Beetroot?", "Why Choose Our Cleanses?")

    # 2. Font weights
    # Replace font-weight: 600, 700, 800, 900 with 500
    content = re.sub(r'font-weight:\s*[6-9]00\s*;?', 'font-weight: 500;', content)
    # Replace bold with 500
    content = re.sub(r'font-weight:\s*bold\s*;?', 'font-weight: 500;', content)
    # Replace 300 with 400
    content = re.sub(r'font-weight:\s*300\s*;?', 'font-weight: 400;', content)
    # Replace font-weight in class attributes (Tailwind like font-bold -> font-medium)
    content = content.replace("font-bold", "font-medium")
    content = content.replace("font-semibold", "font-medium")
    content = content.replace("font-extrabold", "font-medium")
    content = content.replace("font-black", "font-medium")

    # 3. Packages Pricing
    if "packages.html" in filepath.lower():
        content = content.replace("Starting at <strong>$39</strong>", "<strong>$39</strong>")
        content = content.replace("Only <strong>$69</strong>", "<strong>$69</strong>")
        content = content.replace("Complete Program <strong>$99</strong>", "<strong>$99</strong>")
        content = content.replace("Intensive Care <strong>$149</strong>", "<strong>$149</strong>")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for html_file in glob.glob("d:/Fruites Juice/*.html"):
    process_file(html_file)

print("Updated site!")
