from fastapi import FastAPI
from pydantic import BaseModel
from valuation_engine import get_vehicle_value
from report_generator import generate_pdf_report
from fastapi.responses import FileResponse

app = FastAPI(title="AI Vehicle Valuation Agent")
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://vehicle-valuation-agent.vercel.app",  # your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VehicleRequest(BaseModel):
    vin: str
    year: int | None = None
    make: str | None = None
    model: str | None = None
    mileage: int | None = None

@app.post("/value")
def get_value(data: VehicleRequest):
    result = get_vehicle_value(data.vin, data.year, data.make, data.model, data.mileage)
    return result

@app.get("/report/{vin}")
def download_report(vin: str):
    pdf_path = generate_pdf_report(vin)
    return FileResponse(pdf_path, filename=f"{vin}_valuation_report.pdf")
