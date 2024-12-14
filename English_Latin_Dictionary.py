def create_latin_english_dictionary():
    # Step 1: Read the number of English words in the dictionary
    n = int(input("Enter the number of English words in the dictionary: ").strip())

    # Step 2: Initialize a dictionary to store the English-Latin dictionary
    english_to_latin = {}

    # Step 3: Read the English-Latin dictionary entries
    for _ in range(n):
        # Example input: "apple - malum, pomum, popula"
        entry = input("Enter the English word and its Latin translations: ").strip()

        # Split the entry into English word and Latin translations
        english_word, latin_words = entry.split(" - ")

        # Split the Latin translations into a list and store them in the dictionary
        english_to_latin[english_word] = latin_words.split(", ")

    # Step 4: Initialize a dictionary for the Latin-English dictionary
    latin_to_english = {}

    # Step 5: Reverse the English-Latin dictionary into Latin-English
    for english_word, latin_words in english_to_latin.items():
        for latin_word in latin_words:
            # If the Latin word is not already in the dictionary, initialize it with an empty list
            if latin_word not in latin_to_english:
                latin_to_english[latin_word] = []

            # Add the English word to the list of translations for the Latin word
            latin_to_english[latin_word].append(english_word)

    # Step 6: Sort the Latin-English dictionary for the output
    sorted_latin_words = sorted(latin_to_english.keys())  # Sort Latin words alphabetically

    # Step 7: Print the Latin-English dictionary
    for latin_word in sorted_latin_words:
        # Sort the English translations alphabetically
        english_translations = sorted(latin_to_english[latin_word])

        # Print the Latin word followed by its English translations
        print(f"{latin_word} - {', '.join(english_translations)}")

# Call the function to execute the program
create_latin_english_dictionary()