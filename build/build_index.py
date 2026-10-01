# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_shell import *
import art

OUT = "/Users/ravi/Documents/Claude-code/Anshul Work/Nutranurture.com"
S = lambda d: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % d

IC_DROP   = S('<path d="M12 2.8s6 6.4 6 10.4a6 6 0 0 1-12 0c0-4 6-10.4 6-10.4Z"/><path d="M9.5 13.5a2.5 2.5 0 0 0 2.5 2.5"/>')
IC_SCALE  = S('<path d="M12 3v18"/><path d="M5 7h14"/><path d="M5 7 2.5 13a3.2 3.2 0 0 0 5 0Z"/><path d="M19 7l2.5 6a3.2 3.2 0 0 1-5 0Z"/><path d="M9 21h6"/>')
IC_FLOWER = S('<circle cx="12" cy="12" r="2.6"/><path d="M12 9.4c0-2.3-.6-4.4 0-5.4.6 1 0 3.1 0 5.4Zm0 5.2c0 2.3.6 4.4 0 5.4-.6-1 0-3.1 0-5.4Zm2.6-2.6c2.3 0 4.4-.6 5.4 0-1 .6-3.1 0-5.4 0Zm-5.2 0c-2.3 0-4.4.6-5.4 0 1-.6 3.1 0 5.4 0Z"/>')
IC_HEART  = S('<path d="M12 20.3s-7.4-4.6-7.4-9.6A4.1 4.1 0 0 1 12 8.3a4.1 4.1 0 0 1 7.4 2.4c0 5-7.4 9.6-7.4 9.6Z"/><path d="M3 12.5h3.3l1.4-2.4 1.8 4 1.6-3 1.2 1.4H21"/>')
IC_BABY   = S('<circle cx="12" cy="9" r="4.2"/><path d="M10.4 8.6h.01M13.6 8.6h.01"/><path d="M10.6 11a2.4 2.4 0 0 0 2.8 0"/><path d="M6.2 21c.6-3.2 3-5.2 5.8-5.2S17.2 17.8 17.8 21"/>')
IC_CHILD  = S('<circle cx="12" cy="5.6" r="2.8"/><path d="M12 8.4v7"/><path d="m7.4 11 4.6-1.6 4.6 1.6"/><path d="m9 21 3-5.6L15 21"/>')
IC_AWARD  = S('<circle cx="12" cy="9" r="5.2"/><path d="m8.6 13.6-1.3 7L12 18.4l4.7 2.2-1.3-7"/>')
IC_BUILD  = S('<path d="M3 21h18"/><path d="M5 21V6.5l7-3.5 7 3.5V21"/><path d="M9.5 21v-5h5v5"/>')
IC_CLOCK  = S('<circle cx="12" cy="12" r="8.6"/><path d="M12 7.2V12l3 1.8"/>')
IC_USERS  = S('<circle cx="9" cy="8" r="3.4"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16.5 5.2a3.4 3.4 0 0 1 0 6.6"/><path d="M18 14.4A6 6 0 0 1 21.5 20"/>')

specs = [
  (IC_DROP,  "Diabetes &amp; metabolic health",
   "Nutrition to manage blood glucose, stabilise HbA1c, address insulin resistance and reduce medication dependency through balanced meal timing and smart food choices."),
  (IC_SCALE, "Weight management &amp; obesity care",
   "Calorie and nutrient guidance focused on sustainable fat loss, muscle retention and metabolic health &mdash; without crash dieting or rebound weight gain."),
  (IC_FLOWER,"PCOD / PCOS &amp; hormonal balance",
   "Anti-inflammatory, hormone-supportive protocols for irregular cycles, insulin sensitivity, hormonal acne and stubborn weight plateaus."),
  (IC_HEART, "Heart health &amp; lipid management",
   "Dietary planning for cholesterol, triglycerides and blood pressure, backed by specialised research in functional foods and clinical dietetics."),
  (IC_BABY,  "Pre &amp; post-natal nutrition",
   "Care through every trimester &mdash; managing gestational health, supporting fetal growth, enhancing lactation and speeding postpartum recovery."),
  (IC_CHILD, "Child &amp; adolescent nutrition",
   "Growth-focused meal planning to tackle picky eating, build strong immunity and instil positive eating habits from an early age."),
]
spec_cards = "\n".join(
  """      <article class="card reveal" data-delay="{d}">
        <div class="card__icon">{ic}</div>
        <h3>{t}</h3>
        <p>{p}</p>
      </article>""".format(ic=ic, t=t, p=p, d=(i % 3) * 70)
  for i, (ic, t, p) in enumerate(specs))

