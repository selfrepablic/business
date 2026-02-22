import os

file_path = "c:/Users/User/Desktop/my-sideprojects/31.selfrepablic/index.html"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Swiper CSS at the end of head
head_style = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
<style>
    /* Swiper Adjustments */
    html, body {
        position: relative;
        height: 100%;
        overflow: hidden;
    }
    .swiper {
        width: 100%;
        height: 100%;
        background-color: #050505;
    }
    .swiper-slide {
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #050505;
        overflow: hidden;
    }
    .swiper-pagination-bullet {
        background: #fff;
        opacity: 0.3;
        width: 8px;
        height: 8px;
    }
    .swiper-pagination-bullet-active {
        background: var(--accent-gold);
        opacity: 1;
    }
</style>
</head>"""
content = content.replace('</head>', head_style)

# 2. Body Reset
old_body = """    body {
        margin: 0;
        background-color: #111;
        font-family: 'Noto Sans JP', sans-serif;
        color: var(--text-white);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 40px;
        padding: 40px 0;
    }"""
new_body = """    body {
        margin: 0;
        padding: 0;
        background-color: #050505;
        font-family: 'Noto Sans JP', sans-serif;
        color: var(--text-white);
    }"""
content = content.replace(old_body, new_body)

# 3. Page CSS Reset
old_page = """    .page {
        width: 1080px;
        height: 1920px;
        background-color: var(--bg-color);
        position: relative;
        box-shadow: 0 0 30px rgba(0,0,0,0.8);
        overflow: hidden;
        page-break-after: always;
        flex-shrink: 0;
    }"""
new_page = """    .page {
        width: 1080px;
        height: 1920px;
        background-color: var(--bg-color);
        position: relative;
        overflow: hidden;
        flex-shrink: 0;
        transform-origin: center center;
    }"""
content = content.replace(old_page, new_page)

# 4. Create Swiper Structure
content = content.replace('<body>\n', '<body>\n<!-- Swiper Container -->\n<div class="swiper mySwiper">\n    <div class="swiper-wrapper">\n')

content = content.replace('<div class="page ', '<div class="swiper-slide">\n<div class="page ')
content = content.replace('</div>\n\n<!-- P', '</div>\n</div>\n\n<!-- P')
content = content.replace('</div>\n\n</body>', '</div>\n</div>\n\n    </div>\n    <div class="swiper-pagination"></div>\n</div>\n\n<!-- Swiper JS -->\n<script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>\n<script>\n    function resizePages() {\n        const pages = document.querySelectorAll(".page");\n        const scale = Math.min(window.innerWidth / 1080, window.innerHeight / 1920);\n        pages.forEach(page => {\n            page.style.transform = `scale(${scale})`;\n        });\n    }\n    window.addEventListener("resize", resizePages);\n    resizePages();\n\n    var swiper = new Swiper(".mySwiper", {\n        pagination: {\n            el: ".swiper-pagination",\n            dynamicBullets: true,\n        },\n        grabCursor: true,\n        keyboard: {\n            enabled: true,\n        },\n    });\n</script>\n\n</body>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Update completed!")
