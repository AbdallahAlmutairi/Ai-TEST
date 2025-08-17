import Link from "next/link";

export default function Login() {
  return (
    <main className="flex min-h-screen items-center justify-center p-4">
      <form className="w-full max-w-sm space-y-4">
        <h1 className="text-center text-2xl font-semibold">Login</h1>
        <input
          type="email"
          placeholder="Email"
          className="w-full rounded border p-2"
        />
        <input
          type="password"
          placeholder="Password"
          className="w-full rounded border p-2"
        />
        <button
          type="submit"
          className="w-full rounded bg-blue-600 p-2 text-white"
        >
          Sign in
        </button>
        <p className="text-center text-sm">
          <Link href="/register" className="underline">
            Create account
          </Link>
        </p>
      </form>
    </main>
  );
}

