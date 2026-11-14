/* Back-to-home button that matches the RTD sidebar colors */
(function () {
  // Run after DOM is ready
  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  ready(function () {
    var side = document.querySelector('.wy-nav-side');
    if (!side) return;

    // Sphinx supplies the path to this solver's docs root, even on nested pages.
    // The HPR homepage is one level above it, on the current host and protocol.
    var docsRoot = new URL(
      document.documentElement.getAttribute('data-content_root') || './',
      window.location.href
    );
    var target = new URL('../', docsRoot).href;

    // -------- create button --------
    var btn = document.createElement('a');
    btn.className = 'hpr-back-fab';
    btn.appendChild(document.createTextNode('Back to HPR homepage'));
    btn.setAttribute('href', target);

    // -------- inject CSS (no template strings) --------
    var style = document.createElement('style');
    style.type = 'text/css';
    style.appendChild(document.createTextNode(
      '.hpr-back-fab{position:fixed;bottom:0;left:0;width:260px;padding:12px 16px;text-align:center;text-decoration:none;font-weight:600;border:0;border-top:1px solid rgba(255,255,255,.08);box-shadow:none;z-index:2000;transition:filter .15s ease;}' +
      '.hpr-back-fab:hover{filter:brightness(1.06);text-decoration:none;}' +
      '@media (max-width:768px){.hpr-back-fab{display:none;}}'
    ));
    document.head.appendChild(style);

    // -------- match sidebar colors --------
    var cs = window.getComputedStyle(side);
    btn.style.backgroundColor = cs.backgroundColor;
    btn.style.color = cs.color || '#fff';

    document.body.appendChild(btn);

    // -------- keep aligned with sidebar --------
    function syncPos() {
      var r = side.getBoundingClientRect();
      btn.style.left = r.left + 'px';
      btn.style.width = r.width + 'px';
    }
    syncPos();
    window.addEventListener('resize', syncPos);
    window.addEventListener('scroll', syncPos);
  });
})();
