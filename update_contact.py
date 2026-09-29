import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Contact Form Labels
content = content.replace('<label class="contact__form-label" for="name">Name</label>', '<label class="contact__form-label" for="name">Имя</label>')
content = content.replace('placeholder="Enter Your Name"', 'placeholder="Введите ваше имя"')

content = content.replace('<label class="contact__form-label" for="email">Email</label>', '<label class="contact__form-label" for="email">Email или Telegram</label>')
content = content.replace('placeholder="Enter Your Email"', 'placeholder="Куда вам ответить?"')

content = content.replace('<label class="contact__form-label" for="message">Message</label>', '<label class="contact__form-label" for="message">Сообщение</label>')
content = content.replace('placeholder="Enter Your Message"', 'placeholder="Текст сообщения..."')

content = content.replace('<button type="submit" class="btn btn--theme contact__btn">\n              Submit\n            </button>', '<button type="submit" class="btn btn--theme contact__btn">\n              Отправить\n            </button>')

# Social Section text 
content = content.replace('<span>Social</span>', '<span>Соц. сети</span>')

# Save
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
