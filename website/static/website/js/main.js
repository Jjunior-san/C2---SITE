(function () {
  var btn = document.querySelector('.menu-toggle');
  var nav = document.getElementById('navLinks');

  if (btn && nav) {
    btn.addEventListener('click', function () {
      nav.classList.toggle('open');
    });
  }

  if (nav) {
    nav.addEventListener('click', function (e) {
      if (window.innerWidth <= 768 && e.target && e.target.tagName === 'A') {
        nav.classList.remove('open');
      }
    });
  }
})();

(function () {
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return;
  }

  function hideAnimatedElement(el) {
    if (!el) return;
    el.setAttribute('data-original-text', el.innerHTML);
    var height = window.getComputedStyle(el).height;
    if (height && height !== 'auto') {
      el.style.minHeight = height;
    }
    el.style.visibility = 'hidden';
  }

  function runTypewriterOnce(el) {
    if (!el || el.getAttribute('data-typed') === '1') return;

    var target = el.textContent || el.innerText;
    var isHeaderLogo = el.id === 'headerLogoText';
    var speed = isHeaderLogo ? 45 : 30;
    var pretypeBlinks = isHeaderLogo ? 3 : 0;
    var blinkInterval = 400;

    var originalHTML = el.getAttribute('data-original-text') || target;
    var originalMinHeight = el.style.minHeight;

    el.innerHTML = '';
    el.style.visibility = 'visible';

    var index = 0;
    var cursor = false;
    var blinkCount = 0;

    function renderTypingState() {
      var currentText = target.substring(0, index);
      var cursorChar = cursor ? '|' : '&nbsp;';
      el.innerHTML = currentText + cursorChar;
    }

    function finishTyping() {
      el.innerHTML = originalHTML;
      
      var logoTaglineEl = document.getElementById('headerLogoTagline');
      var logoExponentEl = document.getElementById('headerLogoExponent');

      if (isHeaderLogo && logoTaglineEl) {
        logoTaglineEl.style.transition = 'opacity 1s ease';
        logoTaglineEl.style.visibility = 'visible';
        logoTaglineEl.style.opacity = '1';
      }

      if (isHeaderLogo && logoExponentEl) {
        logoExponentEl.setAttribute('opacity', '1');
      }

      el.style.minHeight = originalMinHeight;
      el.setAttribute('data-typed', '1');
    }

    function typeStep() {
      if (index < target.length) {
        index += 1;
        renderTypingState();
        setTimeout(typeStep, speed);
        return;
      }
      finishTyping();
    }

    if (pretypeBlinks === 0) {
      cursor = true;
      typeStep();
      return;
    }

    var blinkTimer = setInterval(function () {
      cursor = !cursor;
      renderTypingState();
      blinkCount += 1;

      if (blinkCount >= pretypeBlinks * 2) {
        clearInterval(blinkTimer);
        cursor = true;
        renderTypingState();
        typeStep();
      }
    }, blinkInterval);
  }

  var selectors = [
    '#headerLogoText',
    '.hero h1',
    '.hero p',
    '.section-header h2',
    '.service-card h3',
    '.post-title'
  ];

  var targets = document.querySelectorAll(selectors.join(','));
  if (!targets.length) {
    return;
  }

  targets.forEach(hideAnimatedElement);

  var tagline = document.getElementById('headerLogoTagline');
  if (tagline) hideAnimatedElement(tagline);

  if (!('IntersectionObserver' in window)) {
    targets.forEach(runTypewriterOnce);
    return;
  }

  var observer = new IntersectionObserver(function (entries, obs) {
    entries.forEach(function (entry) {
      if (!entry.isIntersecting) {
        return;
      }

      runTypewriterOnce(entry.target);
      obs.unobserve(entry.target);
    });
  }, {
    threshold: 0.35,
    rootMargin: '0px 0px -8% 0px'
  });

  targets.forEach(function (el) {
    observer.observe(el);
  });
})();
