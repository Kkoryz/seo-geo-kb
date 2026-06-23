---
title: "hasCategoryCode"
source_url: https://schema.org/hasCategoryCode
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# hasCategoryCode

# hasCategoryCode

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/hasCategoryCode
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+hasCategoryCode)

A Category code contained in this code set.

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/894](https://github.com/schemaorg/schemaorg/issues/894)

### Examples

[Example 1](#eg-0317)

Copied

Example notes or example HTML without markup.

<div> <h1 >Defined Values in The Mammal Classification List</h1> <ul> <li>Carnivore - A mammal that feeds on other animals</li> </ul> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/CategoryCodeSet" id="C1"> <h1>Defined Values in <span itemprop="name">The Mammal Classification List</span></h1> <ul> <li itemprop="hasCategoryCode" itemscope itemtype="https://schema.org/CategoryCode"> <span itemprop="name">Carnivore</span> - <span itemprop="description">A mammal that feeds on other animals</span> <link itemprop="inCodeSet" href="#C1"/> </li> </ul> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="CategoryCodeSet" id="C1"> <h1>Defined Values in <span property="name">The Mammal Classification List</span></h1> <ul> <li property="hasCategoryCode" typeof="CategoryCode"> <span property="name">Carnivore</span> - <span property="description">A mammal that feeds on other animals</span> <link property="inCodeSet" href="#C1"/> </li> </ul> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "CategoryCodeSet", "@id": "_C1", "name": "The Mammal Classification List", "hasCategoryCode": { "@type": "CategoryCode", "name": "Carnivore", "description": "A mammal that feeds on other animals", "inCodeSet": "_C1" } }

Structured representation of the JSON-LD example.

[Example 2](#eg-0318)

Copied

Example notes or example HTML without markup.

<div> <h1>ISO 639-2: Codes for the Representation of Names of Languages<h1> <h2>Listing of codes:</h2> <ul> <li>...</li> <li>cze</li> <li>...</li> </ul> </div> <div> <h2>Czech; tchèque; Tschechisch</h2> <h3>From: ISO 639-2: Codes for the Representation of Names of Languages</h3> English: Czech<br/> French: tchèque<br/> German: Tschechisch<br/> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/CategoryCodeSet" itemid="http://id.loc.gov/vocabulary/iso639-2"> <h1 itemprop="name">ISO 639-2: Codes for the Representation of Names of Languages</h1> <h2>Listing of codes:</h2> <ul> <li>...</li> <li><span itemprop="hasCategoryCode" itemid="http://id.loc.gov/vocabulary/iso639-2/cze">cze</span></li> <li>...</li> </ul> </div> <div itemscope itemtype="https://schema.org/CategoryCode" itemid="http://id.loc.gov/vocabulary/iso639-2/cze"> <meta itemprop="codeValue" content="cze"> <h2>Czech; tchèque; Tschechisch</h2> <link itemprop="inCodeSet" href="http://id.loc.gov/vocabulary/iso639-2"> <h3>From: ISO 639-2: Codes for the Representation of Names of Languages</h3> <span itemprop="name" xml:lang="en" content="Czech">English: Czech</span><br/> <span itemprop="name" xml:lang="fr" content="tchèque">French: tchèque</span><br/> <span itemprop="name" xml:lang="de" content="Tschechisch">German: Tschechisch</span><br/> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="CategoryCodeSet" resource="http://id.loc.gov/vocabulary/iso639-2"> <h1 property="name">ISO 639-2: Codes for the Representation of Names of Languages</h1> <h2>Listing of codes:</h2> <ul> <li>...</li> <li><span property="hasCategoryCode" resource="http://id.loc.gov/vocabulary/iso639-2/cze">cze</span></li> <li>...</li> </ul> </div> <div vocab="https://schema.org/" typeof="CategoryCode" resource="http://id.loc.gov/vocabulary/iso639-2/cze"> <meta property="codeValue" content="cze"> <h2>Czech; tchèque; Tschechisch</h2> <link property="inCodeSet" href="http://id.loc.gov/vocabulary/iso639-2"> <h3>From: ISO 639-2: Codes for the Representation of Names of Languages</h3> <span property="name" xml:lang="en" content="Czech">English: Czech</span><br/> <span property="name" xml:lang="fr" content="tchèque">French: tchèque</span><br/> <span property="name" xml:lang="de" content="Tschechisch">German: Tschechisch</span><br/> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.[ { "@context": "https://schema.org/" }, { "@type": "CategoryCodeSet", "@id": "http://id.loc.gov/vocabulary/iso639-2", "name": "ISO 639-2: Codes for the Representation of Names of Languages", "hasCategoryCode": "http://id.loc.gov/vocabulary/iso639-2/cze" }, { "@type": "CategoryCode", "@id": "http://id.loc.gov/vocabulary/iso639-2/cze", "codeValue": "cze", "name": { "en": "Czech", "fr": "tchèque", "de": "Tschechisch" }, "inCodeSet": "http://id.loc.gov/vocabulary/iso639-2" } ]

Structured representation of the JSON-LD example.
