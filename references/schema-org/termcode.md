---
title: "termCode"
source_url: https://schema.org/termCode
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# termCode

# termCode

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/termCode
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+termCode)

A code that identifies this

[DefinedTerm](/DefinedTerm)within a[DefinedTermSet](/DefinedTermSet).### Values expected to be one of these types


### Used on these types


#### Sub-properties

#### Source

[https://github.com/schemaorg/schemaorg/issues/894](https://github.com/schemaorg/schemaorg/issues/894)

### Examples

[Example 1](#eg-0314)

Copied

Example notes or example HTML without markup.

<div> <h1>Library of Congress Resource Type: <b>Manuscript</b></h1> Code: <b>Man</b> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/DefinedTerm"> <h1>Library of Congress Resource Type: <b><span itemprop="name">Manuscript</span></b></h1> Code: <b><span itemprop="termCode">Man</span></b> <link itemprop="inDefinedTermSet" href="http://id.loc.gov/vocabulary/resourceTypes"/> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="DefinedTerm"> <h1>Library of Congress Resource Type: <b><span property="name">Manuscript</span></b></h1> Code: <b><span property="termCode">Man</span></b> <link property="inDefinedTermSet" href="http://id.loc.gov/vocabulary/resourceTypes"/> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "DefinedTerm", "termCode": "Man", "inDefinedTermSet": "http://id.loc.gov/vocabulary/resourceTypes" }

Structured representation of the JSON-LD example.

[Example 2](#eg-0316)

Copied

Example notes or example HTML without markup.

<div> <h1>Occupation Term defined by <a href="http://onetonline.org">O*Net Online</a></h1> <h2>51-6042.00 - Shoe Machine Operators and Tenders</h2> Operate or tend a variety of machines to join, decorate, reinforce, or finish shoes and shoe parts. </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/DefinedTerm"> <h1>Occupation Term defined by <a itemprop="inDefinedTermSet" href="http://onetonline.org">O*Net Online</a></h1> <h2><span itemprop="termCode">51-6042.00</span> - <span itemprop="name">Shoe Machine Operators and Tenders</span></h2> <span itemprop="description">Operate or tend a variety of machines to join, decorate, reinforce, or finish shoes and shoe parts.</span> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="DefinedTerm"> <h1>Occupation Term defined by <a property="inDefinedTermSet" href="http://onetonline.org">O*Net Online</a></h1> <h2><span property="termCode">51-6042.00</span> - <span property="name">Shoe Machine Operators and Tenders</span></h2> <span property="description">Operate or tend a variety of machines to join, decorate, reinforce, or finish shoes and shoe parts.</span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "DefinedTerm", "name": "Shoe Machine Operators and Tenders", "termCode": "51-6042.00", "description": "Operate or tend a variety of machines to join, decorate, reinforce, or finish shoes and shoe parts.", "inDefinedTermSet": "http://onetonline.org" }

Structured representation of the JSON-LD example.
