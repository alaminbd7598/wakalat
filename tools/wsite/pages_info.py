from .icons import ic
from .layout import *

def about():
    values = [('thumbs-up', 'Positivity'), ('users', 'Teamwork'), ('shield', 'Ownership'), ('heart', 'Customer First'), ('handshake', 'Integrity')]
    vl = ''.join(f'<div class="value reveal"><div class="icon">{ic(i)}</div><h3>{t}</h3></div>' for i, t in values)
    team = [
        ('NM', SITE['md'], 'Managing Director', 'Founder and Managing Director with years of experience in air ticketing, Umrah operations and overseas travel consultancy.'),
        ('HK', SITE['director'], 'Director', 'Oversees finance, customer relations and compliance, ensuring every client receives honest and reliable service.'),
        ('WT', 'Wakalat Travel Desk', 'Consultants & Visa Officers', 'A trained team of ticketing agents, visa officers and Umrah coordinators available six days a week at Mirpur-10.'),
    ]
    tm = ''.join(f'<div class="member reveal"><div class="av">{a}</div><h3>{n}</h3><span>{r}</span><p>{d}</p></div>' for a, n, r, d in team)
    body = banner('About Us', 'A licensed, Dhaka-based travel agency built on trust, transparency and personal service.', 'About Us', IMG['team']) + f'''
<section class="section">
  <div class="container">
    <div class="split">
      <div class="media reveal"><img src="{IMG['about']}" alt="Wakalat Travel & Migration office" loading="lazy"><div class="float-card"><div class="num">2024</div><span>Established<br>in Dhaka</span></div></div>
      <div class="reveal">
        <span class="eyebrow">Our Story</span>
        <h2>Wakalat Travel &amp; Migration Ltd.</h2>
        <p><strong>Wakalat</strong> (وكالة) means <em>agency</em> — one you can entrust with your journey. We are a private limited company incorporated under the Companies Act, 1994 (RJSC No. {SITE['rjsc']}) and registered as a Travel Agency by the Ministry of Civil Aviation &amp; Tourism (Reg. No. {SITE['mocat']}).</p>
        <p>Operating from Shah Ali Plaza, Mirpur-10, we serve pilgrims, families, students, professionals and businesses across Bangladesh with air ticketing, visa processing, Hajj &amp; Umrah packages, holiday tours, hotel booking and migration consultancy.</p>
        <p>The company began operations in October 2024 and adopted its present name in July 2025, bringing together an experienced team with a shared goal: making travel from Bangladesh easier, more affordable and more trustworthy.</p>
        <a class="btn btn-primary" href="contact.html">{ic('send')}Talk to Us</a>
      </div>
    </div>
  </div>
</section>
<section class="section soft">
  <div class="container">
    <div class="grid grid-2">
      <div class="card reveal"><div class="body" style="padding:32px"><div class="service-card" style="padding:0;border:0;box-shadow:none"><div class="icon">{ic('target')}</div></div><h3 style="font-size:22px">Our Mission</h3><p style="font-size:15px">To connect Bangladesh with the world by making travel and migration accessible, affordable and hassle-free — through honest advice, competitive pricing and caring, round-the-clock service.</p></div></div>
      <div class="card reveal"><div class="body" style="padding:32px"><div class="service-card" style="padding:0;border:0;box-shadow:none"><div class="icon">{ic('eye')}</div></div><h3 style="font-size:22px">Our Vision</h3><p style="font-size:15px">To become the most trusted travel and migration partner in Bangladesh — the benchmark of customer choice for Umrah, air travel, visas and overseas opportunities.</p></div></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    {section_head('Core Values', 'What Guides Every Journey We Plan')}
    <div class="values">{vl}</div>
  </div>
</section>
<section class="section soft">
  <div class="container">
    {section_head('Leadership', 'Meet the Team')}
    <div class="team">{tm}</div>
  </div>
</section>
{trust_section()}
<section class="section soft">
  <div class="container">
    {section_head('Company Profile', 'At a Glance')}
    <div class="table-wrap reveal" style="max-width:860px;margin:0 auto"><table>
      <tr><th style="width:40%">Company Name</th><td>{SITE['name']}</td></tr>
      <tr><th>Legal Status</th><td>Private Company Limited by Shares (Companies Act, 1994)</td></tr>
      <tr><th>RJSC Registration No.</th><td>{SITE['rjsc']}</td></tr>
      <tr><th>MoCAT Travel Agency Reg. No.</th><td>{SITE['mocat']} (valid {SITE['mocat_valid']})</td></tr>
      <tr><th>Trade License</th><td>{SITE['trade']} — Dhaka North City Corporation</td></tr>
      <tr><th>Nature of Business</th><td>Air Ticketing, Travel Agency, Visa Processing, Tour Operation, Hajj &amp; Umrah, Migration Consultancy</td></tr>
      <tr><th>Managing Director</th><td>{SITE['md']}</td></tr>
      <tr><th>Registered Office</th><td>{SITE['address']}</td></tr>
      <tr><th>Contact</th><td>{SITE['phone']} · {SITE['email']}</td></tr>
    </table></div>
  </div>
</section>
{cta_banner('Let us plan your next journey', 'Visit our office at Mirpur-10 or reach us on WhatsApp — we would love to hear your travel plans.')}
'''
    return page('about.html', 'About Us', 'About Wakalat Travel & Migration Ltd. — a MoCAT-registered, RJSC-incorporated travel agency in Mirpur-10, Dhaka. Our story, mission, vision, values and leadership.', body)

