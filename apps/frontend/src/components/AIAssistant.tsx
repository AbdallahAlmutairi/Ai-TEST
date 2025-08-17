"use client";

import { useState } from "react";

/**
 * Minimal chat-like widget used on several demo pages.  It does not connect to
 * a real backend but keeps the interface consistent for the exercises.
 */
export default function AIAssistant() {
  const [messages, setMessages] = useState<string[]>([]);
  const [input, setInput] = useState("");

  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input) return;
    setMessages([...messages, input]);
    setInput("");
  };

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto space-y-2 p-2 border rounded">
        {messages.map((m, i) => (
          <div key={i} className="rounded bg-gray-100 p-2 text-sm">
            {m}
          </div>
        ))}
        {messages.length === 0 && (
          <div className="text-sm text-gray-500">Start the conversation…</div>
        )}
      </div>
      <form onSubmit={submit} className="mt-2 flex">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 rounded-l border p-2"
          placeholder="Ask the AI"
        />
        <button
          type="submit"
          className="rounded-r bg-blue-600 px-4 text-white"
        >
          Send
        </button>
      </form>
    </div>
  );
}

