---
title: "inDefinedTermSet"
source_url: https://schema.org/inDefinedTermSet
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# inDefinedTermSet

# inDefinedTermSet

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/inDefinedTermSet
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+inDefinedTermSet)

A

[DefinedTermSet](/DefinedTermSet)that contains this term.### Values expected to be one of these types


### Used on these types


#### Sub-properties

#### Source

[https://github.com/schemaorg/schemaorg/issues/894](https://github.com/schemaorg/schemaorg/issues/894)

### Examples

[Example 1](#eg-0315)

Copied

Example notes or example HTML without markup.

<div> <div> <h1><a href="http://openjurist.org/dictionary/Ballentine">Ballentine's Law Dictionary</a></h1> </div> <div> <h2>Dictionary term</h2> Name: calendar year<br/> Description: The period from January 1st to December 31st, inclusive, of any year.<br/> In Dictionary: Ballentine's Law Dictionary </div> <div> <h2>Dictionary term</h2> Name: schema<br/> Description: A representation of a plan or theory in the form of an outline or model.<br/> In Dictionary: Ballentine's Law Dictionary </div> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div> <div itemscope itemtype="https://schema.org/DefinedTermSet"> <link itemprop="additionalType" href="https://schema.org/Book"> <h1><a itemprop="url" href="http://openjurist.org/dictionary/Ballentine"><span itemprop="name">Ballentine's Law Dictionary</span></a></h1> </div> <div itemscope itemtype="https://schema.org/DefinedTerm"> <h2>Dictionary term</h2> <link itemprop="url" href="http://openjurist.org/dictionary/Ballentine/term/calendar-year"/> Name: <span itemprop="name">calendar year</span><br/> Description: <span itemprop="description">The period from January 1st to December 31st, inclusive, of any year.</span><br/> In Dictionary: Ballentine's Law Dictionary <link itemprop="inDefinedTermSet" href="http://openjurist.org/dictionary/Ballentine"> </div> <div itemscope itemtype="https://schema.org/DefinedTerm"> <h2>Dictionary term</h2> <link itemprop="url" href="http://openjurist.org/dictionary/Ballentine/term/schema"/> Name: <span itemprop="name">schema</span><br/> Description: <span itemprop="description">A representation of a plan or theory in the form of an outline or model.</span><br/> In Dictionary: Ballentine's Law Dictionary <link itemprop="inDefinedTermSet" href="http://openjurist.org/dictionary/Ballentine"> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/"> <div typeof="DefinedTermSet Book"> <h1><a property="url" href="http://openjurist.org/dictionary/Ballentine"><span property="name">Ballentine's Law Dictionary</span></a></h1> </div> <div typeof="DefinedTerm"> <h2>Dictionary term</h2> <link property="url" href="http://openjurist.org/dictionary/Ballentine/term/calendar-year"/> Name: <span property="name">calendar year</span><br/> Description: <span property="description">The period from January 1st to December 31st, inclusive, of any year.</span><br/> In Dictionary: Ballentine's Law Dictionary <link property="inDefinedTermSet" href="http://openjurist.org/dictionary/Ballentine"> </div> <div typeof="DefinedTerm"> <h2>Dictionary term</h2> <link propery="url" href="http://openjurist.org/dictionary/Ballentine/term/schema"/> Name: <span property="name">schema</span><br/> Description: <span property="description">A representation of a plan or theory in the form of an outline or model.</span><br/> In Dictionary: Ballentine's Law Dictionary <link property="inDefinedTermSet" href="http://openjurist.org/dictionary/Ballentine"> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.[ { "@context": "https://schema.org/" }, { "@type": ["DefinedTermSet","Book"], "@id": "http://openjurist.org/dictionary/Ballentine", "name": "Ballentine's Law Dictionary" }, { "@type": "DefinedTerm", "@id": "http://openjurist.org/dictionary/Ballentine/term/calendar-year", "name": "calendar year", "description": "The period from January 1st to December 31st, inclusive, of any year.", "inDefinedTermSet": "http://openjurist.org/dictionary/Ballentine" }, { "@type": "DefinedTerm", "@id": "http://openjurist.org/dictionary/Ballentine/term/schema", "name": "schema", "description": "A representation of a plan or theory in the form of an outline or model.", "inDefinedTermSet": "http://openjurist.org/dictionary/Ballentine" } ]

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
