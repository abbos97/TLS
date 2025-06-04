## 🛡 TLS orqali xavfsiz foydalanuvchi autentifikatsiyasi va xabar yuborish

Bu loyiha orqali foydalanuvchilar TLS asosida serverga ulanishadi, login-parol bilan tizimga kirishadi va AES orqali shifrlangan xabar yuborishadi. Server foydalanuvchini tekshiradi va xabarni ochib ko‘rsatadi.

---

## 📄 add_user.py
- Yangi foydalanuvchi qo‘shish uchun ishlatiladi.
- Ishga tushurish:
  ```bash
  python add_user.py
  ```
- Console’da `username` va `password` so‘raladi.
- Parol `bcrypt` orqali hash qilinib, `server/users.json` faylga yoziladi.

---

## 📄 hashing.py
- `bcrypt` bilan parolni:
  - hash qilish
  - tekshirish
uchun foydalaniladi.

---

## 📄 encryption.py
- Xabarni AES orqali:
  - shifrlash (`encrypt_message`)
  - deshifrlash (`decrypt_message`) funksiyalarini o‘z ichiga oladi.

---

## 📄 server.py
- TLS serverni ishga tushuradi.
- Ishga tushurish:
  ```bash
  python server/server.py
  ```
- Server foydalanuvchidan `username`, `password`, va AES shifrlangan xabarni qabul qiladi.
- Agar foydalanuvchi `users.json` faylda bo‘lsa, xabarni deshifrlaydi va ko‘rsatadi.

---

## 📄 client.py
- Foydalanuvchi interfeysi.
- Ishga tushurish:
  ```bash
  python client/client.py
  ```
- Console’da quyidagilar kiritiladi:
  1. Username
  2. Password
  3. Yuboriladigan xabar
- Agar foydalanuvchi `users.json` faylda bo‘lsa:
  - Serverga xabar yuboriladi
  - Server AES orqali xabarni ochadi va ko‘rsatadi