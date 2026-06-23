---
title: "additionalType"
source_url: https://schema.org/additionalType
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# additionalType

# additionalType

A Schema.org Property

- Canonical URL: https://schema.org/additionalType
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+additionalType)

An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. Typically the value is a URI-identified RDF class, and in this case corresponds to the
use of rdf:type in RDF. Text values can be used sparingly, for cases where useful information can be added without their being an appropriate schema to reference. In the case of text values, the class label should follow the schema.org

[style guide](https://schema.org/docs/styleguide.html).**Subproperty of:**

- rdf:type

### Used on these types


### Examples

[Example 1](#eg-0393)

Copied

Example notes or example HTML without markup.

<!-- Uses both the "Book" and "Product" item types to support Offer relationships --> <div> <h3>Le concerto</h3> <div> Bibliographic Details <table> <tr> <th>Main Author: </th> <td>Ferchault, Guy</td> </tr> </table> </div> </div> <div> Holdings details from Anytown City Library <table> <!-- Example of a copy available for loan --> <tr> <th>Copy </th> <td>Available <div>Barcode: <span>CONC91000937</span></div> <div>Call number: <span>780 R2</span></div> <div>Library: <span>Anytown City Library</span></div> </td> </tr> <table> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<!-- Uses both the "Book" and "Product" item types to support Offer relationships --> <div itemscope itemtype="https://schema.org/Book" itemid="#record"> <link itemprop="additionalType" href="https://schema.org/Product"/> <h3 itemprop="name">Le concerto</h3> <div> Bibliographic Details <table> <tr> <th>Main Author: </th> <td itemprop="author">Ferchault, Guy</td> </tr> </table> </div> </div> <div> Holdings details from Anytown City Library <table> <!-- Example of a copy available for loan --> <tr itemscope itemtype="https://schema.org/Offer"> <th>Copy </th> <td>Available <link itemprop="availability" href="https://schema.org/InStock"> <div>Barcode: <span itemprop="serialNumber">CONC91000937</span></div> <div>Call number: <span itemprop="sku">780 R2</span></div> <div>Library: <span itemprop="offeredBy" itemscope itemtype="https://schema.org/Library" itemid="http://library.anytown.gov.uk" >Anytown City Library</span></div> <link itemprop="businessFunction" href="http://purl.org/goodrelations/v1#LeaseOut"> <link itemprop="itemOffered" href="#record"> </td> </tr> </table> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<!-- Uses both the "Book" and "Product" item types to support Offer relationships --> <div vocab="https://schema.org/" resource="#record" typeof="Book Product"> <h3 property="name"> Le concerto </h3> <div> Bibliographic Details <table> <tr> <th> Main Author: </th> <td property="author"> Ferchault, Guy </td> </tr> </table> </div> </div> <div> Holdings details from Anytown City Library <table vocab="https://schema.org/"> <!-- Example of a copy available for loan --> <tr typeof="Offer"> <th> Copy </th> <td> Available <div> Barcode: <span property="serialNumber">CONC91000937</span> </div> <div> Call number: <span property="sku">780 R2</span> </div> <div> Library: <span property="offeredBy" typeof="Library" resource="http://library.anytown.gov.uk">Anytown City Library</span> </div> </td> </tr> </table> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org/", "@id": "#record", "@type": "Book", "additionalType": "Product", "name": "Le concerto", "author": "Ferchault, Guy", "offers":{ "@type": "Offer", "availability": "https://schema.org/InStock", "serialNumber": "CONC91000937", "sku": "780 R2", "offeredBy": { "@type": "Library", "@id": "http://library.anytown.gov.uk", "name": "Anytown City Library" }, "businessFunction": "http://purl.org/goodrelations/v1#LeaseOut", "itemOffered": "#record" } } </script>

Structured representation of the JSON-LD example.
