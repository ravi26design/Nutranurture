# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_shell import *

OUT = "/Users/ravi/Documents/Claude-code/Anshul Work/Nutranurture.com"
S = lambda d: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % d

IC_MIC   = S('<rect x="9" y="2.8" width="6" height="11" rx="3"/><path d="M5.5 11.5a6.5 6.5 0 0 0 13 0"/><path d="M12 18v3.2"/>')
IC_DESK  = S('<circle cx="12" cy="7" r="3.4"/><path d="M5 20.5a7 7 0 0 1 14 0"/><path d="M2.5 14.5h19"/>')
IC_PLATE = S('<circle cx="12" cy="12" r="8.6"/><circle cx="12" cy="12" r="4"/>')
IC_TENT  = S('<path d="M3 20.5h18"/><path d="M12 3.5 4 20.5"/><path d="m12 3.5 8 17"/><path d="M12 11.5 7.5 20.5h9Z"/>')
IC_PEN   = S('<path d="M15.5 4.5 19.5 8.5 8 20H4v-4Z"/><path d="m13.6 6.4 4 4"/>')
IC_TALK  = S('<path d="M20.5 13.5a2.5 2.5 0 0 1-2.5 2.5H8l-4.5 4V6a2.5 2.5 0 0 1 2.5-2.5h12a2.5 2.5 0 0 1 2.5 2.5Z"/><path d="M8 8.5h8M8 12h5"/>')


def page_hero(crumb, title, lede):
    return f"""<section class="page-hero">
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> / {crumb}</p>
    <h1>{title}</h1>
    <p>{lede}</p>
  </div>
</section>
"""


# ======================================================================  ABOUT
quals = [
  ("2023", "Certified Diabetes Educator", "Dr. Mohan&rsquo;s Diabetes Education Academy"),
  ("2005", "PG Diploma in Preventive &amp; Promotive Healthcare", "Apollo Hospitals, Hyderabad"),
  ("2004", "M.Sc. in Foods and Nutrition / Dietetics", "The Maharaja Sayajirao (M.S.) University of Baroda"),
  ("2002", "B.Sc. in Home Science &mdash; Food &amp; Nutrition", "Lady Irwin College, University of Delhi"),
]
qual_html = "\n".join(
  """        <li class="reveal" data-delay="{d}">
          <span class="year">{y}</span>
          <h3>{t}</h3>
          <p>{w}</p>
        </li>""".format(y=y, t=t, w=w, d=i * 60) for i, (y, t, w) in enumerate(quals))

