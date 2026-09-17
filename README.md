# Wakalat Travel & Migration Ltd. — Website

Official website of **Wakalat Travel & Migration Ltd.**, a MoCAT-registered travel agency at Shah Ali Plaza, Mirpur-10, Dhaka.
Static HTML/CSS/JS — no framework, no build server needed to host.

## Pages

| Page | File |
|------|------|
| Home (hero, search widget, services, routes, deals, destinations, Umrah packages, stats, steps, airlines, testimonials, licences, FAQ, newsletter) | `index.html` |
| Flights | `flights.html` |
| Hotels | `hotels.html` |
| Tour Packages | `tours.html` |
| Visa (tourist / student / work & migration / medical / business) | `visa.html` |
| Hajj & Umrah | `hajj-umrah.html` |
| All Services | `services.html` |
| About Us | `about.html` |
| Contact (WhatsApp form + Google Map) | `contact.html` |
| FAQs | `faqs.html` |
| Privacy Policy · Terms & Conditions · Refund Policy · Baggage Information | `privacy-policy.html` … |
| Login / Register (UI only, portal coming soon) | `login.html`, `register.html` |
| 404 | `404.html` |

## How it works

* All forms (flight/hotel/tour/visa/Umrah search, contact) open **WhatsApp** (`+880 1886-270118`) with the request pre-filled — no backend required.
* Photos are hot-linked from Unsplash; if an image fails to load a branded gradient placeholder is shown automatically.
* Brand assets: `assets/img/logo.svg`, `logo-white.svg`, `logo-black.svg`, `logo.png`, `favicon.svg`, `og-cover.png`.

## Editing content

Pages are generated from Python templates so header, footer and company details stay consistent:

```bash
python3 tools/build.py        # regenerates all *.html, sitemap.xml, robots.txt
```

* Company details (phone, email, address, registration numbers, social links, website URL) → `tools/wsite/layout.py` (`SITE` dict).
* Home page content → `tools/wsite/pages_home.py`; service pages → `pages_services.py`; about/contact/FAQ/legal → `pages_info.py`.
* Styles → `assets/css/style.css`; behaviour → `assets/js/main.js`.

You can also edit the generated HTML files directly if you prefer.

## Deploy

Any static host works (GitHub Pages, Netlify, Vercel, cPanel). For GitHub Pages: Settings → Pages → deploy from the branch root.
Update `SITE['url']` in `tools/wsite/layout.py` to the final domain and rebuild so canonical URLs and the sitemap are correct.
