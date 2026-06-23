---
title: "What Is HTTPS & How Does It Work? [Explained]"
source_url: https://www.semrush.com/blog/what-is-https/
category: semrush-blog
section: "Semrush blog — SEO/GEO methodology"
date: 2020-07-31
---

# What Is HTTPS & How Does It Work? [Explained]

## What Is HTTPS?

Hypertext transfer protocol secure (HTTPS) is an encrypted version of HTTP. Which is the protocol used to transfer data between web browsers (like Chrome) and servers (computers that host websites).

When you visit a website that uses HTTPS, the connection between your browser and the website's server is encrypted (meaning it’s scrambled)

This protects your data from being spied on by attackers.

That data includes all types of confidential information—login credentials, payment information, and browsing activity in general.

So, in other words:

The HTTPS protocol is fundamental for keeping your data private and secure when surfing the web.

But how does it work, exactly? And how is it different from HTTP?

Let’s find out.

## How Does HTTPS Work?

HTTPS works on a request-response model (meaning the browser sends a request and the server responds to that request), just like in HTTP.

But HTTPS uses a secure sockets layer (SSL) and transport layer security (TLS) certificate for encryption. (These are digital documents that prove the identity of a website. So an encrypted connection can be established.)

Here’s how the entire process works:

1. **Browser contacts website**: The user's web browser attempts to connect to a website using HTTPS

2. **SSL certificate sends**: The website's server responds by sending its SSL/TLS certificate to the browser. This certificate contains the website’s public key (encryption key) and is used to establish a secure connection.

3. **Browser verifies certificate**: The browser checks the certificate to ensure it’s valid and is issued by a trusted certificate authority (like GoDaddy, DigiCert, Comodo, etc.). This step is crucial for confirming a website’s authenticity.

4. **Encryption key exchange**: The browser and the server establish an encrypted connection by exchanging keys once the certificate is verified. The browser uses the server's public key to encrypt information, which can only be decrypted by the private key (i.e., the decryption key) the server holds.

5. **Encrypted data transfer**: All data transferred between the browser and the server is encrypted after the secure connection is established. Which ensures it can’t be read by anyone intercepting the data.

6. **Data decryption and display**: The server decrypts the received data using the private key, processes it, and sends back the requested information. This data is also encrypted. The browser then decrypts the incoming data and displays the website content to the user.

## HTTP vs. HTTPS

Now that you know how HTTPS works, let’s quickly go over how it’s different from HTTP.

HTTP works differently from HTTPS on several different levels:

### Encryption

HTTP transfers data as plain text. This means anyone can easily intercept and read it.

HTTPS, on the other hand, leverages encryption to shield the data. So the information remains unintelligible and secure, even if it’s intercepted.

This means hackers would only see a scrambled sequence of characters rather than the actual information.

This is the main distinguishing factor between HTTP and HTTPS.

### Ports

Ports are like virtual doors information travels through between a browser and a website server. And each port is assigned a number.

Both HTTP and HTTPS use standard ports to facilitate communication.

HTTP typically uses port 80 as its default—this was established early in the development of the web for sending and receiving content.

HTTPS uses port 443. Which is reserved for encrypted traffic.

### URL Format

