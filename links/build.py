#!/usr/bin/env python3
"""Builds index.html for kylewhitevc.github.io/links (professional profile links only).

Data: data/links.json holds profile links and the stat band.
Run: python3 build.py, then commit index.html.
"""
import json, os

D = os.path.dirname(os.path.abspath(__file__))
import html
e = html.escape
L = json.load(open(os.path.join(D, 'data/links.json')))

ICON = {'linkedin': '<path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.06c.53-1 1.83-2.06 3.77-2.06 4.03 0 4.77 2.65 4.77 6.1V21h-4v-5.1c0-1.22-.02-2.79-1.7-2.79-1.7 0-1.96 1.33-1.96 2.7V21h-4z"/>', 'x': '<path d="M17.75 3h3.07l-6.7 7.66L22 21h-6.17l-4.83-6.32L5.47 21H2.4l7.17-8.2L2 3h6.33l4.37 5.77zm-1.08 16.2h1.7L7.4 4.73H5.58z"/>', 'instagram': '<path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4zM12 2.5c-2.6 0-2.9 0-3.9.06-3.5.16-5.4 2.1-5.6 5.6C2.5 9.1 2.5 9.4 2.5 12s0 2.9.06 3.9c.16 3.5 2.1 5.4 5.6 5.6 1 .05 1.3.06 3.9.06s2.9 0 3.9-.06c3.5-.16 5.4-2.1 5.6-5.6.05-1 .06-1.3.06-3.9s0-2.9-.06-3.9c-.16-3.5-2.1-5.4-5.6-5.6-1-.05-1.3-.06-3.9-.06zm0 1.7c2.55 0 2.85 0 3.86.06 2.6.12 3.8 1.35 3.92 3.92.05 1 .06 1.3.06 3.86s0 2.85-.06 3.86c-.12 2.56-1.32 3.8-3.92 3.92-1 .05-1.3.06-3.86.06s-2.85 0-3.86-.06c-2.6-.12-3.8-1.36-3.92-3.92C4.2 14.85 4.2 14.55 4.2 12s0-2.85.06-3.86C4.38 5.56 5.6 4.32 8.14 4.2 9.15 4.2 9.45 4.2 12 4.2z"/>', 'site': '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm6.9 6h-2.95a15.6 15.6 0 0 0-1.38-3.56A8.03 8.03 0 0 1 18.9 8zM12 4.04c.83 1.2 1.48 2.53 1.91 3.96h-3.82c.43-1.43 1.08-2.76 1.91-3.96zM4.26 14a8.2 8.2 0 0 1 0-4h3.38a16.5 16.5 0 0 0 0 4zm.84 2h2.95c.32 1.25.78 2.45 1.38 3.56A8 8 0 0 1 5.1 16zm2.95-8H5.1a8 8 0 0 1 4.33-3.56C8.83 5.55 8.37 6.75 8.05 8zM12 19.96A14 14 0 0 1 10.09 16h3.82A14 14 0 0 1 12 19.96zM14.34 14H9.66a14.7 14.7 0 0 1 0-4h4.68a14.7 14.7 0 0 1 0 4zm.25 5.56c.6-1.11 1.06-2.31 1.38-3.56h2.95a8.03 8.03 0 0 1-4.33 3.56zM16.36 14a16.5 16.5 0 0 0 0-4h3.38a8.2 8.2 0 0 1 0 4z"/>', 'cointelegraph': '<path d="M4 4h16v2H4zm0 4h10v2H4zm0 4h16v2H4zm0 4h10v2H4z"/>', 'press': '<path d="M4 4h13v14a2 2 0 0 0 2 2H6a2 2 0 0 1-2-2zm2 2v3h9V6zm0 5v2h9v-2zm0 4v2h6v-2zm13-7h2v10a2 2 0 0 1-2 2z"/>'}
links_html = ''.join(
    f'''<a class="row" href="{e(l['url'])}" target="_blank" rel="noopener">
      <svg class="ic" viewBox="0 0 24 24" aria-hidden="true">{ICON.get(l['id'],'')}</svg><span class="rl">{e(l['label'])}</span><span class="rs">{e(l['sub'])}</span><span class="ar" aria-hidden="true">&rarr;</span></a>'''
    for l in L['links'])

