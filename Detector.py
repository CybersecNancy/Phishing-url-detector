# Phishing URL Detector 
def check_url(url):
    suspicious = ["@", "-", "login", "verify", "free", "secure", "account"]
    score = 0
    
    print(f"\nChecking URL: {url}")
    
    if len(url) > 75:
        print("⚠️ Very long URL - suspicious")
        score += 1
    if url.count(".") > 3:
        print("⚠️ Many dots in URL - suspicious")
        score += 1
    if "http://" in url:
        print("⚠️ Not HTTPS - not secure")
        score += 1
    for word in suspicious:
        if word in url.lower():
            print(f"⚠️ Contains suspicious keyword: {word}")
            score += 1
            
    if score == 0:
        print("Result: Looks SAFE ✅")
    elif score <= 2:
        print("Result: Be CAREFUL ⚠️")
    else:
        print("Result: Possible PHISHING ❌")


check_url(input("Enter URL to check: "))
