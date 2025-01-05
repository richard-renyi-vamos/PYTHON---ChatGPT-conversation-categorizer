import re
from collections import defaultdict

def categorize_conversations(chat_data):
    """
    Categorizes ChatGPT conversations based on predefined keywords and topics.

    Parameters:
        chat_data (list of str): List of conversation strings.

    Returns:
        dict: Dictionary with categories as keys and list of conversations as values.
    """
    # Define categories and keywords
    categories = {
        "Job and Career": ["job", "salary", "position", "business analyst", "Deutsche Telekom"],
        "Personal Life": ["wife", "child", "marriage", "family", "flat", "kindergarten"],
        "Health": ["medicine", "pain", "chest", "Alpranax", "breast enlargement"],
        "Spirituality": ["number 48", "spirituality", "dreams", "goals"],
        "Hobbies and Interests": ["Hebrew", "Israeli pop", "art", "history", "AI", "technology"],
        "Home and Utilities": ["FÉG", "heater", "CO2 monitor", "flat"],
        "Languages": ["German", "language"],
    }

    categorized_data = defaultdict(list)

    for conversation in chat_data:
        categorized = False
        for category, keywords in categories.items():
            for keyword in keywords:
                if re.search(rf'\b{keyword}\b', conversation, re.IGNORECASE):
                    categorized_data[category].append(conversation)
                    categorized = True
                    break
            if categorized:
                break
        if not categorized:
            categorized_data["Uncategorized"].append(conversation)

    return categorized_data


# Example usage
if __name__ == "__main__":
    # Example conversation data
    chat_data = [
        "Richard wants to apply for a new job in 2025 aiming for a better-paying position.",
        "Richard's wife has been prescribed the medication Alpranax.",
        "Richard listens to Hebrew pop mixes on YouTube.",
        "Richard has been with a large Hungarian company since 2010.",
        "Richard prefers speaking in German.",
        "Richard purchased a CO2 monitor to check the levels at home."
    ]

    # Categorize the conversations
    categorized_conversations = categorize_conversations(chat_data)

    # Display results
    for category, conversations in categorized_conversations.items():
        print(f"\nCategory: {category}")
        for convo in conversations:
            print(f"- {convo}")
