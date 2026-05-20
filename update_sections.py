import re

# 1. Update index.html to make the main content about all juices, and keep a specific Beetroot section
with open("d:/Fruites Juice/index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

index_content = index_content.replace(
    "<h3>Rooted in Nature, Bursting with Life</h3>\n            <p>Beetroot has been treasured for centuries — from ancient Roman tables to modern wellness rituals. Our signature juices are crafted from heirloom beets, cold-pressed within hours of harvest.</p>",
    "<h3>Rooted in Nature, Bursting with Life</h3>\n            <p>Our organic juice cleanses are crafted from a vibrant spectrum of heirloom fruits and vegetables. From alkalizing leafy greens to revitalizing citrus, we cold-press our produce within hours of harvest to lock in maximum nutrition.</p>"
)

index_content = index_content.replace(
    "<h2 class=\"section-title\">Why Choose Our Cleanses?</h2>\n        <p class=\"section-sub\">Packed with nature’s most vibrant nutrients — science-backed benefits in every glass</p>",
    "<div class=\"section-tag\" style=\"text-align: center; display: block; margin: 0 auto 1rem;\">Featured Collection</div>\n        <h2 class=\"section-title\">The Beetroot Detox Focus</h2>\n        <p class=\"section-sub\">Our signature beetroot elixirs are packed with nature’s most vibrant nutrients — science-backed benefits for deep cleansing and endurance in every glass.</p>"
)

with open("d:/Fruites Juice/index.html", "w", encoding="utf-8") as f:
    f.write(index_content)


# 2. Update ingredients.html to add actual ingredients, benefits, sourcing, and nutrition, and "Who Is This For?"
with open("d:/Fruites Juice/ingredients.html", "r", encoding="utf-8") as f:
    ing_content = f.read()

# Replace session 3 to the end with the new content
new_sections = """
  <!-- SESSION 3: KEY INGREDIENTS & BENEFITS -->
  <section id="session3" class="session" style="background: linear-gradient(145deg, #FEF3E4 0%, #E9F0E3 100%);">
    <div class="content-container">
      <div class="text-center mb-12 fade-up">
        <span class="text-emerald-700 text-sm font-medium tracking-wider bg-emerald-100/70 px-4 py-1 rounded-full">NATURE'S PHARMACY</span>
        <h2 class="playfair text-4xl md:text-5xl font-medium mt-3 text-gray-800">Our Core Ingredients<br>& Their Benefits</h2>
        <p class="text-gray-600 max-w-2xl mx-auto mt-4">We select only the most nutrient-dense superfoods to craft our functional blends.</p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mt-8">
        <div class="process-step rounded-2xl p-6 text-center shadow-lg">
          <div class="w-16 h-16 bg-red-100 rounded-full flex items-center justify-center mx-auto mb-4"><i class="fas fa-heart text-2xl text-red-700"></i></div>
          <h3 class="font-medium text-xl mb-2">Organic Beetroot</h3>
          <p class="text-gray-600">Rich in nitrates and betalains. Supports healthy blood flow, liver detoxification, and natural stamina.</p>
        </div>
        <div class="process-step rounded-2xl p-6 text-center shadow-lg">
          <div class="w-16 h-16 bg-emerald-100 rounded-full flex items-center justify-center mx-auto mb-4"><i class="fas fa-leaf text-2xl text-emerald-700"></i></div>
          <h3 class="font-medium text-xl mb-2">Leafy Greens</h3>
          <p class="text-gray-600">Kale and spinach packed with chlorophyll. Highly alkalizing, oxygenating, and rich in essential minerals.</p>
        </div>
        <div class="process-step rounded-2xl p-6 text-center shadow-lg">
          <div class="w-16 h-16 bg-yellow-100 rounded-full flex items-center justify-center mx-auto mb-4"><i class="fas fa-sun text-2xl text-yellow-700"></i></div>
          <h3 class="font-medium text-xl mb-2">Turmeric & Ginger</h3>
          <p class="text-gray-600">Nature's most potent anti-inflammatories. Enhances digestion, soothes the gut, and boosts immunity.</p>
        </div>
        <div class="process-step rounded-2xl p-6 text-center shadow-lg">
          <div class="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-4"><i class="fas fa-lemon text-2xl text-orange-700"></i></div>
          <h3 class="font-medium text-xl mb-2">Citrus & Berries</h3>
          <p class="text-gray-600">Abundant in Vitamin C and antioxidants. Promotes skin radiance and protects cells from oxidative stress.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- SESSION 4: SOURCING & NUTRITION -->
  <section id="session4" class="session" style="background: linear-gradient(125deg, #264e2e 0%, #2B5B2F 100%), url('./image/in1.jpg'); background-blend-mode: overlay; background-size: cover; background-position: center;">
    <div class="content-container text-white text-center">
      <div class="max-w-4xl mx-auto fade-up bg-black/30 backdrop-blur-md p-8 md:p-12 rounded-[2rem] border border-white/10">
        <i class="fas fa-seedling text-amber-300 text-4xl mb-4"></i>
        <h2 class="playfair text-4xl md:text-5xl font-medium mb-5">Our Sourcing & Nutrition Promise</h2>
        <p class="text-white/95 text-lg mb-6">We believe that true health begins in the soil. All our ingredients are 100% USDA Certified Organic, sourced directly from regenerative farms that prioritize biodiversity and soil health.</p>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 text-left mt-8">
            <div>
                <h3 class="text-2xl text-amber-300 mb-3 font-medium"><i class="fas fa-globe-americas mr-2"></i> Ethical Sourcing</h3>
                <p class="text-white/80">We partner exclusively with fair-trade cooperatives and local organic farmers. Every bottle supports agricultural practices that restore the earth rather than deplete it.</p>
            </div>
            <div>
                <h3 class="text-2xl text-amber-300 mb-3 font-medium"><i class="fas fa-flask mr-2"></i> Uncompromised Nutrition</h3>
                <p class="text-white/80">Our zero-heat hydraulic cold-press process extracts liquid gold that retains 99% of its vitamins, minerals, and live enzymes. No pasteurization. No HPP. Just raw, living juice.</p>
            </div>
        </div>
      </div>
    </div>
  </section>

  <!-- SESSION 5: WHO IS THIS FOR? -->
  <section id="session5" class="session bg-gradient-to-br from-white to-amber-50/40">
    <div class="content-container">
      <div class="text-center max-w-3xl mx-auto mb-16 fade-up">
        <span class="text-emerald-700 font-medium bg-emerald-100 px-5 py-1.5 rounded-full text-sm"><i class="fas fa-bullseye mr-1"></i> Target Your Wellness Goals</span>
        <h2 class="playfair text-4xl md:text-5xl font-medium text-gray-800 mt-4">Who Is This For?</h2>
        <p class="text-gray-600 text-lg mt-3">Find the perfect cleanse tailored to your unique body and lifestyle objectives.</p>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <!-- Goal: Detox -->
        <div class="stat-card p-8 text-center transition-all duration-500 hover:scale-105 border-t-4 border-green-500">
          <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-5"><i class="fas fa-leaf text-2xl text-green-700"></i></div>
          <h3 class="text-xl font-medium text-gray-800 mb-3">The Detox Seeker</h3>
          <p class="text-gray-600 text-sm mb-4">Perfect if you've been overindulging, feeling sluggish, or experiencing brain fog. Our deep greens and beetroot blends support liver function and cellular reset.</p>
          <a href="./packages.html" class="text-green-600 font-medium text-sm hover:underline">Explore Detox Plans &rarr;</a>
        </div>
        
        <!-- Goal: Energy -->
        <div class="stat-card p-8 text-center transition-all duration-500 hover:scale-105 border-t-4 border-amber-500">
          <div class="w-16 h-16 bg-amber-100 rounded-full flex items-center justify-center mx-auto mb-5"><i class="fas fa-bolt text-2xl text-amber-700"></i></div>
          <h3 class="text-xl font-medium text-gray-800 mb-3">The Energy Chaser</h3>
          <p class="text-gray-600 text-sm mb-4">Ideal for athletes, busy professionals, or those relying on caffeine. Our nitrate-rich juices improve oxygen flow and provide sustained, jitter-free vitality.</p>
          <a href="./packages.html" class="text-amber-600 font-medium text-sm hover:underline">Explore Energy Plans &rarr;</a>
        </div>

        <!-- Goal: Immunity -->
        <div class="stat-card p-8 text-center transition-all duration-500 hover:scale-105 border-t-4 border-orange-500">
          <div class="w-16 h-16 bg-orange-100 rounded-full flex items-center justify-center mx-auto mb-5"><i class="fas fa-shield-alt text-2xl text-orange-700"></i></div>
          <h3 class="text-xl font-medium text-gray-800 mb-3">The Immunity Builder</h3>
          <p class="text-gray-600 text-sm mb-4">For those feeling run down or facing seasonal shifts. Packed with Vitamin C, zinc, and potent anti-inflammatories like turmeric to fortify your defenses.</p>
          <a href="./packages.html" class="text-orange-600 font-medium text-sm hover:underline">Explore Immunity Plans &rarr;</a>
        </div>

        <!-- Goal: Weight Balance -->
        <div class="stat-card p-8 text-center transition-all duration-500 hover:scale-105 border-t-4 border-blue-500">
          <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-5"><i class="fas fa-weight text-2xl text-blue-700"></i></div>
          <h3 class="text-xl font-medium text-gray-800 mb-3">The Weight Balancer</h3>
          <p class="text-gray-600 text-sm mb-4">Designed to break sugar cravings, reduce water retention, and reset your palate. A low-glycemic approach to discovering your body's natural equilibrium.</p>
          <a href="./packages.html" class="text-blue-600 font-medium text-sm hover:underline">Explore Balance Plans &rarr;</a>
        </div>
      </div>
    </div>
  </section>
"""

# Find where session 3 begins and replace everything from there up to the footer
start_idx = ing_content.find('<!-- SESSION 3: Farm-to-Bottle Process -->')
end_idx = ing_content.find('<!-- ==================== ALL SCRIPTS')

if start_idx != -1 and end_idx != -1:
    ing_content = ing_content[:start_idx] + new_sections + ing_content[end_idx:]
    with open("d:/Fruites Juice/ingredients.html", "w", encoding="utf-8") as f:
        f.write(ing_content)
        
print("Updated index and ingredients!")
