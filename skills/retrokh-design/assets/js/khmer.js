// Khmer digits for display. Keep data in ASCII; convert only when rendering.
const KM = '០១២៣៤៥៦៧៨៩';

export const toKhmerDigits = (value) => String(value).replace(/[0-9]/g, (d) => KM[d]);

// "133 / 138" -> "១៣៣ / ១៣៨"
export const kmCount = (current, total) => `${toKhmerDigits(current)} / ${toKhmerDigits(total)}`;
