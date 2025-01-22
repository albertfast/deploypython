from rich import print

shrek_info = {
    "title": "Shrek",
    "release_date": "May 18, 2001",
    "genre": ["Animation", "Comedy", "Fantasy", "Adventure"],
    "directors": ["Andrew Adamson", "Vicky Jenson"],
    "producers": ["Jeffrey Katzenberg", "Aron Warner", "John H. Williams"],
    "production_company": "DreamWorks Animation",
    "runtime_minutes": 90,
    "budget": "$60 million",
    "box_office": "$487 million",
    "awards": {
        "academy_awards": {
            "wins": 1,
            "categories": ["Best Animated Feature"]
        },
        "golden_globe_awards": {
            "nominations": 1,
            "categories": ["Best Motion Picture – Musical or Comedy"]
        }
    },
    "main_characters": {
        "Shrek": {
            "voice_actor": "Mike Myers",
            "description": "An ogre who values his solitude but goes on a quest to save Princess Fiona."
        },
        "Donkey": {
            "voice_actor": "Eddie Murphy",
            "description": "A talkative and humorous donkey who becomes Shrek's loyal companion."
        },
        "Princess Fiona": {
            "voice_actor": "Cameron Diaz",
            "description": "A princess with a secret curse, waiting to be rescued by her true love."
        },
        "Lord Farquaad": {
            "voice_actor": "John Lithgow",
            "description": "The diminutive ruler of Duloc who seeks to marry Fiona to become king."
        }
    },
    "plot_summary": (
        "Shrek, an ogre, lives a solitary life in a swamp until his peace is disturbed by fairy tale "
        "creatures banished by Lord Farquaad. To regain his solitude, Shrek agrees to rescue Princess Fiona "
        "for Farquaad, but discovers Fiona's secret and learns the value of love and friendship along the way."
    ),
    "soundtrack": {
        "notable_songs": [
            "All Star - Smash Mouth",
            "Hallelujah - Rufus Wainwright",
            "I'm a Believer - Smash Mouth"
        ],
        "composer": "Harry Gregson-Williams and John Powell"
    },
    "cultural_impact": {
        "memes": [
            "Shrek is love, Shrek is life",
            "Somebody once told me...",
            "Get out of my swamp!"
        ],
        "spin-offs_and_sequels": [
            "Shrek 2 (2004)",
            "Shrek the Third (2007)",
            "Shrek Forever After (2010)",
            "Puss in Boots (2011)"
        ],
        "broadway_musical": {
            "title": "Shrek the Musical",
            "premiere_year": 2008,
            "notable_songs": ["Who I'd Be", "I Know It's Today", "Big Bright Beautiful World"]
        },
        "theme_parks": ["Universal Studios attractions themed around Shrek."]
    },
    "animation_technique": {
        "innovations": [
            "First film to win the Academy Award for Best Animated Feature.",
            "Use of state-of-the-art CGI to create realistic textures and facial expressions.",
            "Extensive motion capture for character movements."
        ]
    },
    "voice_cast": {
        "Mike Myers": "Shrek",
        "Eddie Murphy": "Donkey",
        "Cameron Diaz": "Princess Fiona",
        "John Lithgow": "Lord Farquaad"
    },
    "quotes": [
        "What are you doing in my swamp?!",
        "Ogres are like onions.",
        "You might have seen a housefly, maybe even a superfly, but I bet you ain't never seen a donkey fly!",
        "Somebody once told me..."
    ]
}

print(shrek_info)