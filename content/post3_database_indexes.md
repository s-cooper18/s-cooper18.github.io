Title: Postgres Indexes and Parallels to Books
Date: 2024-11-10 14:00
Category: Database

I've slowly working my way through [Postgres 14 Internals by Egor Rogov](https://postgrespro.com/community/books/internals) in order to finish filling in the gaps on content for my upcoming Pycon AU talk on Database Indexes. The book is quite dense and requires some prerequisite knowledge of definitions and database concepts. Here, I hope to break down some of these ideas about how postgres behaves from a higher level (with links to understand more deeply).

## Why is an Index?
The simplest explanation of why we add indexes to databases draws paralells to books. You have some kind of topic you are interested in from your dense textbook, say frogs. Representing our query in SQL this could look something like below.

```SQL
SELECT *
FROM my_favourite_book
WHERE topic = 'frogs'
LIMIT 1
```

One way is to read through page by page until you find relevant information. Once you find a page that is about frogs, you stop and have your information.

What if we are interested in all the instances of information about frogs in our book?

```SQL
SELECT *
FROM my_favourite_book
WHERE topic = 'frogs'
```

We could continue reading through the entire book and ignore any information that is not relevant to frogs.

I'm a fan of reading, but wouldn't quite be a fan of this method of searching a book. This is where indexes become useful. What if, our book, like most well designed textbooks, has an index at the back. We could look at the entry for frogs and easily find all the entries in our book that are related to frogs.

```
F
fire 14
flamethrowers 134-140
frogs 11, 212-214, 400
...
```

We could instead navigate to the letter 'F' in our book index and look through the index until we find the entry for frogs. We don't need to look through the book itself in order to determine if the page is about frogs, which is much less intensive on our brains.

Database indexes have a similar purpose. They can be incredibly useful in speeding up data access by eliminating the need to fetch data we don't care about from the table itself.