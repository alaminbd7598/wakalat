"""Shared site data, layout (head/header/footer) and HTML helpers."""
from .icons import ic

SITE = {
    'name': 'Wakalat Travel & Migration Ltd.',
    'short': 'Wakalat',
    'tagline': 'Your Trusted Partner for Travel & Migration',
    'url': 'https://wakalat.com',
    'phone': '+880 1886-270118',
    'phone_raw': '+8801886270118',
    'wa': '8801886270118',
    'email': 'nurmohammed8789@gmail.com',
    'address_short': 'Shah Ali Plaza, Mirpur-10, Dhaka-1216',
    'address': 'Office Space 1310 (B), 13th Floor (Lift 12), Shah Ali Plaza, Mirpur-10, Dhaka-1216, Bangladesh',
    'hours': 'Sat – Thu: 10:00 AM – 7:00 PM',
    'rjsc': 'C-197128',
    'mocat': '0017119',
    'mocat_valid': '21 Apr 2026 – 20 Apr 2029',
    'trade': 'TRAD/DNCC/016549/2024',
    'trade_valid': 'Valid till 30 June 2027',
    'md': 'Nur Mohammed',
    'director': 'Hasna Khanam',
    'fb': 'https://www.facebook.com/',
    'ig': 'https://www.instagram.com/',
    'li': 'https://www.linkedin.com/',
    'yt': 'https://www.youtube.com/',
}
SITE['wa_link'] = f"https://wa.me/{SITE['wa']}?text=" + 'Hello%20Wakalat%20Travel%2C%20I%20would%20like%20to%20know%20about%20'

# Unsplash CDN photos (hot-linked); every <img> has a graceful gradient fallback.
def U(pid, w=900):
    return f'https://images.unsplash.com/{pid}?auto=format&fit=crop&w={w}&q=70'

IMG = {
    'hero': U('photo-1436491865332-7a61a109cc05', 1800),
    'hero2': U('photo-1488085061387-422e29b40080', 1800),
    'about': U('photo-1488646953014-85cb44e25828'),
    'team': U('photo-1521737604893-d14cc237f11d'),
    'support': U('photo-1573497019940-1c28c88b4f3e'),
    'passport': U('photo-1544377193-33dcf4d68fb5'),
    'student': U('photo-1523240795612-9a054b0db644'),
    'airport': U('photo-1569154941061-e231b4725ef1'),
    'makkah': U('photo-1591604129939-f1efa4d9f7fa'),
    'madinah': U('photo-1565552645632-d725f8bfc19a'),
    'dubai': U('photo-1512453979798-5ea266f8880c'),
    'kl': U('photo-1596422846543-75c6fc197f07'),
    'bangkok': U('photo-1508009603885-50cf7c579365'),
    'singapore': U('photo-1525625293386-3f8f99389edd'),
    'maldives': U('photo-1514282401047-d79a71a590e8'),
    'bali': U('photo-1537996194471-e657df975ab4'),
    'istanbul': U('photo-1524231757912-21f4fe3a7200'),
    'cappadocia': U('photo-1519817650390-64a93db51149'),
    'london': U('photo-1513635269975-59663e0ac1ad'),
    'paris': U('photo-1502602898657-3e91760cbb34'),
    'india': U('photo-1548013146-72479768bada'),
    'kashmir': U('photo-1566837497312-7be7830ae9b1'),
    'nepal': U('photo-1544735716-392fe2489ffa'),
    'coxsbazar': U('photo-1621330396173-e41b1cafd17f'),
    'sundarbans': U('photo-1583417319070-4a69db38a482'),
    'sylhet': U('photo-1566043641507-95a1226a03c5'),
    'hotel1': U('photo-1566073771259-6a8506099945'),
    'hotel2': U('photo-1520250497591-112f2f40a3f4'),
    'hotel3': U('photo-1551882547-ff40c63fe5fa'),
    'hotel4': U('photo-1571896349842-33c89424de2d'),
    'beach': U('photo-1552465011-b4e21bf6e79a'),
    'mountain': U('photo-1500530855697-b586d89ba3ee'),
    'flight': U('photo-1569629743817-70d8db6c323b'),
    'canada': U('photo-1517935706615-2717063c2225'),
    'australia': U('photo-1523482580672-f109ba8cb9be'),
    'usa': U('photo-1485738422979-f5c462d49f74'),
    'uk': U('photo-1486299267070-83823f5448dd'),
    'europe': U('photo-1467269204594-9661b134dd2b'),
    'qatar': U('photo-1539650116574-8efeb43e2750'),
}

