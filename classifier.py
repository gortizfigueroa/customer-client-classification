#!/usr/bin/env python3
"""
Smart Support Automation - MVP Simulation
"""

import random
import time

# ---------------------------------------------------------------------
# Mock knowledge base and helpers
# ---------------------------------------------------------------------
FAQ_KB = {
    "login_issue": "Please reset your password at https://app.example.com/reset or contact support if the issue persists.",
    "pricing_query": "Our pricing plans are available at https://example.com/pricing. For teams, contact sales@example.com.",
    "billing_issue": "Please provide your invoice ID so our billing team can correct the VAT.",
    "integration_help": "You can connect to Shopify by following our integration guide: https://example.com/shopify.",
    "data_migration": "We can assist with data export. Please confirm your account email and expected migration date."
}

INTENTS = list(FAQ_KB.keys())
URGENCIES = ["low", "medium", "high"]
PRODUCTS = ["web_app", "billing", "sales", "integration", "migration"]

# ---------------------------------------------------------------------
# Pipeline components
# ---------------------------------------------------------------------
def preprocess(text: str) -> tuple[str, str]:
    """Cleans text and detects language (mocked as English)."""
    clean = text.strip().replace("\n", " ")
    lang = "en"
    print(f"[Preprocess] Text='{clean[:40]}...' | Lang={lang}")
    return clean, lang


def classify_ticket(text: str) -> tuple[str, str, str, float]:
    """Mock classifier returning random intent/urgency/product/confidence."""
    intent = random.choice(INTENTS)
    urgency = random.choice(URGENCIES)
    product = random.choice(PRODUCTS)
    confidence = round(random.uniform(0.7, 0.95), 2)
    print(f"[Classify] Intent={intent}, Urgency={urgency}, Product={product}, Confidence={confidence}")
    return intent, urgency, product, confidence


def retrieve_knowledge(intent: str, lang: str) -> str:
    """Retrieves a simple text snippet from the mock KB."""
    doc = FAQ_KB.get(intent, "No related knowledge found.")
    print(f"[Retrieve] Retrieved context for intent '{intent}'")
    return doc


def suggest_reply(text: str, context: str, product: str, lang: str) -> tuple[str, float]:
    """Generates a simple reply using the KB and a confidence score."""
    confidence = round(random.uniform(0.75, 0.95), 2)
    suggestion = context
    print(f"[Suggest] Reply generated with confidence {confidence}")
    return suggestion, confidence


def decide_and_dispatch(ticket_id: int, intent: str, reply_conf: float, class_conf: float) -> str:
    """Decides whether to auto-suggest or escalate."""
    final_conf = round((reply_conf * 0.5) + (class_conf * 0.5), 2)
    action = "Auto-suggest" if final_conf >= 0.8 else "Escalate to human"
    print(f"[Decision] Ticket#{ticket_id}: FinalConfidence={final_conf} → {action}")
    return action


# ---------------------------------------------------------------------
# Main orchestration
# ---------------------------------------------------------------------
def handle_ticket(ticket_id: int, text: str):
    """Complete pipeline for one ticket."""
    print(f"\n=== Processing Ticket #{ticket_id} ===")
    clean, lang = preprocess(text)
    intent, urgency, product, class_conf = classify_ticket(clean)
    context = retrieve_knowledge(intent, lang)
    suggestion, reply_conf = suggest_reply(clean, context, product, lang)
    action = decide_and_dispatch(ticket_id, intent, reply_conf, class_conf)

    print(f"[Result] Intent='{intent}' | Suggestion='{suggestion[:60]}...' | Action={action}")
    time.sleep(0.2)  # simulate latency


def main():
    tickets = [
        "I can't log in, keeps saying 'invalid credentials' — urgent please",
        "Do you offer team pricing for 10+ users?",
        "My invoice shows wrong VAT for Spain",
        "How do I connect this to my Shopify?",
        "We are migrating, can you help with data export?"
    ]

    print("=== Smart Support Automation MVP Demo ===\n")
    for i, t in enumerate(tickets, start=1):
        handle_ticket(i, t)

    print("\n=== Demo Completed ===")


# ---------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------
if __name__ == "__main__":
    main()
