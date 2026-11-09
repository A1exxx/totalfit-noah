"""Страница «Тест: 8 объявлений» — ровно то, что собрано в кабинете Meta 05.11 (лента 4:5 и Reels 9:16, текст и перевод)."""
import html, pathlib

ROOT = pathlib.Path(__file__).parent
HEAD = "コーチがいつも隣に｜無料体験"

CHECK = {
 "T1": "Цепляет ли главное отличие клуба «тренер рядом», показанное через живое фото.",
 "T2": "То же отличие, но без фото, только текстом: работает ли боль «в большом зале ты один».",
 "T3": "Сообщество: «тебя знают по имени» против одиночества в сетевом зале.",
 "T4": "Женщины-новички: страх «не справлюсь» снимаем кикбоксингом без спаррингов.",
 "T5": "Прямое предложение без истории: просто «бесплатная пробная».",
 "T6": "Цена в кадре: семейный тариф ¥11 000 как главный довод.",
 "T7": "Родители: ребёнок на занятии, родители тренируются в это же время.",
 "T8": "Видео против картинки на ту же мысль, что у T1.",
}

# почему выбрано: на чём основано
WHY = {
 "T1": "Главное отличие клуба от сетевых залов (идея владельца). У конкурентов рядом такого обещания в рекламе нет: в Офуне все говорят о цене и акциях. Живое фото со съёмки клуба: тренер с лапами, лицо видно.",
 "T2": "Та же идея, но проверяем, цепляет ли «боль» без фото. Объявления-текст на ярком фоне в ленте часто выделяются среди фото. Риск: может выглядеть как баннер, и Meta покажет его реже.",
 "T3": "Главная причина, по которой бросают зал: скучно одному (около 40% новичков уходят за полгода). Ставка на атмосферу маленького клуба против больших сетей.",
 "T4": "Женщины-новички — самая частая аудитория пробных занятий в кикбоксинге. У конкурентов в Офуне фитнес-кикбоксинг тоже есть, но без акцента «без спаррингов, смеёмся».",
 "T5": "Прямое предложение без истории. Почти все конкуренты в рекламе дают акцию; проверяем, хватит ли одной «бесплатной пробной». Слабое место: нет срока («до 30.11»), а у конкурентов срок есть почти всегда.",
 "T6": "Цена в кадре — так делают почти все конкуренты. ¥11 000 за всю семью — сильный довод: у сетевых залов столько стоит один взрослый.",
 "T7": "Семьи с детьми — главная аудитория района. Детские группы почти заполнены (среда полная), поэтому ведём на «родители тренируются, пока дети на занятии».",
 "T8": "Конкуренты чаще всего крутят короткие ролики по 15 секунд. Наш ролик собран из фото, это слабее настоящего видео. Проверяем, даёт ли движение больше нажатий, чем картинка T1 с той же мыслью.",
}

