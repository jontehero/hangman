"""Hänga gubben för två spelare i terminalen."""
"""git add hangman.py
git commit -m "Funktion 2: ar_giltigt_ord"
git push"""



MAX_FEL = 6
GUBBE_STEG = []   # ritas på dag 2

# --- FUNKTIONER ---

def normalisera(text):
    """
    .lower() / .strip()

    """
    normal = text.lower().strip()
    return normal
#-------------------------------------
def ar_giltigt_ord(text):
   allowed = "abcdefghijklmnopqrstuvwxyzåäö"
   if len(text) >= 2 and all (c in allowed for c in text):
       return True
   else: return False

def ar_en_bokstav(text):
    allowed = "abcdefghijklmnopqrstuvwxyzåäö"
    if len(text) == 1 and all (c in allowed for c in text):
        return True
    else: return False





# --- TESTER ---
assert normalisera("  KaTt ") == "katt"
assert ar_giltigt_ord("text") 
assert not ar_giltigt_ord("o")
assert not ar_giltigt_ord("hej0")
assert ar_en_bokstav("a")
assert not ar_en_bokstav("")
assert not ar_en_bokstav("ab")
assert not ar_en_bokstav("1")
# spela()   # aktiveras på dag 3