export async function api(path: string, options?: RequestInit) {
  const base = process.env.NEXT_PUBLIC_API_BASE || '';
  const res = await fetch(base + path, options);
  return res.json();
}
