---
title: "iso6523Code"
source_url: https://schema.org/iso6523Code
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# iso6523Code

# iso6523Code

A Schema.org Property

*This term is in the "new" area - implementation feedback and adoption from applications and websites can help improve our definitions.*

- Canonical URL: https://schema.org/iso6523Code
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+iso6523Code)

An organization identifier as defined in

[ISO 6523(-1)](https://en.wikipedia.org/wiki/ISO/IEC_6523). The identifier should be in the`XXXX:YYYYYY:ZZZ`

or `XXXX:YYYYYY`

format. Where `XXXX`

is a 4 digit *ICD*(International Code Designator),`YYYYYY`

is an *OID*(Organization Identifier) with all formatting characters (dots, dashes, spaces) removed with a maximal length of 35 characters, and`ZZZ`

is an optional OPI (Organization Part Identifier) with a maximum length of 35 characters. The various components (ICD, OID, OPI) are joined with a colon character (ASCII `0x3a`

). Note that many existing organization identifiers defined as attributes like [leiCode](https://schema.org/leiCode)(`0199`

), [duns](https://schema.org/duns)(`0060`

) or [GLN](https://schema.org/globalLocationNumber)(`0088`

) can be expressed using ISO-6523. If possible, ISO-6523 codes should be preferred to populating [vatID](https://schema.org/vatID)or[taxID](https://schema.org/taxID), as ISO identifiers are less ambiguous.### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/2915](https://github.com/schemaorg/schemaorg/issues/2915)

### Examples

[Example 1](#eg-0007)

Copied

Example notes or example HTML without markup.

Google.Org Contact Details: Main address: 38 avenue de l'Opéra, F-75002 Paris, France Tel: ( 33 1) 42 68 53 00, Fax: ( 33 1) 42 68 53 01 E-mail: secretariat (at) google.org URL: <a href="http://www.google.org">www.google.org</a> SIRET Code: 443 061 841 00039 VAT Number: FR64443061841 Members: - National Scientific Members in 100 countries and territories: Country1, Country2, ... - Scientific Union Members, 30 organizations listed in this Yearbook: Member 1, Member 2 History:

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Organization"> <span itemprop="name">Google.org (GOOG)</span> Contact Details: <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> Main address: <span itemprop="streetAddress">38 avenue de l'Opéra</span> <span itemprop="postalCode">F-75002</span> <span itemprop="addressLocality">Paris, France</span> , </div> Tel:<span itemprop="telephone">( 33 1) 42 68 53 00 </span>, Fax:<span itemprop="faxNumber">( 33 1) 42 68 53 01 </span>, E-mail: <span itemprop="email">secretariat@example.com</span> SIRET Code: 443 061 841 00039<meta itemprop="iso6523Code" content="0009:44306184100039" /> VAT Number: FR64443061841<meta itemprop="iso6523Code" content="9957:FR64443061841" /> Members: - National Scientific Members in 100 countries and territories: Country1, Country2, ... - Scientific Union Members, 30 organizations listed in this Yearbook: List of Alumni: <span itemprop="alumni" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Jack Dan</span> </span>, <span itemprop="alumni" itemscope itemtype="https://schema.org/Person"> <span itemprop="name">John Smith</span> </span>, History: </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Organization"> <span property="name">Google.org (GOOG)</span> Contact Details: <div property="address" typeof="PostalAddress"> Main address: <span property="streetAddress">38 avenue de l'Opera</span> <span property="postalCode">F-75002</span> <span property="addressLocality">Paris, France</span> , </div> Tel:<span property="telephone">( 33 1) 42 68 53 00 </span>, Fax:<span property="faxNumber">( 33 1) 42 68 53 01 </span>, E-mail: <span property="email">secretariat@example.com</span> SIRET Code: 443 061 841 00039<meta itemprop="iso6523Code" content="0009:44306184100039" /> VAT Number: FR64443061841<meta itemprop="iso6523Code" content="9957:FR64443061841" /> Members: - National Scientific Members in 100 countries and territories: Country1, Country2, ... - Scientific Union Members, 30 organizations listed in this Yearbook: List of Alumni: <span property="alumni" typeof="Person"> <span property="name">Jack Dan</span> </span>, <span property="alumni" typeof="Person"> <span property="name">John Smith</span> </span> History: </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Organization", "address": { "@type": "PostalAddress", "addressLocality": "Paris, France", "postalCode": "F-75002", "streetAddress": "38 avenue de l'Opéra" }, "email": "secretariat@example.com", "faxNumber": "+33142685301", "iso6523Code": [ "0009:44306184100039", "9957:FR64443061841" ], "member": [ { "@type": "Organization" }, { "@type": "Organization" } ], "alumni": [ { "@type": "Person", "name": "Jack Dan" }, { "@type": "Person", "name": "John Smith" } ], "name": "Google.org (GOOG)", "telephone": "+33 1 42 68 53 00" } </script>

Structured representation of the JSON-LD example.
