// mazgo site interactions + trilingual switcher (fi default / en / ar)
const LANGS=['fi','en','ar'];
const storedLang=localStorage.getItem('mazgo-lang');
const urlLang=new URLSearchParams(location.search).get('lang');
let currentLang=(urlLang&&LANGS.includes(urlLang))?urlLang:(storedLang&&LANGS.includes(storedLang))?storedLang:'fi';

function t(key){
    const entry=I18N[key];
    if(!entry) return key;
    return entry[currentLang]||entry.fi;
}

function applyLang(lang){
    currentLang=lang;
    try{localStorage.setItem('mazgo-lang',lang)}catch(e){}
    const isAr=lang==='ar';
    document.documentElement.lang=isAr?'ar':lang;
    document.documentElement.dir=isAr?'rtl':'ltr';
    document.querySelectorAll('[data-i18n]').forEach(el=>{el.textContent=t(el.dataset.i18n)});
    document.querySelectorAll('[data-i18n-ph]').forEach(el=>{el.placeholder=t(el.dataset.i18nPh)});
    document.querySelectorAll('.lang-switch button').forEach(b=>{
        b.classList.toggle('active',b.dataset.lang===lang);
        b.setAttribute('aria-pressed',b.dataset.lang===lang?'true':'false');
    });
    const titleKey=document.body.dataset.titleKey;
    if(titleKey) document.title=t(titleKey);
}

document.querySelectorAll('.lang-switch button').forEach(btn=>{
    btn.addEventListener('click',function(){applyLang(this.dataset.lang)});
});

// Navbar scroll + reading-progress bar + back-to-top button
window.addEventListener('scroll',function(){
    const nav=document.getElementById('navbar');
    if(nav) nav.classList.toggle('scrolled',window.scrollY>50);
    const h=document.documentElement;
    const progress=document.getElementById('progress');
    if(progress){
        const max=h.scrollHeight-h.clientHeight;
        progress.style.width=(max>0?(h.scrollTop/max)*100:0)+'%';
    }
    const backTop=document.getElementById('backTop');
    if(backTop) backTop.classList.toggle('show',h.scrollTop>600);
},{passive:true});

// Highlight the current section's link in the navbar while scrolling
(function(){
    const sections=document.querySelectorAll('section[id]');
    const navLinks=document.querySelectorAll('.nav-links a');
    if(!sections.length||!navLinks.length) return;
    window.addEventListener('scroll',function(){
        let current='';
        sections.forEach(sec=>{if(window.scrollY>=sec.offsetTop-140) current=sec.id});
        navLinks.forEach(a=>a.classList.toggle('active',a.getAttribute('href')==='#'+current));
    },{passive:true});
})();

// Mobile menu
function toggleMenu(){
    document.getElementById('mobileMenu').classList.toggle('open');
    document.getElementById('menuOverlay').classList.toggle('open');
}
function closeMenu(){
    document.getElementById('mobileMenu').classList.remove('open');
    document.getElementById('menuOverlay').classList.remove('open');
}

// Same-page "#section" links: smooth-scroll and close the mobile menu first
document.querySelectorAll('a[href^="#"]').forEach(function(link){
    link.addEventListener('click',function(e){
        e.preventDefault();
        closeMenu();
        const href=this.getAttribute('href');
        if(href.length>1){
            const target=document.querySelector(href);
            if(target) target.scrollIntoView({behavior:'smooth',block:'start'});
        }
    });
});

// FAQ toggle
function toggleFaq(btn){
    const item=btn.parentElement;
    const wasActive=item.classList.contains('active');
    document.querySelectorAll('.faq-item').forEach(i=>i.classList.remove('active'));
    if(!wasActive) item.classList.add('active');
}

// Merchant registration form: client-side validation before the (placeholder) submit
const merchantForm=document.getElementById('merchantForm');
if(merchantForm){
    merchantForm.addEventListener('submit',function(e){
        e.preventDefault();
        const form=e.target;
        let valid=true, firstBad=null;
        form.querySelectorAll('.form-group').forEach(g=>g.classList.remove('has-error'));

        function markBad(field){
            const g=field.closest('.form-group');
            g.classList.add('has-error');
            field.classList.add('error');
            if(!firstBad) firstBad=field;
            field.addEventListener('input',function(){
                g.classList.remove('has-error');
                field.classList.remove('error');
            },{once:true});
        }

        if(form.owner_name.value.trim().length<3){markBad(form.owner_name);valid=false}
        const phone=form.phone.value.replace(/[\s-]/g,'');
        if(!/^(?:\+358|0)\d{6,12}$/.test(phone)){markBad(form.phone);valid=false}
        if(!form.store_name.value.trim()){markBad(form.store_name);valid=false}
        if(!form.category.value){markBad(form.category);valid=false}
        if(!form.city.value){markBad(form.city);valid=false}
        const email=form.email.value.trim();
        if(email&&!/^\S+@\S+\.\S+$/.test(email)){markBad(form.email);valid=false}

        if(!valid){
            showToast(t('toast.fix'),true);
            if(firstBad) firstBad.focus();
            return;
        }

        const btn=document.getElementById('submitBtn');
        const originalLabel=btn.innerHTML;
        btn.textContent=t('form.sending');
        btn.disabled=true;
        setTimeout(()=>{
            btn.innerHTML=originalLabel;
            btn.disabled=false;
            form.reset();
            showToast(t('toast.success'));
        },900);
    });
}

// Toast
function showToast(msg,isError){
    const toast=document.getElementById('toast');
    document.getElementById('toastMsg').textContent=msg;
    toast.classList.toggle('error',!!isError);
    toast.classList.add('show');
    setTimeout(()=>toast.classList.remove('show'),4000);
}

// Scroll animations + number counters (locale-aware)
const LOCALE={fi:'fi-FI',en:'en-US',ar:'ar-EG'};
const observer=new IntersectionObserver((entries)=>{
    entries.forEach(entry=>{
        if(entry.isIntersecting){
            entry.target.classList.add('visible');
            const counters=entry.target.querySelectorAll('[data-target]');
            counters.forEach(counter=>{
                const target=parseFloat(counter.dataset.target);
                const duration=2000;
                const step=target/(duration/16);
                let current=0;
                const timer=setInterval(()=>{
                    current+=step;
                    if(current>=target){current=target;clearInterval(timer)}
                    counter.textContent=Math.floor(current).toLocaleString(LOCALE[currentLang]||'fi-FI');
                },16);
            });
            observer.unobserve(entry.target);
        }
    });
},{threshold:0.1});

document.querySelectorAll('.animate-on-scroll').forEach(el=>observer.observe(el));

// Apply the saved (or default) language once the DOM is ready
applyLang(currentLang);
