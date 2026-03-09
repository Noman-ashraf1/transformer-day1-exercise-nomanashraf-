# Day 3 - Reverse Prompt Engineering Assignment

## Objective
Recreate a reference image as closely as possible using prompt 
conditioning techniques in a text-to-image diffusion model (Z-Image Turbo).

---

## Reference Image
A young East Asian woman sitting side profile at a round wooden 
cafe table, typing on a MacBook laptop showing a dark code editor, 
wearing a cream knit sweater, with a latte and smartphone on the 
table, large cafe window with blurred street view behind her.

---

## Tool Used
- **Model:** Z-Image Turbo  
- **Platform:** Hugging Face Spaces  
- **Link:** https://huggingface.co/spaces/mrfakename/Z-Image-Turbo

---

## Final Prompt
```
Young East Asian woman with straight black shoulder-length 
hair and round black glasses, sitting side profile at a small 
round wooden cafe table, typing on a slim black MacBook laptop 
showing dark IDE code editor with colorful syntax highlighting, 
wearing a cream chunky knit sweater, white ceramic latte cup 
with saucer on table, black smartphone beside cup, floor-to-
ceiling cafe window behind her, warm golden window light, 
blurred street with cars outside, photorealistic, 50mm lens, 
shallow depth of field, soft natural shadows, film grain
```

**Final SEED:** `70216`

---

## Iterative Process

### Attempt 1
**SEED:** `42`  
**Prompt:**
```
Young Asian woman with black hair and glasses, sitting at a 
round wooden cafe table, typing on a black laptop with code 
on screen, wearing a cream/beige knit sweater, a latte coffee 
cup with saucer beside her, large window with soft natural 
daylight, blurred street view outside, warm indoor cafe 
ambiance, photorealistic, 50mm lens, shallow depth of field, 
soft shadows
```
**Result:** Good baseline. Core elements matched — woman, 
laptop, cafe, sweater, coffee. Missing smartphone on table. 
Lighting slightly cool/grey compared to reference.

---

### Attempt 2 (Final)
**SEED:** `70216`  
**Prompt:** *(see Final Prompt above)*  
**Changes Made:**
- Changed SEED to `70216` (matching the assignment's provided seed)
- Added `"black smartphone beside cup"` → phone now visible on table
- Added `"floor-to-ceiling cafe window"` → better window framing
- Added `"colorful syntax highlighting"` → code colors more accurate
- Added `"film grain"` → more photorealistic texture
- Changed to `"warm golden window light"` → warmer, more natural tone
- Specified `"round black glasses"` → glasses shape more accurate

**Result:** Near-perfect match to reference image across all 
key elements — subject, clothing, environment, lighting, and props.

---

## What I Learned
- **SEED control** is critical for fair before/after comparisons
- **Specificity matters** — vague terms like "glasses" are less 
  effective than "round black glasses"
- **Layered descriptors** (subject + clothing + environment + 
  camera + lighting) produce significantly better results
- Small prompt tweaks with the same SEED isolate the effect 
  of each change, making iteration more systematic

---

## Files
| File | Description |
|------|-------------|
| `system_prompt.txt` | Final prompt used for best result |
| `final_image.png` | Final generated image (SEED 70216) |
| `README.md` | This file |