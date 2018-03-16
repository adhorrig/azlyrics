Azlyrics
========

An API wrapper to programatically extract data from azlyrics.com

Installation
------------

You can easily install via ``pip``;

::

    pip install azlyrics

Or, alternatively use ``easy_install``;

::

    easy_install azlyrics

Usage
-----

Firstly, you will need to import the methods from the ``azlyrics``
module;

::

    from azlyrics import artists, songs, artists

You will then be able to use these methods as so;

::

    artists(letter)
    songs(artist)
    lyrics(song, artist)

Artists
^^^^^^^

The artists method will returns all artists associated with a letter.
For example - https://www.azlyrics.com/o.html.

.. code:: python

    print artists("o")

..

    The above method will return the following:

.. code:: json

    [
       "Oakenfold, Paul",
       "Oak Ridge Boys, The",
       "O.A.R. (Of A Revolution)",
       "Oasis",
       "Obel, Agnes",
       "Oberst, Conor",
       "Obie Trice",
       "OB O'Brien",
       "O.C. Dawgs",
       "Oceana",
       "Ocean Alley",
       "Ocean, Billy",
       "Ocean, Frank",
       "Oceanlab",
       "Ocean Park Standoff",
       "Oceans Ate Alaska",
       "Oceans Divide",
       "O'Connor, Sinead",
       "October Fall",
       "O'Day, Aubrey",
       "Odd Future Wolf Gang Kill Them All",
       "Odell, Tom",
       "Odessa",
       "ODESZA",
       "O'Donis, Colby",
       "Ofenbach",
       "OFFAIAH",
       "Off Bloom",
       "Offset",
       "Offspring, The",
       "Of Mice & Men",
       "Of Monsters And Men",
       "Of Montreal",
       "Ogie Alcasid",
       "OG Maco",
       "O\u011fuzhan Ko\u00e7",
       "Oh Hellos, The",
       "Oh Honey",
       "Ohio Players",
       "Oh Land",
       "Oh My Girl",
       "Oh, Sleeper",
       "Oh Wonder",
       "Oingo Boingo",
       "O'Jays, The",
       "OJ Da Juiceman",
       "OK Go",
       "Okkervil River",
       "Olamide",
       "Old 97's",
       "Old Crow Medicine Show",
       "Old Dominion",
       "Oldfield, Mike",
       "Ol' Dirty Bastard",
       "Oleander",
       "Oleta Adams",
       "Olexesh",
       "Oliver Heldens",
       "Olivia",
       "Olivia Holt",
       "Olivia Newton-John",
       "Olivia O'Brien",
       "Olivver The Kid",
       "Olly Murs",
       "Olsen, Angel",
       "Olsen, Steven Lee",
       "Olstead, Renee",
       "Omarion",
       "Omar, Xavier",
       "OMB Peezy",
       "OMC",
       "OMG Girlz",
       "Omi",
       "O'Neal, Jamie",
       "One Chance",
       "One Direction",
       "O'Neil, Melissa",
       "One Less Reason",
       "One Night Only",
       "ONE OK ROCK",
       "OneRepublic",
       "One Sonic Society",
       "One True Voice",
       "One Voice",
       "Ong, Daryl",
       "Only The Young",
       "Onyx",
       "Onze:20",
       "Oomph!",
       "Opeth",
       "OPM",
       "Orange & Lemons",
       "Ora, Rita"
    ]

Get Songs
^^^^^^^^^

This method returns songs for an artist.

.. code:: python

    print songs("Oasis")

..

    The above command will return the following:

