# import_omni_controller.py
from fastapi import APIRouter
from omni.controller import OmniController
from omni.config import get_omni_profile

router = APIRouter()
profile = get_omni_profile()
controller = OmniController(profile=profile)

@router.post("/omni/invoke")
async def invoke_module(request: dict):
    response = controller.invoke(request)
    return {"response": response}