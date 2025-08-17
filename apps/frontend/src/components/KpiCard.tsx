import React from 'react';

interface KpiCardProps {
  label: string;
  value: string | number;
}

export default function KpiCard({ label, value }: KpiCardProps) {
  return (
    <div className="p-4 border rounded">
      <div className="text-sm text-gray-500">{label}</div>
      <div className="text-2xl font-bold">{value}</div>
    </div>
  );
}
