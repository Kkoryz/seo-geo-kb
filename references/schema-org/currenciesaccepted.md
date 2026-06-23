---
title: "currenciesAccepted"
source_url: https://schema.org/currenciesAccepted
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# currenciesAccepted

# currenciesAccepted

A Schema.org Property

- Canonical URL: https://schema.org/currenciesAccepted
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+currenciesAccepted)

The currency accepted.


Use standard formats:

Use standard formats:

[ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD";[Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)for cryptocurrencies, e.g. "BTC"; well known names for[Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)(LETS) and other currency types, e.g. "Ithaca HOUR".### Values expected to be one of these types


### Used on these types


### Examples

[Example 1](#eg-0432)

Copied

Example notes or example HTML without markup.

<h1>Disneyland Paris</h1> <div>It's an amusement park in Marne-la-Vallée, near Paris, in France.</div> <div>Hours: Mo-Fr 10am-7pm Sa 10am-22pm Su 10am-21pm</div> <div>Entrance: with ticket</div> <div>Currency accepted: Euro</div> <div>Payment accepted: Cash, Credit Card</div> <div>Website: <a href="http://www.disneylandparis.it/">www.disneylandparis.it</a> </div>

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/AmusementPark https://schema.org/TouristAttraction"> <h1><span itemprop="name">Disneyland Paris</span></h1> <div> <span itemprop="description">It's an amusement park in Marne-la-Vallée, near Paris, in France and is the most visited theme park in all of France and Europe.</span> </div> <div>Hours: Mo-Fr 10am-7pm Sa 10am-22pm Su 10am-21pm <meta itemprop="openingHours" content="Mo-Fr 10:00-19:00"/> <meta itemprop="openingHours" content="Sa 10:00-22:00"/> <meta itemprop="openingHours" content="Su 10:00-21:00"/> </div> <div> <meta itemprop="isAccessibleForFree" content="false"/>Entrance: with ticket </div> <div> <meta itemprop="currenciesAccepted" content="EUR"/>Currency accepted: Euro </div> <div> <meta itemprop="paymentAccepted" content="Cash, Credit Card"/>Payment accepted: Cash, Credit Card </div> <div>Website: <a href="http://www.disneylandparis.it/" itemprop="url">www.disneylandparis.it</a> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="TouristAttraction AmusementPark"> <h1><span property="name">Disneyland Paris</span></h1> <div> <span property="description">It's an amusement park in Marne-la-Vallée, near Paris, in France and is the most visited theme park in all of France and Europe.</span> </div> <div>Hours: Mo-Fr 10am-7pm Sa 10am-22pm Su 10am-21pm <meta property="openingHours" content="Mo-Fr 10:00-19:00"/> <meta property="openingHours" content="Sa 10:00-22:00"/> <meta property="openingHours" content="Su 10:00-21:00"/> </div> <div> <meta property="isAccessibleForFree" content="false"/>Entrance: with ticket </div> <div> <meta property="currenciesAccepted" content="EUR"/>Currency accepted: Euro </div> <div> <meta property="paymentAccepted" content="Cash, Credit Card"/>Payment accepted: Cash, Credit Card </div> <div>Website: <a href="http://www.disneylandparis.it/" property="url">www.disneylandparis.it</a> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context": "https://schema.org", "@type": ["TouristAttraction", "AmusementPark"], "name": "Disneyland Paris", "description": "It's an amusement park in Marne-la-Vallée, near Paris, in France and is the most visited theme park in all of France and Europe.", "openingHours":["Mo-Fr 10:00-19:00", "Sa 10:00-22:00", "Su 10:00-21:00"], "isAccessibleForFree": false, "currenciesAccepted": "EUR", "paymentAccepted":"Cash, Credit Card", "url":"http://www.disneylandparis.it/" } </script>

Structured representation of the JSON-LD example.
