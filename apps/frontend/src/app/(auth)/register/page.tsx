import Link from "next/link";

export default function Register() {
  return (
    <main className="flex min-h-screen items-center justify-center p-4">
      <form className="w-full max-w-sm space-y-4">
        <h1 className="text-center text-2xl font-semibold">Register</h1>
        <input
          type="text"
          placeholder="Name"
          className="w-full rounded border p-2"
        />
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
          className="w-full rounded bg-green-600 p-2 text-white"
        >
          Create account
        </button>
        <p className="text-center text-sm">
          <Link href="/login" className="underline">
            Already have an account?
          </Link>
        </p>
      </form>
    </main>
  );
}

