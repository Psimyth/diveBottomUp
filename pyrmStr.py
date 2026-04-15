# Pyrm string
# Bottom up dive search

def bottom_up_word_search(haystack, needle, x=0):
    # BASE CASE: The "Floor" (End of the string)
    if x > len(haystack) - len(needle):
        # We stop diving when there isn't enough string left to fit the needle
        return []

    # 1. THE DIVE: Move to the next "depth"
    # This keeps going until it hits the base case above.
    found_indices = bottom_up_word_search(haystack, needle, x + 1)

    # 2. THE BOTTOM-UP ACTION: Check for the word during the recoil
    # We are now moving BACKWARDS from the end of the string to the start.
    current_slice = haystack[x : x + len(needle)]
    
    if current_slice == needle:
        print(f"  [RECOIL] Match found at index {x}!")
        found_indices.append(x)
    else:
        print(f"  [RECOIL] Checking index {x} ('{haystack[x]}')... No match.")

    return found_indices

# --- Execution ---
text_to_search = "FIND THE CAT IN THE CATERPILLAR"
word_to_find = "CAT"

print(f"Searching for '{word_to_find}' bottom-up...\n")
results = bottom_up_word_search(text_to_search, word_to_find)

print(f"\nSearch Complete. Found {len(results)} matches at indices: {results}")