steps = [
  ("Health &amp; lifestyle assessment",
   "We review your medical history, recent lab reports, medication, eating habits, work schedule and physical activity."),
  ("Your personalised plan",
   "A meal guide built around your home food preferences, seasonal ingredients and a cooking routine you can actually keep."),
  ("Monitoring &amp; habit coaching",
   "Weekly or bi-weekly check-ins to track progress, adjust meals and solve real hurdles &mdash; dining out, festivals, travel."),
  ("Long-term maintenance",
   "Reading food labels, portion awareness and intuitive eating, so you stay healthy without needing us."),
]
step_cards = "\n".join(
  """      <div class="step reveal" data-delay="{d}">
        <div class="step__n">{n}</div>
        <h3>{t}</h3>
        <p>{p}</p>
      </div>""".format(n=i + 1, t=t, p=p, d=i * 70)
  for i, (t, p) in enumerate(steps))

institutions = [
  ("Tata Consultancy Services (TCS)", "Employee nutrition counselling, workplace wellness seminars and healthy-living initiatives."),
  ("Apollo Hospitals, Ahmedabad", "Lifestyle health assessments, preventive healthcare guidance and outpatient dietetic counselling."),
  ("Rajasthan Hospital, Ahmedabad", "In-patient clinical dietetics, critical-care nutrition profiles and specialised diabetes camps."),
  ("Eris Lifesciences &amp; healthcare partners", "Clinical training sessions, patient education camps and community awareness workshops."),
  ("AIIMS, New Delhi", "Advanced clinical dietetics and medical nutrition therapy training."),
]
inst_rows = "\n".join(
  """      <li class="reveal"><h3>{n}</h3><p>{d}</p></li>""".format(n=n, d=d)
  for n, d in institutions)

tstm = [
  ("Managing my Type 2 Diabetes felt overwhelming until I started working with Akanksha. Within 4 months my HbA1c dropped significantly &mdash; without giving up family meals. Her practical guidance made all the difference.",
   "Corporate professional, Ahmedabad"),
  ("Akanksha conducted wellness webinars for our employees. Her tips on managing long desk hours, healthy snacking and staying energetic through the workday were practical, engaging and widely appreciated.",
   "HR &amp; employee engagement lead"),
  ("Her guidance through my pregnancy and post-delivery recovery gave me immense confidence. Every meal plan was wholesome, easy to cook and tailored to my changing body. Highly recommended!",
   "New mother"),
]
tstm_cards = "\n".join(
  """      <figure class="tstm reveal" data-delay="{d}">
        <div class="tstm__stars" aria-label="Rated 5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <blockquote>{q}</blockquote>
        <figcaption>{a}</figcaption>
      </figure>""".format(q=q, a=a, d=i * 80)
  for i, (q, a) in enumerate(tstm))

WREATH = art.wreath()
ART_PLATE = art.plate()
ART_POT = art.pot()
ART_SPROUT = art.sprout()

