from fastapi import APIRouter, Query
from core.utility_function.prayer_time_calculator import calculate_prayer_times

router = APIRouter()

@router.get("/prayer-time")
def get_prayer_times(
    lat: float = Query(..., description="Latitude of user's location"),
    lng: float = Query(..., description="Longitude of user's location"),
    method: str = Query("karachi", description="Calculation method (default: karachi)")
):
    result = calculate_prayer_times(lat, lng, method)

    return {
        "location": {"lat": lat, "lng": lng},
        "method": method,
        "prayer_times": result
    }