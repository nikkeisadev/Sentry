import hashlib
sublogo = """
                                                  
 _____ _                 _    _____     _         
|   __| |_ ___ ___ ___ _| |  |  |  |___| |_ _ ___ 
|__   |   | .'|  _| -_| . |  |  |  | .'| | | | -_|
|_____|_|_|__,|_| |___|___|   \___/|__,|_|___|___|

<= Generate Shared Values as hashed hexdigest! =>
           Made with love, by: Nikke.

"""
print(sublogo)
def main():
    getInput = input("[EMPTUM][SHARED_VALUE_HASHING]> Please define the Shared Value: ")
    genSharedValueHash = hashlib.sha256(bytes(getInput, encoding="utf-8")).hexdigest()
    print(f"[EMPTUM][SHARED_VALUE_HASHING]> Shared Value: {genSharedValueHash}")
    main()
main()