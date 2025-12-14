from vision_module import VisionModule
from nlp_module import NLPModule
from speech_module import SpeechModule

ENGINE_REGISTRY = {
    "vision": VisionModule,
    "nlp": NLPModule,
    "speech": SpeechModule
}

def activate_engine(engine_name):
    engine_class = ENGINE_REGISTRY.get(engine_name)
    if not engine_class:
        raise ValueError(f"Engine '{engine_name}' is not recognized.")
    engine_instance = engine_class()
    engine_instance.activate()
    return engine_instance