def contact():
    body = banner('Contact Us', 'We are here to help — call, WhatsApp, email or visit our office in Mirpur-10, Dhaka.', 'Contact', IMG['support']) + f'''
<section class="section">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-info">
        <div class="contact-item reveal"><div class="icon">{ic('map')}</div><div><h3>Office Address</h3><p>{SITE['address']}</p></div></div>
        <div class="contact-item reveal"><div class="icon">{ic('phone')}</div><div><h3>Phone &amp; WhatsApp</h3><a href="tel:{SITE['phone_raw']}">{SITE['phone']}</a><a href="https://wa.me/{SITE['wa']}" target="_blank" rel="noopener">WhatsApp: {SITE['phone']}</a></div></div>
        <div class="contact-item reveal"><div class="icon">{ic('mail')}</div><div><h3>Email</h3><a href="mailto:{SITE['email']}">{SITE['email']}</a></div></div>
        <div class="contact-item reveal"><div class="icon">{ic('clock')}</div><div><h3>Office Hours</h3><p>{SITE['hours']}<br>Friday: Closed (WhatsApp support available)</p></div></div>
        <div class="contact-item reveal"><div class="icon">{ic('award')}</div><div><h3>Registration</h3><p>MoCAT Reg. No. {SITE['mocat']}<br>RJSC No. {SITE['rjsc']} · {SITE['trade']}</p></div></div>
      </div>
      <div class="form-card reveal">
        <h3>Send Us a Message</h3>
        <p>Fill in the form and we will get back to you within a few hours. Submitting opens WhatsApp with your message pre-filled.</p>
        <form data-wa="Website Enquiry">
          <div class="form-grid">
            {field('Full Name', 'name', 'text', None, 'Your name', required=True)}
            {field('Mobile Number', 'mobile', 'tel', None, '01XXX-XXXXXX', required=True)}
            {field('Email', 'email', 'email', None, 'you@example.com')}
            {field('Service', 'service', 'select', None, options=['Air Ticket', 'Visa Processing', 'Umrah / Hajj Package', 'Tour Package', 'Hotel Booking', 'Study Abroad', 'Migration / Work Abroad', 'Other'])}
            {field('Message', 'message', 'textarea', None, 'Tell us your destination, travel dates and number of travellers…', required=True, extra='full')}
          </div>
          <button class="btn btn-primary btn-lg btn-block" style="margin-top:16px" type="submit">{ic('send')}Send Message</button>
          <p class="form-note">By submitting you agree to our <a href="privacy-policy.html" style="color:var(--red)">Privacy Policy</a>.</p>
        </form>
      </div>
    </div>
    <div class="map reveal"><iframe title="Wakalat Travel & Migration Ltd. location — Shah Ali Plaza, Mirpur-10, Dhaka" src="https://www.google.com/maps?q=Shah%20Ali%20Plaza%2C%20Mirpur%2010%2C%20Dhaka%201216&z=16&output=embed" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
</section>
'''
    return page('contact.html', 'Contact Us', 'Contact Wakalat Travel & Migration Ltd. — Office Space 1310 (B), Shah Ali Plaza, Mirpur-10, Dhaka-1216. Phone/WhatsApp +880 1886-270118.', body)

