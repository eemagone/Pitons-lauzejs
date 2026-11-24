import getpass
import hashlib
import urllib.error
import urllib.request

""" Returnable dict examples:
# leaked
{"statuss": "noplucis", "skaits": 123, "kluda": None}

# not found
{"statuss": "nav_atrasts", "skaits": 0, "kluda": None}

# lookup failed (offline, timeout, junk response)
{"statuss": "nav_zinams", "skaits": None, "kluda": "<urlopen error ...>"}
"""

HIBP_URL = "https://api.pwnedpasswords.com/range/"
TIMEOUT = 5

def parbaudi_hibp(parole, url=HIBP_URL):
    hash_pilns = hashlib.sha1(parole.encode("utf-8")).hexdigest().upper()
    
    prefikss = hash_pilns[:5]
    sufikss = hash_pilns[5:]

    pieprasijums = urllib.request.Request(
        url + prefikss,
        headers={"Add-Padding": "true", "User-Agent": "paroles-analizators"},
    )
    try:
        with urllib.request.urlopen(pieprasijums, timeout=TIMEOUT) as atbilde:
            teksts = atbilde.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError, UnicodeDecodeError) as kluda:
        return {"statuss": "nav_zinams", "skaits": None, "kluda": str(kluda)}

    atrasts = 0
    for rinda in teksts.splitlines():

        dalas = rinda.strip().split(":")
        if len(dalas) != 2 or len(dalas[0]) != 35 or not dalas[1].isdigit():
            return {"statuss": "nav_zinams", "skaits": None, "kluda": "neparedzeta atbilde"}
        if dalas[0].upper() == sufikss:
            atrasts = int(dalas[1])
        """
        1E4C9B93F3F0682250B6CF8331B7EE68FD8:123
        dalas[0]=1E4C9B93F3F0682250B6CF8331B7EE68FD8
        dalas[1]=123
        """
    if atrasts > 0:
        return {"statuss": "noplucis", "skaits": atrasts, "kluda": None}
    return {"statuss": "nav_atrasts", "skaits": 0, "kluda": None}


if __name__ == "__main__":
    print(parbaudi_hibp(getpass.getpass("Ievadi paroli: ")))
