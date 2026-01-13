# UI Configuration Constants

PAGE_TITLE = "LangGraph: Build Stateful Agentic AI Chatbot"

LLM_OPTIONS = ["Groq", "OpenAI", "Anthropic"]
USECASE_OPTIONS = [
    "Basic Chatbot",
    "Chatbot with tool",
    "AI news",
    "Blog generator"
]

GROQ_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "qwen.qwen3-32b"
]

SYSTEM_PROMPTS = {
    "Basic Chatbot": "You are a helpful, friendly AI assistant. Answer questions clearly and concisely.",
    
    "Chatbot with tool": "Yosu are an AI assistant with access to tools like web search and calculators. When needed, use these tools to provide accurate answers.",
    
    "AI news": "You are an AI news analyst. Provide insights on the latest developments in artificial intelligence, machine learning, and related technologies. Be factual and cite sources when possible.",
    
    "Blog generator": "You are a professional blog writer. Create engaging, well-structured, SEO-friendly content. Use proper formatting with headings, paragraphs, and examples."
}