def faqs():
    groups = [
        ('General', [
            ('Is Wakalat Travel & Migration Ltd. a licensed travel agency?', f'Yes. We are registered by the Ministry of Civil Aviation &amp; Tourism as a Travel Agency (Reg. No. {SITE["mocat"]}), incorporated with RJSC (No. {SITE["rjsc"]}) and hold DNCC Trade License {SITE["trade"]}.'),
            ('Where is your office?', f'{SITE["address"]}. We are open {SITE["hours"]}.'),
            ('How can I pay?', 'bKash, Nagad, Rocket, Visa/Mastercard, bank transfer or cash at our office. An official money receipt is issued for every payment.'),
            ('Do you have a mobile app?', 'Not yet — but you can book everything through WhatsApp, phone or this website. Our customer portal is coming soon.'),
        ]),
        ('Air Tickets', [
            ('How quickly will I get my ticket?', 'E-tickets are usually issued within 30 minutes of payment confirmation during office hours and sent via WhatsApp and email.'),
            ('Can I change my travel date?', 'Most tickets allow date changes with an airline penalty plus fare difference. Send us your PNR and new date and we will quote the cost.'),
            ('Are the fares on the website final?', 'Fares shown are indicative starting prices. Final fares depend on travel date, airline and seat availability and are confirmed before you pay.'),
            ('Do you offer group fares?', 'Yes, for groups of 10 or more (Umrah, workers, students, corporates) we negotiate block fares with airlines.'),
        ]),
        ('Visa', [
            ('Do you guarantee visa approval?', 'No agency can guarantee approval — the decision rests with the embassy. We maximise your chances with correct, complete documentation.'),
            ('How long does a visa take?', 'Malaysia, Thailand, Dubai, Singapore e-visas: 3–7 working days. India: 5–10 working days. UK, Schengen, USA, Canada, Australia: 3–8 weeks depending on appointment availability.'),
            ('What is your service charge?', 'It varies by country and visa type. We give a written quotation including embassy fee, VFS fee and our service charge before starting.'),
            ('Is my personal information safe?', 'Yes. Documents are used only for your application and handled in line with our Privacy Policy.'),
        ]),
        ('Hajj & Umrah', [
            ('What is included in the Umrah package?', 'Umrah visa, return air ticket, hotels in Makkah and Madinah, airport and inter-city transport, Ziyarah and a Bangla-speaking guide. Meals depend on the package.'),
            ('How far are the hotels from Haram?', 'Economy: 500–800 m, Standard: 200–400 m, Premium: Clock Tower / Haram-view hotels. Exact hotel names are confirmed at booking.'),
            ('Can I customise the package?', 'Yes — duration, hotel category, room sharing and airline can all be adjusted for families and private groups.'),
            ('Do you provide Umrah training?', 'Yes, every group attends a pre-departure training session at our office covering rituals, travel tips and health guidance.'),
        ]),
        ('Refunds & Changes', [
            ('What is your cancellation policy?', 'Refunds follow airline, hotel and package terms. Some promotional fares are non-refundable. Please read our Refund Policy page for full details.'),
            ('How long does a refund take?', 'Airline refunds typically take 7–45 working days depending on the airline. We follow up and pay you as soon as the airline releases the amount.'),
        ]),
    ]
    html = ''
    for g, items in groups:
        html += f'<h2 style="font-size:22px;margin:36px 0 14px;text-align:center">{g}</h2>' + faq_list(items)
    body = banner('FAQs', 'Answers to the questions we hear most often. Still unsure? Call or WhatsApp us any time.', 'FAQs', IMG['airport']) + f'''
<section class="section"><div class="container" style="max-width:940px">{html}</div></section>
{cta_banner("Didn't find your answer?", 'Our team replies to WhatsApp messages within minutes during office hours.')}
'''
    return page('faqs.html', 'FAQs', 'Frequently asked questions about air tickets, visa processing, Umrah packages, payments and refunds at Wakalat Travel & Migration Ltd.', body)

def legal(slug, title, subtitle, content, desc):
    body = banner(title, subtitle, title, IMG['hero2']) + f'<section class="section"><div class="container"><div class="prose reveal"><span class="updated">Last updated: 1 September 2026</span>{content}</div></div></section>'
    return page(slug, title, desc, body)

def privacy():
    c = f'''
<p>{SITE['name']} (“Wakalat”, “we”, “us”) respects your privacy. This policy explains what personal information we collect, how we use it and the choices you have.</p>
<h2>1. Information We Collect</h2>
<ul><li><strong>Identity &amp; contact data:</strong> name, date of birth, gender, phone number, email, postal address.</li><li><strong>Travel documents:</strong> passport, NID, photographs, visa history, vaccination and insurance details — required to issue tickets and process visas.</li><li><strong>Booking data:</strong> itineraries, hotel preferences, special requests and payment references.</li><li><strong>Technical data:</strong> IP address, browser type and pages visited when you use our website.</li></ul>
<h2>2. How We Use Your Information</h2>
<ul><li>To issue air tickets, hotel vouchers, visas and travel packages you request.</li><li>To share necessary data with airlines, hotels, embassies, visa application centres, insurers and government authorities (e.g. Nusuk, BMET) strictly for your booking.</li><li>To contact you about your booking, send receipts and provide customer support.</li><li>To send offers and updates, only if you have subscribed (you can unsubscribe at any time).</li><li>To comply with legal obligations under the laws of Bangladesh.</li></ul>
<h2>3. Data Sharing</h2>
<p>We never sell your personal data. Information is shared only with service providers required to fulfil your booking and with authorities where legally required.</p>
<h2>4. Data Security &amp; Retention</h2>
<p>Documents are stored securely and access is limited to authorised staff. We retain booking records for as long as required by law and airline/embassy audit rules, after which they are deleted.</p>
<h2>5. Your Rights</h2>
<p>You may request a copy of your data, ask for correction or deletion (subject to legal retention requirements) or withdraw marketing consent at any time by emailing <a href="mailto:{SITE['email']}" style="color:var(--red)">{SITE['email']}</a> or visiting our office at {SITE['address']}.</p>
<h2>6. Cookies</h2>
<p>Our website uses only essential cookies and anonymous analytics to improve your experience. Third-party embeds (such as Google Maps) may set their own cookies.</p>
<h2>7. Contact</h2>
<p>Questions about this policy: {SITE['phone']} · {SITE['email']}</p>'''
    return legal('privacy-policy.html', 'Privacy Policy', 'How we collect, use and protect your personal information.', c, 'Privacy Policy of Wakalat Travel & Migration Ltd.')

def terms():
    c = f'''
<p>These Terms &amp; Conditions govern all bookings and services provided by {SITE['name']}. By making a booking, you agree to these terms.</p>
<h2>1. Our Role</h2>
<p>Wakalat acts as an agent for airlines, hotels, tour operators, insurers and visa authorities. Each service is also subject to the supplier's own terms (e.g. airline fare rules).</p>
<h2>2. Bookings &amp; Payment</h2>
<ul><li>A booking is confirmed only after full or agreed part-payment is received and an official money receipt is issued.</li><li>Fares and package prices are subject to change until ticketed/confirmed.</li><li>For Umrah/Hajj and tour packages, the balance must be paid by the due date stated on the booking confirmation; otherwise the booking may be cancelled with applicable charges.</li></ul>
<h2>3. Passports, Visas &amp; Health</h2>
<ul><li>Travellers are responsible for holding a valid passport (minimum 6 months validity), required visas and vaccinations.</li><li>Visa issuance is at the sole discretion of the relevant embassy/authority. Service charges and embassy fees are non-refundable once the application is submitted, regardless of the outcome.</li><li>Names on tickets must exactly match the passport; corrections after issuance may attract airline charges.</li></ul>
<h2>4. Changes &amp; Cancellations</h2>
<p>Changes and cancellations are subject to supplier rules and our <a href="refund-policy.html" style="color:var(--red)">Refund Policy</a>. All requests must be made in writing (email or WhatsApp).</p>
<h2>5. Liability</h2>
<p>Wakalat is not liable for flight delays, cancellations, schedule changes, denied boarding, lost baggage, force majeure events, or acts or omissions of airlines, hotels or authorities. Our liability is limited to the service charge paid to us.</p>
<h2>6. Migration &amp; Employment Services</h2>
<p>Migration, study and overseas employment consultancy is provided subject to prior approval from the appropriate authority and applicable laws of Bangladesh and the destination country. Wakalat does not guarantee employment, admission or visa outcomes.</p>
<h2>7. Governing Law</h2>
<p>These terms are governed by the laws of the People's Republic of Bangladesh. Disputes are subject to the jurisdiction of the courts of Dhaka.</p>
<h2>8. Contact</h2>
<p>{SITE['name']}, {SITE['address']} · {SITE['phone']} · {SITE['email']}</p>'''
    return legal('terms-conditions.html', 'Terms & Conditions', 'The terms that apply to every booking and service.', c, 'Terms and Conditions of Wakalat Travel & Migration Ltd.')