CSS = r"""
:root{--bg:#0e0b09;--bg2:#17120e;--ink:#efe7da;--mute:#a3978a;--brass:#c3a165;--brass2:#e2c88f;--line:rgba(195,161,101,.22)}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-text-size-adjust:100%;background:var(--bg)}
body{background:var(--bg);color:var(--ink);font:15px/1.55 -apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:inherit;text-decoration:none;-webkit-tap-highlight-color:rgba(195,161,101,.15)}
.serif{font-family:"Cormorant Garamond","Cormorant",Garamond,"Times New Roman",serif}
.cap{font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--brass)}
@keyframes run{to{transform:translateX(-50%)}}
/* hero */
.hero{position:relative;max-width:1080px;margin:0 auto}
.hero figure{position:relative;height:min(118vw,560px);overflow:hidden}
.hero img{width:100%;height:100%;object-fit:cover;object-position:50% 18%;filter:sepia(.12) saturate(.9);transform:scale(1.06);animation:settle 2.4s cubic-bezier(.2,.7,.2,1) forwards}
.hero figure:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(14,11,9,0) 35%,rgba(14,11,9,.55) 68%,var(--bg) 100%)}
.intro{position:relative;margin-top:-150px;padding:0 24px;z-index:2}
h1{font-weight:500;font-size:58px;line-height:.95;letter-spacing:-.01em}
h1 i{color:var(--brass2);font-weight:400}
.lede{margin-top:16px;font-size:21px;line-height:1.35;color:var(--ink);max-width:30ch;font-style:italic}
.facts{margin-top:14px;color:var(--mute);font-size:13.5px;max-width:40ch}
@keyframes settle{to{transform:scale(1)}}
.rise{opacity:0;transform:translateY(14px);animation:rise .9s .25s cubic-bezier(.2,.7,.2,1) forwards}
.d2{animation-delay:.45s}.d3{animation-delay:.65s}
@keyframes rise{to{opacity:1;transform:none}}
main{max-width:1080px;margin:0 auto;padding:0 24px 40px}
section{margin-top:52px}
.sh{display:flex;align-items:baseline;justify-content:space-between;border-bottom:1px solid var(--line);padding-bottom:10px;margin-bottom:6px}
.sh h2{font-weight:500;font-size:30px;font-style:italic}
/* rows */
.row{display:grid;grid-template-columns:34px 1fr auto;grid-template-areas:"i l a" "i s a";column-gap:12px;padding:18px 2px;border-bottom:1px solid var(--line);min-height:64px;align-items:center}
.ic{grid-area:i;width:20px;height:20px;fill:var(--brass);align-self:center}
.rl{grid-area:l;font-family:"Cormorant Garamond",Garamond,serif;font-size:25px;line-height:1.1}
.rs{grid-area:s;color:var(--mute);font-size:13px;margin-top:2px}
.ar{grid-area:a;color:var(--brass);font-size:22px;transition:transform .3s}
.row:hover .ar,.row:focus-visible .ar{transform:translateX(5px)}
/* stage */
.stage{margin:44px 0 0;border-top:1px solid var(--line);padding-top:28px}
.stage figcaption{display:block}
.stage .cap{display:block;font-size:10.5px;letter-spacing:.26em;text-transform:uppercase;color:var(--brass);margin-top:14px}
.stage .st{display:block;font-size:34px;line-height:1.05;margin-top:6px;font-style:italic}
.stage .sl{display:block;color:var(--mute);font-size:13.5px;margin-top:8px}
.links{margin-top:40px;border-top:1px solid var(--line)}
.stage img{display:block;width:100%;height:auto;aspect-ratio:1/1;object-fit:cover}

/* vault */
.vault{margin-top:64px;position:relative}
.vk{display:flex;align-items:flex-end;justify-content:space-between;gap:12px}
.vsub{margin-top:14px;color:var(--mute);font-size:14px;max-width:36ch}
.fx{position:absolute;opacity:0;pointer-events:none}
.fam{margin-top:72px}
.fe{margin-top:16px;font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--brass2)}
/* uniform */
.ulede{margin-top:12px;color:var(--mute);font-size:14px;max-width:38ch}
.fo{position:absolute;left:0;right:0;bottom:0;padding:90px 24px 22px;background:linear-gradient(180deg,rgba(14,11,9,0),rgba(14,11,9,.88))}
.fo .no{display:block;font-family:"Cormorant Garamond",Garamond,serif;font-style:italic;color:var(--brass2);font-size:18px}
.fn{display:block;font-family:"Cormorant Garamond",Garamond,serif;font-size:40px;line-height:1;margin-top:6px}
.fp{display:flex;justify-content:space-between;align-items:baseline;margin-top:10px;font-size:15px;font-variant-numeric:tabular-nums}
.fp i{font-style:normal;font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--brass2)}
footer{max-width:1080px;margin:0 auto;padding:28px 24px 48px;border-top:1px solid var(--line);color:var(--mute);font-size:12px;line-height:1.6}
.presby{max-width:1080px;margin:0 auto;padding:9px 24px;display:flex;gap:10px;align-items:baseline;font-size:10px;letter-spacing:.22em;text-transform:uppercase;color:var(--mute);border-bottom:1px solid var(--line)}.presby a{color:var(--brass);text-decoration:none}.presby a:hover{color:var(--brass2)}
.fdisc{margin-top:14px;font-size:11.5px;color:var(--mute);line-height:1.5}
footer .spon{margin:0 0 12px}footer .spon a{color:var(--brass);font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;text-decoration:none;border-bottom:1px solid var(--line);padding-bottom:2px}footer .spon a:hover{color:var(--brass2);border-color:var(--brass)}
footer .sig{font-family:"Cormorant Garamond",Garamond,serif;font-style:italic;font-size:22px;color:var(--brass2);margin-bottom:8px}

.lno{font-size:10.5px;letter-spacing:.26em;text-transform:uppercase;color:var(--brass)}

.rs{font-size:10.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--brass2);text-align:right}

/* stat band */
.stats{display:grid;grid-template-columns:1fr 1fr;margin-top:40px;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.sb{display:flex;flex-direction:column;align-items:flex-start;padding:20px 4px 18px 0}
.sb:nth-child(odd){padding-right:14px}
.sb:nth-child(even){padding-left:18px;border-left:1px solid var(--line)}
.sb:nth-child(n+3){border-top:1px solid var(--line)}
.sn{font-size:42px;line-height:.9;font-weight:500;color:var(--brass2);letter-spacing:-.01em;font-variant-numeric:lining-nums}
.sl2{margin-top:9px;font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:var(--mute)}
.stats+.links{margin-top:0;border-top:0}
@media (min-width:760px){
 .stats{grid-template-columns:repeat(4,1fr)}
 .sb{padding:26px 0 24px 24px!important;border-left:1px solid var(--line);border-top:0!important}
 .sb:first-child{border-left:0;padding-left:0!important}
 .sn{font-size:64px}
}

:focus-visible{outline:2px solid var(--brass);outline-offset:3px}
@media (min-width:760px){
 .hero{display:grid;grid-template-columns:1fr 1fr;align-items:end;gap:40px;padding:48px 24px 0}
 .hero figure{height:600px}
 .hero figure:after{background:linear-gradient(180deg,rgba(14,11,9,0) 70%,rgba(14,11,9,.4))}
 .intro{margin:0 0 30px;padding:0}
 h1{font-size:92px}
 .cols{display:grid;grid-template-columns:1fr 1fr;gap:48px}
 .links{display:grid;grid-template-columns:1fr 1fr;column-gap:40px}
 .stage{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
 .stage .st{font-size:56px}
}
@media (prefers-reduced-motion:reduce){
 *{animation:none!important;transition:none!important}
 .rise{opacity:1;transform:none}.hero img{transform:none}
}
"""

