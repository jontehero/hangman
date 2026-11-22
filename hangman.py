"""Hänga gubben för två spelare i terminalen."""
"""          
git add hangman.py
git commit -m "Funktion 5 : Felaktiga gissningar"
git push                                        """

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

def visa_ord(hemligt_ord, gissade):
    resultat = []
    for bokstav in hemligt_ord:
      
        if bokstav in gissade:
            resultat.append(bokstav)
        else:
            resultat.append("_")
        
    return " ".join(resultat)

def felaktiga_gissningar(hemligt_ord, gissade):
    felaktiga = []
    for bokstav in gissade:
        if not bokstav in hemligt_ord:
             felaktiga.append(bokstav)
    return felaktiga

def har_vunnit(hemligt_ord, gissade):
    for bokstav in hemligt_ord:
        if bokstav not in gissade:
            return False
    return True






# --- TESTER ---
assert normalisera("  KaTt ") == "katt"
assert ar_giltigt_ord("text") 
assert not ar_giltigt_ord("o")
assert not ar_giltigt_ord("hej0")
assert ar_en_bokstav("a")
assert not ar_en_bokstav("")
assert not ar_en_bokstav("ab")
assert not ar_en_bokstav("1")
assert visa_ord("katt",["k", "t"])=="k _ t t"
assert visa_ord("katt", []) == "_ _ _ _"
assert felaktiga_gissningar("katt", ["k", "x", "t", "z"]) == ["x","z"]
assert har_vunnit("katt", ["k", "a", "t"])
assert not har_vunnit("katt", ["k", "t"])


# spela()   # aktiveras på dag 3