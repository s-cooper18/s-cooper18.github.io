Title: PyCon AU 2024 Day 1
Date: 2024-11-27
Category: Reflections

Last weekend I went to my first [PyCon AU](https://2024.pycon.org.au/). The only other Python conference I had been to before was this year's [Kiwi PyCon](https://kiwipycon.nz/), which I had an excellent time at. My main observation of the difference between these was the sheer size of the event! Kiwi PyCon was across two days of the main event and had workshops on the Friday before. PyCon AU had three concurrent talks for most of the conference, excluding keynotes and lightning talks, across three days. My speaker ticket came with the Friday, Saturday and Sunday, so I was there for a full three days.

There were many bits and bobs that I enjoyed at PyCon AU 2024 - so in an effort to preserve these, I am putting in some of the highlights and notes I took from the event.

# Day 1

The first day of PyCon AU 2024 was the specialist track. There were three tracks on Scientific Python, 'DevOops' and Education. I floated between the DevOops and Education tracks, but I've already gone back to watch a couple of talks from the Science track.

## Technical

### ["Why UUIDs are Secretly Incredibly Facinating" - Tom Eastman](https://www.youtube.com/watch?v=n9Cxs0sTqEY)
There are multiple types of uuids. I had an inkling of this, but had never seen anything other than UUID version 4 being used. One of my scribbled notes during the talk state that: "UUID versions 4, 5, 7, 8 may be useful". UUID version 4 consists of completely random data, for better or worse. One of the problems with this is that there's no indication of ordering that can be obtained based on UUID version 4.

UUID version 1 contains the mac address from the node id (for better or worse) and uses Gregorian time as the timestamp. Version 5 is non random based on an input string and namespace. Version 7 goes up over time with the timestamp at the front, which can be good for database indexes. Meanwhile, Version 8 is roll your own UUID!

### ["Coding Competition vs Murphy's Law - Sanjin Dedic"](https://www.youtube.com/watch?v=GhwYsMxbvkQ&list=PLs4CJRBY5F1Jn7fWZyMgogpPsu1vAZKB2&index=23)
- Thoroughly recommend this talk - this was one of my favourites.
- Students taking the Victorian Coding Challenge seemed to always find new ways to break the coding platform and I thoroughly enjoyed the journey in this talk.
- [Locust](https://locust.io/) is an example of a load testing framework

### Misc learnings
- ["Django on AWS for chump change" - Luke Wiwatowski](https://www.youtube.com/watch?v=A58FxdvHcmQ&list=PLs4CJRBY5F1Jn7fWZyMgogpPsu1vAZKB2&index=12)
    - Spot instances of AWS are cheaper
    - You pay for the NAT instance, but also traffic that goes through it
    - "Theoretically" you could just get away with using a postgres container instead of AWS RDS (not recommended)
    - The speaker managed to string together a functioning project for only a few cents a month. I recall using Heroku's free tier to host my (very trash, poorly performing) deep learning model side project. I may need to look into what the options are nowadays.
- There exists a way to store your database in S3 if you are really a cheapskate - have a look at [Django SQlite Object Storage](https://github.com/lukewiwa/django_sqlite_object_storage). I'm curious about how the database in S3 actually works so may have a little poke around.
- There exist tools to generate pipelines for Gitlab using Python
- "A Lazy Person's Guide to Building REST Client or How I Learned to Stop Worrying and Love Dunder Overrides" - Ash Bek
    - The dunder methods `__getattr__` and `__getattribute__` are different methods
    - It's usually `__getattr__` that you want to implement.


## Education

### Transitioning from VB to Python - Mapping a 6 month journey
I was mainly thinking about how the extent of computer subjects that we did when I was back at school was a "how to use Excel", so I'm impressed that they were even using Visual Basic. That said, as someone whose first language in a work environment was ~technically~ Visual Basic, that's certainly not something I would recommend. I'm excited for schools to be hitting the ground running with Python, but then I realised schools weren't really doing this just for fun. I've been out of the loop long enough for it to only occur to me during this talk that the national curriculum is requiring that schools have some kind of programming component now.


### Student talks
- [Pyflagoras](https://github.com/phthallo/pyflagoras) - a command line interface for theming one image with the colour palette of another.
    - The original usecase was to change the colour palette of a Pride Flag with the colours of Celeste (niche meme)
    - Author said they couldn't think of many applications beyond her initial application idea, but the discord began chiming in with other potential applications. My favourite suggestions were the ones for using a colour blind friendly palette in order to map non-colour blind friendly plots into something that colour blind folks can actually see. I would be tempted to do something where you can screenshot the email an inconsiderate coworker sent in green and red highlights in order to convert it to a better palette, but would need to research whether there's a simpler way to do this first.

## Science
### ["How I used Python to Stop Worrying and Love Emoji in Bioinformatics" - Andrew Lonsday](https://www.youtube.com/watch?v=E3-AooF8e2k&list=PLs4CJRBY5F1Jn7fWZyMgogpPsu1vAZKB2&index=27)
I didn't actually go to any of the science track talks on the day, however, one of the first talks to go up was "How I used Python to Stop Worrying and Love Emoji in Bioinformatics". Despite this naming theme getting stale quickly, I really enjoyed this one.
- The speaker created a tool called [FASTQE](https://github.com/fastqe/fastqe) that would convert the quality of reads from arbitrary symbols to being in emojis, which made it a lot easier to quickly understand the quality of bioinformatics data, but also made it more interesting for students that were learning about the tools.
- [Biomojify](https://github.com/fastqe/biomojify) is the speaker's follow-up project which maps the data contained in FASTA, FASTQ or VCF files into emojis.
- I dabbled in bioinformatics related things when I was a student and found the software side of it really fascinating (I also learned that I preferred Software Engineering to research at that point). The speaker made a call to action at the end about being interested in more contributers which I took interest in.