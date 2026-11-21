"""Hänga gubben för två spelare i terminalen."""

MAX_FEL = 6
GUBBE_STEG = []   # ritas på dag 2

# --- FUNKTIONER ---

def normalisera(text):
    normal = text.lower().strip()
    return normal
    
    """
    .lower() / .strip()

    """

#-------------------------------------



# --- TESTER ---
assert normalisera("  KaTt ") == "katt"

# spela()   # aktiveras på dag 3