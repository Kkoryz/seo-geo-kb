---
title: "countryOfOrigin"
source_url: https://schema.org/countryOfOrigin
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# countryOfOrigin

# countryOfOrigin

A Schema.org Property

- Canonical URL: https://schema.org/countryOfOrigin
- Equivalent Property: unece:originCountry
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+countryOfOrigin)

The country of origin of something, including products as well as creative works such as movie and TV content.


In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of


In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.

In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of

[CreativeWork](/CreativeWork)it is difficult to provide fully general guidance, and properties such as[contentLocation](/contentLocation)and[locationCreated](/locationCreated)may be more applicable.In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.

### Values expected to be one of these types


### Examples

[Example 1](#eg-0420)

Copied

Example notes or example HTML without markup.

Ghostbusters was produced by Black Rhino in the United States.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Movie"> <h1 itemprop="name">Ghostbusters</h1> <div itemprop="productionCompany" itemscope itemtype="https://schema.org/Organization"> Produced by: <span itemprop="name">Black Rhino</span><p> </div> <div itemprop="countryOfOrigin" itemscope itemtype="https://schema.org/Country"> Country: <span itemprop="name" content="USA">United States</span><p> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Movie"> <h1 property="name">Ghostbusters</h1> <div property="productionCompany" typeof="Organization"> Produced by: <span property="name">Black Rhino</span><p> </div> <div property="countryOfOrigin" typeof="Country"> Country: <span property="name" content="USA">United States</span><p> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@type": "Movie", "name": "Ghostbusters", "productionCompany": { "@type": "Organization", "name": "Black Rhino" }, "countryOfOrigin": { "@type": "Country", "name": "USA" } } </script>

Structured representation of the JSON-LD example.
