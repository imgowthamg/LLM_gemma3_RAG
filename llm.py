import subprocess
from langchain.llms.base import LLM

class OllamaLLM(LLM):
    """Custom LangChain LLM that interfaces with Ollama."""
    
    @property
    def _llm_type(self) -> str:
        return "ollama"

    def _call(self, prompt: str, stop=None) -> str:
        result = subprocess.run(
            ["ollama", "run", "gemma3:1b", prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()

    async def _acall(self, prompt: str, stop=None) -> str:
        return self._call(prompt, stop)