about = head(
  "About Akanksha Bhargava | Clinical Nutritionist, Ahmedabad",
  "AIIMS-trained Clinical Nutritionist, Lifestyle Consultant and Certified Diabetes Educator with 20+ years across hospital dietetics, corporate wellness and community health.",
  "about.html") + header("about.html") + page_hero(
  "About",
  "Food Is Medicine &mdash; Education, Not Restriction, Makes Wellness Last.",
  "A Clinical Nutritionist, Lifestyle Consultant and Certified Diabetes Educator with over 20 years across individual counselling, hospital clinical nutrition and corporate wellness."
) + f"""
<section class="section">
  <div class="wrap split">
    <div class="reveal">
      <div class="portrait-card">
        <img src="assets/akanksha.jpg" alt="Akanksha Bhargava" width="543" height="740">
        <div class="portrait-card__cap">
          <strong>Akanksha Bhargava</strong>
          <span>M.Sc. Foods &amp; Nutrition &middot; Certified Diabetes Educator</span>
        </div>
      </div>
      <div class="btn-row" style="margin-top:1.25rem">
        <a class="btn btn--primary" href="contact.html">Book a consultation {ICON_ARROW}</a>
      </div>
    </div>

    <div class="prose reveal" data-delay="80">
      <p class="eyebrow">Professional journey</p>
      <h2>Clinical Evidence, Applied to Everyday Living</h2>
      <p style="margin-top:1.1rem">Akanksha Bhargava is a Clinical Nutritionist, Lifestyle Consultant and Certified Diabetes Educator with over 20 years of experience in individual dietetic counselling, hospital clinical nutrition and corporate wellness.</p>
      <p>Her philosophy is anchored in the belief that food is medicine, and that sustainable wellness comes from education rather than restriction. Having trained at India&rsquo;s premier medical and nutrition institutions, she bridges clinical evidence with realistic, day-to-day living. Over her career she has counselled thousands of clients across obesity, diabetes, hypertension, cardiovascular health and women&rsquo;s hormonal conditions.</p>
      <p>Beyond one-on-one consulting, she works with corporate organisations on employee wellness, partners with pharmaceutical firms on community health screening camps, and writes nutrition articles and healthy recipes for wellness publications.</p>

      <h3>Clinical internships &amp; specialised training</h3>
      <ul class="checklist">
        <li><strong>AIIMS, New Delhi</strong> &mdash; dietetics department training in clinical dietetics, medical nutrition therapy and hospital nutritional care.</li>
        <li><strong>Apollo Hospital, New Delhi</strong> &mdash; lifestyle assessment, metabolic disorder management and preventive wellness.</li>
      </ul>

      <h3>Professional affiliations</h3>
      <ul class="chiplist">
        <li>Indian Dietetics Association (IDA)</li>
        <li>Ahmedabad Dietetics Association (ADA)</li>
        <li>Indian Association for Parenteral and Enteral Nutrition (IAPEN)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap split--narrow split">
    <div class="reveal">
      <p class="eyebrow">Credentials</p>
      <h2>Qualifications &amp; Training</h2>
      <p style="margin-top:.9rem">Trained at four of India&rsquo;s most respected institutions for nutrition and preventive healthcare.</p>
    </div>
    <div>
      <ul class="timeline">
{qual_html}
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Research &amp; community</p>
      <h2>Work Beyond the Consulting Room</h2>
    </div>
    <div class="cards cards--3">
      <article class="card reveal">
        <h3>Master&rsquo;s research</h3>
        <p><em>Standardization and Sensory Evaluation of Bakery Products using Barley Flour</em> &mdash; investigating cholesterol reduction in hypercholesterolemic patients through functional grain flours.</p>
      </article>
      <article class="card reveal" data-delay="70">
        <h3>Preventive health research</h3>
        <p><em>Diet and Nutrient Interactions</em> &mdash; evaluating the role of micronutrient bioavailability in lifestyle disease management.</p>
      </article>
      <article class="card reveal" data-delay="140">
        <h3>Community outreach</h3>
        <p>Health and nutrition literacy camps for women in underserved communities, infant nutrition demonstrations for nursing mothers, and solar cooking workshops.</p>
      </article>
    </div>
  </div>
</section>

""" + cta() + footer()


# ===================================================================  SERVICES
programs = [
  ("diabetes", "Diabetes &amp; metabolic health",
   "Pre-diabetes, Type 2 Diabetes, insulin resistance, high cholesterol or hypertension.",
   ["Tailored glycemic management to stabilise blood sugar spikes.",
    "Smart carbohydrate pairing and meal timing strategies.",
    "Regular lab review and physician-coordinated dietary adjustments.",
    "Sustainable cardiovascular and lipid health optimisation."]),
  ("weight", "Sustainable weight &amp; body composition",
   "Stubborn weight plateaus, obesity or lifestyle-related weight gain.",
   ["Balanced nutrition that protects muscle mass and optimises metabolism.",
    "No crash diets, appetite suppressants or extreme detoxes.",
    "Flexible strategies for business dinners, vacations and social events.",
    "Focus on healthy inches, stamina and metabolic markers."]),
  ("hormonal", "Hormonal balance &amp; PCOD / PCOS care",
   "Irregular cycles, hormonal weight gain, acne, hair fall or thyroid imbalance.",
   ["Anti-inflammatory and gut-nourishing nutrition.",
    "Insulin-sensitising diet protocols designed for PCOS management.",
    "Guidance on sleep hygiene, stress and physical activity."]),
  ("maternal", "Maternal &amp; child nutrition",
   "Expectant mothers, breastfeeding women, infants starting solids and growing children.",
   ["Trimester-by-trimester meal plans for a healthy pregnancy.",
    "Support for nausea, heartburn and gestational diabetes prevention.",
    "Nutrient-dense postpartum recovery and lactation-boosting meals.",
    "Child growth, immunity and weaning guidance."]),
]
prog_html = "\n".join(
  """      <article class="program reveal" id="{pid}">
        <h3>{title}</h3>
        <p class="program__for"><strong>Ideal for:</strong> {who}</p>
        <ul class="checklist">
{items}        </ul>
      </article>""".format(
      pid=pid, title=title, who=who,
      items="".join("          <li>%s</li>\n" % b for b in bullets))
  for pid, title, who, bullets in programs)