NAV = [
    ('Home', 'index.html', None),
    ('Flights', 'flights.html', None),
    ('Hotels', 'hotels.html', None),
    ('Tour Packages', 'tours.html', None),
    ('Visa', 'visa.html', [
        ('Tourist Visa', 'visa.html#tourist', 'globe'),
        ('Student Visa', 'visa.html#student', 'graduation'),
        ('Work & Migration', 'visa.html#work', 'briefcase'),
        ('Medical Visa', 'visa.html#medical', 'medical'),
        ('Business Visa', 'visa.html#business', 'building'),
    ]),
    ('Hajj & Umrah', 'hajj-umrah.html', None),
    ('More', '#', [
        ('All Services', 'services.html', 'compass'),
        ('About Us', 'about.html', 'users'),
        ('Contact Us', 'contact.html', 'phone'),
        ('FAQs', 'faqs.html', 'info'),
        ('Baggage Information', 'baggage-information.html', 'luggage'),
    ]),
]

def head(title, desc, slug):
    full = f"{title} | {SITE['name']}" if slug != 'index.html' else f"{SITE['name']} | Air Ticket, Visa, Hajj & Umrah, Tours"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#E8000D">
<link rel="canonical" href="{SITE['url']}/{'' if slug=='index.html' else slug}">
<meta property="og:title" content="{full}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE['url']}/assets/img/og-cover.png">
<link rel="icon" type="image/svg+xml" href="assets/img/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Comfortaa:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"TravelAgency","name":"{SITE['name']}","telephone":"{SITE['phone_raw']}","email":"{SITE['email']}","url":"{SITE['url']}","address":{{"@type":"PostalAddress","streetAddress":"Office Space 1310 (B), Shah Ali Plaza, Mirpur-10","addressLocality":"Dhaka","postalCode":"1216","addressCountry":"BD"}},"openingHours":"Sa-Th 10:00-19:00","priceRange":"$$"}}</script>
</head>
<body>'''

def topbar():
    return f'''
<div class="topbar">
  <div class="container">
    <ul>
      <li>{ic('phone')}<a href="tel:{SITE['phone_raw']}">{SITE['phone']}</a></li>
      <li class="hide-m">{ic('mail')}<a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
      <li class="hide-m">{ic('clock')}{SITE['hours']}</li>
    </ul>
    <div class="social">
      <a href="{SITE['fb']}" aria-label="Facebook" target="_blank" rel="noopener">{ic('facebook')}</a>
      <a href="{SITE['ig']}" aria-label="Instagram" target="_blank" rel="noopener">{ic('instagram')}</a>
      <a href="{SITE['li']}" aria-label="LinkedIn" target="_blank" rel="noopener">{ic('linkedin')}</a>
      <a href="{SITE['yt']}" aria-label="YouTube" target="_blank" rel="noopener">{ic('youtube')}</a>
      <a href="https://wa.me/{SITE['wa']}" aria-label="WhatsApp" target="_blank" rel="noopener">{ic('whatsapp')}</a>
    </div>
  </div>
</div>'''

def header():
    items = []
    mitems = []
    for label, href, sub in NAV:
        if sub:
            dd = ''.join(f'<a href="{h}">{ic(i)}{l}</a>' for l, h, i in sub)
            items.append(f'<li><a href="{href}">{label}{ic("chevron-down")}</a><div class="dropdown">{dd}</div></li>')
            msub = ''.join(f'<a href="{h}">{l}</a>' for l, h, i in sub)
            mitems.append(f'<li><a href="{href}" class="has-sub">{label}{ic("chevron-down")}</a><div class="sub">{msub}</div></li>')
        else:
            items.append(f'<li><a href="{href}">{label}</a></li>')
            mitems.append(f'<li><a href="{href}">{label}</a></li>')
    return f'''
<header class="header">
  <div class="container">
    <a class="logo" href="index.html" aria-label="{SITE['name']}"><img src="assets/img/logo.svg" alt="{SITE['name']}" width="270" height="70"></a>
    <ul class="nav">{''.join(items)}</ul>
    <div class="header-cta">
      <a class="btn btn-outline btn-sm" href="login.html">{ic('user')}Login</a>
      <a class="btn btn-primary btn-sm" href="contact.html">{ic('send')}Get a Quote</a>
      <button class="burger" aria-label="Open menu">{ic('menu')}</button>
    </div>
  </div>
