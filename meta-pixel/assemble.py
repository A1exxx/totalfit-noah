"""Собирает страницу инструкции: стили берёт из meta-setup, тело — из body.part.html."""
import pathlib

HERE = pathlib.Path(__file__).parent
old = (HERE.parent / "meta-setup" / "index.html").read_text(encoding="utf-8")
head = old.split("<body>")[0]
head = head.replace("<title>TOTALFIT NOAH — Meta Ads Setup</title>", "<title>TOTALFIT NOAH — Website form setup</title>")
head = head.replace("</style>", ".copy{align-items:flex-start}\n.copy code{white-space:pre-wrap;font-size:12px;line-height:1.45}\n</style>")
body = (HERE / "body.part.html").read_text(encoding="utf-8")
(HERE / "index.html").write_text(head + body, encoding="utf-8")
print("ok", len(head + body))
