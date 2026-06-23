---
title: "correction"
source_url: https://schema.org/correction
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# correction

# correction

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/correction
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+correction)

Indicates a correction to a

[CreativeWork](/CreativeWork), either via a[CorrectionComment](/CorrectionComment), textually or in another document.### Values expected to be one of these types


### Used on these types


### Acknowledgements

The Trust Project

[The Trust Project](http://thetrustproject.org/).

#### Source

[https://github.com/schemaorg/schemaorg/issues/1950](https://github.com/schemaorg/schemaorg/issues/1950)

### Examples

[Example 1](#eg-0266)

Copied

Example notes or example HTML without markup.

An example showing a CorrectionComment associated with an article.

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "ReportageNewsArticle", "url": "https://www.nytimes.com/2018/01/23/movies/oscars-snubs-surprises.html", "publisher":{ "@type": "Organization", "name": "New York Times", "@id": "https://www.nytimes.com" }, "datePublished":"2018-01-23", "dateModified":"2018-01-23", "headline":"The Snubs and Surprises of the 2018 Oscar Nominations", "mainEntityOfPage": "https://www.nytimes.com/2018/01/23/movies/oscars-snubs-surprises.html", "correction": { "@type": "CorrectionComment", "text": "An earlier version of this article misstated the number of times Denzel Washington has been nominated for an Oscar. His nod for 'Roman J. Israel, Esq.' brings the total to nine, not eight.", "datePublished": "2018-01-23" } } </script>

Structured representation of the JSON-LD example.
