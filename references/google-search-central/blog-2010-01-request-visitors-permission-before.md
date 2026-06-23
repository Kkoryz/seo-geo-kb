---
title: "Request visitors' permission before installing software | Google Search Central Blog | Google for Developers"
source_url: https://developers.google.com/search/blog/2010/01/request-visitors-permission-before
category: google-search-central
section: "Google Search Central — official technical SEO + structured data docs"
date: 2010-01-29
---

# Request visitors' permission before installing software | Google Search Central Blog | Google for Developers

Friday, January 29, 2010

*
Cross-posted on the
Google Korea Blog
*

Legitimate websites may require that their visitors install software. These sites often do so to
provide their users with additional functionality beyond what's available in standard web
browsers, like viewing a special type of document. Please note, however, that if your site
requires specific software for your visitors, the implementation of this software installation
process is very important. Incorrect implementation can appear as though you're installing
[malware](/search/docs/monitor-debug/security/malware), triggering our malware detection
filters, and resulting in your site being labeled with a 'This site may harm your computer'
[malware warning](/search/blog/2008/10/malware-we-dont-need-no-stinking)
in our search results.

If using your site requires a special software install, you need to first inform visitors why they need to install additional software. Here are two bad examples and one good example of how to handle the situation of a new visitor to such a site:

**Bad**: Install the required software without giving the visitor a chance to choose whether or
not they want to install the software.

**Bad**: Pop up a confirmation dialog box that prompts the visitor to agree to install the
software, without providing enough detail for the visitor to make an informed choice. (This
includes the standard ActiveX control installation dialog box, since it doesn't contain enough
meaningful information for a visitor to make an informed decision about that particular piece of
software.)

**Good**: Redirect the new visitor to an information page which provides thorough details on
why a special software installation is required to use the site. From this page the visitor can
initiate the installation of the required software if they decide to proceed with installation.

Has your site been labeled with a malware warning in our search results due to a poorly
implemented software installation requirement? Updating the installation process to ensure that
visitors are fully informed on why the installation is necessary, and giving them a chance to opt
out, should resolve this issue. Once you've got this in place, you can go to
[Webmaster Tools](https://search.google.com/search-console)
and request a
[malware review](/search/blog/2007/08/malware-reviews-via-webmaster-tools)
to expedite the process of removing any malware warnings associated with your site in Google's
search results.
