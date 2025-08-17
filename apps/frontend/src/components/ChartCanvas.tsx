"use client";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  ResponsiveContainer,
} from "recharts";

type Point = { t: string; v: number };

interface Props {
  data: Point[];
}

/** Render a tiny responsive line chart using `recharts`. */
export default function ChartCanvas({ data }: Props) {
  return (
    <div className="h-64 w-full">
      <ResponsiveContainer>
        <LineChart data={data} margin={{ top: 10, right: 10, bottom: 0, left: 0 }}>
          <XAxis dataKey="t" hide />
          <YAxis hide />
          <Line type="monotone" dataKey="v" stroke="#3b82f6" dot={false} />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

