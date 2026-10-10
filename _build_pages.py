#!/usr/bin/env python3
# Builds the mazgo sub-pages from shared partials + i18n keys.
import os

ROOT = "/Users/abdulrazzaqal-jewari/Downloads/itmasha-website-export/mazgo-website"

import re
KEYS = set(re.findall(r'"([a-z0-9.]+)":\{fi:', open(os.path.join(ROOT, "i18n.js")).read()))

SPRITE = """<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
<defs>
<symbol id="i-bars" viewBox="0 0 24 24"><line x1="4" y1="6" x2="20" y2="6"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="18" x2="20" y2="18"/></symbol>
<symbol id="i-arrow-up" viewBox="0 0 24 24"><line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/></symbol>
<symbol id="i-close" viewBox="0 0 24 24"><line x1="5" y1="5" x2="19" y2="19"/><line x1="19" y1="5" x2="5" y2="19"/></symbol>
<symbol id="i-leaf" viewBox="0 0 24 24"><path d="M4 20c0-8 6-14 16-16-2 10-8 16-16 16Z"/><path d="M8 16C12 12 15 9 18 6"/></symbol>
<symbol id="i-download" viewBox="0 0 24 24"><path d="M12 3v12"/><polyline points="7 11 12 16 17 11"/><path d="M5 21h14"/></symbol>
<symbol id="i-store" viewBox="0 0 24 24"><path d="M4 10v10h16V10"/><path d="M2.5 10 5 4h14l2.5 6"/><rect x="9.5" y="14" width="5" height="6"/></symbol>
<symbol id="i-heart" viewBox="0 0 24 24"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.6l-1-1a5.5 5.5 0 1 0-7.8 7.8l1 1L12 21.2l7.8-7.8 1-1a5.5 5.5 0 0 0 0-7.8Z"/></symbol>
<symbol id="i-users" viewBox="0 0 24 24"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></symbol>
<symbol id="i-cart" viewBox="0 0 24 24"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></symbol>
<symbol id="i-check-circle" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><polyline points="8 12.5 11 15.5 16 9.5"/></symbol>
<symbol id="i-send" viewBox="0 0 24 24"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></symbol>
<symbol id="i-chevron" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></symbol>
<symbol id="i-instagram" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="5"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></symbol>
<symbol id="i-facebook" viewBox="0 0 24 24"><path d="M15 3h-2a4 4 0 0 0-4 4v3H7v4h2v7h4v-7h3l1-4h-4V7a1 1 0 0 1 1-1h3Z"/></symbol>
<symbol id="i-x" viewBox="0 0 24 24"><line x1="4" y1="4" x2="20" y2="20"/><line x1="20" y1="4" x2="4" y2="20"/></symbol>
<symbol id="i-question" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.8 2.1c-.8.5-1.3 1-1.3 1.9v.5"/><circle cx="12" cy="17" r=".5" fill="currentColor" stroke="none"/></symbol>
<symbol id="i-envelope" viewBox="0 0 24 24"><rect x="2" y="4" width="20" height="16" rx="2"/><polyline points="22 6 12 13 2 6"/></symbol>
<symbol id="i-warning" viewBox="0 0 24 24"><path d="M12 3 2 20h20L12 3Z"/><line x1="12" y1="10" x2="12" y2="14"/><circle cx="12" cy="17" r=".5" fill="currentColor" stroke="none"/></symbol>
</defs>
</svg>"""