</header>
<div class="drawer" aria-hidden="true">
  <div class="backdrop"></div>
  <div class="panel">
    <div class="panel-head">
      <img src="assets/img/logo.svg" alt="{SITE['short']}" style="height:44px;width:auto">
      <button class="close" aria-label="Close menu">{ic('close')}</button>
    </div>
    <ul class="mnav">{''.join(mitems)}</ul>
    <div class="drawer-cta">
      <a class="btn btn-primary" href="contact.html">{ic('send')}Get a Quote</a>
      <a class="btn btn-outline" href="login.html">{ic('user')}Login / Register</a>
      <a class="btn btn-outline" href="tel:{SITE['phone_raw']}">{ic('phone')}{SITE['phone']}</a>
    </div>
  </div>
</div>'''

def footer():
    return f'''
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="about">
        <img src="assets/img/logo-white.svg" alt="{SITE['name']}" width="270" height="70">
        <p>{SITE['name']} is a Government-registered travel agency in Dhaka offering air ticketing, visa processing, Hajj &amp; Umrah packages, holiday tours and migration consultancy — all under one roof.</p>
        <div class="social">
          <a href="{SITE['fb']}" aria-label="Facebook" target="_blank" rel="noopener">{ic('facebook')}</a>
          <a href="{SITE['ig']}" aria-label="Instagram" target="_blank" rel="noopener">{ic('instagram')}</a>
          <a href="{SITE['li']}" aria-label="LinkedIn" target="_blank" rel="noopener">{ic('linkedin')}</a>
          <a href="{SITE['yt']}" aria-label="YouTube" target="_blank" rel="noopener">{ic('youtube')}</a>
        </div>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About Us</a></li>
          <li><a href="services.html">Our Services</a></li>
          <li><a href="contact.html">Contact Us</a></li>
          <li><a href="faqs.html">FAQs</a></li>
          <li><a href="login.html">Customer Login</a></li>
          <li><a href="register.html">Register</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="flights.html">Air Tickets</a></li>
          <li><a href="hotels.html">Hotel Booking</a></li>
          <li><a href="tours.html">Tour Packages</a></li>
          <li><a href="visa.html">Visa Processing</a></li>
          <li><a href="hajj-umrah.html">Hajj &amp; Umrah</a></li>
          <li><a href="visa.html#work">Migration &amp; Study Abroad</a></li>
        </ul>
      </div>
      <div>
        <h4>Support</h4>
        <ul>
          <li><a href="privacy-policy.html">Privacy Policy</a></li>
          <li><a href="terms-conditions.html">Terms &amp; Conditions</a></li>
          <li><a href="refund-policy.html">Refund Policy</a></li>
          <li><a href="baggage-information.html">Baggage Information</a></li>
          <li><a href="faqs.html">Help Center</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul class="contact-list">
          <li>{ic('map')}<span>{SITE['address']}</span></li>
          <li>{ic('phone')}<a href="tel:{SITE['phone_raw']}">{SITE['phone']}</a></li>
          <li>{ic('whatsapp')}<a href="https://wa.me/{SITE['wa']}" target="_blank" rel="noopener">WhatsApp: {SITE['phone']}</a></li>
          <li>{ic('mail')}<a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
          <li>{ic('clock')}<span>{SITE['hours']}</span></li>
        </ul>
      </div>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container">
      <div>&copy; <span class="year">2026</span> {SITE['name']} &middot; RJSC Reg. No. {SITE['rjsc']} &middot; MoCAT Travel Agency Reg. No. {SITE['mocat']}</div>
      <div class="pay"><span class="bkash">bKash</span><span class="nagad">Nagad</span><span class="rocket">Rocket</span><span class="visa">VISA</span><span class="mc">Mastercard</span><span>Bank Transfer</span><span>Cash</span></div>
    </div>
  </div>
</footer>
<a class="whatsapp-float" href="https://wa.me/{SITE['wa']}?text=Hello%20Wakalat%20Travel%2C%20I%20need%20help%20with%20my%20travel%20plan." target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{ic('whatsapp')}<span>Chat with us</span></a>
<button class="totop" aria-label="Back to top">{ic('arrow-up')}</button>
<script src="assets/js/main.js"></script>
</body>
</html>'''

def page(slug, title, desc, body):
    import re
    html = head(title, desc, slug) + topbar() + header() + body + footer()
    # every image gets a graceful broken-image fallback hook
    html = re.sub(r'<img (?![^>]*data-fallback)([^>]*?)>', r'<img data-fallback \1>', html)
    return html

def banner(title, subtitle, crumb, img):
    return f'''
