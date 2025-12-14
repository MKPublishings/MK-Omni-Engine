# import_nuninex.py
from fastapi import APIRouter
from nuninex.core import NuninexResolver
from nuninex.config import load_nuninex_config

router = APIRouter()
config = load_nuninex_config()
resolver = NuninexResolver(config=config)

@router.post("/nuninex/resolve")
async def resolve_payload(payload: dict):
    result = resolver.process(payload)
    return {"result": result}