NAV = """<nav class="navbar" id="navbar">
<div class="nav-container">
<a href="index.html" class="logo" aria-label="mazgo"><span class="logo-icon"><img src="assets/brand/mazgo-wordmark-ink.png" alt="mazgo"></span></a>
<ul class="nav-links">
<li><a href="index.html#how" data-i18n="nav.how">Näin se toimii</a></li>
<li><a href="index.html#merchants" data-i18n="nav.merchants">Kauppiaille</a></li>
<li><a href="blog.html" data-i18n="nav.blog">Blogi</a></li>
<li><a href="index.html#register" data-i18n="nav.join">Liity mukaan</a></li>
<li><a href="index.html#faq" data-i18n="nav.faq">UKK</a></li>
</ul>
<div class="nav-cta">
<div class="lang-switch" role="group" aria-label="Kieli">
<button type="button" data-lang="fi" class="active">Suomi</button>
<button type="button" data-lang="en">EN</button>
<button type="button" data-lang="ar">عربي</button>
</div>
<a href="index.html#register" class="btn btn-primary" data-i18n="nav.register">Ilmoita liikkeesi</a>
<a href="#" class="btn btn-ghost" data-i18n="nav.download">Lataa sovellus</a>
</div>
<button class="mobile-menu-btn" onclick="toggleMenu()" aria-label="Avaa valikko"><svg class="icon" aria-hidden="true"><use href="#i-bars"/></svg></button>
</div>
</nav>

<div class="mobile-menu-overlay" id="menuOverlay" onclick="toggleMenu()"></div>
<div class="mobile-menu" id="mobileMenu">
<button class="mobile-menu-close" onclick="toggleMenu()" aria-label="Sulje valikko"><svg class="icon" aria-hidden="true"><use href="#i-close"/></svg></button>
<ul>
<li><a href="index.html#how" data-i18n="nav.how">Näin se toimii</a></li>
<li><a href="index.html#merchants" data-i18n="nav.merchants">Kauppiaille</a></li>
<li><a href="blog.html" data-i18n="nav.blog">Blogi</a></li>
<li><a href="index.html#register" data-i18n="nav.join">Liity mukaan</a></li>
<li><a href="index.html#faq" data-i18n="nav.faq">UKK</a></li>
</ul>
<div class="lang-switch" role="group" aria-label="Kieli">
<button type="button" data-lang="fi" class="active">Suomi</button>
<button type="button" data-lang="en">EN</button>
<button type="button" data-lang="ar">عربي</button>
</div>
<a href="index.html#register" class="btn btn-primary" data-i18n="nav.register">Ilmoita liikkeesi</a>
<a href="#" class="btn btn-outline" data-i18n="nav.download">Lataa sovellus</a>
</div>"""

FOOTER = """<footer class="footer">
<div class="footer-container">
<div class="footer-brand">
<a href="index.html" class="logo" aria-label="mazgo"><span class="logo-icon"><img src="assets/brand/mazgo-wordmark-white.png" alt="mazgo"></span></a>
<p data-i18n="footer.tag">mazgo yhdistää sinut lähellä oleviin leipomoihin, ravintoloihin ja kahviloihin.</p>
<div class="footer-social">
<a href="#" aria-label="Instagram"><svg class="icon" aria-hidden="true"><use href="#i-instagram"/></svg></a>
<a href="#" aria-label="Facebook"><svg class="icon" aria-hidden="true"><use href="#i-facebook"/></svg></a>
<a href="#" aria-label="X"><svg class="icon" aria-hidden="true"><use href="#i-x"/></svg></a>
<a href="#" aria-label="Telegram"><svg class="icon" aria-hidden="true"><use href="#i-send"/></svg></a>
</div>
</div>
<div class="footer-col">
<h4 data-i18n="footer.app">Sovellus</h4>
<ul>
<li><a href="index.html#how" data-i18n="nav.how">Näin se toimii</a></li>
<li><a href="#" data-i18n="nav.download">Lataa sovellus</a></li>
<li><a href="terms.html" data-i18n="footer.terms">Käyttöehdot</a></li>
<li><a href="privacy.html" data-i18n="footer.privacy">Tietosuojaseloste</a></li>
<li><a href="delete-account.html" data-i18n="footer.delete">Tilin poistaminen</a></li>
</ul>
</div>
<div class="footer-col">
<h4 data-i18n="footer.forMerchants">Kauppiaille</h4>
<ul>
<li><a href="index.html#register" data-i18n="nav.register">Ilmoita liikkeesi</a></li>
<li><a href="index.html#merchants" data-i18n="nav.merchants">Kauppiaille</a></li>
<li><a href="help.html" data-i18n="footer.help">Ohjekeskus</a></li>
<li><a href="pricing.html" data-i18n="footer.pricing">Hinnasto ja provisio</a></li>
<li><a href="blog.html" data-i18n="nav.blog">Blogi</a></li>
</ul>
</div>
<div class="footer-col">
<h4 data-i18n="footer.contact">Yhteystiedot</h4>
<ul>
<li class="plain" data-i18n="footer.email">tuki@mazgo.fi</li>
<li class="plain" data-i18n="footer.phone">+358 40 123 4567</li>
<li class="plain" data-i18n="footer.city">Helsinki, Suomi</li>
</ul>
</div>
</div>
<div class="footer-bottom">
<div data-i18n="footer.rights">© 2026 mazgo. Kaikki oikeudet pidätetään.</div>
<div data-i18n="footer.made">Suunniteltu Suomessa</div>
</div>
</footer>

<div class="toast" id="toast" role="status"><svg class="icon" aria-hidden="true"><use href="#i-check-circle"/></svg><span id="toastMsg">Valmis!</span></div>

<button id="backTop" onclick="window.scrollTo({top:0,behavior:'smooth'})" aria-label="Takaisin ylös"><svg class="icon" aria-hidden="true"><use href="#i-arrow-up"/></svg></button>"""


