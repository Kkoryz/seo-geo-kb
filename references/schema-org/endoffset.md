---
title: "endOffset"
source_url: https://schema.org/endOffset
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# endOffset

# endOffset

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/endOffset
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+endOffset)

The end time of the clip expressed as the number of seconds from the beginning of the work.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2021](https://github.com/schemaorg/schemaorg/issues/2021)

### Examples

[Example 1](#eg-0267)

Copied

Example notes or example HTML without markup.

A Clip from a longer video.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "VideoObject", "name": "Cat video", "duration": "P10M", "hasPart": { "@type": "Clip", "name": "Segment where cat jumps", "startOffset": 30, "endOffset": 45 } } </script>

Structured representation of the JSON-LD example.
