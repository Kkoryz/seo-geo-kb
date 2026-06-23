---
title: "accessModeSufficient"
source_url: https://schema.org/accessModeSufficient
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# accessModeSufficient

# accessModeSufficient

A Schema.org Property

- Canonical URL: https://schema.org/accessModeSufficient
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+accessModeSufficient)

A list of single or combined access modes that are sufficient to understand all the intellectual content of a resource, including any adaptations. Values should be drawn from the

[approved vocabulary](https://www.w3.org/2021/a11y-discov-vocab/latest/#accessModeSufficient-vocabulary).### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/1100](https://github.com/schemaorg/schemaorg/issues/1100)

### Examples

[Example 1](#eg-0321)

Copied

Example notes or example HTML without markup.

A graphic novel book example. See also https://github.com/daisy/epub-revision-a11y/wiki/ePub-3.1-Accessibility--Proposal-To-Schema.org

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Book", "name": "Some graphic novel", "accessMode": ["textual", "visual"], "accessModeSufficient": [ { "@type": "ItemList", "itemListElement": ["textual", "visual"], "description": "Text and images" }, { "@type": "ItemList", "itemListElement": ["textual"], "description": "Text with textual alternatives and descriptions for images" } ], "accessibilitySummary": "Visual elements are not described." } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0322)

Copied

Example notes or example HTML without markup.

A second example. See also https://github.com/daisy/epub-revision-a11y/wiki/ePub-3.1-Accessibility--Proposal-To-Schema.org

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "Movie", "accessMode": ["auditory", "visual"], "accessibilityFeature": ["audioDescription", "captions"], "accessModeSufficient": [ { "@type": "ItemList", "itemListElement": ["textual", "visual"], "description": "Closed captioning" }, { "@type": "ItemList", "itemListElement": ["auditory"], "description": "Audio description" } ], "accessibilitySummary": "Captions provided in English; short scenes in French have English subtitles instead." }

Structured representation of the JSON-LD example.

[Example 3](#eg-0323)

Copied

Example notes or example HTML without markup.

A third example. See also https://github.com/daisy/epub-revision-a11y/wiki/ePub-3.1-Accessibility--Proposal-To-Schema.org

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "Book", "name": "Alice in Wonderland", "accessMode": ["auditory", "textual", "visual"], "accessibilityFeature": ["alternativeText", "synchronizedAudioText"], "accessModeSufficient": [ { "@type": "ItemList", "itemListElement": ["textual"], "description": "See the text" }, { "@type": "ItemList", "itemListElement": ["textual", "visual"], "description": "See the text and images" }, { "@type": "ItemList", "itemListElement": ["auditory"], "description": "Hear the text and image descriptions" }, { "@type": "ItemList", "itemListElement": ["auditory", "visual"], "description": "Hear the text and see the images" }, { "@type": "ItemList", "itemListElement": ["auditory", "visual", "textual"], "description": "Hear the text and see the text and images" } ], "accessibilitySummary": "Short descriptions are provided; long descriptions of the images are not needed for most readers." }

Structured representation of the JSON-LD example.
