#!/usr/bin/env python3
import numpy as np
from scipy.io import wavfile

SHORT = 0.10
LONG  = 0.22
THRESH = (SHORT + LONG) / 2
WINDOW = 256

def extract_bits(wav):
    sr, x = wavfile.read(wav)

    # mono safety
    if x.ndim > 1:
        x = x[:,0]

    x = x.astype(np.float32)
    x /= np.max(np.abs(x))

    energy = np.convolve(x*x, np.ones(WINDOW)/WINDOW, mode="same")
    on = energy > (0.2 * energy.max())

    bits = []
    i = 0
    while i < len(on):
        if on[i]:
            j = i
            while j < len(on) and on[j]:
                j += 1
            dur = (j - i) / sr
            bits.append('1' if dur > THRESH else '0')
            i = j
        else:
            i += 1

    return ''.join(bits)

# ===================== SOLVE =====================
left  = extract_bits("left.wav")
right = extract_bits("right.wav")
print("[LEFT bits]")
print(left)
print("Length:", len(left))

print("\n[RIGHT bits]")
print(right)
print("Length:", len(right))


n = min(len(left), len(right))
xor_bits = ''.join(str(int(left[i]) ^ int(right[i])) for i in range(n))

out = []
for i in range(0, len(xor_bits), 8):
    byte = xor_bits[i:i+8]
    if len(byte) == 8:
        out.append(chr(int(byte, 2)))

print("".join(out))

