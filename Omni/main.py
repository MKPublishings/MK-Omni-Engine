from fastapi import FastAPI
from import_nuninex import router as nuninex_router
from import_omni_controller import router as omni_router
from slizzai_extension import slizzai_router
from fastapi import APIRouter

router = APIRouter()

@router.get("/slizzai")
async def read_slizzai():
    return {"message": "SlizzAi extension is working"}
# Ritualized import of Nuninex + OmniController
app = FastAPI(title="SlizzAi Unified Engine")
app.include_router(nuninex_router, prefix="/api")
app.include_router(omni_router, prefix="/api")
app = FastAPI(title="SlizzAi Unified Engine")
app.include_router(slizzai_router, prefix="/api")