# номер, о чём, файл ленты, файл Reels (None = видео), текст JA, перевод, заголовок JA, перевод заголовка
ADS = [
 ("T1", "Тренер всегда рядом", "T1-c01-coach-pads-feed.jpg", "T1-c01-coach-pads-reels.jpg",
  "大型ジムに入会したけど、マシンの使い方も分からず一人きり…。TOTALFIT NOAHでは、コーチがいつも隣でサポートします。本郷台エリア・駐車場あり。無料体験は手ぶらでOK。",
  "Записался в большой зал, а как пользоваться тренажёрами — непонятно, и ты один. В TOTALFIT NOAH тренер всегда рядом. Хонгодай, есть парковка. Пробное бесплатно, можно без формы.",
  HEAD, "Тренер всегда рядом | Бесплатная пробная"),
 ("T2", "90% тренажёров не используешь", "T2-c02-90-percent-feed.jpg", "T2-c02-90-percent-reels.jpg",
  "大型ジムのマシン、9割は使わないまま辞めていませんか？人は多いのに、あなたは一人。NOAHでは、毎回コーチが隣で教えます。本郷台エリア・駐車場あり。無料体験受付中。",
  "Бросали большой зал, так и не освоив 90% тренажёров? Людей много, а ты один. В NOAH тренер каждый раз рядом и показывает. Хонгодай, парковка. Пробное бесплатно.",
  "マシンは多い。でも、コーチがいる。", "Тренажёров много. Но здесь есть тренер."),
 ("T3", "Здесь твоё место", "T3-c06-belong-feed.jpg", "T3-c06-belong-reels.jpg",
  "名前で呼び合う仲間と、コーチがいるジム。一人だと続かなかった運動も、ここなら続けられます。本郷台エリア・駐車場あり。無料体験受付中。",
  "Зал, где тебя знают по имени — и участники, и тренер. Если один бросал — здесь получится. Хонгодай, парковка. Пробное бесплатно.",
  "ここが、あなたの居場所。", "Здесь твоё место."),
 ("T4", "Первый раз — и смеёмся", "T4-c09-laugh-kick-feed.jpg", "T4-c09-laugh-kick-reels.jpg",
  "はじめてでも大丈夫。組手なしのキックボクシングで、楽しく体を動かしませんか。女性の方も多く通うアットホームなジムです。本郷台エリア・駐車場あり。無料体験は手ぶらでOK。",
  "Можно с нуля. Кикбоксинг без спаррингов — просто двигаться с удовольствием. Уютный зал, много женщин. Хонгодай, парковка. Пробное бесплатно, без формы.",
  "組手なしキックボクシング｜無料体験", "Кикбоксинг без спаррингов | Бесплатная пробная"),
 ("T5", "Бесплатная пробная", "T5-c10-free-trial-green-feed.jpg", "T5-c10-free-trial-green-reels.jpg",
  "TOTALFIT NOAHの無料体験、受付中。キックボクシング・ピラティス・フィットネス・卓球。手ぶらでOK、本郷台エリア・駐車場あり。（キッズクラスの体験は500円）",
  "Запись на бесплатную пробную открыта: кикбоксинг, пилатес, фитнес, настольный теннис. Без формы, Хонгодай, парковка. (Пробное для детей — ¥500)",
  "無料体験、受付中。手ぶらでOK", "Запись на бесплатную пробную. Можно без формы"),
 ("T6", "Вся семья — ¥11 000", "T6-c11-family-price-feed.jpg", "T6-c11-family-price-reels.jpg",
  "家族みんなで月11,000円（税込・入会金別途）。キッズ・キックボクシング・ピラティス・卓球。本郷台エリア・駐車場あり。まずは体験から。",
  "Вся семья — ¥11 000 в месяц (с налогом, вступительный взнос отдельно). Дети, кикбоксинг, пилатес, теннис. Хонгодай, парковка. Начните с пробного.",
  "家族みんなで月11,000円", "Вся семья — ¥11 000 в месяц"),
 ("T7", "Дети тоже ходят", "T7-c14-kids-feed.jpg", "T7-c14-kids-reels.jpg",
  "子どもも一緒に通えるジム。キッズクラスの間に、パパ・ママはトレーニング。家族みんなで月11,000円（税込・入会金別途）。本郷台エリア・駐車場あり。大人は無料体験、キッズ体験は500円。",
  "Зал, куда можно ходить с детьми: пока ребёнок на занятии, родители тренируются. Семья — ¥11 000 в месяц. Хонгодай, парковка. Взрослым пробное бесплатно, детям — ¥500.",
  "子どもも、一緒に通える。", "Дети тоже могут ходить с вами."),
 ("T8", "Видео: тренер рядом", "T8-v11-coach.mp4", None,
  "人は多いのに、ひとりで筋トレ？NOAHでは、コーチがいつも隣に。重さもフォームもその場でサポート。本郷台エリア・駐車場あり。まずは無料体験から。",
  "Людей много, а тренируешься один? В NOAH тренер всегда рядом — сразу поправит вес и технику. Хонгодай, парковка. Начните с бесплатной пробной.",
  HEAD, "Тренер всегда рядом | Бесплатная пробная"),
]

e = html.escape


def media(src, cls):
    if src.endswith(".mp4"):
        return f'<video class="{cls}" src="img/{src}" autoplay muted loop playsinline></video>'
    return f'<img class="{cls}" src="img/{src}" alt="" loading="lazy">'


