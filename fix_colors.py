import re

with open("d:/Fruites Juice/ingredients.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace emerald with rose (to match crimson accent)
content = content.replace("emerald-700", "rose-700")
content = content.replace("emerald-800", "rose-800")
content = content.replace("emerald-600", "rose-600")
content = content.replace("emerald-100", "rose-100")
content = content.replace("emerald-50", "rose-50")

# Keep amber as secondary color (which matches the orange --accent-secondary)

with open("d:/Fruites Juice/ingredients.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed colors in ingredients.html")
