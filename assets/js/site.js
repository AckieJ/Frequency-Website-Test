/* The Frequency: small helpers. The site still works if this file fails to load. */
(function () {
  'use strict';

  /* Accessible mobile navigation; closes after selecting a link. */
  var navToggle = document.querySelector('.nav-toggle');
  var primaryNav = document.getElementById('primary-navigation');
  if (navToggle && primaryNav) {
    function setNav(open) {
      navToggle.setAttribute('aria-expanded', String(open));
      navToggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
      primaryNav.classList.toggle('nav--open', open);
    }
    navToggle.addEventListener('click', function () {
      setNav(navToggle.getAttribute('aria-expanded') !== 'true');
    });
    primaryNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () { setNav(false); });
    });
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape') setNav(false);
    });
  }

  /* 1. Click a video thumbnail to play it right on the page.
        Without JavaScript the thumbnail is simply a link to YouTube. */
  document.querySelectorAll('a[data-video-id]').forEach(function (link) {
    link.addEventListener('click', function (event) {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.button === 1) return;
      event.preventDefault();

      var iframe = document.createElement('iframe');
      iframe.src = 'https://www.youtube-nocookie.com/embed/' +
        encodeURIComponent(link.getAttribute('data-video-id')) + '?autoplay=1&rel=0';
      iframe.title = link.getAttribute('data-title') || 'Performance video';
      iframe.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
      iframe.setAttribute('allowfullscreen', '');

      var box = document.createElement('div');
      box.className = 'video__thumb';
      box.appendChild(iframe);
      link.replaceWith(box);
      iframe.focus();
    });
  });

  /* 2. Move shows whose date has passed into a "Past shows" list.
        The page only rebuilds when someone edits it, so this keeps it current. */
  var upcoming = document.getElementById('shows-upcoming');
  if (upcoming) {
    var pastList = document.getElementById('shows-past');
    var pastWrap = document.getElementById('shows-past-wrap');
    var emptyNote = document.getElementById('shows-empty');

    var today = new Date();
    today.setHours(0, 0, 0, 0);

    var pastItems = [];
    Array.prototype.slice.call(upcoming.children).forEach(function (item) {
      var parts = (item.getAttribute('data-date') || '').split('-');
      if (parts.length !== 3) return;
      var when = new Date(Number(parts[0]), Number(parts[1]) - 1, Number(parts[2]));
      if (!isNaN(when.getTime()) && when < today) pastItems.push(item);
    });

    /* Newest past show first. */
    pastItems.reverse().forEach(function (item) { pastList.appendChild(item); });

    if (pastItems.length) pastWrap.hidden = false;
    if (!upcoming.children.length) {
      upcoming.hidden = true;
      emptyNote.hidden = false;
    }
  }
})();
