/* Sizes .rs-title to its box. render.py inlines this file.
   data-fit="block" gives every line one size; data-fit="fill" lets each line fill the width. */
(function () {
  /* In stacked shapes the artwork keeps this share of the stage, so a long title cannot crush it. */
  var artShare = { square: .38, portrait: .38 };

  function fit() {
    var title = document.querySelector('.rs-title');
    if (!title) { return; }

    var shape = document.documentElement.dataset.shape || 'landscape';
    var stage = document.querySelector('.rs-stage');
    var head = title.parentElement;
    var foot = document.querySelector('.rs-foot');
    var boxStyle = getComputedStyle(head);
    var width = head.clientWidth - parseFloat(boxStyle.paddingLeft) - parseFloat(boxStyle.paddingRight);
    var gap = parseFloat(boxStyle.rowGap) || 0;
    var stageGap = parseFloat(getComputedStyle(stage).rowGap) || 0;
    var used = parseFloat(boxStyle.paddingTop) + parseFloat(boxStyle.paddingBottom)
      + parseFloat(boxStyle.borderTopWidth) + parseFloat(boxStyle.borderBottomWidth)
      + (foot ? foot.getBoundingClientRect().height + stageGap : 0);

    Array.prototype.forEach.call(head.children, function (child) {
      if (child !== title) { used += child.getBoundingClientRect().height + gap; }
    });

    var maxHeight = stage.clientHeight * (1 - (artShare[shape] || 0)) - used - (artShare[shape] ? stageGap : 0);
    var lines = Array.prototype.slice.call(title.children);

    var sizes = lines.map(function (line) {
      line.style.fontSize = '100px';
      return 100 * width * .985 / line.getBoundingClientRect().width;
    });

    if (title.dataset.fit !== 'fill') {
      var smallest = Math.min.apply(null, sizes);
      sizes = sizes.map(function () { return smallest; });
    } else {
      /* Short lines stop at 1.6x so one huge word cannot starve the others of height. */
      var cap = Math.min.apply(null, sizes) * 1.6;
      sizes = sizes.map(function (size) { return Math.min(size, cap); });
    }

    var height = sizes.reduce(function (sum, size, index) {
      return sum + size * parseFloat(getComputedStyle(lines[index]).lineHeight) / 100;
    }, 0);
    var scale = Math.min(1, maxHeight / height);

    lines.forEach(function (line, index) { line.style.fontSize = (sizes[index] * scale) + 'px'; });

    Array.prototype.forEach.call(document.querySelectorAll('.rs-kicker,.rs-sub,.rs-meta'), function (el) {
      var box = getComputedStyle(el.parentElement);
      var room = el.parentElement.clientWidth - parseFloat(box.paddingLeft) - parseFloat(box.paddingRight);
      var size = parseFloat(getComputedStyle(el).fontSize);
      var longest = el.textContent.trim().split(/\s+/).reduce(function (a, b) { return a.length > b.length ? a : b; }, '');
      var probe = document.createElement('span');

      probe.textContent = el.scrollWidth > room ? longest : '';
      el.appendChild(probe);
      probe.style.cssText = 'position:absolute;visibility:hidden;white-space:nowrap';
      var needed = probe.getBoundingClientRect().width;
      el.removeChild(probe);

      if (needed > room) { el.style.fontSize = (size * room / needed * .98) + 'px'; }
    });

    var art = document.querySelector('.rs-art');

    if (art) {
      var rect = art.getBoundingClientRect();
      var root = document.documentElement.style;

      root.setProperty('--focus-x', (rect.left + rect.width / 2) + 'px');
      root.setProperty('--focus-y', (rect.top + rect.height / 2) + 'px');
      root.setProperty('--art-size', Math.min(rect.width, rect.height) + 'px');
      root.setProperty('--tear-y', Math.max(head.getBoundingClientRect().bottom, head.lastElementChild.getBoundingClientRect().bottom) + 'px');
    }

    document.documentElement.dataset.fitted = '1';
  }

  document.fonts.ready.then(fit);
})();