def page(filename, title_key, title_fi, desc_fi, body):
    html = f"""<!DOCTYPE html>
<html lang="fi" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_fi}</title>
<meta name="description" content="{desc_fi}">
<link rel="icon" type="image/png" href="assets/brand/mazgo-mark-bag.png">
<link href="https://fonts.googleapis.com/css2?family=El+Messiri:wght@400;500;600;700&family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link rel="stylesheet" href="styles.css">
</head>
<body data-title-key="{title_key}">
<div id="progress"></div>

{SPRITE}

{NAV}

{body}

{FOOTER}
<script src="i18n.js"></script>
<script src="script.js"></script>
</body>
</html>
"""
    with open(os.path.join(ROOT, filename), "w") as f:
        f.write(html)
    print("wrote", filename, len(html))


# ---------------- pricing.html ----------------
faq = lambda i: f'''<div class="faq-item animate-on-scroll">
<button class="faq-question" onclick="toggleFaq(this)"><span data-i18n="price.q{i}"></span><span class="fq-icon"><svg class="icon" aria-hidden="true"><use href="#i-chevron"/></svg></span></button>
<div class="faq-answer"><p data-i18n="price.a{i}"></p></div>
</div>'''

body_pricing = f'''
<section class="section" style="padding-top:140px;background:var(--cream)">
<div class="section-header animate-on-scroll">
<a href="index.html" class="legal-back" style="display:inline-flex;margin-bottom:12px"><svg class="icon" aria-hidden="true"><use href="#i-arrow-up"/></svg><span data-i18n="legal.back">Etusivulle</span></a>
<div class="section-label" data-i18n="price.back">Hinnasto kauppiaille</div>
<h1 class="section-title" data-i18n="price.h1">Hinnasto ja provisio</h1>
<p class="section-desc" data-i18n="price.desc">Yksi yksinkertainen ja läpinäkyvä hinnoittelumalli kaikille kauppiaille.</p>
</div>

<div class="pricing-card animate-on-scroll">
<div class="pricing-big">
<div class="pricing-number" data-i18n="price.number">20 %</div>
<div class="pricing-label" data-i18n="price.number.label">provisio vain toteutuneista myynneistä</div>
</div>
<div class="pricing-grid">
<div class="pricing-stat"><div class="pricing-stat-value" data-i18n="price.s1v">0 €</div><div class="pricing-stat-label" data-i18n="price.s1l">kuukausimaksu</div></div>
<div class="pricing-stat"><div class="pricing-stat-value" data-i18n="price.s2v">0 €</div><div class="pricing-stat-label" data-i18n="price.s2l">liittymismaksu</div></div>
<div class="pricing-stat"><div class="pricing-stat-value" data-i18n="price.s3v">Viikottain</div><div class="pricing-stat-label" data-i18n="price.s3l">tilitysväli</div></div>
</div>
</div>

<div class="pricing-details animate-on-scroll">
<h3 data-i18n="price.d1">Miten provisio lasketaan?</h3>
<ul>
<li data-i18n="price.d1.l1"></li>
<li data-i18n="price.d1.l2"></li>
</ul>
<h3 data-i18n="price.d2">Miten tilitys toimii?</h3>
<ul>
<li data-i18n="price.d2.l1"></li>
<li data-i18n="price.d2.l2"></li>
</ul>
<h3 data-i18n="price.d3">Mitä liittymiseen kuuluu (ilman lisäkustannuksia)?</h3>
<ul>
<li data-i18n="price.d3.l1"></li>
<li data-i18n="price.d3.l2"></li>
<li data-i18n="price.d3.l3"></li>
<li data-i18n="price.d3.l4"></li>
<li data-i18n="price.d3.l5"></li>
</ul>
<h3 data-i18n="price.d4">Ainoa liittymisehto</h3>
<ul>
<li data-i18n="price.d4.l1"></li>
</ul>
</div>
</section>

<section class="section faq">
<div class="section-header animate-on-scroll">
<div class="section-label" data-i18n="price.faq.label">Pikakysymyksiä hinnoittelusta</div>
<h2 class="section-title" data-i18n="price.faq.title">Kysymyksiä provisionsta?</h2>
</div>
<div class="faq-container">
{faq(1)}
{faq(2)}
{faq(3)}
{faq(4)}
</div>
</section>

<section class="cta-section">
<div class="cta-content">
<h2 data-i18n="price.cta.title">Valmis aloittamaan myynnin?</h2>
<p data-i18n="price.cta.desc">Ilmoita liikkeesi nyt — ilman ennakkokuluja ja pitkää sitoumusta.</p>
<div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap">
<a href="index.html#register" class="btn btn-primary btn-lg"><svg class="icon" aria-hidden="true"><use href="#i-store"/></svg><span data-i18n="nav.register">Ilmoita liikkeesi</span></a>
</div>
</div>
</section>'''

