import agent  # Import the custom agent module which handles LLM interaction

if __name__ == "__main__":
    # Define the user's request in a structured format as input to the LLM
    user_prompt = """
        Please write a formal and polite email in English.

        1. Recipient email: x@x.com
        2. Subject: Refund Request – Damaged Television
        3. Message: I purchased a television on June 12, 2025, but it arrived with a broken screen. I would like to request a return and a full refund. Could you please inform me about the return process?
        4. Tone: Formal
        5. Additional: Order number: TV-932749
    """

    # Send the prompt to the LLM agent and receive the generated email draft
    email = agent.send_prompt(user_prompt)

    service = agent.gmail_authenticate()
    
     # Set your fields
    sender_email = "your_email@gmail.com"
    recipient = "x@x.com"
    subject = "Refund Request – Damaged Television"

    # Create the draft
    agent.create_draft(service, sender_email, recipient, subject, email)
    # Print the formatted email output to the console
    print("\n--- E-Mail Draft ---\n")
    print(email)
