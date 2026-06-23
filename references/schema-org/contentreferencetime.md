---
title: "contentReferenceTime"
source_url: https://schema.org/contentReferenceTime
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2016-03-21
---

# contentReferenceTime

# contentReferenceTime

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/contentReferenceTime
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+contentReferenceTime)

The specific time described by a creative work, for works (e.g. articles, video objects etc.) that emphasise a particular moment within an Event.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/1050](https://github.com/schemaorg/schemaorg/issues/1050)

### Examples

[Example 1](#eg-0228)

Copied

Example notes or example HTML without markup.

A JSON example for an Article about a particular event.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Article", "name": "Apple announces iPhone SE", "description": "New iPhone announced at 11:30 in California.", "about": { "@type": "Event", "name": "Apple's March 21 Announcements" }, "contentReferenceTime": "2016-03-21T11:30:00-07:00" } </script>

Structured representation of the JSON-LD example.
