# KepfutsiyBot

**KepfutsiyBot** — bu Django asosida qurilgan bot bo'lib, foydalanuvchilarga har kuni ma'noli va motivatsion xabarlarni yuborib turadi. Ushbu loyiha o'z foydalanuvchilarining kunini yaxshilash va ularni ilhomlantirish uchun mo'ljallangan.

Ishlatishdan oldin proyekt papkasida quyidagi o'zgaruvchilar bilan `.env` faylini yarating:

#### Django
- `SECRET_KEY`

#### Database Postgers
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `DB_HOST`
- `DB_PORT`

#### Telegram bot Tokeni
- `TOKEN`

## Loyihani ishlatish

`python manage.py runserver` - djangoni ishga tushirish 

`python manage.py qcluster` - django-Q ni ishga tushirish

`python bot.py` - aigoramni botni ishga tushirish