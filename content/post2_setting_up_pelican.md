Title: Misadventures in Pelican Github Actions
Date: 2024-09-20 16:00
Category: Reflections

As mentioned in my previous post, I heard about Pelican at Kiwi PyCon. I maintain notes for myself in Markdown using [Obsidian](https://obsidian.md/), write documentation at my workplace using markdown and markdown-type shortcuts, so when I heard that Pelican could generate blog posts from Markdown, I was keen to give this a try.

When I had first learnt about Github Pages, I had attempted to wrangle together some basic html in order to slap together some kind of website, but the overhead of working both on thinking of what to put in the site and how to translate it to html had put me off the idea. On the flip side, being ablt to use a tool written in my language of choice (Python) to jot down things I've learnt in Markdown and share them without too much overhead sounded like fun.


# Requirements

In order to constrain the scope of my effort and avoid decision paralysis, I decided the following up-front. I intended to:

- Write my posts in markdown
- Use a package (in this case Pelican) to convert these posts into a static website
- Host the static website on github pages
- Use github actions to deploy the site

If I could not set the blog up by the end of the week I would try using [Hugo](https://gohugo.io/) instead.

# Process

## Local setup

I set up a new virtual environment using [venv](https://docs.python.org/3/library/venv.html) on my personal computer.

```sh
python3 -m venv blog_env
source .venv/bin/activate
```

I followed the [Quickstart](https://docs.getpelican.com/en/latest/quickstart.html) guide for Pelican.

```sh
python -m pip install "pelican[markdown]"
```

I started from the quickstart provided from the documentation and followed the prompts.
```sh
pelican-quickstart
```

I selected default answers to most questions except for the important one for deployment.

```
> Do you want to upload your website using GitHub Pages? (y/N)
```

Running the following previewed the content for the site.
```
pelican content
pelican --listen
```


I had a blank website. I created a markdown file within the content folder and ran the same commands to produce a website that worked locally.

## Deployment

As of writing, there has only been an official way to publish to GitHub pages via a Github Actions workflow for three months. Consequently, searching for the terms 'how to publish github action pelican' into my favourite browser listed what had been used for other people the most: which happened to be a maze of Github marketplace listings lead by the Github Action with the title 'Pelican to Github Pages'.

![A search result for the term 'how to publish github action pelican' in the Duckduckgo search engine displaying two search results, both linking to Github Marketplace. The first search result is labelled 'Pelican to Github Pages' and links to six different implementations of custom Github Actions. The second result is a link to a different github action also on Marketplace](images/search_results.PNG)

As I had not been pointed to any official seeming documentation through my usage of the search engine, I started trying the various Github Actions. They successfully setup my site, however the blog posts were all missing.

It turns out that the missing piece was that a good majority of these custom, undocumented Github Actions weren't necessarily handling or documenting for my specific usecase - to be able to convert markdown pages into html.

The page that saved me in the end was [this example repo](https://github.com/seanh/ghp-pelican-demo) where the usage of the action was explicitly shown for the scenario I was after - for 1000s of markdown files.

The missing line turned out to be to install `pelican[markdown]` rather than just pelican.

# Reflections

In the end, it turned out that the difference between Duckduckgo and Google's search algorithm and the way the pages had ranked within their separate algorithsm had a significant impact on how long it took to successfully use the github action.

In DuckDuckGo, it wasn't until the 9th search result that I was linked to official documentation, whereas for Google this was the third result.

![A google search result for 'how to publish github action pelican'. The first link is to the implementation and documentation of a Github Action. Unlike the search in DuckDuckGo, there is a link to the official documentation guidance as the third search result.](images/google_search.PNG)

If I were to do this again, I would search within the Pelican documentation more thoroughly first, but this was certainly a wake up call for how reliant I, as a software developer, am on the results that are output from search engines.


## Useful links

- [Original github action](https://github.com/seanh/ghp-pelican) (since merged into Pelican)
- [Demo repo](https://github.com/seanh/ghp-pelican-demo) for how to use the Pelican github action
- [How to publish to Github Pages Using a Custom Github Actions Workflow](https://docs.getpelican.com/en/latest/tips.html#publishing-to-github-pages-using-a-custom-github-actions-workflow) - advice from official docs
