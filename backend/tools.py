interactions = []

def log_interaction(message):

    data = {
        "doctor": "Dr Sharma",
        "topic": "Diabetes Drug",
        "sentiment": "Positive"
    }

    interactions.append(data)

    return {
        "status": "interaction logged",
        "data": data
    }


def edit_interaction(message):

    if interactions:
        interactions[0]["sentiment"] = "Neutral"

    return "interaction updated"


def summarize_interaction(message):

    return "Doctor discussed diabetes drug and showed interest"


def suggest_followup(message):

    return "Follow-up suggested: send brochure"


def search_history(message):

    return interactions