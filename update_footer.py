import re

# Update index.html
with open("index.html", "r") as f:
    html = f.read()

new_footer = """
    <footer class="site-footer">
        <div class="footer-top">
            <div class="footer-col col-about">
                <p>RiYad is independent creative<br>director and solopreneur</p>
            </div>
            <div class="footer-col col-explore">
                <h4>Explore</h4>
                <a href="#">Bio</a>
                <a href="#">Newsletter</a>
                <a href="#">Contact</a>
            </div>
            <div class="footer-col col-social">
                <h4>Follow me</h4>
                <div class="social-grid">
                    <a href="#">X @riyadhasan</a>
                    <a href="#">IG @riyadhasan</a>
                    <a href="#">DB @riyadhasan</a>
                    <a href="#">YT @riyadhasan</a>
                    <a href="#">FB @riyadhasan</a>
                </div>
            </div>
            <div class="footer-col col-cta">
                <a href="#" class="cta-block">
                    <div class="cta-header">
                        <span class="cta-title" style="color: #ff4500;">Call RiYad</span>
                        <span class="cta-icon" style="background: #ff4500; color: #fff;">&#8599;</span>
                    </div>
                    <span class="cta-sub">Let's work together</span>
                </a>
                <div class="cta-divider"></div>
                <a href="#" class="cta-block">
                    <div class="cta-header">
                        <span class="cta-title">Courses & Tools</span>
                        <span class="cta-icon">&#8599;</span>
                    </div>
                    <span class="cta-sub">Creative tools</span>
                </a>
            </div>
        </div>

        <div class="footer-middle">
            <h1 class="huge-text">RiYad</h1>
        </div>

        <div class="footer-bottom">
            <div class="fb-left">
                <span>&copy; RiYad 2025</span>
                <a href="#">Privacy Policy</a>
            </div>
            <div class="fb-right">
                <span>Cairo</span>
                <span>12:34 PM</span>
                <span>31&deg;C &#9729;</span>
            </div>
        </div>
    </footer>
"""

html = html.replace('    <script src="frames.js"></script>', new_footer + '\n    <script src="frames.js"></script>')

with open("index.html", "w") as f:
    f.write(html)

# Update styles.css
css_append = """
/* Footer Section */
.site-footer {
    position: relative;
    z-index: 1;
    padding: 6rem 5% 2rem;
    mix-blend-mode: difference;
    color: #fff;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    min-height: 100vh;
}

.footer-top {
    display: grid;
    grid-template-columns: 2fr 1fr 2fr 2fr;
    gap: 2rem;
    margin-bottom: 4rem;
}

.footer-col h4 {
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
}

.footer-col a {
    color: #ccc;
    text-decoration: none;
    display: block;
    margin-bottom: 0.8rem;
    font-size: 0.9rem;
    transition: color 0.3s;
}

.footer-col a:hover {
    color: #fff;
}

.col-about p {
    font-size: 1.5rem;
    font-weight: 500;
    line-height: 1.3;
    max-width: 300px;
}

.social-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.5rem;
}

.cta-block {
    display: flex;
    flex-direction: column;
    text-decoration: none !important;
}

.cta-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 0.5rem;
}

.cta-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #fff;
}

.cta-icon {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: #fff;
    color: #000;
    font-size: 12px;
}

.cta-sub {
    font-size: 0.9rem;
    color: #ccc;
}

.cta-divider {
    height: 1px;
    background: rgba(255,255,255,0.2);
    margin: 1.5rem 0;
}

.footer-middle {
    flex-grow: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    margin: 4rem 0;
}

.huge-text {
    font-size: 28vw;
    font-weight: 800;
    line-height: 0.75;
    letter-spacing: -0.05em;
    margin: 0;
}

.footer-bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 0.8rem;
    color: #aaa;
    border-top: 1px solid rgba(255,255,255,0.2);
    padding-top: 2rem;
}

.fb-left, .fb-right {
    display: flex;
    gap: 2rem;
}

.fb-left a {
    color: #aaa;
    text-decoration: none;
}
.fb-left a:hover {
    color: #fff;
}
"""

with open("styles.css", "a") as f:
    f.write(css_append)

print("Added footer section successfully.")
