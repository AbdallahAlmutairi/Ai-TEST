"use client";

import { useState } from "react";

interface Props {
  onSelect?: (symbol: string) => void;
}

/** Simple symbol search box. */
export default function SymbolSearch({ onSelect }: Props) {
  const [query, setQuery] = useState("");
  return (
    <form
      onSubmit={(e) => {
        e.preventDefault();
        onSelect?.(query.toUpperCase());
      }}
      className="flex gap-2"
    >
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Symbol"
        className="flex-1 rounded border p-2"
      />
      <button type="submit" className="rounded bg-blue-600 px-4 text-white">
        Go
      </button>
    </form>
  );
}

