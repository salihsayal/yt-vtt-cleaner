# 🎬 Subtitle Cleaner for YouTube `.vtt` Files

This simple Python script converts `.vtt` subtitle files (downloaded via [yt-dlp](https://github.com/yt-dlp/yt-dlp)) into clean, readable plain text. It's designed to prepare subtitle data for downstream use in large language models (LLMs) — for summarization, semantic analysis, and more.

## 🚀 Features

- Removes timestamp lines and formatting noise
- Strips HTML-style tags (`<c>`, `<b>`, etc.)
- Eliminates alignment/position metadata
- Deduplicates consecutive identical lines
- Optionally merges short lines (commented out for now)
- Outputs clean text ready for AI models

## 🧠 Why?

LLMs like GPT-4, Claude, and others perform best when given structured and coherent input. YouTube’s `.vtt` subtitle files are cluttered with timestamps and tags that hurt performance. This script gives you clean, lean, and human-like transcripts.

## 📦 Installation

Just clone this repo and use Python 3 (no external dependencies required):

```bash
git clone https://github.com/salihsayal/yt-vtt-cleaner.git
cd yt-vtt-cleaner
```

## 📄 Usage

1. **Download subtitles with `yt-dlp`:**

   ```bash
   yt-dlp --write-auto-sub --sub-lang en --skip-download "https://youtube.com/watch?v=..."
    ```

2. **Run the script to clean the `.vtt` file:**

    ```bash
    python yt-vtt-cleaner.py {your file}
    ```

2. **Result:**

    You’ll get a cleaned `.txt` file `cleaned_subtitles.txt`, ready to be used for LLM summarization or analysis.

---

## 📜 License

MIT License — use freely and modify as needed.

---

*Created to make subtitles useful again.* 🧼
