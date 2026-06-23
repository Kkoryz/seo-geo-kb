---
title: "about"
source_url: https://schema.org/about
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2016-03-21
---

# about

# about

A Schema.org Property

- Canonical URL: https://schema.org/about
- Equivalent Property: dcterms:subject
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+about)

The subject matter of an object.

Inverse-property:
[subjectOf](/subjectOf)

### Values expected to be one of these types


### Used on these types


#### Sub-properties

#### Source

[https://github.com/schemaorg/schemaorg/issues/1670](https://github.com/schemaorg/schemaorg/issues/1670)

[https://github.com/schemaorg/schemaorg/issues/4588](https://github.com/schemaorg/schemaorg/issues/4588)

### Examples

[Example 1](#eg-0228)

Copied

Example notes or example HTML without markup.

A JSON example for an Article about a particular event.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Article", "name": "Apple announces iPhone SE", "description": "New iPhone announced at 11:30 in California.", "about": { "@type": "Event", "name": "Apple's March 21 Announcements" }, "contentReferenceTime": "2016-03-21T11:30:00-07:00" } </script>

Structured representation of the JSON-LD example.