A uniform resource locator ([URL](https://www.semrush.com/blog/what-is-a-url/)) serves as the address for locating resources on the internet. And it’s formatted slightly differently for HTTP and HTTPS.

HTTPS URLs begin with “https://.” Which indicates a secure connection.

But HTTP URLs start with “http://.” And the missing “s” signifies the absence of security.

### SSL/TLS Certificate

Keep in mind what we said earlier about how an SSL/TLS certificate is a digital document that proves a website’s identity and authenticity.

This added level of verification is only used in HTTPS communication—not in traditional HTTP communication.

**Further reading**: [HTTP vs. HTTPS: What’s the Difference?](https://www.semrush.com/blog/http-vs-https/)

## Advantages of HTTPS

We’ve covered some of the benefits of HTTPS already, but here’s a quick refresher in case you need reminding (plus, some additional benefits):

### Enhanced Data Privacy

HTTPS protects users’ privacy. So their sensitive information (such as credit card numbers or login details) remains confidential and inaccessible to hackers.

Compare that to HTTP. Where the data is sent in clear text and can be easily intercepted. Which leaves users’ privacy at risk.

They’re vulnerable to attacks like [man-in-the-middle](https://en.wikipedia.org/wiki/Man-in-the-middle_attack), [packet sniffing](https://en.wikipedia.org/wiki/Sniffing_attack), and [session hijacking](https://en.wikipedia.org/wiki/Session_hijacking).

The encryption used in HTTPS connections prevents these attacks by fully securing data that flows between a browser and a website’s server.

### Enhanced User Experience

HTTPS positively impacts the user experience because it fosters a sense of trust in users when they’re browsing, shopping, or sharing information online.

Users are becoming increasingly aware that they should look for the padlock symbol to confirm whether a website is safe

This means that websites using HTTPS could be more likely to retain visitors, reduce their [bounce rates](https://www.semrush.com/blog/bounce-rate/), and potentially increase conversion rates (as users feel more comfortable making transactions).

### Better SEO Rankings

HTTPS can boost your website’s ranking and visibility on search engines like Google.

Why?

Because Google uses HTTPS as a ranking signal. This means websites that use HTTPS are more likely to appear higher on search engine results pages (SERPs), attracting more organic traffic and potential customers.

If you’re serious about SEO, check your website for HTTPS issues. Which are common among sites that have recently migrated from HTTP to HTTPS.

These issues include:

[Internal links](https://www.semrush.com/blog/internal-links/)(links on your pages that point to other pages on your site) that haven’t been updated to HTTPS (after migration)- Mixed content issues where other resources on a webpage (such as images and CSS files) are still being served over HTTP
- A mismatch between the name your SSL/TLS certificate is registered under and the name displayed in the browser’s address bar

And more.

You can check your site for all these issues using Semrush’s [Site Audit](https://www.semrush.com/siteaudit/) tool.

Open the tool, enter your website URL, and click “**Start Audit**.”

The tool will prompt you to [set up a project](https://www.semrush.com/kb/539-configuring-site-audit). After everything is configured, it’ll start auditing your site.

Once the audit is complete, go to the “HTTPS” section under the “Thematics Reports” module in the “Overview” tab.

And click on the “**View details**” button.

You’ll see how your site is doing across multiple HTTPS-related issues.

Issues are highlighted with the exclamation mark symbol and the orange outline.

You can also learn more about a particular issue by clicking on the “**Learn more**” link or the “**Why and how to fix it**” link under each item.

From there, you can learn how to fix any specific issues.

Now, back to the benefits of HTTPS.

### Compatibility with Browsers

Major browsers like Chrome, Firefox, Microsoft Edge, and Safari have supported HTTPS encryption and the key security protocols involved for many years now.

So, there’s no need to worry about your website visitors not being able to access an HTTPS site—unless they’re using extremely outdated software. Which virtually no one does.

## FAQs

To wrap things up, we’ll cover some frequently asked questions about HTTPS.

### What Does HTTPS Stand For?

HTTPS stands for hypertext transfer protocol secure. It's the secure, encrypted version of the standard HTTP web protocol.

### Is HTTPS Better Than HTTP?

HTTPS is far superior to regular, unencrypted HTTP.

HTTPS connections are encrypted through SSL/TLS certificates. This means HTTPS ensures visitors connect to the real website and that their data is secure from hackers.

HTTP has no encryption at all. So, it leaves websites and visitors vulnerable to attacks.

### What Does the ‘S’ in HTTPS Stand For?

The "S" in HTTPS stands for secure. It differentiates the encrypted HTTPS protocol from regular, unencrypted HTTP communication.

### What Port Does HTTPS Use?

HTTPS uses port 443 by default instead of HTTP's port 80.

Port 443 lets you access websites securely with encryption.

### How Do You Know if Your Site Uses HTTPS?

To confirm that your site is running on HTTPS, click on the tune icon next to the URL in the browser’s address bar and look for the padlock sign. And ensure the URL begins with “https://” rather than “http://.”

Additionally, modern browsers may provide a “Not secure” warning if a site is served over HTTP.

### How Do You Check for HTTPS-Related Issues?

There are multiple tools that can help you find HTTPS-related issues on your website.

One option is [Site Audit](https://www.semrush.com/siteaudit/). It checks your site for 11 different HTTPS-related issues. And presents the results in a report like this:

## Next Steps

Now that you know what HTTPS is, how it works, and what benefits it offers, you might be wondering what to do next.

Try expanding your knowledge about HTTPS with these resources:
