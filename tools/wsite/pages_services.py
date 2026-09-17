from .icons import ic
from .layout import *

def chk(items):
    return '<ul class="list">' + ''.join(f'<li>{ic("check")}{x}</li>' for x in items) + '</ul>'

def flights():
    classes = [
        ('Economy', 'Best value fares on every airline with standard baggage allowance. Ideal for holidays, Umrah groups and workers.'),
        ('Premium Economy', 'Extra legroom, priority boarding and better meals at a modest premium on long-haul routes.'),
        ('Business Class', 'Lie-flat seats, lounge access and generous baggage — perfect for executives and comfortable long journeys.'),
        ('First Class', 'The ultimate in luxury on Emirates, Qatar Airways, Singapore Airlines and more.'),
    ]
    cls = ''.join(f'<div class="card service-card reveal"><div class="icon">{ic("ticket")}</div><h3>{t}</h3><p>{d}</p></div>' for t, d in classes)
    why = [
        ('wallet', 'Lowest Fares', 'Access to airline, GDS and consolidator fares so you always pay less.'),
        ('bolt', 'Instant E-Tickets', 'Tickets issued and delivered by WhatsApp/email within minutes of payment.'),
        ('refresh', 'Date Change & Refund Help', 'We handle reissue, date change and refund requests with the airline on your behalf.'),
        ('users', 'Group & Corporate Fares', 'Special discounted fares for Umrah groups, workers, students and companies.'),
        ('luggage', 'Baggage Guidance', 'Clear information on baggage allowance for every airline before you fly.'),
        ('headset', 'Support During Travel', 'Missed connection or schedule change? Call us any time, we are here 24/7.'),
    ]
    wh = ''.join(f'<div class="feature reveal"><div class="icon">{ic(i)}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in why)
    dom = [("Dhaka → Cox's Bazar", '4,500'), ('Dhaka → Chittagong', '4,200'), ('Dhaka → Sylhet', '4,300'), ('Dhaka → Jashore', '3,900'), ('Dhaka → Saidpur', '4,100'), ('Dhaka → Rajshahi', '4,000'), ('Dhaka → Barishal', '3,800')]
    intl = [('Dhaka → Jeddah', '52,900'), ('Dhaka → Madinah', '54,500'), ('Dhaka → Riyadh', '49,900'), ('Dhaka → Dubai', '38,500'), ('Dhaka → Doha', '41,800'), ('Dhaka → Abu Dhabi', '39,900'), ('Dhaka → Muscat', '36,500'), ('Dhaka → Kuala Lumpur', '27,900'), ('Dhaka → Singapore', '34,200'), ('Dhaka → Bangkok', '26,500'), ('Dhaka → Kolkata', '9,800'), ('Dhaka → Delhi', '18,500'), ('Dhaka → Kathmandu', '17,900'), ('Dhaka → Male', '32,000'), ('Dhaka → Istanbul', '68,000'), ('Dhaka → London', '92,000'), ('Dhaka → Toronto', '1,25,000'), ('Dhaka → New York', '1,18,000')]
    rows = lambda L: ''.join(f'<tr><td>{a}</td><td>Economy · Round trip</td><td><b style="color:var(--red)">BDT {b}</b></td><td><a class="btn btn-outline btn-sm" href="#search">Get Fare</a></td></tr>' for a, b in L)
    body = banner('Air Tickets', 'Domestic & international flight tickets on 18+ airlines at the lowest fares — issued in minutes.', 'Flights', IMG['flight']) + f'''
<div class="container" id="search" style="margin-top:-40px;position:relative;z-index:5">{search_widget(False, 'flight')}</div>
<section class="section">
  <div class="container">
    {section_head('Why Book With Us', 'Air Ticketing Made Simple', 'We are an IATA-standard ticketing desk working directly with airlines and top consolidators of Bangladesh.')}
    <div class="grid grid-3">{wh}</div>
  </div>
</section>
<section class="section soft">
  <div class="container">
    {section_head('Fares', 'Indicative Fares from Dhaka', 'Starting fares for popular routes. Actual fares vary by date, airline and availability — contact us for a live quote.')}
    <div class="grid grid-2" style="align-items:start">
      <div class="reveal"><h3 style="margin-bottom:12px">International</h3><div class="table-wrap"><table><thead><tr><th>Route</th><th>Class</th><th>From</th><th></th></tr></thead><tbody>{rows(intl)}</tbody></table></div></div>
      <div class="reveal"><h3 style="margin-bottom:12px">Domestic</h3><div class="table-wrap"><table><thead><tr><th>Route</th><th>Class</th><th>From</th><th></th></tr></thead><tbody>{rows(dom)}</tbody></table></div>
        <div class="info-box" style="margin-top:20px"><b>Group travel?</b> Umrah groups, worker batches and corporate teams get special block fares. Ask us for a group quotation.</div></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    {section_head('Cabin Classes', 'Choose How You Fly')}
    <div class="grid grid-4">{cls}</div>
  </div>
</section>
{cta_banner('Need a ticket today?', 'Send your route and date on WhatsApp — we reply with the lowest fare within minutes and issue your e-ticket the same day.')}
'''
    return page('flights.html', 'Air Tickets', 'Book domestic and international air tickets at the lowest fares with Wakalat Travel & Migration Ltd., Dhaka. Biman, Saudia, Emirates, Qatar Airways, Malaysia Airlines, AirAsia and more.', body)

def hotels():
    hs = [
        ('hotel1', 'Makkah – Near Haram', '3★ to 5★ hotels within 100–800 m of Masjid al-Haram, including Clock Tower hotels.', '4,500'),
        ('hotel2', 'Madinah – Near Masjid Nabawi', 'Comfortable hotels steps from the Prophet\'s Mosque for a peaceful stay.', '3,800'),
        ('hotel3', 'Dubai', 'Beachfront resorts, Downtown Dubai and budget-friendly Deira hotels.', '6,500'),
        ('hotel4', 'Kuala Lumpur', 'Bukit Bintang and KLCC hotels close to shopping and attractions.', '3,900'),
        ('bangkok', 'Bangkok & Pattaya', 'Sukhumvit, Pratunam and beachside hotels for every budget.', '3,200'),
        ('coxsbazar', "Cox's Bazar", 'Sea-view hotels and resorts on the world\'s longest beach.', '3,500'),
        ('maldives', 'Maldives', 'Water villas and island resorts for honeymoons and family holidays.', '18,000'),
        ('singapore', 'Singapore', 'Marina Bay, Orchard Road and Little India hotels near MRT.', '7,800'),
    ]
    cards = ''.join(f'<div class="card reveal">{media(k, t)}<div class="body"><h3>{t}</h3><p>{d}</p><div class="meta"><span class="price">BDT {p} <small>/ night</small></span><a class="btn btn-outline btn-sm" href="#search">Enquire</a></div></div></div>' for k, t, d, p in hs)
    feats = [('wallet', 'Best Available Rates', 'Direct hotel contracts and global wholesalers for the best nightly rates.'), ('mosque', 'Haram-View Specialists', 'We know Makkah and Madinah hotels street by street — distance, view, shuttle and food.'), ('users', 'Family & Group Rooms', 'Connecting rooms, quad rooms and group blocks for Umrah and tour groups.'), ('check-circle', 'Confirmed Vouchers', 'Hotel confirmation vouchers issued instantly with your name and dates.')]
    ft = ''.join(f'<div class="feature reveal"><div class="icon">{ic(i)}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in feats)
    body = banner('Hotel Booking', 'Confirmed hotel reservations worldwide — from budget rooms to 5-star resorts near Haram.', 'Hotels', IMG['hotel1']) + f'''
<div class="container" id="search" style="margin-top:-40px;position:relative;z-index:5">{search_widget(False, 'hotel')}</div>
<section class="section">
  <div class="container">
    {section_head('Hotel Booking', 'Why Book Hotels With Wakalat')}
    <div class="grid grid-4">{ft}</div>
  </div>
</section>
<section class="section soft">
  <div class="container">
    {section_head('Popular Stays', 'Hotels Our Travellers Book Most', 'Indicative starting rates per night, subject to season and availability.')}
    <div class="grid grid-4">{cards}</div>
  </div>
</section>
{cta_banner('Looking for a hotel near Haram?', 'Tell us your dates, budget and preferred distance from Masjid al-Haram. We will send 3 best options with photos on WhatsApp.')}
'''
    return page('hotels.html', 'Hotel Booking', 'Book hotels in Makkah, Madinah, Dubai, Kuala Lumpur, Bangkok, Cox\'s Bazar and worldwide at the best rates with Wakalat Travel & Migration Ltd.', body)

def tours():
    intl = [
        ('kl', 'Kuala Lumpur & Genting', 'Malaysia', '4N/5D', '58,900', ['Return air ticket', '4★ hotel with breakfast', 'KL city tour & Batu Caves', 'Genting Highlands day trip', 'Airport transfers']),
        ('bangkok', 'Bangkok & Pattaya', 'Thailand', '4N/5D', '54,500', ['Return air ticket', '4★ hotels', 'Coral Island tour', 'Safari World & Marine Park', 'All transfers']),
        ('dubai', 'Dubai Discovery', 'UAE', '5N/6D', '89,500', ['Return air ticket & visa', '4★ hotel', 'Desert safari with BBQ', 'Burj Khalifa 124th floor', 'Dhow cruise dinner']),
        ('singapore', 'Singapore Highlights', 'Singapore', '3N/4D', '72,000', ['Return air ticket', '3★/4★ hotel', 'Universal Studios', 'Gardens by the Bay', 'Night safari']),
        ('maldives', 'Maldives Honeymoon', 'Maldives', '3N/4D', '1,15,000', ['Return air ticket', 'Beach / water villa', 'Speedboat transfers', 'Half board meals', 'Sunset cruise']),
        ('cappadocia', 'Istanbul & Cappadocia', 'Türkiye', '6N/7D', '1,45,000', ['Return air ticket & e-visa', '4★ hotels', 'Bosphorus cruise', 'Cappadocia cave hotel', 'Domestic flight']),
        ('bali', 'Bali Escape', 'Indonesia', '4N/5D', '78,000', ['Return air ticket', 'Private pool villa', 'Ubud & Kintamani tour', 'Uluwatu sunset', 'All transfers']),
        ('kashmir', 'Kashmir – Paradise on Earth', 'India', '5N/6D', '62,000', ['Return air ticket', 'Houseboat + hotel', 'Gulmarg gondola', 'Pahalgam & Sonmarg', 'Indian visa support']),
        ('nepal', 'Kathmandu & Pokhara', 'Nepal', '4N/5D', '42,000', ['Return air ticket', '3★ hotels', 'Pokhara lake & Sarangkot', 'Kathmandu heritage tour', 'On-arrival visa help']),
    ]
    dom = [
        ('coxsbazar', "Cox's Bazar Beach Break", 'Bangladesh', '3N/4D', '12,500', ['AC bus or air ticket', 'Sea-view hotel', 'Himchari & Inani beach', 'Marine Drive tour', 'Breakfast daily']),
        ('sundarbans', 'Sundarbans Mangrove Cruise', 'Bangladesh', '2N/3D', '14,500', ['AC launch from Khulna', 'All meals on board', 'Kotka & Karamjal', 'Forest guide & permits', 'Armed guard']),
        ('sylhet', 'Sylhet & Sreemangal Tea Trail', 'Bangladesh', '2N/3D', '9,900', ['Air / train ticket', 'Resort stay', 'Jaflong & Ratargul', 'Lawachara & tea gardens', 'Private transport']),
    ]
    def cards(L):
        return ''.join(f'<div class="card reveal">{media(k, t, dur, "", "umbrella")}<div class="body"><span class="eyebrow">{c}</span><h3>{t}</h3>{chk(inc)}<div class="meta"><span class="price">BDT {p} <small>/ person</small></span><a class="btn btn-primary btn-sm" href="#search">Book Now</a></div></div></div>' for k, t, c, dur, p, inc in L)
    body = banner('Tour Packages', 'Hand-crafted holiday packages — flights, hotels, transfers and sightseeing in one price.', 'Tour Packages', IMG['beach']) + f'''
<div class="container" id="search" style="margin-top:-40px;position:relative;z-index:5">{search_widget(False, 'tour')}</div>
<section class="section">
  <div class="container">
    {section_head('International', 'Best-Selling International Packages', 'All packages are customisable. Prices are per person on twin sharing and vary with travel dates.')}
    <div class="grid grid-3">{cards(intl)}</div>
  </div>
</section>
<section class="section soft">
  <div class="container">
    {section_head('Domestic', 'Explore Beautiful Bangladesh', 'Weekend getaways and family holidays within the country.')}
    <div class="grid grid-3">{cards(dom)}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="split">
      <div class="media reveal"><img src="{IMG['mountain']}" alt="Custom holiday planning" loading="lazy"></div>
      <div class="reveal">
        <span class="eyebrow">Tailor-Made Holidays</span>
        <h2>Don't See Your Dream Trip? We'll Build It.</h2>
        <p>Honeymoon, family reunion, corporate retreat, student tour or a once-in-a-lifetime Europe trip — tell us your wishes and budget and our tour designers will craft a day-by-day itinerary just for you.</p>
        <ul class="checklist">
          <li>{ic('check-circle')}Flights, visas, hotels, transport &amp; guides arranged together</li>
          <li>{ic('check-circle')}Halal food and prayer-friendly itineraries on request</li>
          <li>{ic('check-circle')}Corporate incentive tours &amp; school/college study tours</li>
        </ul>
        <a class="btn btn-primary" href="contact.html">{ic('send')}Request Custom Itinerary</a>
      </div>
    </div>
  </div>
</section>
{cta_banner('Planning a group tour?', 'Groups of 10+ get special pricing, a free tour leader seat and dedicated coordination. Talk to us today.')}
'''
    return page('tours.html', 'Tour Packages', 'International and domestic holiday packages from Dhaka: Malaysia, Thailand, Dubai, Singapore, Maldives, Turkey, Kashmir, Nepal, Cox\'s Bazar, Sundarbans and more.', body)

def visa():
    types = [
        ('tourist', 'globe', 'Tourist Visa', 'Holiday and visit visas for Malaysia, Thailand, UAE, Singapore, India, Turkey, Schengen, UK, USA, Canada, Australia and more.', ['Document checklist & review', 'Online form filling', 'Appointment / biometrics booking', 'Cover letter & itinerary', 'Hotel & flight booking for visa']),
        ('student', 'graduation', 'Student Visa', 'Admission and study permit guidance for Malaysia, UK, Canada, Australia, USA, Europe, China, Türkiye and more — subject to government approval.', ['University / college selection', 'Offer letter processing', 'SOP & financial documents', 'Visa file preparation', 'Pre-departure briefing']),
        ('work', 'briefcase', 'Work & Migration', 'Overseas employment and skilled migration consultancy for the Middle East, Malaysia, Europe and beyond, subject to prior approval from the appropriate authority.', ['Job & employer verification', 'Work permit processing', 'BMET / manpower clearance guidance', 'Skilled migration assessment', 'Family & dependent visas']),
        ('medical', 'stethoscope', 'Medical Visa', 'Fast-track medical visas for India, Thailand, Singapore, Malaysia and Türkiye with hospital appointment letters.', ['Hospital appointment letter', 'Medical visa file', 'Attendant visa', 'Air ticket & hotel near hospital', 'Airport pick-up']),
        ('business', 'building', 'Business Visa', 'Trade fair, conference and B2B visit visas for China, UAE, Türkiye, Europe, Malaysia and more.', ['Invitation letter guidance', 'Company documents review', 'Visa file & submission', 'Business travel booking', 'Multiple-entry options']),
    ]
    tp = ''.join(f'<div class="card reveal" id="{k}"><div class="body"><div class="service-card" style="padding:0;box-shadow:none;border:0"><div class="icon">{ic(i)}</div></div><h3>{t}</h3><p>{d}</p>{chk(inc)}<a class="btn btn-outline btn-sm" style="margin-top:16px" href="#search">Apply Now</a></div></div>' for k, i, t, d, inc in types)
    countries = [('🇸🇦', 'Saudi Arabia'), ('🇦🇪', 'UAE'), ('🇶🇦', 'Qatar'), ('🇴🇲', 'Oman'), ('🇰🇼', 'Kuwait'), ('🇧🇭', 'Bahrain'), ('🇲🇾', 'Malaysia'), ('🇸🇬', 'Singapore'), ('🇹🇭', 'Thailand'), ('🇮🇩', 'Indonesia'), ('🇻🇳', 'Vietnam'), ('🇨🇳', 'China'), ('🇯🇵', 'Japan'), ('🇰🇷', 'South Korea'), ('🇮🇳', 'India'), ('🇳🇵', 'Nepal'), ('🇱🇰', 'Sri Lanka'), ('🇲🇻', 'Maldives'), ('🇹🇷', 'Türkiye'), ('🇪🇬', 'Egypt'), ('🇬🇧', 'United Kingdom'), ('🇪🇺', 'Schengen'), ('🇺🇸', 'USA'), ('🇨🇦', 'Canada'), ('🇦🇺', 'Australia'), ('🇳🇿', 'New Zealand'), ('🇷🇺', 'Russia'), ('🇿🇦', 'South Africa')]
    ch = ''.join(f'<span class="chip"><span class="flag">{f}</span>{c}</span>' for f, c in countries)
    steps = [('Free Assessment', 'Share your passport copy and purpose of travel. We tell you eligibility, cost and timeline honestly.'), ('Document Preparation', 'We give a personalised checklist and prepare forms, cover letters and supporting papers.'), ('Submission & Biometrics', 'We book appointments and submit to the embassy / VFS / e-visa portal on your behalf.'), ('Visa Delivery', 'Collect your passport or e-visa from our office or receive it by courier — with pre-travel guidance.')]
    st = ''.join(f'<div class="step reveal"><div class="n">{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    docs = ['Valid passport (minimum 6 months validity, 2 blank pages)', 'Recent passport-size photographs (white background)', 'National ID / birth certificate copy', 'Bank statement & solvency certificate (last 6 months)', 'Trade license / NOC / employment letter / student ID', 'Previous visas and travel history', 'Confirmed air ticket & hotel booking (we arrange)', 'Travel insurance (where required)']
    body = banner('Visa Processing', 'Tourist, student, work, medical and business visas for 30+ countries — prepared by experts, submitted on time.', 'Visa', IMG['passport']) + f'''
<div class="container" id="search" style="margin-top:-40px;position:relative;z-index:5">{search_widget(False, 'visa')}</div>
<section class="section">
  <div class="container">
    {section_head('Visa Services', 'Which Visa Do You Need?', 'Every application is handled by a dedicated consultant from checklist to delivery.')}
    <div class="grid grid-3">{tp}</div>
  </div>
</section>
<section class="section soft">
  <div class="container">
    {section_head('Countries', 'Visa Assistance for 30+ Countries')}
    <div class="chips reveal" style="justify-content:center">{ch}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    {section_head('Process', 'How Visa Processing Works')}
    <div class="steps">{st}</div>
  </div>
</section>
<section class="section soft">
  <div class="container">
    <div class="split">
      <div class="reveal">
        <span class="eyebrow">Documents</span>
        <h2>General Document Checklist</h2>
        <p>Requirements differ by country and visa type. This is the general list — we send you an exact checklist after your free assessment.</p>
        <ul class="checklist">{''.join(f'<li>{ic("check-circle")}{d}</li>' for d in docs)}</ul>
        <div class="info-box"><b>Please note:</b> Visa approval is the sole discretion of the respective embassy or immigration authority. Wakalat provides professional documentation and submission assistance and never guarantees visa approval. Migration and overseas employment services are provided subject to prior approval from the appropriate government authority.</div>
      </div>
      <div class="media reveal"><img src="{IMG['student']}" alt="Study abroad consultation" loading="lazy"><div class="float-card"><div class="num">1,200+</div><span>Visas processed<br>successfully</span></div></div>
    </div>
  </div>
</section>
{cta_banner('Start with a free visa assessment', 'Send your passport copy and travel purpose on WhatsApp. We reply with eligibility, cost and timeline — no obligation.')}
'''
    return page('visa.html', 'Visa Processing', 'Tourist, student, work, medical and business visa processing for Saudi Arabia, UAE, Malaysia, Thailand, Singapore, India, Türkiye, UK, Schengen, USA, Canada, Australia and more from Dhaka.', body)

def hajj_umrah():
    pkgs = [
        ('Economy Umrah', '14 Days', '1,45,000', ['Umrah visa & insurance', 'Return air ticket (Dhaka–Jeddah)', '3★ hotel 500–800 m from Haram', '3★ hotel near Masjid Nabawi', 'Makkah–Madinah AC transport', 'Ziyarah in both cities', 'Bangla-speaking guide', 'Ihram, bag & training'], False),
        ('Standard Umrah', '14 Days', '1,75,000', ['Umrah visa & insurance', 'Return air ticket (Saudia / Biman)', '4★ hotel 200–400 m from Haram', '4★ hotel near Masjid Nabawi', 'Private AC transport', 'Ziyarah in both cities', 'Daily breakfast', 'Experienced Moallem'], True),
        ('Premium Umrah', '10–14 Days', '2,45,000', ['Umrah visa & insurance', 'Direct flight (Saudia / Biman)', '5★ Clock Tower / Haram-view hotel', '5★ hotel facing Masjid Nabawi', 'VIP private transport', 'Full board meals', 'Dedicated Moallem & guide', 'Zamzam & gift pack'], False),
    ]
    RIB = '<span class="ribbon">POPULAR</span>'
    def pkg_card(n, d, p, inc, f):
        return (f'<div class="card pkg{" featured" if f else ""} reveal">{RIB if f else ""}<div class="body"><span class="eyebrow">{d}</span><h3>{n}</h3>'
                f'<div style="font-size:26px;color:var(--red);font-weight:700">BDT {p} <small style="font-size:12px;color:var(--muted);font-weight:500">/ person (twin sharing)</small></div>'
                f'{chk(inc)}<a class="btn btn-primary btn-block" style="margin-top:18px" href="#search">Book This Package</a></div></div>')
    pk = ''.join(pkg_card(*x) for x in pkgs)
    incl = [('passport', 'Umrah Visa', 'E-visa processing with Nusuk registration and mandatory insurance.'), ('takeoff', 'Air Tickets', 'Confirmed seats on Saudia, Biman, flynas, Emirates or Qatar Airways.'), ('hotel', 'Hotels', 'Verified hotels in Makkah and Madinah at your chosen distance from Haram.'), ('bus', 'Transport', 'Airport pick-up, Makkah–Madinah transfer and Ziyarah in AC vehicles.'), ('mosque', 'Ziyarah', 'Guided visits to historic sites in Makkah and Madinah.'), ('users', 'Guide & Training', 'Pre-departure Umrah training and Bangla-speaking guide throughout.')]
    inc = ''.join(f'<div class="feature reveal"><div class="icon">{ic(i)}</div><div><h3>{t}</h3><p>{d}</p></div></div>' for i, t, d in incl)
    steps = [('Choose a Package', 'Pick Economy, Standard or Premium, or ask for a custom family/group package.'), ('Submit Documents', 'Passport (6 months validity), photos, NID and vaccination certificate.'), ('Pay & Confirm', 'Pay the booking amount; balance is due before ticket issuance.'), ('Training & Departure', 'Attend our Umrah training, collect your kit and fly with our group.')]
    st = ''.join(f'<div class="step reveal"><div class="n">{i+1}</div><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(steps))
    faqs = [
        ('When are the group departures?', 'We operate Umrah groups every month, with special Ramadan and school-holiday groups. Private departures can be arranged for families on any date.'),
        ('Can women travel without a Mahram?', 'As per current Saudi regulations, women may perform Umrah in a group without a Mahram. Please consult us for the latest rules.'),
        ('What vaccinations are required?', 'Meningitis (ACWY) is mandatory; seasonal influenza and polio may be required. We guide you to the authorised vaccination centres.'),
        ('Do you offer Hajj packages?', 'Yes. Hajj 2027 pre-registration is open. Hajj is operated in accordance with the Government of Bangladesh Hajj policy through licensed Hajj agencies — contact us for details.'),
    ]
    body = banner('Hajj & Umrah', 'Perform your pilgrimage with peace of mind — complete packages with visa, flights, hotels near Haram, transport and guidance.', 'Hajj & Umrah', IMG['makkah']) + f'''
<div class="container" id="search" style="margin-top:-40px;position:relative;z-index:5">{search_widget(False, 'umrah')}</div>
<section class="section">
  <div class="container">
    {section_head('Umrah Packages', 'Umrah Packages 2026–27', 'Transparent, all-inclusive pricing. Prices are per person on twin sharing and vary by month and hotel availability.')}
    <div class="grid grid-3">{pk}</div>
    <div class="info-box" style="max-width:900px;margin:30px auto 0">{ic('info')} <b>Ramadan Umrah 2027:</b> Limited seats for the last 10 days of Ramadan with 5★ hotels walking distance from Haram. Book early to secure your place.</div>
  </div>
</section>
<section class="section soft">
  <div class="container">
    {section_head('Inclusions', "What's Included in Every Package")}
    <div class="grid grid-3">{inc}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="split">
      <div class="media reveal"><img src="{IMG['madinah']}" alt="Masjid an-Nabawi, Madinah" loading="lazy"><div class="float-card"><div class="num">850+</div><span>Pilgrims served<br>with care</span></div></div>
      <div class="reveal">
        <span class="eyebrow">Why Wakalat for Umrah</span>
        <h2>A Pilgrimage Focused on Ibadah, Not Logistics</h2>
        <p>Our founders have years of experience serving pilgrims from Bangladesh. We personally inspect hotels, choose reliable transport and keep group sizes manageable so that our guides can attend to every pilgrim.</p>
        <ul class="checklist">
          <li>{ic('check-circle')}MoCAT-registered agency — your money and journey are protected</li>
          <li>{ic('check-circle')}Hotels verified for distance, cleanliness and food</li>
          <li>{ic('check-circle')}Experienced Moallem &amp; Bangla-speaking guides</li>
          <li>{ic('check-circle')}Special care for elderly pilgrims &amp; wheelchair support</li>
          <li>{ic('check-circle')}24/7 emergency helpline in Saudi Arabia</li>
        </ul>
        <a class="btn btn-primary" href="#search">{ic('mosque')}Enquire Now</a>
      </div>
    </div>
  </div>
</section>
<section class="section soft">
  <div class="container">
    {section_head('Process', 'Your Umrah Journey in 4 Steps')}
    <div class="steps">{st}</div>
  </div>
</section>
<section class="section">
  <div class="container">
    {section_head('FAQ', 'Hajj & Umrah Questions')}
    {faq_list(faqs)}
  </div>
</section>
{cta_banner('Ready for Umrah?', 'Message us your preferred month and number of pilgrims. We will send package details, hotel photos and available dates on WhatsApp.')}
'''
    return page('hajj-umrah.html', 'Hajj & Umrah Packages', 'Umrah packages 2026-27 from Dhaka with visa, air ticket, hotels near Haram, transport, Ziyarah and Bangla-speaking guide. Economy, Standard and Premium packages by Wakalat Travel & Migration Ltd.', body)

def services():
    svc = [
        ('takeoff', 'Air Ticketing', 'Domestic & international air tickets on all airlines, group fares, date change and refund support.', 'flights.html'),
        ('hotel', 'Hotel Booking', 'Confirmed hotels worldwide including Makkah, Madinah, Dubai, Malaysia, Thailand and Bangladesh.', 'hotels.html'),
        ('umbrella', 'Tour Packages', 'International and domestic holiday packages, honeymoon and family tours, corporate retreats.', 'tours.html'),
        ('passport', 'Visa Processing', 'Tourist, business, student, medical and work visas for 30+ countries with expert file preparation.', 'visa.html'),
        ('mosque', 'Hajj & Umrah', 'All-inclusive Umrah packages every month and Hajj pre-registration as per government policy.', 'hajj-umrah.html'),
        ('graduation', 'Study Abroad', 'Admission and student visa guidance for Malaysia, UK, Canada, Australia, Europe, China and more.', 'visa.html#student'),
        ('briefcase', 'Migration & Overseas Employment', 'Skilled migration and employment consultancy, subject to approval from the appropriate authority.', 'visa.html#work'),
        ('stethoscope', 'Medical Tourism', 'Hospital appointments, medical visas, tickets and accommodation in India, Thailand, Singapore and Türkiye.', 'visa.html#medical'),
        ('building', 'Corporate Travel', 'Dedicated corporate desk for business travel, conference trips, staff Umrah and incentive tours.', 'contact.html'),
        ('shield', 'Travel Insurance', 'Travel and Umrah insurance for visa requirements and peace of mind.', 'contact.html'),
        ('car', 'Airport Transfers & Transport', 'Airport pick-up/drop in Dhaka and destination transfers with trusted partners.', 'contact.html'),
        ('users', 'Group & Student Tours', 'School, college, university and organisation group tours with tour leaders and full logistics.', 'tours.html'),
    ]
    sc = ''.join(f'<a class="card service-card reveal" href="{h}"><div class="icon">{ic(i)}</div><h3>{t}</h3><p>{d}</p><span class="link">Learn more {ic("arrow-right")}</span></a>' for i, t, d, h in svc)
    body = banner('Our Services', 'A complete range of travel and migration services under one roof, delivered by a licensed team.', 'Services', IMG['airport']) + f'''
<section class="section">
  <div class="container">
    {section_head('What We Do', 'Services We Offer')}
    <div class="grid grid-3">{sc}</div>
  </div>
</section>
{trust_section()}
{cta_banner('Not sure which service you need?', 'Call or WhatsApp us — a consultant will understand your requirement and guide you to the right solution.')}
'''
    return page('services.html', 'Our Services', 'All services of Wakalat Travel & Migration Ltd.: air ticketing, hotel booking, tour packages, visa processing, Hajj & Umrah, study abroad, migration consultancy, medical tourism and corporate travel.', body)

def build():
    return {'flights.html': flights(), 'hotels.html': hotels(), 'tours.html': tours(), 'visa.html': visa(), 'hajj-umrah.html': hajj_umrah(), 'services.html': services()}
