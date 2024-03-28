import requests
from colorama import Fore, init

init()
T4 = ["ss", "js", "images", "fonts", "ocs", "assets", "pages", "videos", "audio", "uploads",
       "downloads", "scripts", "styles", "layouts", "templates", "includes", "data", "files", "media", "gallery",
       "resources", "backups", "news", "articles", "projects", "apps", "mobile", "desktop", "panel", "admin", "theme",
       "plugins", "errors", "logs", "cache", "temp", "archives", "log", "shop", "products", "art", "checkout",
       "orders", "accounts", "profile", "messages", "notifications", "events", "calendar", "search", "contact",
       "forms", "about", "team", "services", "careers", "contact-us", "support", "faq", "terms", "privacy", "policy",
       "legal", "sign-in", "sign-up", "forgot-password", "reset-password", "dashboard", "settings", "references",
       "notifications", "messages", "invites", "friends", "connections", "followers", "following", "likes", "dislikes",
       "events", "locations", "map", "apps", "search", "bookmarks", "history", "watchlist", "favorites", "recommendations",
       "trending", "recently-viewed", "top-rated", "new-arrivals", "promotions", "discounts", "feature", "best-sellers",
       "trending-now", "special-offers", "clearance"]

print(Fore.BLUE + "                      creator of Satan")
print(Fore.BLUE + "  FIB https://t.me/ARP1210")

T1 = input("URL: ")
if not T1:
    raise ValueError("URL cannot be empty!")

for page in T4:
    req = requests.get("https://" + T1 + "/" + page)
    if req.status_code == 200:
        print(Fore.GREEN + "[+] " + Fore.WHITE + "OK bod " + T1 + "/" + page)
    else:
        print(Fore.RED + "[+] " + Fore.WHITE + "OK nbod " + T1 + "/" + page)