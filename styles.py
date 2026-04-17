CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&display=swap');
html, body, [class*="css"] { font-family: 'Cormorant Garamond', Georgia, serif; }
.main .block-container { padding: 0 !important; max-width: 820px !important; }

.hero-block {
    background: #1a2e1a; padding: 3.5rem 2rem 2.5rem;
    text-align: center; border-bottom: 3px solid #b8a97a;
    position: relative; overflow: hidden;
}
.hero-mountains { position: absolute; bottom: 0; left: 0; width: 100%; z-index: 1; }
.hero-content { position: relative; z-index: 2; }
.eyebrow {
    font-family: 'Cormorant Garamond', serif; font-size: 0.72rem;
    letter-spacing: 5px; text-transform: uppercase; color: #b8a97a; margin-bottom: 1rem;
}
.hero-title {
    font-family: 'Cormorant Garamond', serif; font-size: 3.2rem;
    font-weight: 300; color: #fdfcf8; line-height: 1.15; margin-bottom: 0.5rem;
}
.hero-title em { font-style: italic; color: #b8a97a; }
.gold-line { width: 80px; height: 1px; background: #b8a97a; margin: 1rem auto; }
.hero-sub {
    font-family: 'Cormorant Garamond', serif; font-size: 1.1rem;
    font-weight: 300; color: #c8c0a8; letter-spacing: 2px;
}
.pill-row { display: flex; justify-content: center; flex-wrap: wrap; gap: 1.2rem; margin-top: 1.2rem; }
.pill {
    font-family: 'Cormorant Garamond', serif; font-size: 0.68rem;
    letter-spacing: 3px; text-transform: uppercase; color: #b8a97a;
}

.illus-band { background: #f0ebe0; }
.illus-band-inner { display: flex; align-items: stretch; }
.illus-band-copy { width: 38%; padding: 1.5rem 1.5rem 1rem; }
.illus-band-copy.right { text-align: right; }
.illus-band-art { width: 62%; }
.illus-eyebrow { font-size: 0.65rem; letter-spacing: 3px; text-transform: uppercase; color: #8b7a5a; margin-bottom: .4rem; }
.illus-title { font-size: 1.45rem; font-weight: 300; color: #1a2e1a; line-height: 1.2; margin-bottom: .4rem; }
.illus-title em { font-style: italic; color: #5a7a3a; }
.illus-desc { font-size: 0.85rem; color: #4a3a2a; line-height: 1.65; }
.illus-link {
    font-size: 0.78rem; color: #5a7a3a; border-bottom: 0.5px solid #5a7a3a;
    text-decoration: none; display: inline-block; margin-top: .4rem;
}

.adventure-band { background: #f0ebe0; border-top: 0.5px solid #e0d8c8; }
.adventure-header { text-align: center; padding: 1.5rem 2rem .75rem; }
.adventure-eyebrow { font-size: 0.65rem; letter-spacing: 4px; text-transform: uppercase; color: #8b7a5a; margin-bottom: .35rem; }
.adventure-title { font-size: 1.75rem; font-weight: 300; font-style: italic; color: #1a2e1a; }

.body-wrap { background: #fdfcf8; padding: 2rem 2.5rem; }
.day-row { display: flex; gap: 0; margin-bottom: 2.5rem; align-items: flex-start; }
.content-left { flex: 1; border-right: 1px solid #c8b882; padding-right: 1.5rem; }
.content-right { flex: 1; border-left: 1px solid #c8b882; padding-left: 1.5rem; }
.icon-col { width: 90px; flex-shrink: 0; display: flex; flex-direction: column; align-items: center; padding-top: .25rem; }
.day-name { font-size: 1.4rem; font-weight: 400; color: #1a2e1a; margin-bottom: .8rem; }
.event-row { display: flex; gap: 1rem; margin-bottom: .55rem; align-items: baseline; }
.event-time { font-size: 0.72rem; letter-spacing: 1px; color: #8b7a5a; min-width: 68px; flex-shrink: 0; }
.event-desc { font-size: 0.92rem; color: #2c2c2a; line-height: 1.7; }
.event-desc strong { font-weight: 500; color: #1a2e1a; }
.event-desc a { color: #5a7a3a; text-decoration: none; border-bottom: 0.5px solid #5a7a3a; }
.icon-label { font-size: 0.58rem; letter-spacing: 2px; text-transform: uppercase; color: #b8a97a; margin-top: .5rem; text-align: center; }

.childcare-note { background: #f8f2e4; border-top: 1px solid #e0d8c8; padding: 1.25rem 2.5rem; text-align: center; }
.childcare-note p { font-size: 0.88rem; font-style: italic; color: #6a5a3a; letter-spacing: .5px; line-height: 1.7; }

.rsvp-eyebrow { font-size: 0.65rem; letter-spacing: 4px; text-transform: uppercase; color: #8b7a5a; margin-bottom: .3rem; }
.rsvp-title { font-size: 1.4rem; font-weight: 300; font-style: italic; color: #1a2e1a; margin-bottom: .5rem; }

.footer-block { background: #fdfcf8; text-align: center; padding: 2rem; border-top: 1px solid #e8e0cc; }
.footer-block p { font-size: 0.88rem; color: #8b7a5a; letter-spacing: 1px; margin-bottom: .4rem; }
.footer-sig { font-style: italic; color: #b8a97a !important; font-size: 1rem !important; }
</style>
"""
