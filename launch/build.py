"""Страница для клуба: что запускаем, 8 объявлений, куда приходят заявки, как их обрабатывать, что нужно от клуба (EN/RU)."""
import html, pathlib, sys

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT.parent / "test8"))
e = html.escape

# номер, о чём (EN, RU), файл ленты, текст JA, перевод EN, перевод RU
ADS = [
 ("T1", "Coach always by your side", "Тренер всегда рядом", "T1-c01-coach-pads-feed.jpg",
  "大型ジムに入会したけど、マシンの使い方も分からず一人きり…。TOTALFIT NOAHでは、コーチがいつも隣でサポートします。本郷台エリア・駐車場あり。無料体験は手ぶらでOK。",
  "Joined a big gym, but no idea how to use the machines and you're on your own… At TOTALFIT NOAH a coach is always by your side. Hongodai area, parking. Free trial, no gear needed.",
  "Записался в большой зал, а как пользоваться тренажёрами — непонятно, и ты один. В TOTALFIT NOAH тренер всегда рядом. Хонгодай, парковка. Пробное бесплатно, можно без формы."),
 ("T2", "You never use 90% of the machines", "90% тренажёров не используешь", "T2-c02-90-percent-feed.jpg",
  "大型ジムのマシン、9割は使わないまま辞めていませんか？人は多いのに、あなたは一人。NOAHでは、毎回コーチが隣で教えます。本郷台エリア・駐車場あり。無料体験受付中。",
  "Quit a big gym without ever using 90% of the machines? Lots of people, yet you're alone. At NOAH a coach shows you every time. Hongodai, parking. Free trial open.",
  "Бросали большой зал, так и не освоив 90% тренажёров? Людей много, а ты один. В NOAH тренер каждый раз рядом и показывает. Хонгодай, парковка. Пробное бесплатно."),
 ("T3", "This is your place", "Здесь твоё место", "T3-c06-belong-feed.jpg",
  "名前で呼び合う仲間と、コーチがいるジム。一人だと続かなかった運動も、ここなら続けられます。本郷台エリア・駐車場あり。無料体験受付中。",
  "A gym where members and coaches know you by name. If you quit alone before, here you'll keep going. Hongodai, parking. Free trial open.",
  "Зал, где тебя знают по имени — и участники, и тренер. Если один бросал — здесь получится. Хонгодай, парковка. Пробное бесплатно."),
 ("T4", "First time — and laughing", "Первый раз — и смеёмся", "T4-c09-laugh-kick-feed.jpg",
  "はじめてでも大丈夫。組手なしのキックボクシングで、楽しく体を動かしませんか。女性の方も多く通うアットホームなジムです。本郷台エリア・駐車場あり。無料体験は手ぶらでOK。",
  "Total beginners welcome. Kickboxing with no sparring — just fun movement. A friendly gym with many women members. Hongodai, parking. Free trial, no gear needed.",
  "Можно с нуля. Кикбоксинг без спаррингов — просто двигаться с удовольствием. Уютный зал, много женщин. Хонгодай, парковка. Пробное бесплатно."),
 ("T5", "Free trial", "Бесплатная пробная", "T5-c10-free-trial-green-feed.jpg",
  "TOTALFIT NOAHの無料体験、受付中。キックボクシング・ピラティス・フィットネス・卓球。手ぶらでOK、本郷台エリア・駐車場あり。（キッズも無料体験。ダンスクラスの体験は500円）",
  "Free trial now open: kickboxing, Pilates, fitness, table tennis. No gear needed, Hongodai, parking. (Kids' trial free, dance class trial ¥500)",
  "Запись на бесплатную пробную: кикбоксинг, пилатес, фитнес, настольный теннис. Без формы, Хонгодай, парковка. (Детям пробное тоже бесплатно, пробное на танцы — ¥500)"),
 ("T6", "Whole family — ¥11,000", "Вся семья — ¥11 000", "T6-c11-family-price-feed.jpg",
  "家族みんなで月11,000円（税込・入会金別途）。キッズ・キックボクシング・ピラティス・卓球。本郷台エリア・駐車場あり。まずは体験から。",
  "The whole family for ¥11,000/month (tax incl., joining fee extra). Kids, kickboxing, Pilates, table tennis. Hongodai, parking. Start with a trial.",
  "Вся семья — ¥11 000 в месяц (с налогом, взнос отдельно). Дети, кикбоксинг, пилатес, теннис. Хонгодай, парковка. Начните с пробного."),
 ("T7", "Kids come too", "Дети тоже ходят", "T7-c14-kids-feed.jpg",
  "子どもも一緒に通えるジム。キッズクラスの間に、パパ・ママはトレーニング。家族みんなで月11,000円（税込・入会金別途）。本郷台エリア・駐車場あり。大人もキッズも無料体験（ダンスクラスの体験は500円）。",
  "A gym your kids can join too: while they're in class, parents train. Family ¥11,000/month. Hongodai, parking. Trial free for adults and kids (dance class trial ¥500).",
  "Зал, куда можно ходить с детьми: пока ребёнок на занятии, родители тренируются. Семья — ¥11 000. Хонгодай, парковка. Пробное бесплатно и взрослым, и детям (танцы — ¥500)."),
 ("T8", "Video: coach by your side", "Видео: тренер рядом", "T8-v11-coach.mp4",
  "人は多いのに、ひとりで筋トレ？NOAHでは、コーチがいつも隣に。重さもフォームもその場でサポート。本郷台エリア・駐車場あり。まずは無料体験から。",
  "Lots of people, yet you train alone? At NOAH a coach is always next to you — fixes weight and form on the spot. Hongodai, parking. Start with a free trial.",
  "Людей много, а тренируешься один? В NOAH тренер всегда рядом — сразу поправит вес и технику. Хонгодай, парковка. Начните с бесплатной пробной."),
]


