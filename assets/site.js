(function () {
  var base = window.SITE_BASE || "";
  var index = window.SEARCH_INDEX || [];
  var input = document.getElementById("search-input");
  var results = document.getElementById("search-results");
  var sidebar = document.getElementById("sidebar");
  var menuBtn = document.getElementById("menu-btn");
  var active = -1;

  menuBtn.addEventListener("click", function () {
    var open = sidebar.classList.toggle("open");
    menuBtn.setAttribute("aria-expanded", open);
  });

  var current = sidebar.querySelector("a.current");
  if (current && current.scrollIntoView) current.scrollIntoView({ block: "center" });

  function esc(s) {
    return s.replace(/[&<>"]/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c];
    });
  }

  function highlight(text, terms) {
    var out = esc(text);
    terms.forEach(function (t) {
      out = out.replace(new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig"), "<mark>$1</mark>");
    });
    return out;
  }

  function search(query) {
    var terms = query.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) return [];
    var hits = [];
    index.forEach(function (page) {
      var title = page.t.toLowerCase();
      var body = page.c.toLowerCase();
      var score = 0;
      for (var i = 0; i < terms.length; i++) {
        var inTitle = title.indexOf(terms[i]) !== -1;
        var pos = body.indexOf(terms[i]);
        if (!inTitle && pos === -1) return;
        score += inTitle ? 10 : 1;
      }
      var at = body.indexOf(terms[0]);
      var start = Math.max(0, at - 50);
      var snippet = at === -1 ? "" : (start ? "…" : "") + page.c.substr(start, 140) + "…";
      hits.push({ page: page, score: score, snippet: snippet });
    });
    hits.sort(function (a, b) { return b.score - a.score; });
    return hits.slice(0, 12).map(function (h) { h.terms = terms; return h; });
  }

  function show(hits, query) {
    active = -1;
    if (!query.trim()) { results.hidden = true; results.innerHTML = ""; return; }
    results.innerHTML = hits.length
      ? hits.map(function (h) {
          return '<li><a href="' + base + h.page.u + '">' +
            '<div class="r-title">' + highlight(h.page.t, h.terms) + "</div>" +
            (h.page.s ? '<div class="r-section">' + esc(h.page.s) + "</div>" : "") +
            '<div class="r-snippet">' + highlight(h.snippet, h.terms) + "</div></a></li>";
        }).join("")
      : '<li class="empty">No pages match that search.</li>';
    results.hidden = false;
  }

  input.addEventListener("input", function () { show(search(input.value), input.value); });
  input.addEventListener("focus", function () { if (input.value.trim()) show(search(input.value), input.value); });
  input.addEventListener("keydown", function (e) {
    var links = results.querySelectorAll("a");
    if (e.key === "Escape") { results.hidden = true; input.blur(); return; }
    if (!links.length) return;
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {
      e.preventDefault();
      active = (active + (e.key === "ArrowDown" ? 1 : -1) + links.length) % links.length;
      links.forEach(function (a, i) { a.classList.toggle("active", i === active); });
      links[active].scrollIntoView({ block: "nearest" });
    } else if (e.key === "Enter") {
      e.preventDefault();
      links[active === -1 ? 0 : active].click();
    }
  });
  document.addEventListener("click", function (e) {
    if (!e.target.closest(".search")) results.hidden = true;
    if (!e.target.closest(".sidebar") && !e.target.closest(".menu-btn")) {
      sidebar.classList.remove("open");
      menuBtn.setAttribute("aria-expanded", "false");
    }
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "/" && document.activeElement !== input) { e.preventDefault(); input.focus(); }
  });
})();
