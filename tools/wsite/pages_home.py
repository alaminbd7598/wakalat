from .icons import ic
from .layout import *

def build():
    services = [
        ('takeoff', 'Air Ticketing', 'Domestic & international air tickets on all major airlines at the lowest available fares, with instant confirmation.', 'flights.html'),
        ('passport', 'Visa Processing', 'Tourist, business, student, medical and work visas — full documentation support and embassy submission.', 'visa.html'),
        ('mosque', 'Hajj & Umrah', 'Complete Umrah and Hajj packages with visa, flights, hotels near Haram, transport, Ziyarah and guide.', 'hajj-umrah.html'),
        ('umbrella', 'Holiday Packages', 'Customised domestic and international tour packages for families, honeymooners, students and corporates.', 'tours.html'),
        ('hotel', 'Hotel Booking', 'Best rates at 500,000+ hotels worldwide, from budget rooms to luxury 5-star resorts.', 'hotels.html'),
        ('briefcase', 'Migration & Study Abroad', 'Guidance for study permits, skilled migration and overseas employment, subject to government approval.', 'visa.html#work'),
    ]
    svc = ''.join(f'<a class="card service-card reveal" href="{h}"><div class="icon">{ic(i)}</div><h3>{t}</h3><p>{d}</p><span class="link">Explore {ic("arrow-right")}</span></a>' for i, t, d, h in services)

    features = [
        ('shield', 'Govt. Licensed Agency', 'Registered with MoCAT (No. 0017119), RJSC and DNCC — a legally compliant travel partner.'),
        ('wallet', 'Best Price Guarantee', 'Direct airline & consolidator fares mean you always get competitive, transparent pricing.'),
        ('headset', '24/7 Customer Support', 'Reach us on phone, WhatsApp or email any time — before, during and after your journey.'),
        ('clipboard', 'Expert Visa Team', 'Experienced consultants prepare your file to maximise approval chances the first time.'),
        ('lock', 'Secure Payments', 'Pay by bKash, Nagad, Rocket, card or bank transfer with proper receipts for every payment.'),
        ('heart', 'Personalised Service', 'Every trip is planned around your budget, dates and preferences — no one-size-fits-all.'),
    ]
    feat = ''.join(f'<div class="feature reveal"><div class="icon">{ic(i)}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in features)

    routes = [
        ('Dhaka → Jeddah', 'DAC – JED · Saudia / Biman', '52,900'), ('Dhaka → Dubai', 'DAC – DXB · Emirates / flydubai', '38,500'),
        ('Dhaka → Kuala Lumpur', 'DAC – KUL · Malaysia Airlines / AirAsia', '27,900'), ('Dhaka → Singapore', 'DAC – SIN · Singapore Airlines / Biman', '34,200'),
        ('Dhaka → Bangkok', 'DAC – BKK · Thai Airways / US-Bangla', '26,500'), ('Dhaka → Doha', 'DAC – DOH · Qatar Airways', '41,800'),
        ('Dhaka → Riyadh', 'DAC – RUH · Saudia / Biman', '49,900'), ('Dhaka → Kolkata', 'DAC – CCU · Biman / IndiGo', '9,800'),
        ('Dhaka → London', 'DAC – LHR · Biman / Qatar Airways', '92,000'), ("Dhaka → Cox's Bazar", 'DAC – CXB · Biman / US-Bangla / NovoAir', '4,500'),
    ]
    rts = ''.join(f'<a class="route reveal" href="flights.html"><div class="plane">{ic("takeoff")}</div><div class="cities"><b>{a}</b><span>{b}</span></div><div class="fare"><small>Starting from</small><b>BDT {c}</b></div></a>' for a, b, c in routes)

    deals = [
        ('umrah_deal', 'makkah', 'Umrah Special', 'Ramadan Umrah Package 2027', '14 days · 5★ hotels walking distance from Haram · Saudia direct flight · Ziyarah included.', 'BDT 1,85,000', 'per person', 'hajj-umrah.html', 'gold'),
        ('kl_deal', 'kl', 'Save 15%', 'Kuala Lumpur & Genting Getaway', '4 nights 5 days · 4★ hotel · Airport transfers · Batu Caves & Genting Highlands tour.', 'BDT 58,900', 'per person', 'tours.html', ''),
        ('dubai_deal', 'dubai', 'Hot Deal', 'Dubai Discovery Tour', '5 nights 6 days · Desert safari · Burj Khalifa · Dhow cruise · Visa & flights included.', 'BDT 89,500', 'per person', 'tours.html', ''),
    ]
    dls = ''.join(f'<a class="card reveal" href="{h}">{media(img, t, tag, tc, "gift")}<div class="body"><h3>{t}</h3><p>{d}</p><div class="meta"><span class="price">{p} <small>{pu}</small></span><span class="btn btn-outline btn-sm">Book Now</span></div></div></a>' for _, img, tag, t, d, p, pu, h, tc in deals)

    dests = [
        ('makkah', 'Makkah & Madinah', 'Saudi Arabia', 'Umrah & Hajj'), ('dubai', 'Dubai', 'United Arab Emirates', 'From BDT 38,500'),
        ('kl', 'Kuala Lumpur', 'Malaysia', 'From BDT 27,900'), ('bangkok', 'Bangkok', 'Thailand', 'From BDT 26,500'),
        ('singapore', 'Singapore', 'Singapore', 'From BDT 34,200'), ('maldives', 'Maldives', 'Indian Ocean', 'Honeymoon special'),
        ('istanbul', 'Istanbul', 'Türkiye', 'From BDT 68,000'), ('coxsbazar', "Cox's Bazar", 'Bangladesh', 'From BDT 4,500'),
    ]
    dst = ''.join(f'<a class="card reveal" href="tours.html">{media(k, t)}<div class="body"><h3>{t}</h3><p>{c}</p><div class="meta"><span>{ic("takeoff")} {f}</span><span style="color:var(--red);font-weight:600">View</span></div></div></a>' for k, t, c, f in dests)

    pkgs = [
        ('Economy Umrah', '14 Days', '1,45,000', ['Umrah visa & insurance', 'Return air ticket (Dhaka–Jeddah)', '3★ hotel 500–800m from Haram', 'Makkah–Madinah AC transport', 'Ziyarah in Makkah & Madinah', 'Bangla-speaking guide'], False),
        ('Standard Umrah', '14 Days', '1,75,000', ['Umrah visa & insurance', 'Return air ticket (Saudia / Biman)', '4★ hotel 200–400m from Haram', 'Private AC transport', 'Ziyarah in Makkah & Madinah', 'Daily breakfast & guide'], True),
        ('Premium Umrah', '10–14 Days', '2,45,000', ['Umrah visa & insurance', 'Direct flight (Saudia / Biman)', '5★ hotel (Clock Tower / Haram view)', 'VIP private transport', 'Full board meals', 'Dedicated Moallem & guide'], False),
    ]
    RIB = '<span class="ribbon">POPULAR</span>'
    def pkg_card(n, d, p, inc, f):
        items = ''.join(f'<li>{ic("check")}{x}</li>' for x in inc)
        return (f'<div class="card pkg{" featured" if f else ""} reveal">{RIB if f else ""}<div class="body"><span class="eyebrow">{d}</span><h3>{n}</h3>'
                f'<div class="price" style="font-size:26px;color:var(--red);font-weight:700">BDT {p} <small style="font-size:12px;color:var(--muted)">/ person</small></div>'
                f'<ul class="list">{items}</ul><a class="btn btn-primary btn-block" style="margin-top:18px" href="hajj-umrah.html">View Package</a></div></div>')
    pk = ''.join(pkg_card(*x) for x in pkgs)

    steps = [
        ('Tell Us Your Plan', 'Search on the website or message us on WhatsApp with your destination, dates and travellers.'),
        ('Get the Best Options', 'Our consultants share the lowest fares, hotel choices or visa checklist within minutes.'),
        ('Confirm & Pay Securely', 'Pay via bKash, Nagad, card or bank transfer and receive an official receipt.'),
        ('Travel Worry-Free', 'Receive e-tickets, vouchers and visa on time — with 24/7 support during your trip.'),
    ]
    st = ''.join(f'<div class="step reveal"><div class="n">{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))

    airlines = ['Biman Bangladesh Airlines', 'US-Bangla Airlines', 'NovoAir', 'Saudia', 'Emirates', 'Qatar Airways', 'Etihad Airways', 'Turkish Airlines', 'Malaysia Airlines', 'Singapore Airlines', 'Thai Airways', 'AirAsia', 'flydubai', 'Air Arabia', 'IndiGo', 'SriLankan Airlines', 'Cathay Pacific', 'China Southern']
    al = ''.join(f'<span class="partner">{ic("takeoff")}{a}</span>' for a in airlines)

    faqs = [
        ('Is Wakalat Travel & Migration Ltd. a government-approved agency?', f'Yes. We are registered with the Ministry of Civil Aviation &amp; Tourism (Travel Agency Reg. No. {SITE["mocat"]}), incorporated with RJSC (No. {SITE["rjsc"]}) and hold a valid DNCC trade license.'),
        ('How do I book an air ticket?', 'Use the flight search on our website, call us or send a WhatsApp message with your route and dates. We will share the best fares and issue your e-ticket after payment.'),
        ('How long does visa processing take?', 'It depends on the country: Malaysia, Thailand and Dubai e-visas usually take 3–7 working days; Schengen, UK, USA and Canada can take 3–8 weeks. We give an estimated timeline before we start.'),
        ('What is included in your Umrah packages?', 'Umrah visa, return air ticket, hotel in Makkah and Madinah, airport & inter-city transport, Ziyarah and a Bangla-speaking guide. Meals depend on the package.'),
        ('What payment methods do you accept?', 'bKash, Nagad, Rocket, Visa/Mastercard, bank transfer and cash at our Mirpur-10 office.'),
    ]
    marquee = ''.join(f'<span>{ic("check-circle")}{x}</span>' for x in ['Govt. Registered Travel Agency', 'Lowest Air Fares Guaranteed', 'Umrah Packages from BDT 1,45,000', 'Visa Processing for 30+ Countries', 'Hotels Worldwide', '24/7 WhatsApp Support', 'Secure Online Payment'])

    body = f'''
<section class="hero">
  <div class="bg"><img src="{IMG['hero']}" alt="" loading="eager" fetchpriority="high"></div>
  <div class="container">
    <div class="hero-content">
      <span class="badge">{ic('award')} MoCAT Registered Travel Agency · Reg. No. {SITE['mocat']}</span>
      <h1>Your Trusted Partner for <span>Travel &amp; Migration</span></h1>
      <p>Air tickets, visa processing, Hajj &amp; Umrah, holiday packages and hotel booking — everything you need for a smooth journey, from Mirpur to the world.</p>
      <div class="hero-actions">
        <a class="btn btn-primary btn-lg" href="hajj-umrah.html">{ic('mosque')}Umrah Packages</a>
        <a class="btn btn-ghost btn-lg" href="https://wa.me/{SITE['wa']}" target="_blank" rel="noopener">{ic('whatsapp')}WhatsApp Us</a>
      </div>
      <div class="hero-stats">
        <div><b>5,000+</b><span>Happy Travellers</span></div>
        <div><b>30+</b><span>Visa Destinations</span></div>
        <div><b>18+</b><span>Airline Partners</span></div>
        <div><b>24/7</b><span>Customer Support</span></div>
      </div>
    </div>
  </div>
</section>
<div class="container">{search_widget(True)}</div>

<div class="marquee" style="margin-top:40px"><div>{marquee}{marquee}</div></div>

<section class="section">
  <div class="container">
    {section_head('Our Services', 'Everything for Your Journey, Under One Roof', 'From a single air ticket to a complete migration plan — Wakalat handles it end to end.')}
    <div class="grid grid-3">{svc}</div>
  </div>
</section>

<section class="section soft">
  <div class="container">
    <div class="split">
      <div class="media reveal"><img src="{IMG['about']}" alt="Planning a trip with Wakalat Travel" loading="lazy"><div class="float-card"><div class="num">2024</div><span>Serving travellers<br>since</span></div></div>
      <div class="reveal">
        <span class="eyebrow">Why Choose Wakalat</span>
        <h2>Travel With Confidence, Every Single Time</h2>
        <p>Wakalat Travel &amp; Migration Ltd. is a Dhaka-based, government-registered travel agency led by experienced professionals. We combine honest advice, competitive fares and round-the-clock support so that your journey — whether for Umrah, holiday, study or work — is stress-free.</p>
        <ul class="checklist">
          <li>{ic('check-circle')}Registered with MoCAT, RJSC &amp; Dhaka North City Corporation</li>
          <li>{ic('check-circle')}Transparent pricing with no hidden charges</li>
          <li>{ic('check-circle')}Dedicated consultant for every customer</li>
          <li>{ic('check-circle')}Office at Shah Ali Plaza, Mirpur-10 — visit us any day</li>
        </ul>
        <a class="btn btn-primary" href="about.html">{ic('arrow-right')}More About Us</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head('Why Us', 'The Wakalat Advantage', 'Six reasons thousands of travellers trust us with their most important journeys.')}
    <div class="grid grid-3">{feat}</div>
  </div>
</section>

<section class="section soft">
  <div class="container">
    {section_head('Popular Routes', 'Routes Travellers Are Searching Most', 'The 10 most requested routes this month with the lowest fares found. Fares are indicative and subject to availability.')}
    <div class="route-list">{rts}</div>
    <div style="text-align:center;margin-top:30px"><a class="btn btn-outline" href="flights.html">{ic('takeoff')}Search All Flights</a></div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head('Hot Deals', 'Exclusive Offers This Season', 'Limited-time packages hand-picked by our team. Book early for the best prices.')}
    <div class="grid grid-3">{dls}</div>
  </div>
</section>

<section class="section soft">
  <div class="container">
    {section_head('Popular Destinations', 'Where Would You Like to Go?', 'Explore the destinations our travellers love the most.')}
    <div class="grid grid-4">{dst}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head('Hajj &amp; Umrah', 'Umrah Packages 2026–27', 'Carefully designed packages for a peaceful and spiritually fulfilling pilgrimage. Group departures every month.')}
    <div class="grid grid-3">{pk}</div>
  </div>
</section>

<section class="section navy">
  <div class="container">
    {section_head('Our Numbers', 'Trusted by Travellers Across Bangladesh')}
    <div class="stats">
      <div class="stat reveal"><div class="num" data-count="5000" data-suffix="+">0<span>+</span></div><p>Happy Travellers</p></div>
      <div class="stat reveal"><div class="num" data-count="1200">0<span>+</span></div><p>Visas Processed</p></div>
      <div class="stat reveal"><div class="num" data-count="850">0<span>+</span></div><p>Umrah Pilgrims Served</p></div>
      <div class="stat reveal"><div class="num" data-count="30">0<span>+</span></div><p>Countries Covered</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head('How It Works', 'Book in 4 Simple Steps', 'No apps to install, no complicated forms — just fast, human service.')}
    <div class="steps">{st}</div>
  </div>
</section>

<section class="section soft">
  <div class="container">
    {section_head('Airline Partners', 'We Issue Tickets on All Major Airlines')}
    <div class="partners reveal">{al}</div>
  </div>
</section>

{testimonials()}
{trust_section()}

<section class="section soft">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Book on WhatsApp</span>
        <h2>Your Travel Desk, Right in Your Pocket</h2>
        <p>No need to download an app. Send us your travel plan on WhatsApp and receive fares, visa checklists and package details in minutes — anytime, anywhere.</p>
        <ul class="checklist">
          <li>{ic('check-circle')}Instant fare quotes &amp; e-ticket delivery</li>
          <li>{ic('check-circle')}Share documents securely for visa processing</li>
          <li>{ic('check-circle')}Track your Umrah or visa application status</li>
        </ul>
        <a class="btn btn-primary btn-lg" href="https://wa.me/{SITE['wa']}?text=Hello%20Wakalat%20Travel%2C%20I%20want%20to%20plan%20a%20trip." target="_blank" rel="noopener">{ic('whatsapp')}Chat on WhatsApp: {SITE['phone']}</a>
      </div>
      <div class="media reveal"><img src="{IMG['support']}" alt="Wakalat customer support" loading="lazy"><div class="float-card"><div class="num">24/7</div><span>Support on call,<br>WhatsApp &amp; email</span></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    {section_head('FAQ', 'Frequently Asked Questions')}
    {faq_list(faqs)}
    <div style="text-align:center;margin-top:26px"><a class="btn btn-outline" href="faqs.html">View All FAQs</a></div>
  </div>
</section>

<section class="section soft" style="padding-top:0">
  <div class="container">
    <div class="newsletter reveal">
      <div><h3>Get Deals Before Everyone Else</h3><p>Subscribe for Umrah offers, flight sales and visa updates. No spam, unsubscribe anytime.</p></div>
      <form data-demo="Thank you! You are subscribed to Wakalat deals."><input type="email" placeholder="Enter your email address" required><button class="btn btn-primary" type="submit">{ic('send')}Subscribe</button></form>
    </div>
  </div>
</section>
'''
    return {'index.html': page('index.html', 'Home', 'Wakalat Travel & Migration Ltd. — a MoCAT-registered travel agency in Mirpur, Dhaka. Air tickets, visa processing, Hajj & Umrah packages, holiday tours, hotel booking and migration consultancy.', body)}
