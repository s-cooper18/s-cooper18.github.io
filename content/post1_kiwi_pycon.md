Title: Kiwi PyCon XIII and Using the Momentum to Start a Blog 
Date: 2024-08-29 10:20
Category: Reflections

I went to [Kiwi PyCon](https://kiwipycon.nz/) last week. In the Lightning Talk sessions on Sunday, one of the speakers mentioned how they had created a blog about their particular interest using [Pelican](https://getpelican.com/). I recall that their static website looked beautifully formatted and was impressively handled using Python. I wrote down the name of the framework and something about pandoc and 'can make fancy looking drop caps'.

As I returned home from Wellington, I had developed a haphazard list of notes stored on my phone about my learnings and thoughts from Kiwi PyCon. I wanted to organise and collate these thoughts into something I could revisit later once I had lost the context of what cryptic single line thoughts I had written down and link back to the videos from the conference once they were available. So here we are: two birds with one stone, using something I learnt from Kiwi PyCon to note down things that I learnt at Kiwi PyCon.

# Notes and Thoughts from PyCon

## Communication

- Everything (documentation) should be available in one place and if not in one place, should link to each other.
- The word and concept of [diátaxis](https://diataxis.fr/)
- In the context of public speaking, do not make assumptions about what your audience knows or put in-jokes / old memes into your slides. (I still don't know what [banana water](https://www.heb.com/product-detail/elmhurst-naturals-banana-water-original/1978140) has to do with cybersecurity)
- For presentations: focus on what your one point or takeaway should be.

## Engineering
- Release notes are an easy way to thank and acknowledge the people who have given their time along the way, especially if they did not have to as part of their job or it was in a volunteer or open source capacity

- An interface is a concept in fiber arts. A definition for an interface is: "A surface forming a common boundary between adjacent regions, bodies, substances, or phases" ([wordnik](https://www.wordnik.com/words/interface)). There are numerous other parallels between fiber arts, especially given the context of the first computer programs being inspired by Jaquard looms.


### Testing
- Mocks are like border controls for your code to ensure that you aren't testing anything other than the main purpose of the test.

- The difference between Fail Safe (default state is unlocked) and Fail Secure (default state is locked), can be disastrous in the context of a [runaway train](https://www.atsb.gov.au/publications/investigation_reports/2003/rair/rair2003001).

- Adding notes or constructing assertions in a way to allow notes on them can aid in readability rather than having a cryptic failure because 0 = 1 is false.

### Security

- [Reserved domains](https://www.iana.org/domains/reserved) are those that are set aside and cannot be transferred. One example of this is example.com. Registering other common domains (as per one of the lightning talks) that sound similar but are not actually reserved can yield some mildly horrifying results.

- The [OWASP Top Ten](https://owasp.org/www-project-top-ten/) demonstrates the most critical security risks to web applications. Burp suite and a locally hosted insecure flask application can demonstrate the kinds of chaos that can occur when things are not set up appropriately.

- There exist ways of [exploiting Django ORM](https://www.elttam.com/blog/plormbing-your-django-orm/) to leak data (and is relatively recent research too).


## Python

- Pythons many uses in addition to web applications, APIs and data analysis also includes [programming](https://micropython.org/) [microcontrollers](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html) and writing [native apps](https://beeware.org/). (I wish that I could time travel and teach embedded programming using Python instead)
- The Python 2 to 3 migration gave little incentive for organisations to stick with Python, given it would not be that much harder to change to a different programming language (e.g. possibly backstory for why Javascript is dominant on the web).

### Language Details
- Immutable python objects are not actually immutable in the traditional programming language sense. There is a small amount of mutable state used for reference counting. [Immortal objects](https://peps.python.org/pep-0683/) are true immutable objects in that they do not have a mutable refcount.
- The removal (or at least non-enforcement) of the Global Interpreter Lock in Python could be a possible split or death of the Python community if it is handled badly, so much so that an exit clause is included in the [PEP703](https://peps.python.org/pep-0703/) to allow for it to be rolled back if necessary.
- There also exists a proposal ([PEP683](https://peps.python.org/pep-0683/)) to allow a per interpretor Global Interpreter Lock, building upon the benefits of immortal objects.



