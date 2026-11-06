<script setup>
// links: [{ label, href, current? }]. Add document.documentElement.classList.add('js') once (main.js) so phones collapse the menu.
import { ref } from 'vue';

defineProps({
  brand: { type: String, required: true },
  links: { type: Array, required: true },
  menuLabel: { type: String, default: 'ម៉ឺនុយ' },
});
const open = ref(false);
</script>

<template>
  <header class="rk-nav" :data-open="open || undefined">
    <div class="rk-container rk-nav-inner">
      <a class="rk-nav-brand" href="/"><span class="rk-display">{{ brand }}</span></a>
      <button class="rk-btn rk-btn-ghost rk-btn-icon rk-nav-toggle" :aria-label="menuLabel" :aria-expanded="open"
        aria-controls="rk-links" @click="open = !open">
        <svg class="rk-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16" /></svg>
      </button>
      <nav style="display:contents">
        <ul id="rk-links" class="rk-nav-links">
          <li v-for="l in links" :key="l.href">
            <a :href="l.href" :aria-current="l.current ? 'page' : undefined" @click="open = false">{{ l.label }}</a>
          </li>
        </ul>
      </nav>
    </div>
  </header>
  <div class="rk-zigzag" aria-hidden="true"></div>
</template>
