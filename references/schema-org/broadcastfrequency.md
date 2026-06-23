---
title: "broadcastFrequency"
source_url: https://schema.org/broadcastFrequency
category: schema-org
section: "schema.org — structured-data vocabulary reference"
date: 2026-03-19
---

# broadcastFrequency

# broadcastFrequency

A Schema.org Property

- Canonical URL: https://schema.org/broadcastFrequency
[Check for open issues.](https://github.com/schemaorg/schemaorg/issues?q=is%3Aissue+is%3Aopen+broadcastFrequency)

The frequency used for over-the-air broadcasts. Numeric values or simple ranges, e.g. 87-99. In addition a shortcut idiom is supported for frequencies of AM and FM radio channels, e.g. "87 FM".

### Values expected to be one of these types


### Used on these types


#### Source

[https://github.com/schemaorg/schemaorg/issues/1004](https://github.com/schemaorg/schemaorg/issues/1004)

### Examples

[Example 1](#eg-0319)

Copied

Example notes or example HTML without markup.

A radio station on 107.9 FM.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/BroadcastService"> <span itemprop="name">WXKS-FM</span> <span itemprop="broadcastDisplayName">Kiss 108</span> <div itemprop="broadcastFrequency" itemscope itemtype="https://schema.org/BroadcastFrequencySpecification"> <meta itemprop="broadcastFrequencyValue" content="107.9" /> <meta itemprop="broadcastSignalModulation" content="FM" /> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="BroadcastService"> <span property="name">WXKS-FM</span> <span property="broadcastDisplayName">Kiss 108</span> <div property="broadcastFrequency" typeof="BroadcastFrequencySpecification"> <meta property="broadcastFrequencyValue" content="107.9" /> <meta property="broadcastSignalModulation" content="FM" /> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"BroadcastService", "name": "WXKS-FM", "broadcastDisplayName": "Kiss 108", "broadcastFrequency": { "@type": "BroadcastFrequencySpecification", "broadcastFrequencyValue": 107.9, "broadcastSignalModulation": "FM" } } </script>

Structured representation of the JSON-LD example.

[Example 2](#eg-0320)

Copied

Example notes or example HTML without markup.

A radio station on 1030 AM.

Example encoded as

[Microdata](https://en.wikipedia.org/wiki/Microdata_(HTML))embedded in HTML.<div itemscope itemtype="https://schema.org/BroadcastService"> <span itemprop="name">WBZ-AM</span> <span itemprop="broadcastDisplayName">WBZ NewsRadio</span> <div itemprop="broadcastFrequency" itemscope itemtype="https://schema.org/BroadcastFrequencySpecification"> <meta itemprop="broadcastFrequencyValue" content="1030" /> <meta itemprop="broadcastSignalModulation" content="AM" /> </div> </div>

Example encoded as

[RDFa](https://en.wikipedia.org/wiki/RDFa)embedded in HTML.<div vocab="https://schema.org/" typeof="BroadcastService"> <span property="name">WBZ-AM</span> <span property="broadcastDisplayName">WBZ NewsRadio</span> <div property="broadcastFrequency" typeof="BroadcastFrequencySpecification"> <meta property="broadcastFrequencyValue" content="1030" /> <meta property="broadcastSignalModulation" content="AM" /> </div> </div>

Example encoded as

[JSON-LD](https://en.wikipedia.org/wiki/JSON-LD)in a HTML script tag.<script type="application/ld+json"> { "@context":"https://schema.org", "@type":"BroadcastService", "name": "WBZ-AM", "broadcastDisplayName": "WBZ NewsRadio", "broadcastFrequency": { "@type": "BroadcastFrequencySpecification", "broadcastFrequencyValue": 1030, "broadcastSignalModulation": "AM" } } </script>

Structured representation of the JSON-LD example.
