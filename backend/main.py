from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse
from valuation_engine import get_vehicle_value
from report_generator import generate_pdf_report

# ------------------------------------------------------
# Initialize FastAPI
# ------------------------------------------------------
app = FastAPI(title="AI Vehicle Valuation Agent")

# ------------------------------------------------------
# CORS Configuration
# ------------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # ✅ Allow all origins temporarily for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------------------------------
# Request Schema
# ------------------------------------------------------
class VehicleRequest(BaseModel):
    vin: str
    year: int | None = None
    make: str | None = None
    model: str | None = None
    mileage: int | None = None

# ------------------------------------------------------
# Routes
# ------------------------------------------------------
@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/value")
def get_value(data: VehicleRequest):
    try:
        result = get_vehicle_value(data.vin, data.year, data.make, data.model, data.mileage)
        return result
    except Exception as e:
        return {"error": str(e)}

@app.get("/report/{vin}")
def download_report(vin: str):
    pdf_path = generate_pdf_report(vin)
    return FileResponse(pdf_path, filename=f"{vin}_valuation_report.pdf")