<section class="page-banner">
  <img src="{img}" alt="" loading="eager">
  <div class="container">
    <div class="crumbs"><a href="index.html">Home</a><span class="sep">/</span><span class="cur">{crumb}</span></div>
    <h1>{title}</h1>
    <p>{subtitle}</p>
  </div>
</section>'''

# ---------- small component helpers ----------
def media(img_key, alt, tag=None, tag_cls='', icon='globe'):
    t = f'<span class="tag {tag_cls}">{tag}</span>' if tag else ''
    return f'<div class="media"><img src="{IMG[img_key]}" alt="{alt}" loading="lazy" data-fallback><div class="fallback">{ic(icon)}</div>{t}</div>'

def section_head(eyebrow, title, text='', left=False):
    p = f'<p>{text}</p>' if text else ''
    return f'<div class="section-head{" left" if left else ""} reveal"><span class="eyebrow">{eyebrow}</span><h2>{title}</h2>{p}</div>'

def field(label, name, kind='text', icon=None, placeholder='', options=None, value='', required=False, extra=''):
    req = ' required' if required else ''
    ico = ic(icon) if icon else ''
    plain = '' if icon else ' plain'
    if kind == 'select':
        opts = ''.join(f'<option value="{o}"{" selected" if o == value else ""}>{o}</option>' for o in options)
        ctl = f'<select name="{name}" data-label="{label}"{req}>{opts}</select>'
    elif kind == 'textarea':
        ctl = f'<textarea name="{name}" data-label="{label}" rows="4" placeholder="{placeholder}"{req}></textarea>'
    else:
        ctl = f'<input type="{kind}" name="{name}" data-label="{label}" placeholder="{placeholder}" value="{value}"{req}>'
    return f'<div class="field{plain} {extra}"><label>{label}</label><div class="control">{ico}{ctl}</div></div>'

CITIES = ['Dhaka (DAC)', 'Chittagong (CGP)', 'Sylhet (ZYL)', "Cox's Bazar (CXB)", 'Jeddah (JED)', 'Madinah (MED)', 'Riyadh (RUH)', 'Dubai (DXB)', 'Doha (DOH)', 'Abu Dhabi (AUH)', 'Muscat (MCT)', 'Kuala Lumpur (KUL)', 'Singapore (SIN)', 'Bangkok (BKK)', 'Kolkata (CCU)', 'Delhi (DEL)', 'Chennai (MAA)', 'Kathmandu (KTM)', 'Male (MLE)', 'Istanbul (IST)', 'London (LHR)', 'Toronto (YYZ)', 'New York (JFK)', 'Sydney (SYD)']

def search_widget(float_=True, active='flight'):
    tabs = [('flight', 'takeoff', 'Flight'), ('hotel', 'hotel', 'Hotel'), ('tour', 'umbrella', 'Tour'), ('visa', 'passport', 'Visa'), ('umrah', 'mosque', 'Hajj & Umrah')]
    tab_html = ''.join(f'<button type="button" data-tab="tab-{k}" class="{"active" if k == active else ""}">{ic(i)}{l}</button>' for k, i, l in tabs)
    trav = ['1 Traveller', '2 Travellers', '3 Travellers', '4 Travellers', '5+ Travellers / Group']
    cls = ['Economy', 'Premium Economy', 'Business', 'First Class']
    flight = f'''
<form class="search-panel{" active" if active == "flight" else ""}" id="tab-flight" data-wa="Flight Search Request">
  <div class="trip-type">
    <label><input type="radio" name="trip" value="Round Trip" data-label="Trip" checked> Round Trip</label>
    <label><input type="radio" name="trip" value="One Way" data-label="Trip"> One Way</label>
    <label><input type="radio" name="trip" value="Multi City" data-label="Trip"> Multi City</label>
  </div>
  <div class="fields">
    {field('From', 'from', 'select', 'takeoff', options=CITIES, value='Dhaka (DAC)')}
    {field('To', 'to', 'select', 'map', options=CITIES, value='Jeddah (JED)')}
    {field('Departure', 'departure', 'date', 'calendar', required=True)}
    {field('Return', 'return', 'date', 'calendar', extra='return-field')}
    {field('Travellers & Class', 'travellers', 'select', 'users', options=[f'{t} · {c}' for c in cls for t in trav][:20])}
    <button class="btn btn-primary" type="submit">{ic('search')}Search Flights</button>
  </div>
  <div class="search-note">{ic('check-circle')}Lowest fares on Biman, Saudia, Emirates, Qatar Airways, Turkish, Malaysia Airlines, AirAsia, US-Bangla &amp; more.</div>