steps = [
  ("Health &amp; lifestyle assessment",
   "We review your medical history, recent lab reports, medication, eating habits, work schedule and physical activity levels."),
  ("Your personalised plan",
   "A meal guide crafted around your home food preferences, seasonal ingredients and realistic cooking routines."),
  ("Monitoring &amp; habit coaching",
   "Weekly or bi-weekly check-ins to evaluate progress, adjust meals and address real hurdles like dining out or business travel."),
  ("Long-term maintenance",
   "Reading food labels, portion awareness and intuitive eating, so you remain healthy independently."),
]
step_html = "\n".join(
  """      <div class="step reveal" data-delay="{d}">
        <div class="step__n">{n}</div>
        <h3>{t}</h3>
        <p>{p}</p>
      </div>""".format(n=i + 1, t=t, p=p, d=i * 70) for i, (t, p) in enumerate(steps))

services = head(
  "Personal Nutrition Consultations | NutraNurture",
  "Personalised clinical nutrition programmes for diabetes, weight management, PCOS and hormonal health, and maternal & child nutrition. In person in Ahmedabad or online across India.",
  "services.html") + header("services.html") + page_hero(
  "Consultations",
  "Plans Built Around Your Reports, Your Kitchen and Your Week",
  "No starvation, no extreme restriction, no generic diet chart. Every plan is designed around your medical history, cultural food habits and real daily routine."
) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">How it works</p>
      <h2>The Four-Step Care Journey</h2>
    </div>
    <div class="steps">
{step_html}
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Programmes</p>
      <h2>Four Focused Programmes</h2>
      <p>Not sure which fits? The first assessment will tell you &mdash; and plans are often combined where conditions overlap.</p>
    </div>

    <div class="programs">
{prog_html}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Consultation formats</p>
      <h2>In Ahmedabad, or Anywhere</h2>
    </div>
    <div class="cards cards--2">
      <article class="card reveal">
        <div class="card__icon">{ICON_PIN}</div>
        <h3>In person</h3>
        <p>Face-to-face assessment and follow-ups in Ahmedabad, Gujarat &mdash; ideal for detailed first assessments and report reviews.</p>
      </article>
      <article class="card reveal" data-delay="80">
        <div class="card__icon">{ICON_VIDEO}</div>
        <h3>Online video consultation</h3>
        <p>Pan-India and international sessions over Zoom or Google Meet, with reports shared ahead of time and plans delivered digitally.</p>
      </article>
    </div>
  </div>
</section>