page("pricing.html", "price.title", "Hinnasto ja provisio — mazgo",
     "Hinnasto ja provisio mazgo-kauppiaille: 20 % provisio toteutuneista myynneistä, ei kuukausimaksua, viikoittainen tilitys.",
     body_pricing)

# ---------------- help.html ----------------
def hq(cat, i, icon):
    return f'''<div class="help-category animate-on-scroll">
<h3><svg class="icon" aria-hidden="true"><use href="#{icon}"/></svg><span data-i18n="help.{cat}"></span></h3>
<div class="faq-item">
<button class="faq-question" onclick="toggleFaq(this)"><span data-i18n="help.q{i}"></span><span class="fq-icon"><svg class="icon" aria-hidden="true"><use href="#i-chevron"/></svg></span></button>
<div class="faq-answer"><p data-i18n="help.a{i}"></p></div>
</div>
<div class="faq-item">
<button class="faq-question" onclick="toggleFaq(this)"><span data-i18n="help.q{i+1}"></span><span class="fq-icon"><svg class="icon" aria-hidden="true"><use href="#i-chevron"/></svg></span></button>
<div class="faq-answer"><p data-i18n="help.a{i+1}"></p></div>
</div>
<div class="faq-item">
<button class="faq-question" onclick="toggleFaq(this)"><span data-i18n="help.q{i+2}"></span><span class="fq-icon"><svg class="icon" aria-hidden="true"><use href="#i-chevron"/></svg></span></button>
<div class="faq-answer"><p data-i18n="help.a{i+2}"></p></div>
</div>
</div>'''

body_help = f'''
<section class="section legal-page" style="padding-top:140px;padding-bottom:60px">
<div class="section-header animate-on-scroll" style="margin-bottom:40px">
<a href="index.html" class="legal-back" style="display:inline-flex;margin-bottom:12px"><svg class="icon" aria-hidden="true"><use href="#i-arrow-up"/></svg><span data-i18n="legal.back">Etusivulle</span></a>
<h1 class="section-title" data-i18n="help.h1">Ohjekeskus</h1>
<p class="section-desc" data-i18n="help.desc">Vastauksia yleisimpiin kysymyksiin.</p>
</div>

{hq("cat1",1,"i-cart")}
{hq("cat2",4,"i-wallet-x")}
{hq("cat3",7,"i-store")}
{hq("cat4",10,"i-user-x")}

<div class="help-contact animate-on-scroll" style="margin-top:60px">
<div class="help-contact-card"><svg class="icon" aria-hidden="true"><use href="#i-envelope"/></svg><h4 data-i18n="help.c1.h">Sähköposti</h4><p data-i18n="help.c1.p">support@mazgo.fi — vastaus 24 h sisällä</p></div>
<div class="help-contact-card"><svg class="icon" aria-hidden="true"><use href="#i-send"/></svg><h4 data-i18n="help.c2.h">WhatsApp-tuki</h4><p data-i18n="help.c2.p">Aukeaa, kun tukinumero on asetettu</p></div>
<div class="help-contact-card"><svg class="icon" aria-hidden="true"><use href="#i-question"/></svg><h4 data-i18n="help.c3.h">Palaute</h4><p data-i18n="help.c3.p">Ideat ja toiveet — kuulemme mielellämme</p></div>
</div>
</section>'''

# help uses two extra icons not in sprite: i-wallet-x and i-user-x -> replace with existing ones
body_help = body_help.replace('i-wallet-x', 'i-cart').replace('i-user-x', 'i-check-circle')

page("help.html", "help.title", "Ohjekeskus — mazgo",
     "mazgo-ohjekeskus: vastauksia tilauksiin, noutoon, maksamiseen ja kauppiaiden toimintoihin.",
     body_help)

# ---------------- delete-account.html ----------------
body_del = '''
<section class="section legal-page" style="padding-top:140px">
<div class="legal-container animate-on-scroll">
<a href="index.html" class="legal-back"><svg class="icon" aria-hidden="true"><use href="#i-arrow-up"/></svg><span data-i18n="legal.back">Etusivulle</span></a>
<h1 class="legal-title" data-i18n="del.h1">Tilin poistaminen</h1>
<p class="legal-updated" style="margin-bottom:32px" data-i18n="del.desc">Voit poistaa mazgo-tilisi itse sovelluksesta muutamassa sekunnissa.</p>

<div class="legal-notice"><svg class="icon" aria-hidden="true"><use href="#i-warning"/></svg><span data-i18n="del.warn">Poisto on pysyvä. Jos haluat myöhemmin käyttää mazgoa uudelleen, luot vain uuden tilin.</span></div>

<div class="legal-section">
<h3 data-i18n="del.s1.t">1. Avaa sovellus ja mene Tilini-välilehdelle</h3>
<p data-i18n="del.s1.p">Kirjaudu ensiksi sisään samalla tavalla kuin kirjautuisit normaalisti.</p>
</div>
<div class="legal-section">
<h3 data-i18n="del.s2.t">2. Valitse Omat tietoni → Poista tilini</h3>
<p data-i18n="del.s2.p">Vahvista poisto antamalla tilillesi lähetetty vahvistuskoodi.</p>
</div>
<div class="legal-section">
<h3 data-i18n="del.s3.t">3. Tili poistuu välittömästi</h3>
<p data-i18n="del.s3.p">Kirjautuminen lakkaa toimimasta kaikilla laitteillasi.</p>
</div>
<div class="legal-section" style="background:var(--white);border-radius:var(--radius);padding:22px 26px;box-shadow:var(--shadow-sm)">
<h3 data-i18n="del.alt.t">Etkö pääse kirjautumaan sisään?</h3>
<p data-i18n="del.alt.p">Lähetä viesti osoitteeseen support@mazgo.fi samasta sähköpostiosoitteesta tai puhelinnumerosta, jolla rekisteröidyit.</p>
</div>
</div>
</section>'''

