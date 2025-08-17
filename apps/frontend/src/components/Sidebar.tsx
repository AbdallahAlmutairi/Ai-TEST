import Link from "next/link";

/** Simple vertical navigation sidebar. */
export default function Sidebar() {
  return (
    <aside className="min-h-screen w-48 border-r p-4">
      <nav className="flex flex-col space-y-2 text-sm">
        <Link href="/dashboard">Dashboard</Link>
        <Link href="/alerts">Alerts</Link>
        <Link href="/chat">Chat</Link>
        <Link href="/learn">Learn</Link>
        <Link href="/admin">Admin</Link>
      </nav>
    </aside>
  );
}

