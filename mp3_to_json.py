import whisper
import json
import os

model = whisper.load_model("base")

audios = os.listdir("audios")

os.makedirs("jsons", exist_ok=True)

for audio in audios:
    numbers = audio.split("_", 1)[0]
    title = audio.split("_", 1)[1]

    print({"Numbers": numbers, "Title": title})

    result = model.transcribe(
        audio=f"trimmed_audios/{audio}",
        language="en"
    )

    chunks = []
    for segment in result["segments"]:
        chunks.append({
            "number": numbers,          # ← FIXED (was segment["numbers"])
            "title": title,             # ← FIXED (was segment["title"])
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"]
        })

    chunks_with_meta_data = {
        "chunks": chunks,
        "text": result["text"]
    }

    # ← FIXED: actually use a dynamic filename
    output_path = f"jsons/{numbers}_{title}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks_with_meta_data, f, indent=2)

    print("JSON WRITE DONE")
