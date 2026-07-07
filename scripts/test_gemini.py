from app.ai.factory import LLMFactory
from app.ai.models import LLMRequest

provider = LLMFactory.create()

response = provider.generate(
    LLMRequest(
        prompt="Reply with exactly: Hello VoiceOps"
    )
)

print(response.content)