def refund():
    c = f'''
<p>We want you to book with confidence. This policy explains how refunds work for each service.</p>
<h2>1. Air Tickets</h2>
<ul><li>Refundability depends on the fare rules of the airline. Promotional and some economy fares are non-refundable.</li><li>Airline cancellation penalties, plus a Wakalat service fee of BDT 500–1,500 per ticket, are deducted from refundable fares.</li><li>Refunds are processed after the airline releases the amount, typically within 7–45 working days.</li><li>No-show tickets are generally non-refundable except for taxes where permitted by the airline.</li></ul>
<h2>2. Hotels</h2>
<p>Refunds follow the hotel's cancellation policy shown on your voucher. Non-refundable rates cannot be cancelled. Cancellations within the free-cancellation window are refunded in full less any bank charges.</p>
<h2>3. Tour, Umrah &amp; Hajj Packages</h2>
<div class="table-wrap"><table><thead><tr><th>Cancellation notice before departure</th><th>Cancellation charge</th></tr></thead><tbody><tr><td>More than 45 days</td><td>Booking amount / non-refundable components (visa, ticket deposit)</td></tr><tr><td>30–45 days</td><td>50% of package price</td></tr><tr><td>15–29 days</td><td>75% of package price</td></tr><tr><td>Less than 15 days / no-show</td><td>100% of package price</td></tr></tbody></table></div>
<p style="margin-top:14px">Umrah/Hajj visas, once issued, are non-refundable as per Saudi regulations.</p>
<h2>4. Visa Services</h2>
<p>Embassy fees, VFS/application centre fees and our service charge are non-refundable once the application has been submitted, regardless of approval or rejection. If you cancel before submission, the service charge is refunded less BDT 1,000 processing fee.</p>
<h2>5. How to Request a Refund</h2>
<ol><li>Send a written request by email or WhatsApp with your booking reference / PNR.</li><li>We confirm the applicable charges and expected timeline in writing.</li><li>Refund is paid to the original payment method (bKash/Nagad/bank) after the supplier releases the amount.</li></ol>
<h2>6. Contact</h2>
<p>{SITE['phone']} · {SITE['email']}</p>'''
    return legal('refund-policy.html', 'Refund Policy', 'Cancellation and refund rules for tickets, hotels, packages and visa services.', c, 'Refund and cancellation policy of Wakalat Travel & Migration Ltd.')

