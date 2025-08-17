interface Props {
  indicators: Record<string, number>;
}

/** Display a small grid of technical indicator values. */
export default function IndicatorsPanel({ indicators }: Props) {
  return (
    <div className="grid grid-cols-2 gap-2 text-sm">
      {Object.entries(indicators).map(([k, v]) => (
        <div key={k} className="rounded border p-2">
          <div className="text-gray-500">{k}</div>
          <div className="font-medium">{v.toFixed(2)}</div>
        </div>
      ))}
      {Object.keys(indicators).length === 0 && (
        <div className="col-span-2 text-center text-gray-500">
          No indicators
        </div>
      )}
    </div>
  );
}

