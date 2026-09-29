import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Names
content = content.replace('John Doe', 'Дмитрий Бордос')
content = content.replace('Ram Maheshwari Logo Image', 'Дмитрий Бордос')

# Replace Hero section
content = re.sub(
    r'<h1 class="heading-primary">.*?</h1>',
    '<h1 class="heading-primary">Привет, я Дмитрий Бордос</h1>',
    content,
    flags=re.DOTALL
)

content = re.sub(
    r'<p class="text-primary">.*?</p>',
    '<p class="text-primary">Фуллстек и мобильный разработчик. Создаю производительные приложения, от социальных сервисов до сложных систем управления (WMS) и игр.</p>',
    content,
    flags=re.DOTALL
)

# About Me
about_html = """<h3 class="about__content-title">Кратко обо мне!</h3>
            <div class="about__content-details">
              <p class="about__content-details-para">
                Привет! Я Дмитрий, Full-Stack и Mobile разработчик. За время своей практики я успел поработать над самыми разными проектами: от кроссплатформенных мобильных приложений и интерактивных карт до сложных складских систем учета (WMS) и даже игровых механик на Unity.
              </p>
              <p class="about__content-details-para">
                Люблю решать нетривиальные задачи, писать чистый и поддерживаемый код, а также пробовать новые технологии. В основном пишу на <strong>TypeScript</strong> для веба и <strong>Dart (Flutter)</strong> для мобилок, но всегда готов залезть в бэкенд на Python или C++.
              </p>
              <p class="about__content-details-para">
                Открыт для интересных предложений и классных проектов. Связаться со мной можно в Telegram: <a href="https://t.me/morphy_prod" target="_blank"><strong>@morphy_prod</strong></a>.
              </p>
            </div>
            <a href="./#contact" class="btn btn--med btn--theme dynamicBgClr"
              >Связаться</a
            >"""

content = re.sub(
    r'<h3 class="about__content-title">Get to know me!</h3>.*?<a href="\./#contact" class="btn btn--med btn--theme dynamicBgClr"\s*>Contact</a\s*>',
    about_html,
    content,
    flags=re.DOTALL
)

# About Header Subtitle
content = re.sub(
    r'<span class="heading-sec__sub">\s*Lorem ipsum dolor sit amet consectetur adipisicing elit\. Hic facilis\s*tempora explicabo quae quod deserunt eius sapiente\s*</span>',
    '<span class="heading-sec__sub">\n            Здесь вы найдете информацию обо мне, моих навыках и текущем стеке технологий, с которым я работаю.\n          </span>',
    content,
    flags=re.DOTALL
)


# Skills
skills = [
    "TypeScript", "JavaScript", "Dart", "Flutter",
    "HTML", "CSS", "Kotlin", "Swift",
    "C#", "Unity", "Python", "PostgreSQL", "C++"
]
skills_html = '<div class="skills">\n'
for skill in skills:
    skills_html += f'              <div class="skills__skill">{skill}</div>\n'
skills_html += '            </div>'

content = re.sub(
    r'<div class="skills">.*?</div>\s*</div>',
    skills_html + '\n          </div>',
    content,
    flags=re.DOTALL
)


# Projects Section Subtitle
content = re.sub(
    r'<h2 class="heading heading-sec heading-sec__mb-bg">\s*<span class="heading-sec__main">Projects</span>\s*<span class="heading-sec__sub">.*?</span>\s*</h2>',
    '<h2 class="heading heading-sec heading-sec__mb-bg">\n          <span class="heading-sec__main">Проекты</span>\n          <span class="heading-sec__sub">\n            Некоторые из моих личных проектов и решений. Больше кода можно найти в моем GitHub.\n          </span>\n        </h2>',
    content,
    flags=re.DOTALL
)


# Projects
projects_html = """
        <div class="projects__content">
          <!-- Project 1 -->
          <div class="projects__row">
            <div class="projects__row-content">
              <h3 class="projects__row-content-title">NearU — Карта друзей</h3>
              <p class="projects__row-content-desc">
                Кроссплатформенное мобильное приложение (социальная сеть с картой, наподобие Zenly). 
                Написано на Dart/Flutter с использованием нативных Kotlin и Swift модулей, а также C++ под капотом.
              </p>
              <a
                href="https://github.com/morphy000/nearu"
                class="btn btn--med btn--theme dynamicBgClr"
                target="_blank"
                >GitHub</a
              >
            </div>
          </div>
          <!-- Project 2 -->
          <div class="projects__row">
            <div class="projects__row-content">
              <h3 class="projects__row-content-title">IT-TED OMS & JUZZA</h3>
              <p class="projects__row-content-desc">
                Комплексная система управления фулфилментом (WMS). 
                Крупный enterprise-проект на TypeScript, предназначенный для учета и логистики товаров в e-commerce.
              </p>
              <a
                href="https://github.com/morphy000/it-ted-oms"
                class="btn btn--med btn--theme dynamicBgClr"
                target="_blank"
                >GitHub</a
              >
            </div>
          </div>
          <!-- Project 3 -->
          <div class="projects__row">
            <div class="projects__row-content">
              <h3 class="projects__row-content-title">GameDev & Shaders</h3>
              <p class="projects__row-content-desc">
                Мои эксперименты в геймдеве и графике. Множество проектов на движке Unity (C#) и ShaderLab,
                включая дрифт-игры и различные шейдеры.
              </p>
              <a
                href="https://github.com/morphy000/yandexgame"
                class="btn btn--med btn--theme dynamicBgClr"
                target="_blank"
                >GitHub</a
              >
            </div>
          </div>
        </div>
"""

content = re.sub(
    r'<div class="projects__content">.*?</div>\s*</div>\s*</section>',
    projects_html + '\n      </div>\n    </section>',
    content,
    flags=re.DOTALL
)

# Contact Section
content = re.sub(
    r'<h2 class="heading heading-sec heading-sec__mb-med">\s*<span class="heading-sec__main heading-sec__main--lt">Contact</span>\s*<span class="heading-sec__sub heading-sec__sub--lt">.*?</span>\s*</h2>',
    '<h2 class="heading heading-sec heading-sec__mb-med">\n          <span class="heading-sec__main heading-sec__main--lt">Контакты</span>\n          <span class="heading-sec__sub heading-sec__sub--lt">\n            Свяжитесь со мной, если у вас есть предложения по работе или просто хотите пообщаться.\n          </span>\n        </h2>',
    content,
    flags=re.DOTALL
)

# Footer
content = re.sub(
    r'<p class="main-footer__short-desc">.*?</p>',
    '<p class="main-footer__short-desc">\n              Full-Stack и Mobile разработчик. Пишу код, который работает.\n            </p>',
    content,
    flags=re.DOTALL
)

# Update Github Links
content = content.replace('href="#"', 'href="https://github.com/morphy000"')
content = content.replace('href="./index.html#projects"', 'href="./index.html#projects"')
# Replace Home, About, Projects, Contact links text
content = content.replace('Home', 'Главная')
content = content.replace('About', 'Обо мне')
content = content.replace('Projects', 'Проекты')
content = content.replace('Contact', 'Контакты')
content = content.replace('PROJECTS', 'ПРОЕКТЫ')

# Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