""" + cta() + footer()


# ==================================================================  CORPORATE
def offer_cards(items):
    out = []
    for i, (icon, title, text, bullets) in enumerate(items):
        lis = "".join("<li>%s</li>" % b for b in bullets)
        ul = '<ul class="checklist" style="margin-top:.9rem">%s</ul>' % lis if lis else ""
        out.append("""      <article class="card reveal" data-delay="{d}">
        <div class="card__icon">{icon}</div>
        <h3>{title}</h3>
        <p>{text}</p>
        {ul}
      </article>""".format(icon=icon, title=title, text=text, ul=ul, d=i * 80))
    return "\n".join(out)

corp = [
  (IC_MIC, "Health webinars &amp; seminars",
   "High-engagement sessions designed for working teams, delivered on site or virtually.",
   ["Smart eating for busy professionals: combating 3&nbsp;PM brain fog",
    "Desk-friendly nutrition &amp; beating metabolic syndrome",
    "Stress, sleep and food: building resilience at work"]),
  (IC_DESK, "On-site &amp; virtual nutrition desks",
   "Confidential one-on-one nutrition counselling for executives and employees, scheduled around work hours.", []),
  (IC_PLATE, "Cafeteria &amp; pantry menu audits",
   "A structured review of office meal and snack options, with practical swaps that introduce healthier, energy-sustaining alternatives.", []),
]
partner = [
  (IC_TENT, "Patient health camps",
   "On-site dietary counselling at screening camps for diabetes, hypertension, obesity and cardiac care.", []),
  (IC_PEN, "Patient education content",
   "Evidence-based articles, healthy recipes and disease-specific lifestyle guides for patient magazines and clinical brochures.", []),
  (IC_TALK, "Workshops &amp; speaker sessions",
   "Educational talks on lifestyle intervention for doctor roundtables, patient support groups and CME programmes.", []),
]

corporate = head(
  "Corporate Wellness &amp; Healthcare Partnerships | NutraNurture",
  "Workplace wellness webinars, on-site nutrition desks, cafeteria audits, and health screening camps with pharmaceutical, hospital and diagnostic partners.",
  "corporate.html") + header("corporate.html") + page_hero(
  "Corporate",
  "Healthy Employees Create Resilient Organisations",
  "Desk work, irregular hours, travel and workplace stress quietly erode focus and health. NutraNurture partners with HR and employee wellness teams to build proactive workplace health cultures."
) + f"""
<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">For corporate organisations</p>
      <h2>Wellness Programming Your Teams Turn Up For</h2>
    </div>
    <div class="cards cards--3">
{offer_cards(corp)}
    </div>
    <p class="reveal" style="margin-top:1.75rem"><strong>Corporate experience:</strong> engaged with leading enterprises including Tata Consultancy Services (TCS), delivering employee nutrition counselling, wellness seminars and healthy-living initiatives.</p>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">For pharma, hospitals &amp; labs</p>
      <h2>Patient-Centred Nutrition Education</h2>
      <p>Collaborations with healthcare organisations, doctor clinics and pharmaceutical partners to deliver patient education at scale.</p>
    </div>
    <div class="cards cards--3">
{offer_cards(partner)}
    </div>
    <p class="reveal" style="margin-top:1.75rem"><strong>Track record:</strong> partnered with Eris Lifesciences, and multi-specialty hospitals including Apollo Hospitals and Rajasthan Hospital, Ahmedabad.</p>
  </div>
</section>

""" + cta() + footer()


# ====================================================================  STORIES
stories_list = [
  ("Diabetes management", "Corporate professional, Ahmedabad",
   "Managing my Type 2 Diabetes felt overwhelming until I started working with Akanksha. Within 4 months, my HbA1c dropped significantly without me having to give up family meals. Her practical guidance made all the difference."),
  ("Corporate wellness", "HR &amp; employee engagement lead",
   "Akanksha conducted wellness webinars for our employees. Her tips on managing long desk hours, healthy snacking and staying energetic throughout the workday were practical, engaging and widely appreciated."),
  ("Pregnancy &amp; postnatal care", "New mother",
   "Her guidance through my pregnancy and post-delivery recovery gave me immense confidence. Every meal plan was wholesome, easy to cook and tailored to my changing body. Highly recommended!"),
]
stories_html = "\n".join(
  """      <figure class="tstm reveal" data-delay="{d}">
        <div class="tstm__stars" aria-label="Rated 5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="card__tag">{tag}</p>
        <blockquote>{q}</blockquote>
        <figcaption>{who}</figcaption>
      </figure>""".format(tag=tag, who=who, q=q, d=i * 80)
  for i, (tag, who, q) in enumerate(stories_list))

stories = head(
  "Client Stories | NutraNurture by Akanksha Bhargava",
  "Real experiences from clients managing diabetes, corporate wellness programmes, and pregnancy & postnatal nutrition with NutraNurture.",
  "stories.html") + header("stories.html") + page_hero(
  "Client Stories",
  "The Proof Is in Ordinary Weeks, Not Crash Results",
  "Clients come for a specific concern &mdash; blood sugar, weight, a pregnancy, a workplace programme &mdash; and stay because the plan survives contact with real life."
) + f"""
<section class="section">
  <div class="wrap">
    <div class="cards cards--3">
{stories_html}
    </div>

    <div class="cta__panel reveal" style="margin-top:clamp(2.5rem,5vw,3.5rem)">
      <div>
        <h2>Read Unfiltered Reviews on Google</h2>
        <p>More first-hand accounts from individuals and families across Ahmedabad and beyond.</p>
      </div>
      <div class="btn-row">
        <a class="btn btn--primary" href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener">Open Google Reviews {ICON_ARROW}</a>
      </div>
    </div>
  </div>
