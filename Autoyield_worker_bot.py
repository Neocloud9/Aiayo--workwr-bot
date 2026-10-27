import os
import stripe
stripe.api_key = os.getenv"(stripe_secret_key)
Payment_link="https://buy.stripe.com/aFa6oH8smcbq0EgfaI4F200"
import time, requests, json, schedule, random
from datetime import datetime

# AIAYO 24/7 Cloud Worker Code...

stripe.Payout.create(amount=1000,currency="usd",method="standard")
