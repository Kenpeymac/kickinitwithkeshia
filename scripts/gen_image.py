#!/usr/bin/env python3
"""Image edit/generate via Gemini image API (the 'nano banana' model), bypassing
the deprecated gemini CLI auth. Usage:
  gen_image.py <model> <source_image_or_-> <output.png> <<<"prompt"
"""
import sys, os, base64, json, urllib.request

KEY = os.environ["GEMINI_API_KEY"]
model = sys.argv[1]
src = sys.argv[2]
out = sys.argv[3]
prompt = sys.stdin.read().strip()

parts = [{"text": prompt}]
if src != "-":
    with open(src, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    mime = "image/jpeg" if src.lower().endswith((".jpg", ".jpeg")) else "image/png"
    parts.append({"inline_data": {"mime_type": mime, "data": b64}})

body = json.dumps({
    "contents": [{"parts": parts}],
    "generationConfig": {"responseModalities": ["IMAGE"]},
}).encode()

url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={KEY}"
req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
try:
    resp = urllib.request.urlopen(req, timeout=240)
    data = json.load(resp)
except urllib.error.HTTPError as e:
    print("HTTP_ERROR", e.code, e.read().decode()[:800]); sys.exit(1)

cand = (data.get("candidates") or [])
if not cand:
    print("NO_CANDIDATES", json.dumps(data)[:800]); sys.exit(1)
saved = False
for p in cand[0]["content"]["parts"]:
    if "inlineData" in p or "inline_data" in p:
        d = (p.get("inlineData") or p.get("inline_data"))["data"]
        with open(out, "wb") as f:
            f.write(base64.b64decode(d))
        saved = True
        print("SAVED", out)
        break
if not saved:
    txt = " ".join(p.get("text", "") for p in cand[0]["content"]["parts"])
    print("NO_IMAGE_RETURNED", txt[:600]); sys.exit(1)