</section>

""" + cta() + footer()


# ====================================================================  CONTACT
contact = head(
  "Contact &amp; Appointments | NutraNurture by Akanksha Bhargava",
  "Book a personal nutrition consultation or send a corporate, pharma or media inquiry. Call or WhatsApp +91 99200 39625. Ahmedabad and online consultations across India.",
  "contact.html") + header("contact.html") + page_hero(
  "Contact",
  "Let&rsquo;s Talk About What Your Body Actually Needs",
  "Book a personal consultation, plan a corporate wellness programme, or start a healthcare partnership. Most inquiries are answered within one working day."
) + f"""
<section class="section">
  <div class="wrap contact-grid">
    <div class="reveal">
      <p class="eyebrow">Get in touch</p>
      <h2 style="margin-bottom:1.5rem">Reach Out Directly</h2>

      <ul class="contact-list">
        <li>{ICON_PHONE}<div><span>Phone / WhatsApp</span><a href="tel:{PHONE.replace(' ','')}">{PHONE_PRETTY}</a></div></li>
        <li>{ICON_PHONE}<div><span>Alternate phone</span><a href="tel:{PHONE_ALT.replace(' ','')}">{PHONE_ALT_PRETTY}</a></div></li>
        <li>{ICON_MAIL}<div><span>Email</span><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
        <li>{ICON_PIN}<div><span>Location</span><p>Ahmedabad, Gujarat, India</p></div></li>
        <li>{ICON_VIDEO}<div><span>Consultation formats</span><p>In person in Ahmedabad, or online across India and internationally via Zoom / Google Meet</p></div></li>
      </ul>

      <div class="btn-row">
        <a class="btn btn--primary" href="{WA}" target="_blank" rel="noopener">Chat on WhatsApp {ICON_ARROW}</a>
        <a class="btn btn--outline" href="tel:{PHONE.replace(' ','')}">Call now</a>
      </div>
    </div>

    <div class="form-card reveal" data-delay="80">
      <h2 style="margin-bottom:.5rem">Send an Inquiry</h2>
      <p style="margin-bottom:1.75rem">Tell us a little about your health goals or your organisation&rsquo;s requirements.</p>

      <form id="inquiry-form" novalidate>
        <div class="field-row">
          <div class="field">
            <label for="name">Full name</label>
            <input id="name" name="name" type="text" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="email">Email address</label>
            <input id="email" name="email" type="email" autocomplete="email" required>
          </div>
        </div>

        <div class="field-row">
          <div class="field">
            <label for="phone">Phone / WhatsApp</label>
            <input id="phone" name="phone" type="tel" autocomplete="tel" required>
          </div>
          <div class="field">
            <label for="city">City <span class="opt">(optional)</span></label>
            <input id="city" name="city" type="text" autocomplete="address-level2">
          </div>
        </div>

        <div class="field">
          <label for="inquiry">What is this about?</label>
          <select id="inquiry" name="inquiry" required>
            <option value="">Please choose&hellip;</option>
            <option>Personal diet &amp; health consultation</option>
            <option>Corporate wellness programme / talk</option>
            <option>Pharma / health camp partnership</option>
            <option>Content, media or workshop collaboration</option>
          </select>
        </div>

        <div class="field">
          <label for="message">Your health goals or requirements <span class="opt">(optional)</span></label>
          <textarea id="message" name="message" rows="5"></textarea>
        </div>

        <button class="btn btn--primary" type="submit" style="width:100%">Send inquiry {ICON_ARROW}</button>
        <p class="form-note">Your details are used only to respond to this inquiry.</p>
        <p class="form-status" id="form-status" role="status" aria-live="polite"></p>
      </form>
    </div>
  </div>
</section>

""" + footer()

for name, doc in [("about.html", about), ("services.html", services),
                  ("corporate.html", corporate), ("stories.html", stories),
                  ("contact.html", contact)]:
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(park_ctas(doc))
    print(name, len(doc), "bytes")
