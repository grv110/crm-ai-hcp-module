from tools import log_interaction, edit_interaction, summarize_interaction, suggest_followup, search_history

def run_agent(message):

    if "log" in message:
        return log_interaction(message)

    if "edit" in message:
        return edit_interaction(message)

    if "summary" in message:
        return summarize_interaction(message)

    if "follow" in message:
        return suggest_followup(message)

    if "history" in message:
        return search_history(message)

    return "AI Agent could not understand"