cards = []
for num, title, feed, reels, ja, ru, hja, hru in ADS:
    reels = reels or feed
    kind = "видео 8 сек, без звука" if feed.endswith(".mp4") else "картинка"
    cards.append(f"""
<section class="ad">
  <h2><span class="num">{num}</span>{e(title)} <small>{kind}</small></h2>
  <div class="mocks">
    <figure class="phone feed">
      <figcaption>Лента Instagram / Facebook</figcaption>
      <div class="screen">
        <div class="top"><span class="ava"></span><b>totalfit.noahgym</b><span class="spon">広告</span></div>
        <p class="txt">{e(ja)}</p>
        {media(feed, "pic")}
        <div class="cta"><span>{e(hja)}</span><button>予約する</button></div>
      </div>
    </figure>
    <figure class="phone reels">
      <figcaption>Reels и Stories</figcaption>
      <div class="screen tall">
        {media(reels, "full")}
        <div class="rbar"><b>totalfit.noahgym</b> · 広告<button>予約する</button></div>
      </div>
    </figure>
    <div class="tr">
      <h3>Что написано (перевод)</h3>
      <p><b>Текст:</b> {e(ru)}</p>
      <p><b>Заголовок:</b> {e(hru)}</p>
      <p><b>Кнопка:</b> «Забронировать» → форма заявки прямо в Instagram (путь А)</p>
      <p class="chk"><b>Что проверяем:</b> {e(CHECK[num])}</p>
      <details><summary>Почему выбрано это объявление</summary><p>{e(WHY[num])}</p></details>
    </div>
  </div>
</section>""")

