---
title: "actor"
source_url: https://schema.org/actor
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# actor

# actor

A Schema.org Property

- Canonical URL: https://schema.org/actor
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+actor)

An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.

### Values expected to be one of these types


### Used on these types


#### Sub-properties

| Supersedes |
|---|
```
``` |

### Examples

[Example 1](#eg-0205)

Copied

Example notes or example HTML without markup.

A JSON example of a PerformanceRole, in which the Role represents the acting contribution made by Bill Murray in the film Ghostbusters. The Role entity allows us to additional information, such as the character's name that he played in the film.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Movie"> <span itemprop="name">Ghostbusters</span> <link itemprop="sameAs" href="http://en.wikipedia.org/wiki/Ghostbusters"/> <div itemprop="actor" itemscope itemtype="https://schema.org/PerformanceRole"> <div itemprop="actor" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Bill Murray</span> </div> <span itemprop="characterName">Dr. Peter Venkman</span> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Movie"> <span property="name">Ghostbusters</span> <link property="sameAs" href="http://en.wikipedia.org/wiki/Ghostbusters"/> <div property="actor" typeof="PerformanceRole"> <div property="actor" typeof="Person"> <span property="name">Bill Murray</span> </div> <span property="characterName">Dr. Peter Venkman</span> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Movie", "name": "Ghostbusters", "sameAs": "http://en.wikipedia.org/wiki/Ghostbusters", "actor": { "@type": "PerformanceRole", "actor": { "@type": "Person", "name": "Bill Murray" }, "characterName": "Dr. Peter Venkman" } } </script>

Structured representation of the JSON-LD example.