.. code:: json

    {
       "albums":{
          "\"Definitely Maybe\"":[
             "Rock 'n' Roll Star",
             "Shakermaker",
             "Live Forever",
             "Up In The Sky",
             "Columbia",
             "Supersonic",
             "Bring It On Down",
             "Cigarettes & Alcohol",
             "Digsy's Diner",
             "Slide Away",
             "Married With Children",
             "Sad Song"
          ],
          "\"Dig Out Your Soul\"":[
             "(As Long As They've Got) Cigarettes In Hell",
             "(I Got) The Fever",
             "Alice",
             "Alive",
             "Angel Child",
             "Boy With The Blues",
             "Carry Us All",
             "Cloudburst",
             "Cum On Feel The Noize",
             "D'Yer Wanna Be A Spaceman",
             "Eyeball Tickler",
             "Flashbax",
             "Full On",
             "Helter Skelter",
             "Heroes",
             "I Will Believe",
             "Idler's Dream",
             "If We Shadows",
             "It's Better People",
             "Just Getting Older",
             "Let's All Make Believe",
             "My Sister Lover",
             "One Way Road",
             "Round Are Way",
             "Step Out",
             "Street Fighting Man",
             "Take Me",
             "Take Me Away",
             "The Fame",
             "Whatever",
             "You've Got To Hide Your Love Away"
          ],
          "\"Be Here Now\"":[
             "D'You Know What I Mean?",
             "My Big Mouth",
             "Magic Pie",
             "Stand By Me",
             "I Hope, I Think, I Know",
             "The Girl In The Dirty Shirt",
             "Fade In-Out",
             "Don't Go Away",
             "Be Here Now",
             "All Around The World",
             "It's Getting Better (Man!!)"
          ],
          "\"Standing On The Shoulder Of Giants\"":[
             "Fuckin' In The Bushes",
             "Go Let It Out",
             "Who Feels Love?",
             "Put Yer Money Where Yer Mouth Is",
             "Little James",
             "Gas Panic!",
             "Where Did It All Go Wrong?",
             "Sunday Morning Call",
             "I Can See A Liar",
             "Roll It Over"
          ],
          "\"Heathen Chemistry\"":[
             "The Hindu Times",
             "Force Of Nature",
             "Hung In A Bad Place",
             "Stop Crying Your Heart Out",
             "Song Bird",
             "Little By Little",
             "(Probably) All In The Mind",
             "She Is Love",
             "Born On A Different Cloud",
             "Better Man"
          ],
          "\"Don't Believe The Truth\"":[
             "Turn Up The Sun",
             "Mucky Fingers",
             "Lyla",
             "Love Like A Bomb",
             "The Importance Of Being Idle",
             "The Meaning Of Soul",
             "Guess God Thinks I'm Abel",
             "Part Of The Queue",
             "Keep The Dream Alive",
             "A Bell Will Ring",
             "Let There Be Love"
          ],
          "\"(What's The Story) Morning Glory\"":[
             "Hello",
             "Roll With It",
             "Wonderwall",
             "Don't Look Back In Anger",
             "Hey Now",
             "Some Might Say",
             "Cast No Shadow",
             "She's Electric",
             "Morning Glory",
             "Champagne Supernova",
             "Bonehead's Bank Holiday"
          ],
          "\"The Masterplan\"":[
             "Acquiesce",
             "Underneath The Sky",
             "Talk Tonight",
             "Going Nowhere",
             "Fade Away",
             "I Am The Walrus (Live)",
             "Listen Up",
             "Rockin' Chair",
             "Half The World Away",
             "(It's Good) To Be Free",
             "Stay Young",
             "Headshrinker",
             "The Masterplan"
          ]
       },
       "artist":"oasis"
    }

Get Lyrics
^^^^^^^^^^

This method returns lyrics for a song.

.. code:: python

    print lyrics("Oasis", "Magic Pie")

..

    The above command returns the following:

.. code:: json

    [u"\n\r\nAn extraordinary guy\nCan never have an ordinary day,\nHe might live a long goodbye\nBut that is not for me to say\nI dig his friends, I dig his shoes\nBut he is just a child with nothing to lose\nBut his mind \n\nThey are sleeping while they dream\nAnd then they want to be adored\nThey who don't say what they mean\nWill live and die by their own sword.\nI dig their friends, I dig their shoes\nBut they are like a child with nothing to lose\nIn their minds, their minds. \n\nBut I'll have my way\nIn my own time\nI'll have my say\nMy star will shine \n\nCos you see me I got my Magic Pie\nThink of me yeah that was me I was that passer by\nI've been and now I've gone. \n\nThere are but a thousand days preparing for a thousand years\nMany minds to educate and people who have disappeared\nD'you dig my friends? D'you dig my shoes?\nI am like a child with nothing to lose but my mind\nMy mind\n"]

Depending on your use, you may want to print line by line;

.. code:: python

    from azlyrics import lyrics
    wd = lyrics("Oasis", "Magic Pie")
    for line in wd:
        print(line)

Will be outputted as;

::

    An extraordinary guy
    Can never have an ordinary day,
    He might live a long goodbye
    But that is not for me to say
    I dig his friends, I dig his shoes
    But he is just a child with nothing to lose
    But his mind 

    They are sleeping while they dream
    And then they want to be adored
    They who don't say what they mean
    Will live and die by their own sword.
    I dig their friends, I dig their shoes
    But they are like a child with nothing to lose
    In their minds, their minds. 

    But I'll have my way
    In my own time
    I'll have my say
    My star will shine 

    Cos you see me I got my Magic Pie
    Think of me yeah that was me I was that passer by
    I've been and now I've gone. 

    There are but a thousand days preparing for a thousand years
    Many minds to educate and people who have disappeared
    D'you dig my friends? D'you dig my shoes?
    I am like a child with nothing to lose but my mind
    My mind
