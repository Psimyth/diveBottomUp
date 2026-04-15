# Searches a character inside a string
# Bottom up dive

def recursive_string_search(text, target, x=0):
    # BASE CASE: The "Floor" of the dive (End of the string)
    if x >= len(text):
        print(f"Reached the bottom (index {x}). Starting recoil...")
        return False

    # 1. THE DIVE: Keep going deeper until we hit the end
    # We increment x (height/depth) just like your pseudo-code
    found_in_deeper_layers = recursive_string_search(text, target, x + 1)

    # 2. THE BOTTOM-UP ACTION: Check characters as we move BACKWARD
    current_char = text[x]
    is_match = current_char == target
    
    if is_match:
        print(f"  [RECOIL] Found '{target}' at index {x}!")
    else:
        print(f"  [RECOIL] Passing index {x} ('{current_char}')...")

    # Return True if found here OR found in a deeper layer
    return is_match or found_in_deeper_layers

# --- Execution ---
search_text = "GEMINI"
target_char = "E"

print(f"Searching for '{target_char}' in '{search_text}' bottom-up:\n")
found = recursive_string_search(search_text, target_char)
print(f"\nSearch Complete. Result: {'Found' if found else 'Not Found'}")