html = head(
  "NutraNurture | Akanksha Bhargava &mdash; Clinical Nutritionist, Ahmedabad",
  "Practical, science-backed nutrition plans for diabetes, weight, PCOS, heart health and maternal care. AIIMS-trained Clinical Nutritionist Akanksha Bhargava — in person in Ahmedabad or online across India.",
  "index.html") + header("index.html") + f"""
<section class="hero">
  <div class="wrap hero__grid">
    <div>
      <p class="hero__name">Akanksha Bhargava</p>
      <h1>Sustainable Nutrition for Real Life.</h1>
      <p class="hero__lede">Clinical Nutritionist, Certified Diabetes Educator and Corporate Wellness Consultant. <strong>Personalised, practical nutrition plans</strong> built around your medical history, your routine and the food you already cook at home &mdash; <strong>no starvation, no extreme restrictions</strong>.</p>
      <div class="btn-row">
        <a class="btn btn--primary is-parked" aria-disabled="true" tabindex="-1">Book a Consultation {CHIP}</a>
        <a class="btn btn--outline is-parked" aria-disabled="true" tabindex="-1">How It Works {CHIP}</a>
      </div>
      <p class="hero__assure">{ICON_CHECK} Free 10-minute call first, to check we are the right fit.</p>
    </div>

    <div class="hero__media">
      {WREATH}
      <div class="hero__photo">
        <img src="assets/akanksha.jpg" alt="Akanksha Bhargava, Clinical Nutritionist and Certified Diabetes Educator" width="543" height="740">
      </div>
      <div class="hero__badge">
        <b>20+</b><span>years of clinical practice</span>
      </div>
    </div>
  </div>
</section>

<section class="creds">
  <div class="wrap">
    <ul>
      <li>{IC_AWARD}<div><strong>AIIMS, New Delhi</strong><span>Trained in clinical dietetics</span></div></li>
      <li>{IC_DROP}<div><strong>Certified Diabetes Educator</strong><span>Dr. Mohan&rsquo;s Diabetes Education Academy</span></div></li>
      <li>{IC_BUILD}<div><strong>TCS &amp; Apollo Hospitals</strong><span>Former consulting nutritionist</span></div></li>
      <li>{IC_CLOCK}<div><strong>20+ years experience</strong><span>Clinical, preventive &amp; corporate</span></div></li>
    </ul>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">The NutraNurture approach</p>
      <h2>Real Food. Real Routines. Real Results.</h2>
    </div>

    <div class="circles">
      <div class="reveal">
        <div class="circle__img">{ART_PLATE}</div>
        <h3>Grounded in Clinical Science</h3>
        <p>Every recommendation starts from your reports, your physiology and a full medical assessment &mdash; never a template.</p>
      </div>
      <div class="reveal" data-delay="90">
        <div class="circle__img">{ART_POT}</div>
        <h3>Built on Home Cooking</h3>
        <p>Plans are written around everyday Indian home food, seasonal produce and the way your kitchen actually runs.</p>
      </div>
      <div class="reveal" data-delay="180">
        <div class="circle__img">{ART_SPROUT}</div>
        <h3>Habits That Keep Growing</h3>
        <p>You learn to make good choices at home, at work and while eating out &mdash; so the results outlast the plan.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Where would you like to begin?</p>
      <h2>Two Ways to Work Together</h2>
    </div>

    <div class="cards cards--2">
      <article class="card reveal">
        <p class="card__tag">For individuals &amp; families</p>
        <h3>Personal nutrition consultations</h3>
        <p>Evidence-based diet programmes designed around your routine, blood work and favourite home-cooked meals &mdash; for diabetes, thyroid health, PCOD, weight, pregnancy and children.</p>
        <a class="textlink" href="services.html">View personal programmes {CHIP}</a>
      </article>

      <article class="card reveal" data-delay="90">
        <p class="card__tag">For corporates &amp; healthcare partners</p>
        <h3>Workplace wellness &amp; health camps</h3>
        <p>Corporate wellness seminars, one-on-one executive nutrition desks, and pharmaceutical-collaborative health screening camps that bring measurable health awareness to teams.</p>
        <a class="textlink" href="corporate.html">Explore corporate offerings {CHIP}</a>
      </article>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">Areas of care</p>
      <h2>Find the Concern You Are Living With</h2>
      <p>Every plan starts with your reports, your kitchen and your schedule &mdash; never a generic diet chart.</p>
    </div>

    <div class="cards cards--3">
{spec_cards}
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">How it works</p>
      <h2>Four Simple Steps</h2>
      <p>Clear expectations from day one, so you always know what happens next.</p>
    </div>

    <div class="steps">
{step_cards}
    </div>

    <div class="btn-row btn-row--center reveal" style="margin-top:2.5rem">
      <a class="btn btn--primary" href="contact.html">Start Your Assessment {CHIP}</a>
      <a class="btn btn--outline" href="services.html">See What&rsquo;s Included</a>
    </div>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap quote-panel">
    <blockquote class="quote reveal">
      Eating healthy should never feel like a punishment. True wellness begins when you understand what your body needs &mdash; and build habits you can enjoy for the rest of your life.
      <cite>Akanksha Bhargava</cite>
    </blockquote>

    <div class="pillars reveal" data-delay="90">
      <div class="pillar">
        <h3>Rooted in clinical science</h3>
        <p>Every recommendation is grounded in human physiology, clinical dietetics and a full medical assessment.</p>
      </div>
      <div class="pillar">
        <h3>Built around Indian home food</h3>
        <p>Plans use everyday home cooking, seasonal produce and your own dietary preferences.</p>
      </div>
      <div class="pillar">
        <h3>Teaching, not dictating</h3>
        <p>You learn how to make good choices at home, at work and while eating out &mdash; not how to follow a chart.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">Experience</p>
      <h2>Two Decades Across Hospitals, Workplaces and Camps</h2>
    </div>

    <div class="stats reveal" style="margin-bottom:clamp(2.5rem,5vw,3.5rem)">
      <div class="stat">{IC_CLOCK}<b>20+</b><span>years of practice</span></div>
      <div class="stat">{IC_USERS}<b>1000+</b><span>clients counselled</span></div>
      <div class="stat">{IC_BUILD}<b>5</b><span>hospital, pharma &amp; corporate partners</span></div>
      <div class="stat">{IC_AWARD}<b>4</b><span>academic &amp; clinical qualifications</span></div>
    </div>

    <ul class="rows">
{inst_rows}
    </ul>
  </div>
</section>

<section class="section section--soft">
  <div class="wrap">
    <div class="section-head section-head--center reveal">
      <p class="eyebrow">Client stories</p>
      <h2>What People Say</h2>
      <p>Read more first-hand experiences on <a class="textlink" href="{GOOGLE_REVIEWS}" target="_blank" rel="noopener">Google Reviews {CHIP}</a></p>
    </div>

    <div class="cards cards--3">
{tstm_cards}
    </div>

    <div class="btn-row btn-row--center reveal" style="margin-top:2.25rem">
      <a class="btn btn--soft" href="stories.html">Read All Client Stories {CHIP}</a>
    </div>
  </div>
</section>

""" + cta() + footer()

open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(park_ctas(html))
print("index.html", len(html), "bytes")
