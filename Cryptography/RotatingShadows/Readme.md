# Rotating Shadows — Write-up

<img width="436" height="739" alt="image" src="https://github.com/user-attachments/assets/6433c1aa-51d7-474e-9988-889a990bb292" />

## Step 1: Identify What Is and Is Not Ciphertext

The challenge text includes a sentence that stands out:

> “Not Less Visible, but always rotating, gears under.”

This sentence is not part of the ciphertext file and does not resemble encrypted data.
Given the hints and wording (“etched”, “handwritten”), it is likely intentional and meaningful.

## Step 2: Examine the Structure of the Sentence

Instead of interpreting the sentence semantically, we examine its structure.

Taking the initial letters of each word:

```
Not        → N  
Less       → L  
Visible,   → V  
but        → b  
always     → a  
rotating,  → r  
gears      → g  
under.     → u  
```

This yields:

`NLVbargu`

The mixed casing suggests it should be used as-is, not decoded further.

## Step 3: Interpreting the Extracted String

The extracted string `NLVbargu` does not resemble ciphertext, a key, or encoded data.

In CTFs, such identifiers are often used as **external references***.
Trying it as a path on common public paste services leads to:

```
https://pastebin.com/NLVbargu
```

This Pastebin contains the **missing description of the cipher mechanism**, including:

- Two alphabet wheels
- Their initial configurations
- How they change after each character

## Step 4: Understanding the Cipher Mechanism

From the Pastebin notes, the cipher operates mechanically as follows:

<img width="1508" height="867" alt="image" src="https://github.com/user-attachments/assets/af25a04c-cf9a-4dcb-b0ac-43bda85ed741" />

## Step 5: Decrypting the Ciphertext

Using the algorithm from the Pastebin and the ciphertext provided in the text file:

```
PFRLGJEUCZIVFCNGXOMTRKYH
```

We simulate the wheel behavior in reverse:

- For each ciphertext character:
  - Find its index in Wheel B
  - Take the character at the same index in Wheel A as plaintext
  - Apply the same rotations and wheel mutations

**Code**

```
# decrypt_custom.py
# Decrypts the custom rotating-wheel cipher

CIPHERTEXT = "PFRLGJEUCZIVFCNGXOMTRKYH"

LEFT_START  = "GZQFHKDOVYINRUXTCALSPBEMWJ"
RIGHT_START = "YPMRDFZKQHATVJCNWOGIBLUESX"

def rotate(lst, n):
    return lst[n:] + lst[:n]

L = list(LEFT_START)
R = list(RIGHT_START)

plaintext = ""

for ch in CIPHERTEXT:
    idx = R.index(ch)
    pt = L[idx]
    plaintext += pt

    # rotate BOTH wheels by same index
    L = rotate(L, idx)
    R = rotate(R, idx)

    # wheel mutations
    L = L[:2] + L[3:] + [L[2]]
    R = R[:1] + R[2:] + [R[1]]

print("Recovered message:")
print(plaintext)
```

Running this process over the full ciphertext yields:

`ZKQBLUEMTHPRDXCSWAGNQHFV`

## Step 6: Constructing the Flag

The challenge specifies the submission format:

L3m0nCTF{...}

Placing the recovered message inside the wrapper:

**Flag**

```
L3m0nCTF{ZKQBLUEMTHPRDXCSWAGNQHFV}
```