page("delete-account.html", "del.title", "Tilin poistaminen — mazgo",
     "Ohjeet mazgo-tilin poistamiseen sovelluksesta tai sähköpostitse.",
     body_del)

# ---------------- terms.html ----------------
def sec(h, p):
    return f'<div class="legal-section"><h3 data-i18n="{h}"></h3><p data-i18n="{p}"></p></div>'

body_terms = f'''
<section class="section legal-page" style="padding-top:140px">
<div class="legal-container animate-on-scroll">
<a href="index.html" class="legal-back"><svg class="icon" aria-hidden="true"><use href="#i-arrow-up"/></svg><span data-i18n="legal.back">Etusivulle</span></a>
<div class="legal-notice"><svg class="icon" aria-hidden="true"><use href="#i-warning"/></svg><span data-i18n="legal.notice">Tämä on luonnos, joka odottaa lakimiehen tarkistusta.</span></div>
<h1 class="legal-title" data-i18n="t.h1">Käyttöehdot</h1>
<p class="legal-updated" data-i18n="legal.updated">Viimeksi päivitetty: lokakuu 2026 · Versio 1.0 (luonnos)</p>
<p data-i18n="t.intro" style="margin-bottom:30px"></p>
{sec("t.s1.h","t.s1.p")}
{sec("t.s2.h","t.s2.p")}
{sec("t.s3.h","t.s3.p")}
{sec("t.s4.h","t.s4.p")}
{sec("t.s5.h","t.s5.p")}
{sec("t.s6.h","t.s6.p")}
{sec("t.s7.h","t.s7.p")}
{sec("t.s8.h","t.s8.p")}
{sec("t.s9.h","t.s9.p")}
{sec("t.s10.h","t.s10.p")}
{sec("t.s11.h","t.s11.p")}
{sec("t.s12.h","t.s12.p")}
{sec("t.s13.h","t.s13.p")}
</div>
</section>'''

page("terms.html", "t.title", "Käyttöehdot — mazgo",
     "mazgo-palvelun käyttöehdot (luonnos): tilaukset, nouto, maksut ja vastuut.",
     body_terms)

# ---------------- privacy.html ----------------
def pli(h, items):
    lis = "\n".join(f'<li data-i18n="{items}{i}"></li>' for i in range(1, 6) if f'{items}{i}' in KEYS)
    return f'<div class="legal-section"><h3 data-i18n="{h}"></h3><ul>{lis}</ul></div>'

def psec(h, p):
    return f'<div class="legal-section"><h3 data-i18n="{h}"></h3><p data-i18n="{p}"></p></div>'

body_privacy = f'''
<section class="section legal-page" style="padding-top:140px">
<div class="legal-container animate-on-scroll">
<a href="index.html" class="legal-back"><svg class="icon" aria-hidden="true"><use href="#i-arrow-up"/></svg><span data-i18n="legal.back">Etusivulle</span></a>
<div class="legal-notice"><svg class="icon" aria-hidden="true"><use href="#i-warning"/></svg><span data-i18n="legal.notice">Tämä on luonnos, joka odottaa lakimiehen tarkistusta.</span></div>
<h1 class="legal-title" data-i18n="pp.h1">Tietosuojaseloste</h1>
<p class="legal-updated" data-i18n="legal.updated">Viimeksi päivitetty: lokakuu 2026 · Versio 1.0 (luonnos)</p>
<p data-i18n="pp.intro" style="margin-bottom:30px"></p>
{psec("pp.s1.h","pp.s1.p")}
{pli("pp.s2.h","pp.s2.l")}
{pli("pp.s3.h","pp.s3.l")}
{psec("pp.s4.h","pp.s4.p")}
{psec("pp.s5.h","pp.s5.p")}
{psec("pp.s6.h","pp.s6.p")}
{psec("pp.s7.h","pp.s7.p")}
{pli("pp.s8.h","pp.s8.l")}
{psec("pp.s9.h","pp.s9.p")}
{pli("pp.s10.h","pp.s10.l")}
{psec("pp.s11.h","pp.s11.p")}
{psec("pp.s12.h","pp.s12.p")}
</div>
</section>'''

