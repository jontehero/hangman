"""Hänga gubben för två spelare i terminalen."""
"""          
git add hangman.py
git commit -m "Funktion 5 : Felaktiga gissningar"
git push                                        """
"KONSTANTER"
MAX_FEL = 6
GUBBE_STEG = ["0 fel", "1 fel", "2 fel", "3 fel", "4 fel", "5 fel", "6 fel"]

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


def correct_procent(antal_ratt, antal_gissningar):
    
    if antal_gissningar > 0:   
        procent = antal_ratt / antal_gissningar * 100 
        return round(procent)
    elif antal_gissningar < 1:
        return 0

def visa_gubbe(fel):
    return GUBBE_STEG[fel]







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
assert correct_procent(0, 0) == 0
assert correct_procent(3, 3) == 100
assert correct_procent(3, 4) == 75
assert len(GUBBE_STEG) == 7
assert visa_gubbe(0) == GUBBE_STEG[0]
assert visa_gubbe(6) == GUBBE_STEG[6]





# spela()   # aktiveras på dag 3