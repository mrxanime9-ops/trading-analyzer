# main.py

from fastapi import FastAPI, File, UploadFile
from analyzer import analyze_chart

app = FastAPI()

@app.post("/analyze-chart")
async def analyze_chart_api(file: UploadFile = File(...)):
    # এখানে ভবিষ্যতে real image processing হবে
    result = analyze_chart()
    return {
        "status": "success",
        "analysis": result
    }
