const frameCount = FRAMES.length;
  const canvas = document.getElementById('frameCanvas');
  const ctx = canvas.getContext('2d');
  const stage = document.querySelector('.scroll-stage');

  const images = new Array(frameCount);

  function preloadImages() {
    for (let i = 0; i < frameCount; i++) {
      const img = new Image();
      img.src = FRAMES[i];
      img.onload = () => { if (i === 0) drawFrame(0); };
      images[i] = img;
    }
  }

  function resizeCanvas() {
    canvas.width = window.innerWidth * window.devicePixelRatio;
    canvas.height = window.innerHeight * window.devicePixelRatio;
    drawFrame(targetProgress);
  }

  // Draws with sub-frame interpolation: crossfades between the two
  // nearest frames so the motion doesn't feel like it's stepping.
  function drawFrame(progress) {
    const exact = progress * (frameCount - 1);
    const i0 = Math.floor(exact);
    const i1 = Math.min(frameCount - 1, i0 + 1);
    const t = exact - i0;

    const img0 = images[i0];
    const img1 = images[i1];
    if (!img0 || !img0.complete || img0.naturalWidth === 0) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawCover(img0, 1);
    if (t > 0.02 && img1 && img1.complete && img1.naturalWidth > 0) {
      drawCover(img1, t);
    }
  }

  function drawCover(img, alpha) {
    const canvasRatio = canvas.width / canvas.height;
    const imgRatio = img.naturalWidth / img.naturalHeight;

    let drawWidth, drawHeight, offsetX, offsetY;
    if (imgRatio > canvasRatio) {
      drawHeight = canvas.height;
      drawWidth = drawHeight * imgRatio;
      offsetX = (canvas.width - drawWidth) / 2;
      offsetY = 0;
    } else {
      drawWidth = canvas.width;
      drawHeight = drawWidth / imgRatio;
      offsetX = 0;
      offsetY = (canvas.height - drawHeight) / 2;
    }

    ctx.globalAlpha = alpha;
    ctx.drawImage(img, offsetX, offsetY, drawWidth, drawHeight);
    ctx.globalAlpha = 1;
  }

  let targetProgress = 0;
  let currentProgress = 0;

  function getScrollProgress() {
    const scrollTop = window.scrollY || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
    if (scrollHeight <= 0) return 0;
    return Math.min(Math.max(scrollTop / scrollHeight, 0), 1);
  }

  // Smoothly eases currentProgress toward targetProgress every frame
  // instead of snapping straight to the scroll position.
  function animate() {
    currentProgress += (targetProgress - currentProgress) * 0.15;
    if (Math.abs(targetProgress - currentProgress) < 0.0005) {
      currentProgress = targetProgress;
    }
    drawFrame(currentProgress);
    requestAnimationFrame(animate);
  }

  window.addEventListener('scroll', () => {
    targetProgress = getScrollProgress();
  }, { passive: true });

  window.addEventListener('resize', resizeCanvas);
  window.addEventListener('load', () => {
    resizeCanvas();
    preloadImages();
    targetProgress = getScrollProgress();
    currentProgress = targetProgress;
    animate();
  });

  // Footer: live Bangladesh time + current year
  function updateFooterClock() {
    const yearEl = document.getElementById('currentYear');
    if (yearEl) yearEl.textContent = new Date().getFullYear();

    const timeEl = document.getElementById('bdTime');
    if (timeEl) {
      timeEl.textContent = new Date().toLocaleTimeString('en-US', {
        timeZone: 'Asia/Dhaka',
        hour: 'numeric',
        minute: '2-digit',
        hour12: true
      });
    }
  }

  updateFooterClock();
  setInterval(updateFooterClock, 1000 * 30);