</form>'''
    hotel = f'''
<form class="search-panel{" active" if active == "hotel" else ""}" id="tab-hotel" data-wa="Hotel Booking Request">
  <div class="fields f4">
    {field('City / Hotel', 'city', 'text', 'map', 'e.g. Makkah, Dubai, Kuala Lumpur', required=True)}
    {field('Check-in', 'checkin', 'date', 'calendar', required=True)}
    {field('Check-out', 'checkout', 'date', 'calendar', required=True)}
    {field('Rooms & Guests', 'guests', 'select', 'users', options=['1 Room · 2 Guests', '1 Room · 1 Guest', '2 Rooms · 4 Guests', '3 Rooms · 6 Guests', 'Group booking'])}
    <button class="btn btn-primary" type="submit">{ic('search')}Search Hotels</button>
  </div>
  <div class="search-note">{ic('check-circle')}Over 500,000 hotels worldwide, from budget stays to 5-star resorts near Haram.</div>
</form>'''
    tour = f'''
<form class="search-panel{" active" if active == "tour" else ""}" id="tab-tour" data-wa="Tour Package Enquiry">
  <div class="fields f4">
    {field('Destination', 'destination', 'select', 'compass', options=["Cox's Bazar", 'Sundarbans', 'Sylhet & Sreemangal', 'Saint Martin', 'Kuala Lumpur', 'Bangkok & Pattaya', 'Singapore', 'Dubai', 'Maldives', 'Bali', 'Istanbul & Cappadocia', 'Kashmir', 'Nepal', 'Egypt', 'Europe'])}
    {field('Travel Date', 'date', 'date', 'calendar', required=True)}
    {field('Duration', 'duration', 'select', 'clock', options=['2 Nights 3 Days', '3 Nights 4 Days', '4 Nights 5 Days', '5 Nights 6 Days', '7+ Nights'])}
    {field('Travellers', 'travellers', 'select', 'users', options=['2 Adults', '1 Adult', '2 Adults + 1 Child', '2 Adults + 2 Children', 'Family / Group (5+)'])}
    <button class="btn btn-primary" type="submit">{ic('search')}Find Packages</button>
  </div>
  <div class="search-note">{ic('check-circle')}Customisable holiday packages with flights, hotels, transfers and sightseeing.</div>
</form>'''
    visa = f'''
<form class="search-panel{" active" if active == "visa" else ""}" id="tab-visa" data-wa="Visa Assistance Request">
  <div class="fields f4">
    {field('Country', 'country', 'select', 'globe', options=['Saudi Arabia', 'UAE (Dubai)', 'Qatar', 'Malaysia', 'Singapore', 'Thailand', 'India', 'Turkey', 'China', 'United Kingdom', 'Schengen (Europe)', 'USA', 'Canada', 'Australia', 'Japan', 'South Korea', 'Other'])}
    {field('Visa Type', 'visa_type', 'select', 'passport', options=['Tourist Visa', 'Business Visa', 'Student Visa', 'Work / Employment Visa', 'Medical Visa', 'Family / Visit Visa'])}
    {field('Applicants', 'applicants', 'select', 'users', options=['1 Applicant', '2 Applicants', '3 Applicants', '4+ Applicants'])}
    {field('Your Mobile', 'mobile', 'tel', 'phone', '01XXX-XXXXXX', required=True)}
    <button class="btn btn-primary" type="submit">{ic('send')}Apply for Visa</button>
  </div>
  <div class="search-note">{ic('check-circle')}Document checklist, form filling, appointment booking and embassy submission by our visa experts.</div>
</form>'''
    umrah = f'''
