import re

with open("index.html", "r") as f:
    html = f.read()

# 1. Navbar
html = html.replace('<div class="logo">Folioblox</div>', '<div class="logo">Riyad</div>')
html = re.sub(
    r'<nav class="nav-links">.*?</nav>',
    '''<nav class="nav-links">
            <a href="#">Home</a>
            <a href="#">Projects</a>
            <a href="#">Writeups</a>
            <a href="#">Hall of Fame</a>
        </nav>''',
    html,
    flags=re.DOTALL
)
html = html.replace('<button class="btn-primary">Get in touch &rarr;</button>', '<button class="btn-primary">Contact &rarr;</button>')

# 2. Hero Section
html = html.replace('<p class="subtitle">Hey, I\'m a</p>', '<p class="subtitle">Security Researcher</p>')
html = html.replace('<h1 class="title">Creative<br>Director</h1>', '<h1 class="title" style="font-size: 4.5rem;">Bug Bounty<br>Hunter</h1>')
html = html.replace('<h2>Great design should<br>feel invisible.</h2>', '<h2>Learning.<br>Building.<br>Breaking.<br>Securing.</h2>')
html = html.replace('<p>From logo to language, I build brands that<br>connect and convert.</p>', '<p>I identify web application vulnerabilities, build offensive security tools, and continuously improve my skills through real-world testing and research.</p>')

# Hero Bottom
html = html.replace('<span class="name">Brand Strategy</span>', '<span class="name">Web App Security</span>')
html = html.replace('<span class="name">Brand Identity Design</span>', '<span class="name">Bug Bounty Hunting</span>')
html = html.replace('<span class="name">Packaging Design</span>', '<span class="name">Reconnaissance</span>')
html = html.replace('<span class="name">Creative Direction</span>', '<span class="name">Automation Setup</span>')

# 3. Brands -> Skills
html = html.replace('<p>Trusted by Brands I\'ve<br>Helped Shape</p>', '<p>Core Skills &<br>Technologies</p>')
html = html.replace('<div class="brand"><span class="icon circle"></span> Supa Blox</div>', '<div class="brand"><span class="icon circle"></span> Python</div>')
html = html.replace('<div class="brand"><span class="icon hourglass"></span> Hype Blox</div>', '<div class="brand"><span class="icon hourglass"></span> Burp Suite</div>')
html = html.replace('<div class="brand"><span class="icon half-circle"></span> Frame Blox</div>', '<div class="brand"><span class="icon half-circle"></span> Linux</div>')
html = html.replace('<div class="brand"><span class="icon dots"></span> Ultra Blox</div>', '<div class="brand"><span class="icon dots"></span> OWASP</div>')

# 4. Behind Designs -> Featured Project
html = html.replace('<p class="section-subtitle">Behind the Designs</p>', '<p class="section-subtitle">Featured Project</p>')
html = html.replace('<h2 class="section-title">Shaping<br>Experiences That<br>Make Life Simpler</h2>', '<h2 class="section-title">RH2<br>Enum<br>Framework</h2>')
html = html.replace('<p class="description">I\'m a product designer focused on<br>building clean, intuitive interfaces<br>that solve real-world problems.</p>', '<p class="description">Advanced authentication enumeration framework built with Python.<br>Features intelligent response comparison, precision diffing,<br>and enumeration automation.</p>')
html = html.replace('<p class="small-text">Let\'s Build Something<br>Meaningful Together</p>', '<p class="small-text">Open-source security<br>tools & research</p>')
html = re.sub(
    r'<div class="action-area">\s*<p class="small-text">Open-source security<br>tools & research</p>\s*<button class="btn-primary">Contact &rarr;</button>\s*</div>',
    '''<div class="action-area">
                    <p class="small-text">Open-source security<br>tools & research</p>
                    <button class="btn-primary">View on GitHub &rarr;</button>
                </div>''',
    html,
    flags=re.DOTALL
)

# 5. Footer Update
html = html.replace('<p>RiYad is independent creative<br>director and solopreneur</p>', '<p>Riyad is a Bug Bounty Hunter & Security Researcher.</p>')
html = re.sub(
    r'<div class="footer-col col-explore">.*?</div>',
    '''<div class="footer-col col-explore">
                <h4>Explore</h4>
                <a href="#">About</a>
                <a href="#">Projects</a>
                <a href="#">Writeups</a>
                <a href="#">Hall of Fame</a>
            </div>''',
    html,
    flags=re.DOTALL
)
html = re.sub(
    r'<div class="social-grid">.*?</div>',
    '''<div class="social-grid">
                    <a href="#">IG @rzz_arthur</a>
                    <a href="#">X @isnt_arthur</a>
                    <a href="#">GH RH2-1</a>
                    <a href="#">reyadhasan100az@gmail.com</a>
                </div>''',
    html,
    flags=re.DOTALL
)
html = html.replace('<span class="cta-title" style="color: #ff4500;">Call RiYad</span>', '<span class="cta-title" style="color: #ff4500;">Work With Riyad</span>')
html = html.replace('<span class="cta-sub">Let\'s work together</span>', '<span class="cta-sub">Security Research & Pentesting</span>')
html = html.replace('<span class="cta-title">Courses & Tools</span>', '<span class="cta-title">Future Projects</span>')
html = html.replace('<span class="cta-sub">Creative tools</span>', '<span class="cta-sub">RH2 Recon, Scanner, Fuzzer</span>')

html = html.replace('<span>&copy; RiYad 2025</span>', '<span>&copy; 2026 Riyad</span>')
html = html.replace('<span>Cairo</span>', '<span>Bangladesh</span>')
html = html.replace('<span>31&deg;C &#9729;</span>', '<span>Bug Hunting</span>')

with open("index.html", "w") as f:
    f.write(html)
