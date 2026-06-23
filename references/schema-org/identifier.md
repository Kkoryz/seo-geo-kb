---
title: "identifier"
source_url: https://schema.org/identifier
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# identifier

# identifier

A Schema.org Property

- Canonical URL: https://schema.org/identifier
-
Equivalent Property: cmns-id:identifiedBy

Equivalent Property: dcterms:identifier [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+identifier)

The identifier property represents any kind of identifier for any kind of

[Thing](/Thing), such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for representing many of these, either as textual strings or as URL (URI) links. See[background notes](/docs/datamodel.html#identifierBg)for more details.### Values expected to be one of these types


### Used on these types


#### Sub-properties

-
[accountId](/accountId) -
[asin](/asin) -
[callSign](/callSign) -
[confirmationNumber](/confirmationNumber) -
[duns](/duns) -
[editEIDR](/editEIDR) -
[flightNumber](/flightNumber) -
[globalLocationNumber](/globalLocationNumber) -
[gtin](/gtin) -
[gtin12](/gtin12) -
[gtin13](/gtin13) -
[gtin14](/gtin14) -
[gtin8](/gtin8) -
[hasGS1DigitalLink](/hasGS1DigitalLink) -
[isbn](/isbn) -
[issn](/issn) -
[legislationIdentifier](/legislationIdentifier) -
[leiCode](/leiCode) -
[nsn](/nsn) -
[orderNumber](/orderNumber) -
[productID](/productID) -
[serialNumber](/serialNumber) -
[sku](/sku) -
[taxID](/taxID) -
[titleEIDR](/titleEIDR) -
[usNPI](/usNPI)

### Examples

[Example 1](#eg-0372)

Copied

Example notes or example HTML without markup.

<p> Title: Library linked data in the cloud : OCLC's experiments with new models of resource description<br/> Author: Carol Jean Godby<br/> ISBN: 9781627052191<br/> oclcnum: 889647468<br/> Details: <a href="http://www.worldcat.org/oclc/889647468">WorldCat.org</a> </p>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Book"> Title: <span itemprop="name">Library linked data in the cloud : OCLC's experiments with new models of resource description</span><br> Author: <span itemprop="author">Carol Jean Godby</span><br> ISBN: <span itemprop="isbn">9781627052191</span><br> <div itemscope itemprop="identifier" itemtype="https://schema.org/PropertyValue"> <span itemprop="propertyID">OCoLC</span>: <span itemprop="value">889647468</span> </div><br> Details: <a itemprop="sameAs" href="http://www.worldcat.org/oclc/889647468">WorldCat.org</a> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Book"> Title: <span property="name">Library linked data in the cloud : OCLC's experiments with new models of resource description</span><br> Author: <span property="author">Carol Jean Godby</span><br> ISBN: <span property="isbn">9781627052191</span><br> <div property="identifier" typeof="PropertyValue"> <span property="propertyID">OCoLC</span>: <span property="value">889647468</span> </div> </div> <br> Details: <a property="sameAs" href="http://www.worldcat.org/oclc/889647468">WorldCat.org</a>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "Book", "name": "Library linked data in the cloud : OCLC's experiments with new models of resource description", "author": "Carol Jean Godby", "isbn": "9781627052191", "identifier": { "@type": "PropertyValue", "propertyID": "OCoLC", "value": "889647468" }, "sameAs": "http://www.worldcat.org/oclc/889647468" }

Structured representation of the JSON-LD example.

[Example 2](#eg-0373)

Copied

Example notes or example HTML without markup.

<div"> Company Record <h1>A UK Organization Ltd</h1> Registered office address: 1 A Street, London<br/> Company Number: 99065782 </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/LocalBusiness"> Company Record <h1 itemprop="name">A UK Organization Ltd</h1> Registered office address: <span itemprop="address">1 A Street, London</span><br> <div itemscope="" itemprop="identifier" itemtype="https://schema.org/PropertyValue"> <span itemprop="propertyID">Company Number</span>: <span itemprop="value">99065782</span> </div><br> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="LocalBusiness"> Company Record <h1 property="name"> A UK Organization Ltd</h1> Registered office address: <span property="address">1 A Street, London</span><br> <div property="identifier" typeof="PropertyValue"> <span property="propertyID">Company Number</span>: <span property="value">99065782</span> </div><br> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.{ "@context": "https://schema.org/", "@type": "LocalBusiness", "name": "A UK Organization Ltd", "address": "1 A Street, London", "identifier": { "@type": "PropertyValue", "propertyID": "Company Number", "value": "99065782" } }

Structured representation of the JSON-LD example.
