## Lost Signal — Full WriteUp

<img width="437" height="601" alt="image" src="https://github.com/user-attachments/assets/53b2e3dd-171d-492a-9bee-0c5d35a25ea4" />

### Given in the challenge

File: [](challenge_color_random.png)

Clue:

``Seed = 739391``

No other hints.

### Step 1: Understand what the seed implies

The challenge explicitly provides a **seed**.

A seed is **not encryption** by itself — it is used to:

- Initialize a pseudo-random number generator
- Produce a **deterministic order**

So from the question alone, the solver can infer:

> The hidden data depends on a **specific order**, reproducible using the seed.

Since:

- The file is an image
- Metadata, strings, binwalk, StegSolve show nothing

The only reasonable conclusion is:

The seed defines an **order of pixels**, not bytes or files.

### Step 2: Work at pixel level (not StegSolve)

StegSolve fails because:

- Any meaningful structure has been **shuffled**
- No spatially coherent pattern exists

So you must:

- Load the image programmatically
- Treat it as a pixel array

### Step 3: Separate brightness from color

RGB mixes color and brightness.

For hidden data, brightness is the most likely carrier because:

- Small brightness changes are visually invisible
- Color changes are more noticeable

So convert the image to **YCbCr** and extract **Y (luminance)**.

Code:
```
python3 - << 'EOF'
from PIL import Image
import numpy as np

img = Image.open("challenge_color_random.png").convert("YCbCr")
Y, Cb, Cr = img.split()

Y_arr = np.array(Y, dtype=np.uint8)
np.save("Y.npy", Y_arr)

print("Y channel extracted:", Y_arr.shape)
EOF
```

### Step 4: Recreate the permutation using the seed

The seed must recreate the exact pixel order used during embedding.

Code:

```
python3 - << 'EOF'
import numpy as np

seed = 739391
Y = np.load("Y.npy")
h, w = Y.shape

rng = np.random.RandomState(seed)
indices = np.arange(h * w)
rng.shuffle(indices)

np.save("perm.npy", indices)
print("Permutation generated")
EOF
```

Now indices represents the correct pixel visit order.

### Step 5: Extract hidden bits correctly

A simple LSB dump fails, which means:

- More than one bit is used
- Bits are interleaved

The correct approach is:

- Extract two least significant bits
- Alternate between them
- Follow the shuffled pixel order

Bitplanes used:

``[0,1]``

Code:
```
python3 - << 'EOF'
import numpy as np

Y = np.load("Y.npy")
perm = np.load("perm.npy")
h, w = Y.shape

LSBS = [0, 1]
total_bits = h * w
qr_flat = np.zeros(total_bits, dtype=np.uint8)

for i in range(total_bits):
    pix_idx = perm[i // len(LSBS)]
    bitplane = LSBS[i % len(LSBS)]

    y = pix_idx // w
    x = pix_idx % w

    qr_flat[i] = (Y[y, x] >> bitplane) & 1

np.save("qr_flat.npy", qr_flat)
print("Bitstream recovered")
EOF
```

Without:

- the seed
- the correct order
- both bitplanes

the output is pure noise.

### Step 6: Rebuild the hidden image

The recovered bitstream must be reshaped back into an image.

Code

```
python3 - << 'EOF'
from PIL import Image
import numpy as np

qr_flat = np.load("qr_flat.npy")
Y = np.load("Y.npy")
h, w = Y.shape

qr = qr_flat.reshape((h, w))

# invert for proper QR colors
qr_img = (255 * (1 - qr)).astype(np.uint8)

Image.fromarray(qr_img).save("solved_qr.png")
print("QR image saved as solved_qr.png")
EOF
```

The QR will be generated.

Now you just scan the qr you will get the flag.

<img width="1499" height="876" alt="image" src="https://github.com/user-attachments/assets/0de87e6e-6cd4-4149-8b7a-ec253324bcb5" />

**Flag : ``L3m0nCTF{1nv1s1bl3_b1tpl4n3_x0r_qr}``**
