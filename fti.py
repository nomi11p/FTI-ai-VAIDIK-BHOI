import google.generativeai as genai
from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0

# TERA KEY
genai.configure(api_key="AIzaSyB2esPAWxN-E-PxWUogL9ID-AnJYLTA8H0")
model = genai.GenerativeModel('gemini-2.5-flash')

# TERA BRAND
CREATOR = "Vaidik Bhoi"

print("FTI AI LIVE HAI!\n")

while True:
    try:
        user = input(">>> ")
        if user.strip() == "":
            continue
        if user.lower() in ['bye', 'exit', 'quit', 'band']:
            print("Bye bhai! Vaidik Bhoi ka AI band! 🇮🇳\n")
            break

        # LANGUAGE DETECT
        try:
            lang = detect(user)
        except:
            lang = 'en'

        # FINAL PROMPT — POLITE + BHAI STYLE
        prompt = f"""
        Tu FTI AI hai.
        Malik: {CREATOR}
        
        RULES:
        - Jawab **user ki language mein de**
        - Hamesha **polite**, **bhai wala pyar**, **respectful**
        - Koi bhi batamizi, slang, "yo", "bro" mat bolna
        - Short, helpful, natural
        - Malik → "{CREATOR}"
        - Tu kaun → "Main FTI AI hoon, {CREATOR} ne banaya hai."
        
        User ne poocha ({lang}): {user}
        """

        reply = model.generate_content(prompt).text.strip()
        print(reply + "\n")

    except:
        print("Thoda ruk bhai, soch raha hoon...\n")