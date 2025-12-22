# 🧩 Layers of Trust — CTF Writeup

**Category:** Forensics / Crypto  

---

<img width="651" height="619" alt="image" src="https://github.com/user-attachments/assets/2171bf59-6f5c-4430-b78e-1d4c777d7179" />

---

## 🔍 Initial Analysis

The challenge explicitly mentions:

- **Raw email dump**
- **Structure**
- **Attachments**
- **Encrypted content**
- Multiple **layers**

This indicates the challenge is **not solved by reading the email body alone**.  
Instead, the solver must inspect the **email container itself**.

The correct first step is to analyze the `.eml` file as a MIME object.

---

## 🧪 Step 1: Inspect Email Structure

`file mysterious_mail.eml`

Expected output confirms it is an RFC 822 email.

On inspecting the file you can conclude there is a

