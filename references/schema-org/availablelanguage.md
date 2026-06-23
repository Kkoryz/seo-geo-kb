---
title: "availableLanguage"
source_url: https://schema.org/availableLanguage
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# availableLanguage

# availableLanguage

A Schema.org Property

- Canonical URL: https://schema.org/availableLanguage
- Equivalent Property: gs1:availableLanguage
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+availableLanguage)

A language someone may use with or at the item, service or place. Please use one of the language codes from the

[IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also[inLanguage](/inLanguage).### Used on these types


### Examples

[Example 1](#eg-0369)

Copied

Example notes or example HTML without markup.

This example is in microdata only.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/Hotel"> <h1><span itemprop="name">ACME Hotel Innsbruck</span></h1> <span itemprop="description">A beautifully located business hotel right in the heart of the alps. Watch the sun rise over the scenic Inn valley while enjoying your morning coffee.</span> We speak: <ul> <li itemprop="availableLanguage" itemscope itemtype="https://schema.org/Language"> <span itemprop="name">English</span> </li> <li itemprop="availableLanguage" itemscope itemtype="https://schema.org/Language"> <span itemprop="name">German</span> </li> </ul> </div>

[Example 2](#eg-0433)

Copied

Example notes or example HTML without markup.

<h1>Neuschwanstein Castle</h1> <div>Neuschwanstein Castle is a nineteenth-century Romanesque Revival palace in Schwangau, in southwest Bavaria, Germany.</div> <div>Guided tours in German and English.</div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/TouristAttraction"> <h1><span itemprop="name">Neuschwanstein Castle</span></h1> <div>It is a nineteenth-century Romanesque Revival palace in <div itemprop="address" itemscope itemtype="https://schema.org/PostalAddress"> <span itemprop="addressLocality">Schwangau</span>, in <span itemprop="addressCountry">Germany</span>. </div> </div> <div>Guided tours in <div itemprop="availableLanguage" itemscope itemtype="https://schema.org/Language"> <span itemprop="name">German</span> </div> and <div itemprop="availableLanguage" itemscope itemtype="https://schema.org/Language"> <span itemprop="name">English</span>. </div> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org" typeof="TouristAttraction"> <h1><span property="name">Neuschwanstein Castle</span></h1> <div>It is a nineteenth-century Romanesque Revival palace in <div property="address" typeof="PostalAddress"> <span property="addressLocality">Schwangau</span>, in <span property="addressCountry">Germany</span>. </div> </div> <div>Guided tours in <div property="availableLanguage" typeof="Language"> <span property="name">German</span> </div> and <div property="availableLanguage" typeof="Language"> <span property="name">English</span>. </div> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": "TouristAttraction", "name": "Neuschwanstein Castle", "address": { "@type": "PostalAddress", "addressLocality": "Schwangau", "addressCountry": "Germany" }, "availableLanguage": [ { "@type": "Language", "name": "German" }, { "@type": "Language", "name": "English" } ] } </script>

Structured representation of the JSON-LD example.
