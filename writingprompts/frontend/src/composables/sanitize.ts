// Function to remove whitespace, commas and periods from string.
export function sanitizeString(value: string): string {
  return value.replace(/[\s,.]/g, '')
}
