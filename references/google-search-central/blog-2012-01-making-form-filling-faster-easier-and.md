---
title: "Making form-filling faster, easier and smarter | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2012/01/making-form-filling-faster-easier-and
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2012-01-25
---

# Making form-filling faster, easier and smarter | Google Search Central Blog | Google for Developers

Wednesday, January 25, 2012

One of the biggest bottlenecks on any conversion funnel is filling out an online form – shopping and registration flows all rely on forms as a crucial and demanding step in accomplishing the goals of your site. For many users, online forms mean repeatedly typing common information like our names and addresses on different sites across the web – a tedious task that causes many to give up and abandon the flow entirely.

Chrome's Autofill and other form-filling providers help to break down this barrier by remembering
common profile information and pre-populating the form with those values. Unfortunately, up to
now it has been difficult for webmasters to ensure that Chrome and other form-filling providers
can parse their form correctly. Some
[standards exist](https://www.rfc-editor.org/rfc/rfc4112.html);
but they put onerous burdens on the implementation of the website, so they're not used much in
practice.

Today we're pleased to announce support in Chrome for an experimental new "autocomplete type"
attribute for form fields that allows web developers to unambiguously label `text`

and `select`

fields with common data types such as 'full-name' or 'street-address'.
With this attribute, web developers can drive conversions on their sites by marking their forms
for auto-completion without changing the user interface or the backend.

Just add an attribute to the input element, for example an email address field might look like:

<input type="text" name="field1" x-autocompletetype="email" />

We've been working on this design in collaboration with several other autofill vendors. Like any
early stage proposal we expect this will change and evolve as the web standards community provides
feedback, but we believe this will serve as a good starting point for the discussion on how to
best support autofillable forms in the HTML5 spec. For now, this new attribute is implemented in
Chrome as `x-autocompletetype`

to indicate that this is still experimental and not yet
a standard, similar to the `webkitspeech`

attribute we
[released](https://chrome.blogspot.com/2011/04/everybodys-talking-and-translating-with.html)
last summer.

For more information, you can read the
[full text of the proposed specification](https://wiki.whatwg.org/wiki/Autocompletetype),
ask questions on the
[Webmaster help forum](https://support.google.com/webmasters/community),
or you can share your feedback in the
[standardization discussion](https://lists.whatwg.org/htdig.cgi/whatwg-whatwg.org/2011-December/034198.html)!
