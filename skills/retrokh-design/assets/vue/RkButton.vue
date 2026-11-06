<script setup>
// variant: primary | system | accent | raised | ghost | paper. iconOnly needs `label` (becomes aria-label).
defineProps({
  variant: { type: String, default: 'ghost' },
  iconOnly: Boolean,
  label: String,
  href: String,
});
</script>

<template>
  <component :is="href ? 'a' : 'button'" :href="href" :aria-label="iconOnly ? label : undefined"
    :class="['rk-btn', `rk-btn-${variant}`, { 'rk-btn-icon': iconOnly }]">
    <slot name="icon" /><slot v-if="!iconOnly" />
  </component>
</template>
