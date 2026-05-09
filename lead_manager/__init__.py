# Lead Manager A2A Agent
try:
    from . import agent, agent_executor
except ImportError:
    # ADK dependencies not available, use simple version
    pass