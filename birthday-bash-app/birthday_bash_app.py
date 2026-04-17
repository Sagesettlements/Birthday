import streamlit as st
from assets import (
    RIVER_SVG, MOUNTAIN_SVG, ADVENTURE_SVG, PINE_DIVIDER_SVG,
    ICON_FISH, ICON_CARDS, ICON_CHAMPAGNE, ICON_RAFT, ICON_PLANE,
)
from styles import CSS

st.set_page_config(
    page_title="Sarah & Willy's 30th Birthday Bash",
    page_icon="🏔️",
    layout="centered",
)


def render_hero():
    st.markdown("""
    <div class="hero-block">
      <svg class="hero-mountains" viewBox="0 0 820 110" xmlns="http://www.w3.org/2000/svg">
        <polygon points="0,110 0,65 90,22 185,70 285,5 400,58 510,10 620,62 710,26 820,48 820,110" fill="#0f1f0f"/>
        <polygon points="0,110 0,80 70,50 155,84 250,32 365,74 470,28 580,68 670,40 780,62 820,52 820,110" fill="#162a16"/>
        <polygon points="0,110 0,96 50,80 120,98 200,72 305,94 410,68 520,92 620,76 720,94 820,80 820,110" fill="#1a2e1a"/>
        <circle cx="410" cy="28" r="9" fill="#f0e8c8" opacity="0.85"/>
        <circle cx="438" cy="16" r="3" fill="#f0e8c8" opacity="0.45"/>
        <circle cx="384" cy="35" r="2" fill="#f0e8c8" opacity="0.35"/>
      </svg>
      <div class="hero-content">
        <div class="eyebrow">Jackson Hole, Wyoming</div>
        <div class="hero-title">Sarah &amp; Willy's<br><em>30th Birthday Bash</em></div>
        <div class="gold-line"></div>
        <div class="hero-sub">August 6 &#8211; 10, 2025</div>
        <div class="pill-row">
          <span class="pill">Fly Fishing</span>
          <span class="pill">Grand Teton</span>
          <span class="pill">Murder Mystery</span>
          <span class="pill">The Rose</span>
          <span class="pill">Choose Your Own Adventure</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)


def render_river_band():
    st.markdown("""
    <div class="illus-band">
      <div class="illus-band-inner">
        <div class="illus-band-copy">
          <div class="illus-eyebrow">Wednesday &#8211; Thursday</div>
          <div class="illus-title"><em>South Fork River</em><br>Overnight Camp</div>
          <div class="illus-desc">Two days of guided fly fishing on one of Idaho's most celebrated stretches of water, hosted by <strong>West Bank Anglers</strong>. Expect cutthroat, browns, and a campfire cookout under a sky full of stars.</div>
          <a class="illus-link" href="https://westbankanglers.com/pages/overnight-guided-fly-fishing-trips" target="_blank">westbankanglers.com &#8599;</a>
        </div>
        <div class="illus-band-art">
    """, unsafe_allow_html=True)
    st.markdown(RIVER_SVG, unsafe_allow_html=True)
    st.markdown("</div></div></div>", unsafe_allow_html=True)


def render_mountain_band():
    st.markdown("""
    <div class="illus-band" style="border-top:0.5px solid #e0d8c8;">
      <div class="illus-band-inner" style="flex-direction:row-reverse;">
        <div class="illus-band-copy right">
          <div class="illus-eyebrow">Friday</div>
          <div class="illus-title"><em>Grand Teton</em><br>Saddle Hike</div>
          <div class="illus-desc">One of Wyoming's most iconic ascents &#8212; a long, strenuous climb to the saddle of the Grand Teton. The views are unlike anything else. Come prepared and ready to earn it.</div>
        </div>
        <div class="illus-band-art">
    """, unsafe_allow_html=True)
    st.markdown(MOUNTAIN_SVG, unsafe_allow_html=True)
    st.markdown("</div></div></div>", unsafe_allow_html=True)


def render_adventure_band():
    st.markdown("""
    <div class="adventure-band">
      <div class="adventure-header">
        <div class="adventure-eyebrow">Saturday, August 9</div>
        <div class="adventure-title">Choose Your Own Adventure</div>
        <div class="gold-line"></div>
      </div>
    """, unsafe_allow_html=True)
    st.markdown(ADVENTURE_SVG, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def render_days():
    st.markdown('<div class="body-wrap">', unsafe_allow_html=True)

    # Wednesday (content left, icon right)
    st.markdown(f"""
    <div class="day-row">
      <div class="content-left">
        <div class="day-name">Wednesday, August 6</div>
        <div class="event-row">
          <span class="event-time">2:00 pm</span>
          <span class="event-desc">Depart <strong>Meacham International Airport (KFTW)</strong> in Fort Worth. Please arrive by 1:15 pm so we can board together and get in the air on time.</span>
        </div>
        <div class="event-row">
          <span class="event-time">Afternoon</span>
          <span class="event-desc">Arrive <strong>Driggs Airport</strong> and transfer directly to our overnight camp on the <strong>South Fork River</strong> with <a href="https://westbankanglers.com/pages/overnight-guided-fly-fishing-trips" target="_blank">West Bank Anglers</a>. <strong>Please pack a separate river go bag</strong> for this leg &#8212; your main luggage will go straight to the house. Children are welcome at the lodge, and we will have nannies to watch them while we're on the water.</span>
        </div>
        <div class="event-row">
          <span class="event-time">Evening</span>
          <span class="event-desc">Fish the afternoon and evening guided by West Bank Anglers' expert team. The South Fork is renowned for wild <strong>cutthroat and brown trout</strong>. As the sun sets, we'll gather around a campfire for a proper outdoor cookout &#8212; grilled fish, bonfires, and cocktails under a sky full of stars. We will glamp at the river camp that night.</span>
        </div>
      </div>
      <div class="icon-col">
        {ICON_FISH}
        <div class="icon-label">Fly fishing</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Thursday (icon left, content right)
    st.markdown(f"""
    <div class="day-row">
      <div class="icon-col">
        {ICON_CARDS}
        <div class="icon-label">Murder mystery</div>
      </div>
      <div class="content-right">
        <div class="day-name">Thursday, August 7</div>
        <div class="event-row">
          <span class="event-time">Morning</span>
          <span class="event-desc">Rise with the river. After a camp breakfast, we're back on the water with our guides for one final morning session on the <strong>South Fork</strong>. Make the most of it &#8212; this is world-class fishing.</span>
        </div>
        <div class="event-row">
          <span class="event-time">Late PM</span>
          <span class="event-desc">Break camp and drive back to the house. Families reunite mid-afternoon for some downtime before the evening festivities.</span>
        </div>
        <div class="event-row">
          <span class="event-time">Evening</span>
          <span class="event-desc"><strong>Catered dinner at the house</strong>, followed by a full murder mystery night. We highly recommend watching <em>The Traitors</em> in advance &#8212; the perfect primer on suspicion and keeping a poker face. Come ready to accuse. Nannies are arranged so everyone can enjoy an uninterrupted evening.</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Friday (content left, icon right)
    st.markdown(f"""
    <div class="day-row">
      <div class="content-left">
        <div class="day-name">Friday, August 8</div>
        <div class="event-row">
          <span class="event-time">Morning</span>
          <span class="event-desc">We set out early for the <strong>Grand Teton saddle hike</strong> &#8212; one of Wyoming's most iconic ascents. Expect 10&#8211;12 miles round trip with significant elevation gain. <strong>Please bring proper hiking shoes, trek poles, warm layers, and plenty of water.</strong> Children are welcome &#8212; <strong>front packs and backpack carriers will be available</strong>, or nannies will be at the house all day. We'll return late afternoon.</span>
        </div>
        <div class="event-row">
          <span class="event-time">Evening</span>
          <span class="event-desc">After a quick turnaround, we head into downtown Jackson for dinner at <strong>Snake River Grill</strong>, one of Jackson's most celebrated restaurants. The evening continues with a <strong>bottle service reservation at The Rose</strong>. Wear your dancing shoes &#8212; a party bus will bring everyone safely back to the house at the end of the night.</span>
        </div>
      </div>
      <div class="icon-col">
        {ICON_CHAMPAGNE}
        <div class="icon-label">Snake River Grill &amp; The Rose</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Saturday (icon left, content right)
    st.markdown(f"""
    <div class="day-row">
      <div class="icon-col">
        {ICON_RAFT}
        <div class="icon-label">Adventure day</div>
      </div>
      <div class="content-right">
        <div class="day-name">Saturday, August 9</div>
        <div class="event-row">
          <span class="event-time">Daytime</span>
          <span class="event-desc">Time to choose your adventure. We'll split into groups &#8212; just let us know your preference and we'll handle all the logistics and bookings.<br><br>
          <strong>Option A &#8212; Whitewater rafting:</strong> hit the Snake River for a thrilling run through Class III&#8211;IV rapids with a professional outfitter.<br><br>
          <strong>Option B &#8212; Mountain biking:</strong> explore Jackson Hole's incredible trail network with rentals and a guided route.<br><br>
          <strong>Option C &#8212; House day:</strong> stay back, relax, and enjoy the property with the kids. No pressure &#8212; it's been a full few days.</span>
        </div>
        <div class="event-row">
          <span class="event-time">Evening</span>
          <span class="event-desc">A <strong>relaxed night at the house</strong> together &#8212; good company, easy food, and an early bedtime. We have a <strong>6:00 am departure</strong> Sunday morning (please be ready by 5:15 am), as the plane continues on an international trip immediately after dropping us in Dallas and we cannot miss that window.</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Sunday (content left, icon right)
    st.markdown(f"""
    <div class="day-row">
      <div class="content-left">
        <div class="day-name">Sunday, August 10</div>
        <div class="event-row">
          <span class="event-time">5:15 am</span>
          <span class="event-desc"><strong>Please be loaded and ready to leave for the airport by 5:15 am.</strong> Set two alarms &#8212; we are on a firm schedule because the aircraft is continuing on an international trip immediately after dropping us in Dallas, and we cannot delay departure.</span>
        </div>
        <div class="event-row">
          <span class="event-time">6:00 am</span>
          <span class="event-desc"><strong>Wheels up from Jackson Hole.</strong> The early start is the price of paradise.</span>
        </div>
        <div class="event-row">
          <span class="event-time">~9:00 am</span>
          <span class="event-desc">Touch down in <strong>Dallas</strong> and back to real life &#8212; but what a weekend it will have been. <strong>Happy 30th, Sarah &amp; Willy.</strong></span>
        </div>
      </div>
      <div class="icon-col">
        {ICON_PLANE}
        <div class="icon-label">Homeward bound</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def render_childcare_note():
    st.markdown("""
    <div class="childcare-note">
      <p>We will provide child care on all days and across all activities &#8212; you are welcome to bring your children if you so choose.</p>
    </div>
    """, unsafe_allow_html=True)


def render_rsvp():
    st.markdown(PINE_DIVIDER_SVG, unsafe_allow_html=True)
    st.markdown('<div class="body-wrap">', unsafe_allow_html=True)
    st.markdown("""
    <div class="rsvp-eyebrow">Kindly respond by July 15, 2025</div>
    <div class="rsvp-title">Please let us know you're coming</div>
    <div class="gold-line" style="margin:0 0 1.5rem;"></div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your full name")
        email = st.text_input("Email address")
        children_coming = st.selectbox(
            "Are you bringing children?",
            ["— please select —", "No children", "Yes — see details below"],
        )
    with col2:
        adults = st.text_area(
            "All adults in your party (full names)",
            height=100,
            placeholder="e.g. John Smith, Jane Smith",
        )
        activity = st.selectbox(
            "Saturday activity",
            [
                "— please select —",
                "Whitewater rafting on the Snake River",
                "Mountain biking",
                "Relaxing at the house",
            ],
        )

    children_names = st.text_input(
        "Children's names and ages (if applicable)",
        placeholder="e.g. Emma Smith, age 4 · Jack Smith, age 7",
    )
    dietary = st.text_area(
        "Dietary restrictions or allergies (list for each person in your party)",
        height=80,
        placeholder="e.g. John — gluten free · Jane — no shellfish · None",
    )
    notes = st.text_area(
        "Anything else we should know?",
        height=80,
        placeholder="Notes, questions, special needs...",
    )

    if st.button("Send RSVP"):
        if (
            name
            and activity != "— please select —"
            and children_coming != "— please select —"
        ):
            st.success(
                f"Thank you, {name}! We've received your RSVP and can't wait to "
                f"celebrate with you in Jackson Hole. 🥂"
            )
        else:
            st.warning(
                "Please fill in your name, Saturday activity, and whether you're "
                "bringing children."
            )

    st.markdown("</div>", unsafe_allow_html=True)


def render_footer():
    st.markdown("""
    <div class="footer-block">
      <div class="gold-line"></div>
      <p style="margin-top:1rem;">Questions? Reach out to Sarah or Willy directly.</p>
      <p class="footer-sig">With love &amp; anticipation &#8212; Sarah &amp; Willy</p>
    </div>
    """, unsafe_allow_html=True)


def main():
    st.markdown(CSS, unsafe_allow_html=True)
    render_hero()
    render_river_band()
    render_mountain_band()
    render_adventure_band()
    render_days()
    render_childcare_note()
    render_rsvp()
    render_footer()


if __name__ == "__main__":
    main()
