---
title: "A quick word about Googlebombs | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2007/01/quick-word-about-googlebombs
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2007-01-26
---

# A quick word about Googlebombs | Google Search Central Blog | Google for Developers

Friday, January 26, 2007

We wanted to give a quick update about "Googlebombs." By improving our analysis of the link structure of the web, Google has begun minimizing the impact of many Googlebombs. Now we will typically return commentary, discussions, and articles about the Googlebombs instead. The actual scale of this change is pretty small (there are under a hundred well-known Googlebombs), but if you'd like to get more details about this topic, read on.

First off, let's back up and give some background. Unless you read all about search engines all day, you might wonder "What is a Googlebomb?" Technically, a "Googlebomb" (sometimes called a "linkbomb" since they're not specific to Google) refers to a prank where people attempt to cause someone else's site to rank for an obscure or meaningless query. Googlebombs very rarely happen for common queries, because the lack of any relevant results for that phrase is part of why a Googlebomb can work. One of the earliest Googlebombs was for the phrase "talentless hack," for example.

People have asked about how we feel about Googlebombs, and we have talked about them
[in the past](https://googleblog.blogspot.com/2005/09/googlebombing-failure.html).
Because these pranks are normally for phrases that are well off the beaten path, they haven't been
a very high priority for us. But over time, we've seen more people assume that they are Google's
opinion, or that Google has hand-coded the results for these Googlebombed queries. That's not
true, and it seemed like it was worth trying to correct that misperception. So a few of us who
work here got together and came up with an algorithm that minimizes the impact of many
Googlebombs.

The next natural question to ask is "Why doesn't Google just edit these search results by hand?"
To answer that, you need to know a little bit about how Google works. When we're faced with a bad
search result or a relevance problem, our first instinct is to look for an automatic way to solve
the problem instead of trying to fix a particular search by hand. Algorithms are great because
they scale well: computers can process lots of data very fast, and robust algorithms often work
well in many different languages. That's what we did in this case, and the extra effort to find a
good algorithm helps detect Googlebombs in many different languages. We wouldn't claim that this
change handles every prank that someone has attempted. But if you are aware of other potential
Googlebombs, we are happy to hear feedback in our
[Google Web Search Help Group](https://support.google.com/websearch/community).

Again, the impact of this new algorithm is very limited in scope and impact, but we hope that the affected queries are more relevant for searchers.
