---
title: "sharedContent"
source_url: https://schema.org/sharedContent
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# sharedContent

# sharedContent

A Schema.org Property

- Canonical URL: https://schema.org/sharedContent
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+sharedContent)

A CreativeWork such as an image, video, or audio clip shared as part of this posting.

### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0423)

Copied

Example notes or example HTML without markup.

<h1>Leaked new BMW 2 series (m235i)</h1> <p>Date posted: March 4, 2014</p> <p>Author: <a href="https://www.pinterest.com/ryansammy/">Ryan Sammy</a></p> <p> <b><a href="http://www.reddit.com/r/BMW/comments/1oyh6j/leaked_new_bmw_2_series_m235i_ahead_of_oct_25/"> Leaked new BMW 2 series (m235i) ahead of oct 25 reveal</a></b> </p> <p>Author: threal135i</p>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemid="https://www.pinterest.com/pin/201887995769400347/" itemscope itemtype="https://schema.org/SocialMediaPosting"> <h1 itemprop="headline">Leaked new BMW 2 series (m235i)</h1> <p>Date posted: March 4, 2014 <meta itemprop="datePublished" content="2014-03-04" /></p> <p>Author: <span itemprop="author" itemscope itemtype="https://schema.org/Person"> <span itemprop="name"> <a itemprop="url" href="https://www.pinterest.com/ryansammy/">Ryan Sammy</a></span> </span> </p> <div itemprop="sharedContent" itemscope itemtype="https://schema.org/WebPage"> <p> <b itemprop="headline"><a itemprop="url" href="http://www.reddit.com/r/BMW/comments/1oyh6j/leaked_new_bmw_2_series_m235i_ahead_of_oct_25/"> Leaked new BMW 2 series (m235i) ahead of oct 25 reveal</a></b> </p> <p>Author: <span itemprop="author" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">threal135i</span> </span> </p> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="SocialMediaPosting" resource="https://www.pinterest.com/pin/201887995769400347/"> <h1 property="headline">Leaked new BMW 2 series (m235i)</h1> <p>Date posted: March 4, 2014 <meta property="datePublished" content="2014-03-04" /></p> <p>Author: <span property="author" typeof="Person"> <span property="name"> <a property="url" href="https://www.pinterest.com/ryansammy/">Ryan Sammy</a></span> </span> </p> <div property="sharedContent" typeof="WebPage"> <p> <b property="headline"><a property="url" href="http://www.reddit.com/r/BMW/comments/1oyh6j/leaked_new_bmw_2_series_m235i_ahead_of_oct_25/"> Leaked new BMW 2 series (m235i) ahead of oct 25 reveal</a></b> </p> <p>Author: <span property="author" typeof="Person"> <span property="name">threal135i</span> </span> </p> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"SocialMediaPosting", "@id":"https://www.pinterest.com/pin/201887995769400347/", "datePublished":"2014-03-04", "author":{ "@type":"Person", "name":"Ryan Sammy", "url":"https://www.pinterest.com/ryansammy/" }, "headline":"Leaked new BMW 2 series (m235i)", "sharedContent":{ "@type":"WebPage", "headline":"Leaked new BMW 2 series (m235i) ahead of oct 25 reveal", "url":"http://www.reddit.com/r/BMW/comments/1oyh6j/leaked_new_bmw_2_series_m235i_ahead_of_oct_25/", "author":{ "@type":"Person", "name":"threal135i" } } } </script>

Structured representation of the JSON-LD example.