page = f"""<!doctype html><html lang="ru"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>TOTALFIT NOAH — тест 8 объявлений</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
:root{{--bg:#F4F4EF;--ink:#111;--muted:#666;--card:#fff;--green:#B2FF00}}
*{{box-sizing:border-box;margin:0}}
body{{background:var(--bg);color:var(--ink);font:16px/1.5 Inter,'Noto Sans JP',sans-serif;padding:0 16px 48px}}
.brandbar{{background:#111;margin:0 -16px;padding:12px 16px}}.brandbar img{{height:28px;width:auto;display:block;max-width:1100px;margin:0 auto}}
header{{max-width:1100px;margin:0 auto;padding:32px 0 8px}}
header h1{{font-size:clamp(26px,5vw,40px);font-weight:800;letter-spacing:-.02em}}
header p{{color:var(--muted);margin-top:8px;max-width:720px}}
.facts{{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px}}
.facts span{{background:#111;color:#fff;border-radius:999px;padding:6px 14px;font-size:14px}}
.facts span.g{{background:var(--green);color:#111}}
.ad{{max-width:1100px;margin:32px auto 0;background:var(--card);border-radius:24px;padding:24px}}
.ad h2{{font-size:22px;font-weight:800;display:flex;align-items:center;gap:12px;flex-wrap:wrap}}
.ad h2 small{{font-size:14px;color:var(--muted);font-weight:400}}
.num{{background:var(--green);border-radius:10px;padding:2px 10px}}
.mocks{{display:grid;grid-template-columns:320px 220px 1fr;gap:24px;margin-top:18px;align-items:start}}
figure{{margin:0}} figcaption{{font-size:13px;color:var(--muted);margin-bottom:6px}}
.screen{{background:#000;border-radius:22px;overflow:hidden;border:6px solid #111}}
.feed .screen{{background:#fff}}
.top{{display:flex;align-items:center;gap:8px;padding:10px;font-size:13px}}
.ava{{width:28px;height:28px;border-radius:50%;background:#111 url(logo.svg) center/80% no-repeat}}
.spon{{color:var(--muted);font-size:12px}}
.txt{{font:13px/1.5 'Noto Sans JP';padding:0 10px 8px;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}}
.pic{{display:block;width:100%;aspect-ratio:4/5;object-fit:cover}}
.cta{{display:flex;justify-content:space-between;align-items:center;gap:8px;padding:10px;background:#f3f3f3;font:700 13px 'Noto Sans JP'}}
button{{border:0;background:#0866ff;color:#fff;border-radius:8px;padding:7px 12px;font:700 12px 'Noto Sans JP';white-space:nowrap}}
.tall{{position:relative;aspect-ratio:9/16}}
.full{{width:100%;height:100%;object-fit:cover;display:block}}
.rbar{{position:absolute;left:0;right:0;bottom:0;padding:10px;color:#fff;font-size:12px;background:linear-gradient(0deg,rgba(0,0,0,.7),transparent);display:flex;justify-content:space-between;align-items:center}}
.tr h3{{font-size:16px;margin-bottom:8px}} .tr p{{margin-bottom:10px;color:#333}}
nav{{display:flex;flex-wrap:wrap;gap:8px 16px;margin-top:16px}} nav a{{color:#111;font-weight:600;font-size:14px}}
.blk{{max-width:1100px;margin:32px auto 0;background:var(--card);border-radius:24px;padding:24px}}
.blk h2,.sec{{font-size:24px;font-weight:800;letter-spacing:-.01em}} .sec{{max-width:1100px;margin:40px auto 0}}
.blk h3{{font-size:17px;margin:22px 0 10px}} .lead{{margin-top:8px;color:#333;max-width:820px}}
.flow{{list-style:none;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;counter-reset:s}}
.flow li{{counter-increment:s;background:var(--bg);border-radius:14px;padding:12px 12px 12px 44px;position:relative;font-size:14px;color:#444}}
.flow li::before{{content:counter(s);position:absolute;left:12px;top:12px;width:24px;height:24px;border-radius:50%;background:var(--green);font-weight:800;text-align:center;line-height:24px;color:#111}}
.flow.b li::before{{background:#111;color:#fff}}
.flow li b{{display:block;color:#111;font-size:15px}}
.vs{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:16px}} .vs div{{border:1.5px solid #ddd;border-radius:14px;padding:12px;font-size:14px}}
table{{width:100%;border-collapse:collapse;margin-top:12px;font-size:15px}} th,td{{text-align:left;padding:8px;border-bottom:1px solid #e5e5e5}} th{{color:var(--muted);font-weight:600}}
.note{{color:var(--muted);font-size:13px;margin-top:6px}}
.rules,.weeks{{margin-top:14px;padding-left:20px}} .rules li,.weeks li{{margin-bottom:10px}}
details{{margin-top:10px;background:var(--bg);border-radius:12px;padding:10px 12px}} summary{{cursor:pointer;font-weight:700}} details p,details li{{margin-top:8px;color:#333;font-size:15px}} details ul{{padding-left:20px}}
.chk{{background:var(--bg);border-radius:12px;padding:10px}}
@media (max-width:860px){{.flow{{grid-template-columns:1fr 1fr}}.vs{{grid-template-columns:1fr}}}}
@media (max-width:520px){{.flow{{grid-template-columns:1fr}}}}
@media (max-width:860px){{.mocks{{grid-template-columns:1fr 1fr}}.tr{{grid-column:1/-1}}}}
@media (max-width:520px){{.mocks{{grid-template-columns:1fr}}.reels{{max-width:240px}}}}
</style></head><body>
<div class="brandbar"><img src="logo.svg" alt="TOTALFIT NOAH"></div>
<header>
<h1>Тест рекламы: путь, правила, 8 объявлений</h1>
<p>План первого теста на утверждение. Объявления ниже уже собраны в рекламном кабинете клуба. Кампания выключена и ничего не показывает, пока её не включат.</p>
<div class="facts"><span>Все от 25 лет</span><span>Круг 6 км вокруг станции Хонгодай</span><span>Без интересов</span><span>Заявка через форму в Instagram</span><span class="g">¥2 000 в день</span></div>
<nav><a href="#path">Путь человека</a><a href="#rules">Что выключаем и добавляем</a><a href="#steps">По неделям</a><a href="#need">Что нужно до старта</a><a href="#ads">8 объявлений</a></nav>
</header>

<section class="blk" id="path">
<h2>Путь человека: от рекламы до абонемента</h2>
<p class="lead">Все 8 объявлений ведут в одно место: форму заявки прямо в Instagram и Facebook (путь А). Так честно сравниваем картинки: отличается только объявление. Форму на сайте (путь Б) включаем вторым этапом, когда клуб поставит на сайт код Meta.</p>
<h3>Путь А — форма Meta (с первого дня, все 8 объявлений)</h3>
<ol class="flow">
<li><b>Видит рекламу</b>в ленте или Reels, только если живёт в 6 км от Хонгодая и ему 25+</li>
<li><b>Жмёт «Забронировать»</b>из Instagram не уходит, сайт не открывается</li>
<li><b>Открывается форма</b>на японском: имя, почта и телефон подставляются из профиля сами, остаётся выбрать программу (кикбоксинг, пилатес, фитнес, дети, теннис)</li>
<li><b>Экран «Проверьте данные»</b>ещё одно нажатие: отсекает тех, кто нажал случайно</li>
<li><b>«Спасибо»</b>и кнопка на сайт клуба, если хочет почитать подробнее</li>
<li><b>Заявка у клуба</b>сейчас её видно только в кабинете Meta, нужно настроить письмо или таблицу</li>
<li><b>Клуб связывается в течение часа</b>звонок, письмо или LINE, записывает на пробное</li>
<li><b>Пробное → абонемент</b>клуб отмечает, кто пришёл и кто купил: только так видно, какое объявление приводит клиентов, а не просто заявки</li>
</ol>
<h3>Путь Б — форма на сайте (со 2-й недели, 2 лучших объявления)</h3>
<ol class="flow b">
<li><b>Видит рекламу</b>те же лучшие картинки</li>
<li><b>Жмёт «Подробнее»</b>открывается сайт totalfitnoah.com</li>
<li><b>Читает сайт</b>цены, расписание, фото</li>
<li><b>Заполняет форму на сайте</b>сам вводит имя, телефон и почту</li>
<li><b>Страница «Спасибо»</b>в этот момент код Meta сообщает рекламе: заявка есть</li>
<li><b>Заявка на почту клубу</b>дальше так же: звонок, пробное, абонемент</li>
</ol>
<div class="vs">
<div><b>Чего ждём от А:</b> заявок больше и дешевле, но часть людей «холоднее» и хуже берёт трубку.</div>
<div><b>Чего ждём от Б:</b> заявок меньше и дороже, зато человек уже видел цены и сайт, чаще доходит до пробного.</div>
<div><b>Как решаем:</b> побеждает путь, где дешевле <u>человек, пришедший на пробное</u>, а не просто заявка.</div>
</div>
</section>

<section class="blk" id="rules">
<h2>Что считаем успехом, что выключаем, что добавляем</h2>
<table>
<tr><th>Цифра</th><th>Хорошо</th><th>Нормально</th><th>Плохо</th></tr>
<tr><td>Цена заявки</td><td>до ¥3 500</td><td>¥3 500–6 000</td><td>дороже ¥8 000</td></tr>
<tr><td>Доля нажавших на рекламу</td><td>от 1,5%</td><td>0,8–1,5%</td><td>меньше 0,8%</td></tr>
<tr><td>Из заявок дошли до пробного</td><td>от 60%</td><td>40–60%</td><td>меньше 30%</td></tr>
</table>
<p class="note">Японских цифр по спортзалам в открытых данных нет, это мировые ориентиры. Через 2 недели заменим своими.</p>
<details class="src"><summary>На основании чего эти цифры</summary>
<p><b>Цена заявки.</b> Японских данных по заявкам для спортзалов в открытом доступе нет: ни у Meta, ни у японских агентств. Поэтому взяли мировые:</p>
<ul>
<li>WordStream, 2025: средняя заявка в Facebook по всем отраслям — $27,66 (около ¥4 100).</li>
<li>Superads, июль 2025 – июнь 2026: фитнес-центры и тренировки — около $40,60 (около ¥6 100).</li>
<li>Отсюда «нормально» — ¥3 500–6 000, «плохо» — дороже ¥8 000 (это уже на треть дороже среднего по фитнесу).</li>
</ul>
<p><b>Доля нажавших.</b> Это наша рабочая планка, а не японская статистика. Средняя доля нажатий в рекламе Meta по миру — около 1–1,5%. Меньше 0,8% обычно значит, что картинка не цепляет.</p>
<p><b>Дошли до пробного.</b> Keepme (2026, США и Канада): из записавшихся приходят около 75%. Glofox: на пробные не приходят 20–40%. С учётом тех, кто оставил заявку и не ответил на звонок, «хорошо» — от 60% заявок.</p>
<p><b>Правило выключения ¥7 500.</b> Это полторы средние заявки. Если объявление потратило столько и не дало ни одной, ждать дальше дорого.</p>
<p><b>Чего нет:</b> настоящих цифр клуба — сколько людей сейчас приходит на пробное и сколько покупает. Если клуб их даст, заменим ими мировые ориентиры.</p>
<p><b>Конкуренты</b> (смотрели их рекламу в библиотеке Meta 04.11): у Хонгодая спортзалы рекламу не крутят; в Офуне 5 студий пилатеса, фитнес-кикбоксинг, 16.11 открывается студия RINNE. Почти все дают акцию со сроком, запись через LINE, короткие ролики и цену в кадре.</p>
</details>
<ul class="rules">
<li><b>Первые 7 дней ничего не трогаем.</b> Meta учится, любая правка сбрасывает обучение.</li>
<li><b>Выключаем объявление,</b> если потратило ¥7 500 и не дало ни одной заявки, или после 3 заявок цена выше ¥8 000.</li>
<li><b>Не спешим выключать,</b> если на объявление почти не тратят: значит, Meta пока его не выбрала. Это тоже ответ — картинка слабее.</li>
<li><b>Добавляем новое на 8-й день:</b> 2–3 варианта на идею победителя (другое фото, видео вместо картинки, другая цена в заголовке).</li>
<li><b>Увеличиваем бюджет</b> на 20% раз в 3 дня, пока цена заявки держится в «нормально».</li>
<li><b>Честно про бюджет:</b> при ¥2 000 в день за 2 недели будет около 5–8 заявок. Этого хватит понять, какие картинки цепляют, но мало, чтобы точно сравнить цену заявки. Для точного ответа нужно ¥3 000–4 000 в день.</li>
</ul>
</section>

<section class="blk" id="steps">
<h2>По неделям</h2>
<ol class="weeks">
<li><b>Неделя 1.</b> Включаем 8 объявлений, путь А. Каждый день проверяем только поломки: объявление отклонено, нет показов, заявка не дошла до клуба.</li>
<li><b>День 8.</b> Первые выводы по правилам выше: оставляем 3–4 лучших, остальные выключаем. Клуб присылает, кто из заявок пришёл на пробное.</li>
<li><b>Неделя 2.</b> Добавляем 2–3 варианта победителя. Если код Meta уже на сайте — запускаем путь Б с 2 лучшими картинками, бюджет пополам.</li>
<li><b>Недели 3–4.</b> Оставляем лучший путь и лучшие картинки, наращиваем бюджет. Следующие гипотезы: запись через LINE, англоязычная группа, люди 50+ на настольный теннис, детские танцы отдельной группой.</li>
<li><b>Через месяц.</b> Подводим итоги по своим цифрам: цена заявки, доля пришедших, доля купивших.</li>
</ol>
</section>

<section class="blk" id="need">
<h2>Что нужно до старта</h2>
<ul class="rules">
<li><b>Подтвердить телефон рекламного аккаунта</b> — без этого Meta не даст включить кампанию. Делает владелец кабинета.</li>
<li><b>Решить, кто отвечает на заявки</b> и в течение какого времени: заявка, на которую ответили через день, почти всегда пропадает.</li>
<li><b>Настроить доставку заявок клубу</b> — письмом или в таблицу, а не только в кабинете Meta.</li>
<li><b>Клуб проверяет японские тексты</b> на этой странице.</li>
<li><b>Для пути Б:</b> клуб ставит на сайт код Meta по инструкции a1exxx.github.io/totalfit-noah/meta-pixel/</li>
</ul>
</section>

<h2 class="sec" id="ads">8 объявлений теста</h2>
{''.join(cards)}
</body></html>"""

(ROOT / "index.html").write_text(page, encoding="utf-8")
print("ok", len(ADS))
