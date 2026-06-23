---
title: "addressLocality"
source_url: https://schema.org/addressLocality
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# addressLocality

# addressLocality

A Schema.org Property

- Canonical URL: https://schema.org/addressLocality
-
Equivalent Property: fibo-fnd-plc-adr:hasMunicipality

Equivalent Property: gs1:addressLocality [Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+addressLocality)

The locality in which the street address is, and which is in the region. For example, Mountain View.

### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0001)

Copied

Example notes or example HTML without markup.

Jane Doe <img src="janedoe.jpg" alt="Photo of Jane Doe"/> Professor 20341 Whitworth Institute Suite 123 405 Whitworth Seattle WA 98052 (425) 123-4567 <a href="mailto:jane-doe@xyz.edu">jane-doe@illinois.edu</a> Jane's home page: <a href="http://www.janedoe.com">janedoe.com</a> Graduate students: <a href="http://www.xyz.edu/students/alicejones.html">Alice Jones</a> <a href="http://www.xyz.edu/students/bobsmith.html">Bob Smith</a>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Person"> <span itemprop="name">Jane Doe</span> <img src="janedoe.jpg" itemprop="image" alt="Photo of Jane Doe"/> <span itemprop="jobTitle">Professor</span> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress"> 20341 Whitworth Institute Suite 123 405 N. Whitworth </span> <span itemprop="addressLocality">Seattle</span>, <span itemprop="addressRegion">WA</span> <span itemprop="postalCode">98052</span> </div> <span itemprop="telephone">(425) 123-4567</span> <a href="mailto:jane-doe@xyz.edu" itemprop="email"> jane-doe@xyz.edu</a> Jane's home page: <a href="http://www.janedoe.com" itemprop="url">janedoe.com</a> Graduate students: <a href="http://www.xyz.edu/students/alicejones.html" itemprop="colleague"> Alice Jones</a> <a href="http://www.xyz.edu/students/bobsmith.html" itemprop="colleague"> Bob Smith</a> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="Person"> <span property="name">Jane Doe</span> <img src="janedoe.jpg" property="image" alt="Photo of Jane Doe"/> <span property="jobTitle">Professor</span> <div property="address" typeof="PostalAddress"> <span property="streetAddress"> 20341 Whitworth Institute Suite 123 405 N. Whitworth </span> <span property="addressLocality">Seattle</span>, <span property="addressRegion">WA</span> <span property="postalCode">98052</span> </div> <span property="telephone">(425) 123-4567</span> <a href="mailto:jane-doe@xyz.edu" property="email"> jane-doe@xyz.edu</a> Jane's home page: <a href="http://www.janedoe.com" property="url">janedoe.com</a> Graduate students: <a href="http://www.xyz.edu/students/alicejones.html" property="colleague"> Alice Jones</a> <a href="http://www.xyz.edu/students/bobsmith.html" property="colleague"> Bob Smith</a> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "Person", "address": { "@type": "PostalAddress", "addressLocality": "Seattle", "addressRegion": "WA", "postalCode": "98052", "streetAddress": "20341 Whitworth Institute 405 N. Whitworth", "extendedAddress": "Suite 123" }, "colleague": [ "http://www.xyz.edu/students/alicejones.html", "http://www.xyz.edu/students/bobsmith.html" ], "email": "mailto:jane-doe@xyz.edu", "image": "janedoe.jpg", "jobTitle": "Professor", "name": "Jane Doe", "telephone": "(425) 123-4567", "url": "http://www.janedoe.com" } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0007)

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

[Example 3](#eg-0015)

Copied

Example notes or example HTML without markup.

<h1>Beachwalk Beachwear & Giftware</h1> A superb collection of fine gifts and clothing to accent your stay in Mexico Beach. 3102 Highway 98 Mexico Beach, FL Phone: 850-648-4200

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/LocalBusiness"> <h1><span itemprop="name">Beachwalk Beachwear & Giftware</span></h1> <span itemprop="description"> A superb collection of fine gifts and clothing to accent your stay in Mexico Beach.</span> <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="streetAddress">3102 Highway 98</span> <span itemprop="addressLocality">Mexico Beach</span>, <span itemprop="addressRegion">FL</span> </div> Phone: <span itemprop="telephone">850-648-4200</span> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="LocalBusiness"> <h1><span property="name">Beachwalk Beachwear & Giftware</span></h1> <span property="description"> A superb collection of fine gifts and clothing to accent your stay in Mexico Beach.</span> <div property="address" typeof="PostalAddress"> <span property="streetAddress">3102 Highway 98</span> <span property="addressLocality">Mexico Beach</span>, <span property="addressRegion">FL</span> </div> Phone: <span property="telephone">850-648-4200</span> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "LocalBusiness", "address": { "@type": "PostalAddress", "addressLocality": "Mexico Beach", "addressRegion": "FL", "streetAddress": "3102 Highway 98" }, "description": "A superb collection of fine gifts and clothing to accent your stay in Mexico Beach.", "name": "Beachwalk Beachwear & Giftware", "telephone": "850-648-4200" } </script>

Structured representation of the JSON-LD example.