<form class="search-panel{" active" if active == "umrah" else ""}" id="tab-umrah" data-wa="Hajj / Umrah Package Enquiry">
  <div class="fields f4">
    {field('Package', 'package', 'select', 'mosque', options=['Umrah – Economy', 'Umrah – Standard', 'Umrah – Premium (5★ near Haram)', 'Ramadan Umrah', 'Hajj 2027', 'Custom Group Umrah'])}
    {field('Preferred Month', 'month', 'month', 'calendar', required=True)}
    {field('Pilgrims', 'pilgrims', 'select', 'users', options=['1 Pilgrim', '2 Pilgrims', '3–4 Pilgrims', '5–10 Pilgrims', 'Group (10+)'])}
    {field('Your Mobile', 'mobile', 'tel', 'phone', '01XXX-XXXXXX', required=True)}
    <button class="btn btn-primary" type="submit">{ic('send')}Get Package Details</button>
  </div>
  <div class="search-note">{ic('check-circle')}Includes visa, return air ticket, hotel, transport, Ziyarah and experienced Bangla-speaking guide.</div>
</form>'''
    return f'''
<div class="search-box{" float" if float_ else ""}">
  <div class="search-tabs">{tab_html}</div>
  {flight}{hotel}{tour}{visa}{umrah}
</div>'''

def cta_banner(title, text, btn1=('Get a Free Quote', 'contact.html'), btn2=('WhatsApp Us', None)):
    b2href = btn2[1] or f"https://wa.me/{SITE['wa']}"
    return f'''
<section class="section" style="padding-top:0">
  <div class="container">
    <div class="cta-banner reveal">
      <div><h2>{title}</h2><p>{text}</p></div>
      <div class="actions"><a class="btn btn-white" href="{btn1[1]}">{ic('send')}{btn1[0]}</a><a class="btn btn-ghost" href="{b2href}" target="_blank" rel="noopener">{ic('whatsapp')}{btn2[0]}</a></div>
    </div>
  </div>
</section>'''

def faq_list(items):
    return '<div class="faq">' + ''.join(f'<div class="faq-item"><button type="button">{q}{ic("plus")}</button><div class="ans">{a}</div></div>' for q, a in items) + '</div>'

def testimonials():
    t = [
        ('Md. Rafiqul Islam', 'Umrah Pilgrim, Mirpur', 'Alhamdulillah, our family Umrah with Wakalat was smooth from visa to hotel near Haram. The guide was very helpful and everything was arranged exactly as promised.', 'R'),
        ('Sadia Afrin', 'Student, Malaysia', 'They handled my student visa file for Malaysia with full transparency. Every document was checked carefully and I got my visa within the expected time.', 'S'),
        ('Tanvir Ahmed', 'Business Traveller, Dhaka', 'I book all my Dubai and Singapore tickets through Wakalat. Best fares, quick response on WhatsApp and no hidden charges. Highly recommended.', 'T'),
    ]
    stars = ''.join(ic('star') for _ in range(5))
    cards = ''.join(f'<div class="testi reveal"><span class="quote">{ic("quote")}</span><div class="stars">{stars}</div><p>“{q}”</p><div class="who"><div class="av">{av}</div><div><b>{n}</b><span>{w}</span></div></div></div>' for n, w, q, av in t)
    return f'''
<section class="section soft">
  <div class="container">
    {section_head('Testimonials', 'What Our Travellers Say', 'Real experiences shared by customers who travel with us every month.')}
    <div class="testi-track">{cards}</div>
  </div>
</section>'''

def trust_section():
    return f'''
<section class="section">
  <div class="container">
    {section_head('Licensed & Registered', 'A Government-Approved Travel Agency', 'Wakalat Travel &amp; Migration Ltd. is fully registered with the authorities of Bangladesh, so you can book with complete confidence.')}
    <div class="trust">
      <div class="trust-card reveal"><div class="seal">{ic('award')}</div><h3>Ministry of Civil Aviation &amp; Tourism</h3><div class="no">Reg. No. {SITE['mocat']}</div><p>Registered Travel Agency under the Bangladesh Travel Agency (Registration &amp; Control) Act, 2013. Valid {SITE['mocat_valid']}.</p></div>
      <div class="trust-card reveal"><div class="seal">{ic('building')}</div><h3>RJSC Incorporated Company</h3><div class="no">Reg. No. {SITE['rjsc']}</div><p>A private company limited by shares, incorporated under the Companies Act, 1994 with the Registrar of Joint Stock Companies &amp; Firms.</p></div>
      <div class="trust-card reveal"><div class="seal">{ic('shield')}</div><h3>Dhaka North City Corporation</h3><div class="no">{SITE['trade']}</div><p>Trade License for Air Ticketing, Travel Agency &amp; Visa Processing. {SITE['trade_valid']}.</p></div>
    </div>
  </div>
</section>'''
