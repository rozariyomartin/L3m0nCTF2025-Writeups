# Challenge Writeup : Hotel Bagavathi

## Problem

Target: larry lmn
The target is sloppy. They posted a link to their new project on one of their social media accounts. Locate the account, find the project source code, and recover the hidden location metadata. And not only that there is more to find out

We need two things:

The BSSID of the WiFi network.

The Total Bill amount found in the evidence.

Flag Format: L3m0nCTF{BSSID_TOTALBILL}

**Authors** : R0z4riy0 & akvnn

---

### Step1 : Find the social media account

First find out all the social media apps which are popular and try to find the user account.

We can find it on **VK**, it's a popular russian social media platform.

<img width="556" height="404" alt="image" src="https://github.com/user-attachments/assets/9eac20c5-3181-4863-b098-06f556852a09" />

He had uploaded a post where the github link is present open it and it will redirect you to the github page.

<img width="1798" height="700" alt="image" src="https://github.com/user-attachments/assets/e364b962-5333-4fa8-ab8a-19c3e3bf494f" />

### Step2 : Searching for any clues in github repositories

Clone the repository and search for any keywords present in it

<img width="1018" height="424" alt="image" src="https://github.com/user-attachments/assets/97b05619-22aa-48ab-af00-dcdf3ed7da72" />

Then after it you can see that there is a base 64 encoded one

`aHR0cHM6Ly9vcGVuLnNwb3RpZnkuY29tL3V2ZXIVMzF4NnB1M3hoY2YyNm1sMzRtdWNqZDdzcWgodT9zaT12ZGZnQWVfbVIxbUp4SkZSdXVEWDh3`

On decoding that in CyberChef i got a spotify link

<img width="1521" height="559" alt="image" src="https://github.com/user-attachments/assets/89816884-6e65-4d77-b9f5-aab4dd366b86" />

### Step3 : Finding clues in Spotify

If you search through the profile you can  find a playlist with a few songs

<img width="1427" height="757" alt="image" src="https://github.com/user-attachments/assets/0b5ec5fb-bb8c-4761-9d43-a7bcc9892df3" />

In this playlist if you just take the first letter from every songs you can find a hidden clue which is `INSTAARIVUDAS`

From the name you can be somewhat clear that the profile may exist in Instagram searching it we can find a profile in it

