export function connect(path: string): WebSocket {
  return new WebSocket(path);
}
