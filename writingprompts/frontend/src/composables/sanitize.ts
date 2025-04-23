export function sanitizeString(value: string): string {
  return value.replace(/[\s,]/g, '')
}
