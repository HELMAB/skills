<script setup>
import { useId } from 'vue'; // Vue 3.5+; on older 3.x pass a unique `id` prop instead

const props = defineProps({
  title: { type: String, required: true },
  eyebrow: String, // e.g. "០១ · សេវាកម្ម"
  tone: { type: String, default: 'ground' }, // ground | paper | ink | halftone
  center: Boolean,
  id: String,
});
const headingId = props.id ? `${props.id}-title` : useId();
</script>

<template>
  <section :id="id" :aria-labelledby="headingId"
    :class="['rk-section', { 'rk-section-paper': tone === 'paper', 'rk-section-ink': tone === 'ink', 'rk-halftone': tone === 'halftone' }]">
    <div class="rk-container">
      <div :class="['rk-section-head', { 'is-center': center }]">
        <span v-if="eyebrow" class="rk-eyebrow">{{ eyebrow }}</span>
        <h2 :id="headingId" class="rk-section-title">{{ title }}</h2>
      </div>
      <slot />
    </div>
  </section>
</template>