page("privacy.html", "pp.title", "Tietosuojaseloste — mazgo",
     "mazgo-palvelun tietosuojaseloste (luonnos): mitä tietoja kerätään, miksi, ja mitä oikeuksia sinulla on.",
     body_privacy)

# ---------------- blog.html ----------------
card = lambda n, href, img, alt: f'''<div class="blog-card animate-on-scroll">
<a href="{href}"><img class="blog-card-img" src="assets/blog/{img}" alt="{alt}" loading="lazy"></a>
<div class="blog-card-body">
<span class="blog-card-tag" data-i18n="blog.c{n}.tag"></span>
<h3><a href="{href}" data-i18n="blog.c{n}.title"></a></h3>
<p data-i18n="blog.c{n}.ex"></p>
<a href="{href}" class="blog-card-link"><span data-i18n="blog.read">Lue artikkeli</span> ←</a>
</div>
</div>'''

body_blog = f'''
<section class="section legal-page" style="padding-top:140px;padding-bottom:60px">
<div class="section-header animate-on-scroll" style="margin-bottom:40px">
<a href="index.html" class="legal-back" style="display:inline-flex;margin-bottom:12px"><svg class="icon" aria-hidden="true"><use href="#i-arrow-up"/></svg><span data-i18n="legal.back">Etusivulle</span></a>
<h1 class="section-title" data-i18n="blog.h1">Blogi</h1>
<p class="section-desc" data-i18n="blog.desc">Artikkeleita ruokahävikistä ja sen vähentämisestä.</p>
</div>
<div class="blog-grid">
{card(1,"blog-finland-food-waste.html","finland-food-waste.jpg","Suomalainen keittiö ja ruokahävikki")}
{card(2,"blog-global-food-waste-numbers.html","global-food-waste.jpg","Ruokahävikki kauppojen jätteessä")}
{card(3,"blog-best-before-dates.html","best-before.jpg","Elintarvikkeiden päiväysmerkinnät")}
<div class="blog-card-placeholder animate-on-scroll" data-i18n="blog.soon">Lisää artikkeleita on tulossa…</div>
</div>
</section>'''

page("blog.html", "blog.title", "Blogi — mazgo",
     "mazgo-blogi: artikkeleita ruokahävikistä Suomessa ja maailmalla sekä sen vähentämisestä.",
     body_blog)

# ---------------- blog articles ----------------
def article(fname, key, title_fi, img, alt):
    cn = {"a1":1,"a2":2,"a3":3}[key]
    p5 = f'<p data-i18n="{key}.p5"></p>' if f"{key}.p5" in KEYS else ''
    stats = "\n".join(f'''<div class="article-stat"><b data-i18n="{key}.stat{i}"></b><span data-i18n="{key}.stat{i}l"></span></div>''' for i in (1,2,3))
    body = f'''
<section class="section legal-page" style="padding-top:140px;padding-bottom:60px">
<div class="blog-article animate-on-scroll">
<a href="blog.html" class="legal-back"><svg class="icon" aria-hidden="true"><use href="#i-arrow-up"/></svg><span data-i18n="blog.all">Kaikki artikkelit</span></a>
<div class="blog-article-meta"><span class="blog-card-tag" data-i18n="blog.c{cn}.tag"></span><span data-i18n="{key}.meta"></span></div>
<h1 class="legal-title" style="margin-bottom:24px" data-i18n="blog.c{cn}.title">{title_fi}</h1>
<img class="blog-article-img" src="assets/blog/{img}" alt="{alt}">
<p class="lead" data-i18n="{key}.lead"></p>
<h2 data-i18n="{key}.h1"></h2>
<p data-i18n="{key}.p1"></p>
<p data-i18n="{key}.p2"></p>
<h2 data-i18n="{key}.h2"></h2>
<p data-i18n="{key}.p3"></p>
<p data-i18n="{key}.p4"></p>
<h2 data-i18n="{key}.h3"></h2>
{p5}
<div class="article-stats">
{stats}
</div>
<div class="blog-sources"><p data-i18n="{key}.src"></p></div>
</div>
</section>'''
    return body

