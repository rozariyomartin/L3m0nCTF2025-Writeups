# Challenge Writeup : Hotel Bagavathi

## Problem

Target: larry lmn
The target is sloppy. They posted a link to their new project on one of their social media accounts. Locate the account, find the project source code, and recover the hidden location metadata. And not only that there is more to find out

We need two things:

The BSSID of the WiFi network.

The Total Bill amount found in the evidence.

Flag Format: L3m0nCTF{BSSID_TOTALBILL}

**Authors** : R0z4riy0 & [akvnn](https://github.com/Akashvarunn14)

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

On searching it we can conclude that this account exists in Instagram

<img width="1255" height="697" alt="image" src="https://github.com/user-attachments/assets/ac704929-5522-45f6-af5c-e42b8ff4f5d7" />

So there are three reels here if see them one by one on a specific reel (the recent reel) it conains two screenshots each of 0.01 seconds you need to see throygh it to proceed to the next clue. 

I have added those screenshots below,

<img width="770" height="1600" alt="image" src="https://github.com/user-attachments/assets/d61759fe-c23a-426e-8db3-250bd841ea1f" />

<img width="1007" height="1599" alt="image" src="https://github.com/user-attachments/assets/e8e6bab8-672e-4269-96c6-2b79acce7b33" />

So here we can see a conversation of user (instaantonydas) and instaarivudas here he mentioned that, due to the poor signal of **wifi** and also the **coffee** too he has reviewed one star rating to the shop.

First we need to find where the shop is right.

If you see the profile picture its a photo in the movie scene of **LEO** where he is in the cafe, if you watched the movie you could have easily guessed it's **Sifar Cafe**.

If you didnt watch the movie though you can search it in google lens and you can find the scen and check where the movie was shot.

### Step4 : Finding the Review

He mentioned in the image that he had reviewed one star for his shop. So now we need to search through the cafe review websites.

One of the well known review websites is the **Tripadvisor**.

[link]([link](https://www.tripadvisor.in/Restaurant_Review-g1891000-d24101216-Reviews-Sifar-Anantnag_Anantnag_District_Kashmir_Jammu_and_Kashmir.html))

So in it if you search for the cafe and when you check the reviews you can find this specific review which is kinda sus,

<img width="817" height="476" alt="image" src="https://github.com/user-attachments/assets/2eb983b8-65fb-4df1-b72c-d26913bd9345" />

Here you can see that the BSSID of the wifi is given here which is a part of the flag.

### Step5 : Finding other clues

Also, we can see that the profile is also kinda sus why is specifically given in alphanumericals which gives no meaning so on seaching it we can find that it is a **pastebin url**

```
https://pastebin.com/88fFyTM1
```

<img width="1686" height="525" alt="image" src="https://github.com/user-attachments/assets/c6faf04f-8e5c-4585-89d3-6584ecbb52fa" />

We can see another url in this pastebin link itself. 

So redirecting to this URL we can find hat it is a website full of Racing Blogs from Vetrivel

As our scenario is set in Jammu and Kashmir, lets look for srinagar if any events occured there so if we see it we can find a blog of **Srinagar F4 Street Demo**

<img width="758" height="1080" alt="image" src="https://github.com/user-attachments/assets/65949932-8deb-4d14-87b2-7324f6d86f66" />

In it if you read they mentioned about the amount he paid that day which was 494.72.

Constructing the details we can get the flag.

### Flag
`L3m0nCTF{00:1A:2B:3E:4D:5A_494.72}`