GC_HEAD = r'''<!-- Analytics Desk: GoatCounter (installed 2026-10-26) -->
<script>
window.goatcounter = {path: function(p){ return '/links' + p }};
document.addEventListener('click', function(e){
  var a = e.target.closest && e.target.closest('a[href]'); if(!a || !window.goatcounter.count) return;
  var h = a.hostname, ev = null;
  if (/sponsored|affiliate/.test(a.rel) || a.hasAttribute('data-aff')) ev = 'out/links/aff/' + h;
  else if (/calendar\.app\.google|calendly|cal\.com|booking|book/i.test(a.href)) ev = 'out/links/book/' + h;
  else if (/^mailto:/.test(a.href)) ev = 'out/links/mail';
  else if (h && h !== location.hostname) ev = 'out/links/link/' + h;
  if (ev) window.goatcounter.count({path: ev, title: (a.textContent||'').trim().slice(0,60), event: true});
});
</script>
<script data-goatcounter="https://kylewhitevc.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>'''
stats_html = ''.join(f'<div class="sb"><span class="sn serif">{e(x["n"])}</span><span class="sl2">{e(x["l"])}</span></div>' for x in L.get('stats',[]))
page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Kyle White</title>
<meta name="description" content="Kyle White: accelerator builder and venture investor from Youngstown, Ohio.">
<link rel="canonical" href="https://kylewhitevc.github.io/links/">
<meta property="og:type" content="profile">
<meta property="og:title" content="Kyle White">
<meta property="og:description" content="Accelerator builder and venture investor from Youngstown, Ohio.">
<meta property="og:image" content="https://kylewhitevc.github.io/links/img/kyle-og.jpg">
<meta property="og:url" content="https://kylewhitevc.github.io/links/">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#070504">
<link rel="icon" href="favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="img/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="img/icon-192.png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400;1,500&display=swap">
<link rel="preload" as="image" href="img/kyle-hero.webp">
<style>{CSS}</style>
{GC_HEAD}
</head>
<body>
<header class="hero">
  <figure><img src="img/kyle-hero.webp" width="752" height="940" alt="Kyle White" fetchpriority="high"></figure>
  <div class="intro">
    <p class="cap rise">Youngstown, Ohio</p>
    <h1 class="serif rise d2">Kyle <i>White</i></h1>
    <p class="lede serif rise d3">I build accelerators and investor programs from zero, and I back the builders of American industry.</p>
    <p class="facts rise d3">Built the Cointelegraph accelerator: 60 investments across four cohorts, $125M in follow-on funding. Techstars All-Star Mentor.</p>
  </div>
</header>
<main>
  <div class="stats" aria-label="Reach and track record">{stats_html}</div>
  <section class="links">{links_html}</section>
  <figure class="stage"><img src="img/kyle-cis.webp" width="720" height="720" alt="Kyle White speaking on a panel at the Crypto Invest Summit" loading="lazy" decoding="async"><figcaption><span class="cap">On stage</span><span class="st serif">Crypto Invest Summit</span><span class="sl">Panelist, Blockchain Technology Investing track.</span></figcaption></figure>
</main>
<footer>
  <p class="sig">Grazie for stopping by.</p>
</footer>
</body>
</html>
'''
import hashlib, re
def _v(m):
    p = os.path.join(D, m.group(1))
    h = hashlib.md5(open(p, 'rb').read()).hexdigest()[:8] if os.path.exists(p) else ''
    return f'src="{m.group(1)}?v={h}"' if h else m.group(0)
page = re.sub(r'src="((?:img|data|vendor)/[^"?]+)"', _v, page)
page = re.sub(r'href="(img/[^"?]+)"', lambda m: 'href=' + _v(m)[4:], page)
open(os.path.join(D, 'index.html'), 'w').write(page)
print('built', len(page), 'bytes')