def baggage():
    rows = [('Biman Bangladesh Airlines', '7 kg', '30–40 kg (Middle East 40 kg)'), ('US-Bangla Airlines', '7 kg', '20–30 kg'), ('NovoAir (domestic)', '7 kg', '20 kg'), ('Saudia', '7 kg', '2 × 23 kg'), ('Emirates', '7 kg', '30–35 kg'), ('Qatar Airways', '7 kg', '30 kg'), ('Etihad Airways', '7 kg', '30 kg'), ('Turkish Airlines', '8 kg', '30 kg'), ('Malaysia Airlines', '7 kg', '30 kg'), ('Singapore Airlines', '7 kg', '30 kg'), ('Thai Airways', '7 kg', '30 kg'), ('AirAsia', '7 kg', 'Purchase separately (20/25/30 kg)'), ('flydubai', '7 kg', '20–30 kg (fare dependent)'), ('Air Arabia', '10 kg', '20–30 kg (fare dependent)'), ('IndiGo', '7 kg', '20–30 kg')]
    tb = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in rows)
    c = f'''
<p>Baggage allowances vary by airline, route and fare type. The table below is a general guide for economy class — always confirm the exact allowance printed on your e-ticket.</p>
<div class="table-wrap"><table><thead><tr><th>Airline</th><th>Cabin baggage</th><th>Checked baggage (Economy)</th></tr></thead><tbody>{tb}</tbody></table></div>
<h2>Important Notes</h2>
<ul><li>Zamzam water (5 litres) is usually allowed free on flights from Saudi Arabia in addition to the allowance — please carry it in the official sealed pack.</li><li>Power banks, lithium batteries and lighters must be carried in cabin baggage only.</li><li>Liquids in cabin baggage are limited to 100 ml containers in a clear 1-litre bag.</li><li>Excess baggage is charged per kg or per piece at airline rates — pre-purchasing online is usually cheaper than paying at the airport.</li><li>Infants (under 2) typically receive 10 kg checked baggage plus a stroller.</li></ul>
<div class="info-box"><b>Need extra baggage?</b> Tell us at booking time — we can add pre-paid baggage at discounted rates on most airlines.</div>'''
    return legal('baggage-information.html', 'Baggage Information', 'Cabin and checked baggage allowances of major airlines flying from Bangladesh.', c, 'Baggage allowance guide for Biman, Saudia, Emirates, Qatar Airways, Malaysia Airlines, AirAsia and other airlines flying from Dhaka.')

def auth(slug, title, sub, form, alt):
    body = f'''
<section class="auth">
  <div class="form-card reveal">
    <div class="logo"><img src="assets/img/logo.svg" alt="{SITE['name']}" style="height:56px;width:auto"></div>
    <h3 style="text-align:center">{title}</h3>
    <p style="text-align:center">{sub}</p>
    {form}
    <p class="alt">{alt}</p>
  </div>
</section>'''
    return page(slug, title, f'{title} — Wakalat Travel & Migration Ltd. customer portal.', body)

def login():
    form = f'''<form data-demo="Customer portal is launching soon. Please WhatsApp us for bookings."><div class="form-grid">{field('Mobile or Email', 'user', 'text', 'user', '01XXX-XXXXXX', required=True, extra='full')}{field('Password', 'password', 'password', 'lock', '••••••••', required=True, extra='full')}</div><button class="btn btn-primary btn-block btn-lg" style="margin-top:16px" type="submit">Login</button></form>'''
    return auth('login.html', 'Customer Login', 'Access your bookings, e-tickets and visa status.', form, 'New customer? <a href="register.html">Create an account</a> · <a href="contact.html">Need help?</a>')

def register():
    form = f'''<form data-demo="Thank you! Registration will be activated when the portal launches. We will contact you."><div class="form-grid">{field('Full Name', 'name', 'text', 'user', 'As per passport', required=True, extra='full')}{field('Mobile', 'mobile', 'tel', 'phone', '01XXX-XXXXXX', required=True)}{field('Email', 'email', 'email', 'mail', 'you@example.com', required=True)}{field('Password', 'password', 'password', 'lock', '••••••••', required=True, extra='full')}</div><button class="btn btn-primary btn-block btn-lg" style="margin-top:16px" type="submit">Create Account</button></form>'''
    return auth('register.html', 'Create Account', 'Register to manage bookings and receive exclusive deals.', form, 'Already registered? <a href="login.html">Login here</a>')

def notfound():
    body = f'<section class="notfound"><h1>404</h1><h2 style="margin:10px 0">Page Not Found</h2><p style="color:var(--muted);margin-bottom:24px">The page you are looking for has flown away. Let\'s get you back on track.</p><a class="btn btn-primary" href="index.html">{ic("home")}Back to Home</a></section>'
    return page('404.html', 'Page Not Found', 'Page not found.', body)

def build():
    return {'about.html': about(), 'contact.html': contact(), 'faqs.html': faqs(), 'privacy-policy.html': privacy(), 'terms-conditions.html': terms(), 'refund-policy.html': refund(), 'baggage-information.html': baggage(), 'login.html': login(), 'register.html': register(), '404.html': notfound()}
