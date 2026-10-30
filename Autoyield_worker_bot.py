import os
import stripe
stripe.api_key = os.getenv ("stripe_secret_key")
Payment_link="https://buy.stripe.com/aFa6oH8smcbq0EgfaI4F200"
import time, requests, json, schedule, random
from datetime import datetime

while True:# AIAYO 24/7 Cloud Worker Code...
    # Fetch your current Stripe balance
    balance = stripe.Balance.retrieve()
    
    # Get the available amount in the primary currency (e.g., USD cents)
    # Assumes balance.available contains at least one currency entry
    available_amount = balance.available[0].amount if balance.available else 0
    currency = balance.available[0].currency if balance.available else "usd"
    
    # Define your target payout amount (in cents, e.g., $10.00 = 1000)
    payout_amount = 150  
    
    if available_amount >= payout_amount:
        # Proceed with the payout if funds are sufficient
        try:
            payout = stripe.Payout.create(
                amount=payout_amount,
                currency=currency,
            )
            print(f"Payout successful: {payout.id}")
            time.sleep(43200)
        except Exception as e:
            print(f"Payout failed: {e}")
    else:
    print(f"Skipping payout: Available balance ({available_amount}) is below the required amount ({payout_amount}).")