body_privacy = f'''
<section class="section legal-page" style="padding-top:140px">
<div class="legal-container animate-on-scroll">
<a href="index.html" class="legal-back"><svg class="icon" aria-hidden="true"><use href="#i-arrow-up"/></svg><span data-i18n="legal.back">Etusivulle</span></a>
<div class="legal-notice"><svg class="icon" aria-hidden="true"><use href="#i-warning"/></svg><span data-i18n="legal.notice">Tämä on luonnos, joka odottaa lakimiehen tarkistusta.</span></div>
<h1 class="legal-title" data-i18n="pp.h1">Tietosuojaseloste</h1>
<p class="legal-updated" data-i18n="legal.updated">Viimeksi päivitetty: lokakuu 2026 · Versio 1.0 (luonnos)</p>
<p data-i18n="pp.intro" style="margin-bottom:30px"></p>
{psec("pp.s1.h","pp.s1.p")}
{pli("pp.s2.h","pp.s2.l")}
{pli("pp.s3.h","pp.s3.l")}
{psec("pp.s4.h","pp.s4.p")}
{psec("pp.s5.h","pp.s5.p")}
{psec("pp.s6.h","pp.s6.p")}
{psec("pp.s7.h","pp.s7.p")}
{pli("pp.s8.h","pp.s8.l")}
{psec("pp.s9.h","pp.s9.p")}
{pli("pp.s10.h","pp.s10.l")}
{psec("pp.s11.h","pp.s11.p")}
{psec("pp.s12.h","pp.s12.p")}
</div>
</section>'''
page("privacy.html", "pp.title", "Tietosuojaseloste — mazgo",
     "mazgo-palvelun tietosuojaseloste (luonnos): mitä tietoja kerätään, miksi, ja mitä oikeuksia sinulla on.",
     body_privacy)

page("blog-finland-food-waste.html", "blog.c1.title", "Miksi Suomi heittää ruokaa roskiin — mazgo blogi",
     "Suomalaiset tuntevat hävikkiluvut, mutta ruokaa päätyy silti biojätteeseen lähes 400 miljoonaa kiloa vuodessa. Mistä kuilu tietojen ja tekojen välillä johtuu?",
     article("blog-finland-food-waste.html","a1","Miksi Suomi heittää ruokaa roskiin — tietoisuudesta huolimatta?","finland-food-waste.jpg","Suomalainen keittiö ja ruokahävikki"))

page("blog-global-food-waste-numbers.html", "blog.c2.title", "Maailman ruokahävikki lukuina — mazgo blogi",
     "1,05 miljardia tonnia ruokaa vuodessa. UNEP:n tuoreimmat luvut kertovat hävikin määrästä, jakautumisesta ja ilmastovaikutuksista.",
     article("blog-global-food-waste-numbers.html","a2","Maailman ruokahävikki lukuina: UNEP:n raportti","global-food-waste.jpg","Ruokahävikki kauppojen jätteessä"))

page("blog-best-before-dates.html", "blog.c3.title", "Parasta ennen ei tarkoita pilaantunutta — mazgo blogi",
     "Suuri osa ruoasta on syömäkelpoista päiväyksen jälkeen. Näin luet pakkausmerkintöjä oikein ja säästät ruokaa — ja rahaa.",
     article("blog-best-before-dates.html","a3","\"Parasta ennen\" ei tarkoita \"pilaantunutta\"","best-before.jpg","Elintarvikkeiden päiväysmerkinnät"))

print("done")
