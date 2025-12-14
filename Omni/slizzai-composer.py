"""
SlizzAi Composer module: Orchestrates Nuninex, Omni, and optional Feedback engines.
"""

from loguru import logger

try:
    from nuninex.core import NuninexResolver
except ImportError:
    NuninexResolver = None
    logger.warning("nuninex.core.NuninexResolver could not be imported.")

try:
    from omni.controller import OmniController
except ImportError:
    OmniController = None
    logger.warning("omni.controller.OmniController could not be imported.")

try:
    from feedback_loop import FeedbackEngine  # Optional module
except (ImportError, AttributeError):
    FeedbackEngine = None
    logger.warning("feedback_loop.FeedbackEngine could not be imported or does not exist.")

class SlizzAiComposer:
    """
    Composer class for orchestrating Nuninex, Omni, and Feedback engines.
    """

    def __init__(self, config):
        """
        Initialize the SlizzAiComposer with configuration for each engine.
        """
        self.nuninex = NuninexResolver(config.get("nuninex")) if NuninexResolver else None
        self.omni = OmniController(config.get("omni")) if OmniController else None
        self.feedback = FeedbackEngine(config.get("feedback")) if FeedbackEngine and config.get("feedback") else None

    def compose(self, payload: dict) -> dict:
        """
        Compose the invocation arc using Nuninex, Omni, and optionally Feedback.
        """
        logger.info("🔮 Composing SlizzAi invocation arc")

        # Step 1: Nuninex Resolution
        nuninex_input = payload.get("nuninex", {})
        nuninex_result = self.nuninex.process(nuninex_input) if self.nuninex else None

        # Step 2: Omni Invocation
        omni_input = payload.get("omni", {})
        omni_response = self.omni.invoke(omni_input) if self.omni else None

        # Step 3: Feedback Loop (optional)
        feedback_result = None
        if self.feedback:
            feedback_input = {
                "nuninex": nuninex_result,
                "omni": omni_response
            }
            feedback_result = self.feedback.evaluate(feedback_input)

        return {
            "nuninex_result": nuninex_result,
            "omni_response": omni_response,
            "feedback": feedback_result,
            "status": "SlizzAi-Composer completed arc"
        }

    def health_check(self) -> dict:
        """
        Public method to check the health of the composer and its engines.
        """
        return {
            "nuninex": self.nuninex is not None,
            "omni": self.omni is not None,
            "feedback": self.feedback is not None
        }