def b(en, ru, tag="p", cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} data-l="en">{en}</{tag}><{tag}{c} data-l="ru">{ru}</{tag}>'


def media(src):
    p = f"../test8/img/{src}"
    if src.endswith(".mp4"):
        return f'<video src="{p}" autoplay muted loop playsinline></video>'
    return f'<img src="{p}" alt="" loading="lazy">'


cards = "".join(f"""
<article class="ad">
  <div class="ph"><div class="ig"><b>totalfit.noahgym</b><span>広告 · Ad</span></div>{media(f)}<div class="cta"><span>無料体験</span><i>予約する</i></div></div>
  <div class="tx"><h3><span class="n">{n}</span><span data-l="en">{e(ten)}</span><span data-l="ru">{e(tru)}</span></h3>
  <p class="ja">{e(ja)}</p>{b(e(en), e(ru), cls="tr")}</div>
</article>""" for n, ten, tru, f, ja, en, ru in ADS)

NEED = [
 ("Check the Japanese texts of the 8 ads below. Anything wrong or unnatural — tell us.",
  "Проверить японские тексты 8 объявлений ниже. Что-то не так или звучит неестественно — сказать нам."),
 ("Confirm the people in these photos agreed to appear in ads (especially the children in T7). In Japan this is required.",
  "Подтвердить, что люди на этих фото согласны быть в рекламе (особенно дети на T7). В Японии это обязательно."),
 ("Confirm the offers: trial free for adults and kids, dance class trial ¥500, family ¥11,000/month tax incl. How much is the joining fee? Any campaign we can mention (e.g. joining fee free)?",
  "Подтвердить предложения: пробное бесплатно и взрослым, и детям, танцы ¥500, семья ¥11 000 в месяц с налогом. Сколько вступительный взнос? Есть ли акция, которую можно указать (например, без взноса)?"),
 ("Name one person who answers new requests, and give us the email (and LINE, if you use it) where requests should arrive.",
  "Назвать одного человека, который отвечает на новые заявки, и дать почту (и LINE, если пользуетесь), куда присылать заявки."),
 ("Tell us which classes have free places, and which are full (we know kids on Wednesday is full) — we will not advertise full classes.",
  "Сказать, в каких занятиях есть места, а какие заполнены (знаем, что дети в среду — полная группа). Полные занятия рекламировать не будем."),
 ("Website: invite us to Netlify (1 minute) — or paste the code yourself. Instructions: <a href=\"../meta-pixel/\">meta-pixel page</a>. Needed for the website test from week 2 — and so that website requests also arrive in the Telegram group.",
  "Сайт: пригласить нас в Netlify (1 минута) или вставить код самим. Инструкция: <a href=\"../meta-pixel/\">страница про код сайта</a>. Нужно для проверки формы сайта со 2-й недели и чтобы заявки с сайта тоже приходили в группу Telegram."),
 ("Check your email: did our test request from the website (name テスト送信（連絡不要）, Nov 5) arrive?",
  "Проверить почту: пришла ли наша тестовая заявка с сайта (имя テスト送信（連絡不要）, 5 ноября)?"),
 ("Join our Telegram group for requests (link in chat) — or tell us if your team prefers LINE.",
  "Вступить в нашу группу заявок в Telegram (ссылка в чате) или сказать, если команде удобнее LINE."),
 ("Install the free <b>Meta Business Suite</b> app on the phone of the person who answers requests and turn on notifications — new requests and Instagram messages will pop up there.",
  "Поставить бесплатное приложение <b>Meta Business Suite</b> на телефон того, кто отвечает на заявки, и включить уведомления — туда будут приходить новые заявки и сообщения из Instagram."),
]

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>TOTALFIT NOAH — Ads launch</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#F4F4EF;--ink:#111;--muted:#5f5f5f;--card:#fff;--green:#B2FF00}}
*{{box-sizing:border-box;margin:0}}
body{{background:var(--bg);color:var(--ink);font:16px/1.55 Inter,'Noto Sans JP',sans-serif;padding:0 16px 56px}}
html[lang=en] [data-l=ru],html[lang=ru] [data-l=en]{{display:none!important}}
.top{{position:sticky;top:0;z-index:5;background:#111;color:#fff;margin:0 -16px;padding:10px 16px}}
.top-in{{max-width:1000px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;gap:12px}}
.brand{{font-weight:800;letter-spacing:.02em}} .lang button{{background:none;border:1.5px solid #555;color:#fff;border-radius:999px;padding:4px 12px;font:600 13px Inter;margin-left:6px;cursor:pointer}}
.lang button.on{{background:var(--green);color:#111;border-color:var(--green)}}
main{{max-width:1000px;margin:0 auto}}
.hero{{padding:32px 0 8px}} h1{{font-size:clamp(26px,5vw,40px);font-weight:800;letter-spacing:-.02em;line-height:1.15}}
.hero p{{color:#333;margin-top:10px;max-width:720px}}
.chips{{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}} .chips span{{background:#111;color:#fff;border-radius:999px;padding:6px 14px;font-size:14px}} .chips span.g{{background:var(--green);color:#111}}
nav{{display:flex;flex-wrap:wrap;gap:6px 16px;margin-top:16px}} nav a{{color:#111;font-weight:600;font-size:14px}}
.blk{{background:var(--card);border-radius:22px;padding:22px;margin-top:24px}}
.blk h2{{font-size:23px;font-weight:800;letter-spacing:-.01em;margin-bottom:10px}} .blk h3{{font-size:17px;margin:18px 0 8px}}
.blk p{{margin-bottom:8px;color:#333}}
ol.steps{{list-style:none;padding:0;counter-reset:s;display:grid;gap:8px}}
ol.steps li{{counter-increment:s;background:var(--bg);border-radius:14px;padding:12px 12px 12px 48px;position:relative}}
ol.steps li::before{{content:counter(s);position:absolute;left:12px;top:12px;width:26px;height:26px;border-radius:50%;background:var(--green);font-weight:800;text-align:center;line-height:26px}}
ul.need{{list-style:none;padding:0;display:grid;gap:8px}} ul.need li{{display:flex;gap:10px;align-items:flex-start;background:var(--bg);border-radius:14px;padding:12px}}
ul.need input{{width:20px;height:20px;margin-top:3px;flex:none;accent-color:#111}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:12px}} .two>div{{border:1.5px solid #ddd;border-radius:16px;padding:14px}}
.two h3{{margin-top:0}}
.script{{background:#111;color:#fff;border-radius:16px;padding:16px;margin-top:8px}} .script .ja{{font:16px/1.7 'Noto Sans JP';color:#fff}} .script p{{color:#cfcfcf;font-size:14px;margin-top:6px}}
table{{width:100%;border-collapse:collapse;font-size:15px}} th,td{{text-align:left;padding:8px;border-bottom:1px solid #e5e5e5;vertical-align:top}} th{{color:var(--muted);font-weight:600}}

.tg{{margin-top:16px;border:2px solid var(--green);border-radius:16px;padding:14px}} .tg h3{{margin-top:0}} .msg{{background:#e9f7d2;border-radius:12px;padding:10px 12px;font:14px/1.6 'Noto Sans JP',Inter;margin:8px 0 12px}}
.tw{{overflow-x:auto}}
.ads{{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px}}
.ad{{background:var(--card);border-radius:20px;padding:14px;display:grid;grid-template-columns:200px 1fr;gap:14px}}
.ph{{border:5px solid #111;border-radius:18px;overflow:hidden;background:#fff;align-self:start}}
.ig{{display:flex;justify-content:space-between;padding:6px 8px;font-size:11px}} .ig span{{color:var(--muted)}}
.ph img,.ph video{{display:block;width:100%;aspect-ratio:4/5;object-fit:cover}}
.cta{{display:flex;justify-content:space-between;align-items:center;background:#f2f2f2;padding:6px 8px;font:700 11px 'Noto Sans JP'}} .cta i{{font-style:normal;background:#0866ff;color:#fff;border-radius:6px;padding:4px 8px}}
.tx h3{{font-size:17px;display:flex;gap:8px;align-items:center;flex-wrap:wrap}} .n{{background:var(--green);border-radius:8px;padding:0 8px}}
.tx .ja{{font:14px/1.6 'Noto Sans JP';margin-top:6px}} .tx .tr{{font-size:14px;color:var(--muted);margin-top:6px}}
.note{{font-size:14px;color:var(--muted)}}
footer{{margin-top:32px;color:var(--muted);font-size:13px;text-align:center}}
@media (max-width:820px){{.ads,.two{{grid-template-columns:1fr}}}}
@media (max-width:480px){{.ad{{grid-template-columns:1fr}}.ph{{max-width:260px}}}}
</style></head><body>
<header class="top"><div class="top-in"><div class="brand">TOTALFIT NOAH</div><div class="lang"><button data-set="en">EN</button><button data-set="ru">RU</button></div></div></header>
<main>
<section class="hero">
{b("Instagram & Facebook ads: what we launch and what you do with the requests", "Реклама в Instagram и Facebook: что запускаем и что делать с заявками", "h1")}
{b("A short plan for the team. Please read it, check the list in section 4, and reply «OK» or send corrections. The ads are switched off until you approve.",
   "Короткий план для команды клуба. Прочитайте, проверьте список в разделе 4 и ответьте «ОК» или пришлите правки. Реклама выключена, пока вы не одобрите.")}
<div class="chips"><span data-l="en">People 25+ within 6 km of Hongodai</span><span data-l="ru">Люди 25+ в 6 км от Хонгодая</span><span data-l="en">8 ads in Japanese</span><span data-l="ru">8 объявлений на японском</span><span class="g" data-l="en">¥2,000 / day</span><span class="g" data-l="ru">¥2 000 в день</span><span data-l="en">Goal: trial bookings</span><span data-l="ru">Цель: записи на пробное</span></div>
<nav><a href="#how" data-l="en">1. How it works</a><a href="#how" data-l="ru">1. Как это работает</a><a href="#leads" data-l="en">2. Where requests arrive</a><a href="#leads" data-l="ru">2. Куда приходят заявки</a><a href="#handle" data-l="en">3. How to answer</a><a href="#handle" data-l="ru">3. Как отвечать</a><a href="#need" data-l="en">4. What we need from you</a><a href="#need" data-l="ru">4. Что нужно от вас</a><a href="#ads" data-l="en">5. The 8 ads</a><a href="#ads" data-l="ru">5. 8 объявлений</a></nav>
</section>

<section class="blk" id="how">
{b("1. How it works", "1. Как это работает", "h2")}
<ol class="steps">
<li>{b("A person near the gym sees our ad in Instagram or Facebook.", "Человек рядом с клубом видит наше объявление в Instagram или Facebook.", "span")}</li>
<li>{b("Taps «予約する» (Book). A short form opens inside Instagram — name, phone, email fill in automatically, they choose a program.", "Нажимает «予約する» (Забронировать). Прямо в Instagram открывается короткая форма: имя, телефон, почта подставляются сами, человек выбирает программу.", "span")}</li>
<li>{b("The request arrives in our Telegram group (section 2). <b>You contact the person within 1 hour</b> and book a trial.", "Заявка приходит в нашу группу Telegram (раздел 2). <b>Вы связываетесь с человеком в течение часа</b> и записываете на пробное.", "span")}</li>
<li>{b("Trial → membership. You mark who came and who joined — this tells us which ad brings real members.", "Пробное → абонемент. Вы отмечаете, кто пришёл и кто купил: так мы видим, какое объявление приводит настоящих клиентов.", "span")}</li>
</ol>
<h3>{b("What to expect", "Чего ожидать", "span")}</h3>
<p>{b("<b>First 7 days</b> Meta is learning: requests come unevenly. We do not change anything during this week. At ¥2,000/day expect roughly <b>5–8 requests in the first 2 weeks</b>. Then we switch off the weak ads and spend more on the best ones.",
   "<b>Первые 7 дней</b> Meta учится, заявки идут неровно. Всю неделю мы ничего не меняем. При ¥2 000 в день ожидайте примерно <b>5–8 заявок за первые 2 недели</b>. Потом выключаем слабые объявления и вкладываем больше в лучшие.", "span")}</p>
<p>{b("<b>From week 2</b> we also test the website form: the 2 best ads lead to totalfitnoah.com, the person fills the form there. We compare which way brings more people <u>who actually come to the trial</u>.",
   "<b>Со 2-й недели</b> проверяем и форму сайта: 2 лучших объявления ведут на totalfitnoah.com, человек заполняет форму там. Сравниваем, какой путь приводит больше людей, <u>которые реально приходят на пробное</u>.", "span")}</p>
<p>{b("<b>Language:</b> all ads are in Japanese. Almost all people within 6 km read Japanese, the form is in Japanese, and all competitors advertise in Japanese. The English-speaking coach is used as an advantage <i>inside</i> Japanese ads. An English group can be added later as a separate small test.",
   "<b>Язык:</b> все объявления на японском. Почти все в радиусе 6 км читают по-японски, форма на японском, и все конкуренты рекламируются на японском. Англоговорящий тренер — это преимущество, о котором говорим <i>внутри</i> японских объявлений. Английскую группу можно добавить позже отдельным маленьким тестом.", "span")}</p>
</section>

<section class="blk" id="leads">
{b("2. Where requests arrive", "2. Куда приходят заявки", "h2")}
<div class="two">
<div>{b("Instagram form (from day 1)", "Форма в Instagram (с первого дня)", "h3")}
{b("Arrives in <b>Meta Business Suite</b> → Leads (on the computer: business.facebook.com, on the phone: Meta Business Suite app). We also set up an automatic copy <b>to your email / a Google Sheet</b> — tell us the address.",
   "Приходит в <b>Meta Business Suite</b> → Лиды (на компьютере business.facebook.com, на телефоне приложение Meta Business Suite). Ещё мы настроим автоматическую копию <b>на вашу почту или в Google-таблицу</b> — скажите адрес.")}
{b("You get: name, phone, email, chosen program.", "Вы получаете: имя, телефон, почту, выбранную программу.")}</div>
<div>{b("Website form (from week 2)", "Форма на сайте (со 2-й недели)", "h3")}
{b("Arrives the same way as today: the website form on totalfitnoah.com sends it <b>to the club email</b>.",
   "Приходит так же, как сейчас: форма на totalfitnoah.com присылает её <b>на почту клуба</b>.")}
{b("To know the request came from an ad, we add a code to the website (section 4). Without it Meta cannot learn from website requests.",
   "Чтобы понимать, что заявка пришла из рекламы, на сайт ставится код (раздел 4). Без него Meta не учится на заявках с сайта.")}</div>
</div>
<div class="tg">{b("All requests in one place: a Telegram group", "Все заявки в одном месте: группа в Telegram", "h3")}
{b("Every new request — from the Instagram form <b>and</b> from the website — comes as a message to one Telegram group «TOTALFIT NOAH — 申込み / Leads». The group and the bot are ready and tested; you only join.",
   "Каждая новая заявка — и из формы Instagram, <b>и</b> с сайта — приходит сообщением в одну группу Telegram «TOTALFIT NOAH — 申込み / Leads». Группа и бот уже готовы и проверены, вам нужно только вступить.")}
<div class="msg"><b>📩 新しい申込み / New lead — Instagram/Facebook</b><br>🕒 11/10 14:32 (JST)<br>名前 / Name: 山田 花子<br>電話 / Phone: 090-xxxx-xxxx<br>メール / Email: hanako@…<br>体験したいプログラムは？: キックボクシング<br><br>1時間以内に連絡してください。連絡したら ✅ を返信。</div>
<ol class="steps">
<li>{b("Install Telegram (free) on the phone of the person who answers requests.", "Поставить Telegram (бесплатно) на телефон того, кто отвечает на заявки.", "span")}</li>
<li>{b("Open the invite link we send you — you are in the group.", "Открыть ссылку-приглашение, которую мы пришлём, — и вы в группе.", "span")}</li>
<li>{b("When you contact the person, reply to the message with ✅ — everyone sees the request is taken. Booked a trial — reply with the date.", "Когда связались с человеком, ответьте на сообщение ✅ — все видят, что заявку взяли. Записали на пробное — ответьте датой.", "span")}</li>
</ol>
{b("Requests also stay in Meta Business Suite and in the website email as a backup. If your team works only in LINE, tell us — we can send the same messages to a LINE group instead.",
   "Заявки при этом остаются и в Meta Business Suite, и на почте сайта — как запасной вариант. Если команда работает только в LINE, скажите: те же сообщения можно слать в группу LINE.", cls="note")}
</div>
{b("Also: people may write to Instagram Direct or comment on an ad. Please answer them the same day — it is a request too.",
   "Кроме того: люди могут писать в Директ Instagram или комментировать объявление. Отвечайте им в тот же день — это тоже заявка.", cls="note")}
</section>

<section class="blk" id="handle">
{b("3. How to answer a request", "3. Как отвечать на заявку", "h2")}
<ol class="steps">
<li>{b("<b>Within 1 hour</b> (in opening hours): call. A request answered the next day is usually lost.", "<b>В течение часа</b> (в рабочее время): позвонить. Заявка, на которую ответили на следующий день, обычно пропадает.", "span")}</li>
<li>{b("No answer → send SMS or email right away (text below), then call again the next day. Up to <b>3 tries</b> in 3 days.", "Не взял трубку → сразу SMS или письмо (текст ниже), на следующий день снова звонок. До <b>3 попыток</b> за 3 дня.", "span")}</li>
<li>{b("Offer two concrete times: «Tuesday 19:00 or Saturday 10:00?» — easier than «when is good for you».", "Предложите два конкретных времени: «вторник 19:00 или суббота 10:00?» — так проще, чем «когда вам удобно».", "span")}</li>
<li>{b("The day before the trial — a reminder (LINE or SMS). This cuts no-shows a lot.", "Накануне пробного — напоминание (LINE или SMS). Это сильно уменьшает неявки.", "span")}</li>
<li>{b("After the trial — offer membership the same day, softly. No pressure: in Japan pushy sales after free trials get complaints.", "После пробного — в тот же день мягко предложить абонемент. Без давления: в Японии на навязчивые продажи после бесплатных пробных жалуются.", "span")}</li>
</ol>
<h3>{b("Message if they don't pick up", "Сообщение, если не взяли трубку", "span")}</h3>
<div class="script"><div class="ja">〇〇様、TOTALFIT NOAHです。無料体験のお申し込みありがとうございます！ご都合のよい日時を2〜3つ教えていただけますか？（例：火曜19時／土曜10時）本郷台駅から徒歩15分、駐車場もあります。</div>
{b("«Mr/Ms 〇〇, this is TOTALFIT NOAH. Thank you for booking a free trial! Could you send 2–3 times that suit you? (e.g. Tue 19:00 / Sat 10:00) 15 min walk from Hongodai station, parking available.»",
   "«〇〇-сан, это TOTALFIT NOAH. Спасибо за заявку на бесплатное пробное! Напишите 2–3 удобных времени (например, вт 19:00 / сб 10:00). 15 минут пешком от станции Хонгодай, есть парковка.»")}</div>
<h3>{b("Keep a simple table (we will make it for you)", "Ведите простую таблицу (мы её подготовим)", "span")}</h3>
<div class="tw"><table>
<tr><th>{b("Date","Дата","span")}</th><th>{b("Name","Имя","span")}</th><th>{b("Source","Откуда","span")}</th><th>{b("Contacted","Связались","span")}</th><th>{b("Trial booked","Записан","span")}</th><th>{b("Came","Пришёл","span")}</th><th>{b("Joined","Купил","span")}</th></tr>
<tr><td>11/10</td><td>山田</td><td>Instagram</td><td>✓ 11/10</td><td>11/12 19:00</td><td>✓</td><td>{b("Family","Семья","span")}</td></tr>
</table></div>
{b("Once a week send us this table — that is how we know which ads bring members, not just requests.", "Раз в неделю присылайте нам таблицу — только так мы видим, какие объявления приводят клиентов, а не просто заявки.", cls="note")}
</section>

<section class="blk" id="need">
{b("4. What we need from you before launch", "4. Что нужно от вас до запуска", "h2")}
{b("Everything in the ad account we do ourselves — you already gave us access. Only these things need you:", "Всё в рекламном кабинете мы делаем сами — доступ вы уже дали. От вас нужно только это:")}
<ul class="need">{''.join(f'<li><input type="checkbox">{b(en, ru, "span")}</li>' for en, ru in NEED)}</ul>
</section>

<section id="ads">
<div class="blk" style="margin-bottom:0">{b("5. The 8 ads we test", "5. 8 объявлений, которые проверяем", "h2")}
{b("Each one tests a different idea. Every ad also has a tall version for Reels and Stories. Under each: the Japanese text people see and a translation.",
   "Каждое проверяет свою идею. У каждого есть и вертикальная версия для Reels и Stories. Под каждым — японский текст, который увидят люди, и перевод.")}</div>
<div class="ads">{cards}</div>
</section>
<footer>TOTALFIT NOAH · {b("Ads plan, November 2026", "План рекламы, ноябрь 2026", "span")}</footer>
</main>
<script>
(function(){{
  function setLang(l){{document.documentElement.lang=l;document.querySelectorAll('.lang button').forEach(function(x){{x.classList.toggle('on',x.dataset.set===l)}});try{{localStorage.setItem('tfn-launch-lang',l)}}catch(e){{}}}}
  var q=new URLSearchParams(location.search).get('lang'),s=null;try{{s=localStorage.getItem('tfn-launch-lang')}}catch(e){{}}
  setLang(q||s||'en');
  document.querySelectorAll('.lang button').forEach(function(x){{x.onclick=function(){{setLang(x.dataset.set)}}}});
}})();
</script>
</body></html>"""

(ROOT / "index.html").write_text(page, encoding="utf-8")
print("ok")
