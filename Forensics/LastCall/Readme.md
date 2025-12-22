## Challenge Write-Up — Mystery Call

<img width="445" height="676" alt="image" src="https://github.com/user-attachments/assets/1ea56118-63d8-44a4-a851-3da8766684cb" />

### Overview

We are given a single audio file, mystery_call.wav.

The audio contains nothing except a sequence of repetitive electronic tones.
There is no speech, no music, and no obvious audible message.

At first listen, the tones resemble telephone beeps, but decoding them directly does not reveal any readable text.

The goal is to determine **what information is hidden inside these tones**.

### Step 1: File Inspection

We begin by checking the file type.

`file mystery_call.wav`

<img width="782" height="110" alt="image" src="https://github.com/user-attachments/assets/9ee78a35-93aa-476c-bb32-541458e8ac29" />

The output confirms:

- WAV audio
- Stereo
- Fixed sample rate

This is important — the file has two channels, not one.

### Step 2: Initial Decoding Attempt

Since the tones resemble telephone signals, we try a standard DTMF decoder.

`multimon-ng -a DTMF -t wav mystery_call.wav`

<img width="1868" height="384" alt="image" src="https://github.com/user-attachments/assets/bc65c082-1dae-41da-b295-1ee9903821f6" />


This produces a long stream of same repeated digits.

However:

- The output does not resemble a flag
- The sequence is far too long
- No readable structure appears

This tells us something important:

**The decoded DTMF symbols themselves are not the message.**

### Step 3: Channel Separation

On opening this file in audacity we can see that both left channel and right channel doesnt resemble same  sound.

<img width="1905" height="298" alt="image" src="https://github.com/user-attachments/assets/74af7526-be26-4625-976c-0b1be6b4e486" />

So, we separate the channels.

`sox mystery_call.wav left.wav  remix 1`

`sox mystery_call.wav right.wav remix 2`

Now we have:

- left.wav
- right.wav

Each channel contains valid tones.

Running a DTMF decoder on either channel alone still does not produce meaningful text.

So:

- The message is **not** stored in a single channel
- The channels must be **used together**

### Step 4: Observing the Real Signal Property

When visualizing the waveform or spectrogram, one key detail stands out:

- The frequencies do not change meaningfully
- The only variation is tone duration

Each tone is either:

- **Short**
- **Long**

This strongly suggests binary encoding.

We treat:

- Short tone → 0
- Long tone → 1

### Step 5: Extracting Binary From Each Channel

For each channel independently:

1.Convert audio to mono signal

2.Compute short-time energy

3.Detect tone “on” segments

4.Measure duration of each segment

5.Convert duration to bits

The extraction logic is implemented in a helper script
![extract_bits.py](link)

Running this script produces two binary streams:

This produces two binary strings:

<img width="1893" height="179" alt="image" src="https://github.com/user-attachments/assets/b96ed226-4dba-4bf8-b40b-5a2cc6e48512" />

Neither stream alone forms valid ASCII.

### Step 6: Channel Combination

Because both channels are synchronized and neither decodes meaningfully by itself, the next step is to **combine them.**

The intended operation is a **bitwise XOR** between corresponding bits:

`FINAL_BIT = LEFT_BIT ⊕ RIGHT_BIT`

This operation removes the decoy structure present in each channel individually and reconstructs the original data.

The XOR and decoding process is handled by the that code even:

### Step 7: Binary to ASCII

The resulting binary stream is grouped into 8-bit chunks and converted to ASCII.

This yields the final message:

`L3m0nCTF{DTMF_X0R_5T3R30_1S_N0T_4UD10_3V3RY0N3}`
